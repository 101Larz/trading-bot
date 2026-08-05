"""
Trading Bot Dashboard — Flask web server.
Serves four pages (overview, positions, research, trades) and JSON API
endpoints that the frontend polls every 60 seconds for live data.
"""

import os
import re
import sys
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import yfinance as yf
from flask import Flask, render_template, jsonify, abort, redirect, request, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "scripts"))

MEMORY_DIR   = ROOT / "memory"
RESEARCH_DIR = MEMORY_DIR / "research"   # per-day research files: YYYY-MM-DD.md
JOURNAL_DIR  = ROOT / "journal"

ALPACA_KEY    = os.getenv("APCA_API_KEY_ID", "")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY", "")
BROKER_BASE   = os.getenv("APCA_BASE_URL", "https://paper-api.alpaca.markets")
PAPER_MODE    = os.getenv("PAPER_MODE", "true").lower() == "true"


# ---------------------------------------------------------------------------
# Alpaca helpers
# ---------------------------------------------------------------------------

def _ah():
    return {"APCA-API-KEY-ID": ALPACA_KEY, "APCA-API-SECRET-KEY": ALPACA_SECRET}


def _alpaca(path: str, base: str = None) -> dict | list:
    url = f"{base or BROKER_BASE}{path}"
    try:
        r = requests.get(url, headers=_ah(), timeout=8)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def get_account() -> dict:
    raw = _alpaca("/v2/account")
    if "error" in raw:
        return raw
    return {
        "portfolio_value": float(raw.get("portfolio_value", 0)),
        "cash":            float(raw.get("cash", 0)),
        "buying_power":    float(raw.get("buying_power", 0)),
        "equity":          float(raw.get("equity", 0)),
        "long_market_value": float(raw.get("long_market_value", 0)),
        "status":          raw.get("status", "unknown"),
        "paper_mode":      PAPER_MODE,
    }


def get_positions() -> list:
    raw = _alpaca("/v2/positions")
    if isinstance(raw, dict) and "error" in raw:
        return []
    return [
        {
            "symbol":          p["symbol"],
            "qty":             float(p["qty"]),
            "side":            p["side"],
            "market_value":    float(p["market_value"]),
            "avg_entry_price": float(p["avg_entry_price"]),
            "current_price":   float(p["current_price"]),
            "unrealized_pl":   float(p["unrealized_pl"]),
            "unrealized_plpc": round(float(p["unrealized_plpc"]) * 100, 2),
            "change_today":    float(p.get("change_today", 0)),
        }
        for p in raw
    ]


def get_clock() -> dict:
    return _alpaca("/v2/clock")


# ---------------------------------------------------------------------------
# Markdown parsers
# ---------------------------------------------------------------------------

def parse_performance() -> dict:
    """
    Parse memory/performance.md for summary stats and the daily P&L log table.
    Returns { stats: {...}, daily: [{date, pnl, pct, trades}], trades: [...] }
    """
    path = MEMORY_DIR / "performance.md"
    if not path.exists():
        return {"stats": {}, "daily": [], "trades": []}

    text = path.read_text(encoding="utf-8")

    # ── Summary stats (| Metric | Value | table) ────────────────────────────
    stats = {}
    in_summary = False
    for line in text.splitlines():
        if "## Summary Statistics" in line:
            in_summary = True
            continue
        if in_summary:
            if line.startswith("## "):
                break
            m = re.match(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
            if m and m.group(1) not in ("Metric", "---", ""):
                stats[m.group(1).strip()] = m.group(2).strip()

    # ── Daily P&L log ────────────────────────────────────────────────────────
    daily = []
    in_daily = False
    for line in text.splitlines():
        if "## Daily P&L Log" in line:
            in_daily = True
            continue
        if in_daily:
            if line.startswith("## "):
                break
            # | Date | Starting Value | Ending Value | Daily P&L | Daily % | Trades | Notes |
            cols = [c.strip() for c in line.split("|") if c.strip()]
            if (
                len(cols) >= 5
                and cols[0] not in ("Date", "---", "—")
                and not cols[0].startswith("---")
            ):
                try:
                    daily.append({
                        "date":   cols[0],
                        "start":  _to_float(cols[1]),
                        "end":    _to_float(cols[2]),
                        "pnl":    _to_float(cols[3]),
                        "pct":    _to_float(cols[4]),
                        "trades": _to_int(cols[5]) if len(cols) > 5 else 0,
                        "notes":  cols[6] if len(cols) > 6 else "",
                    })
                except Exception:
                    pass

    # ── Trade Exit blocks (### Trade Exit — YYYY-MM-DD ... heading + vertical kv table)
    # The bot logs exits as structured blocks; the ## Closed Trade Log table is never
    # populated by the EOD routine, so we parse the blocks directly instead.
    trades = []
    lines_list = text.splitlines()
    idx = 0
    while idx < len(lines_list):
        line = lines_list[idx]
        if line.startswith("### Trade Exit"):
            date_m = re.search(r"(\d{4}-\d{2}-\d{2})", line)
            exit_date = date_m.group(1) if date_m else ""
            kv: dict[str, str] = {}
            idx += 1
            while idx < len(lines_list):
                row = lines_list[idx]
                if not row.strip().startswith("|"):
                    break
                m = re.match(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|", row)
                if m and m.group(1).strip() not in ("Field", "---", ""):
                    kv[m.group(1).strip()] = m.group(2).strip()
                idx += 1
            if kv.get("Symbol"):
                pnl_raw = kv.get("Realized P&L", "0")
                pnl_m = re.search(r"([-+]?)\s*\$?([\d,]+\.?\d*)", pnl_raw)
                if pnl_m:
                    sign = -1 if pnl_m.group(1) == "-" else 1
                    pnl_val = sign * float(pnl_m.group(2).replace(",", ""))
                else:
                    pnl_val = 0.0
                hold_raw = kv.get("Hold Days", "0")
                hold_m = re.search(r"(\d+)", hold_raw)
                hold_days = int(hold_m.group(1)) if hold_m else 0
                trades.append({
                    "date":        exit_date,
                    "symbol":      kv.get("Symbol", ""),
                    "side":        "SELL",
                    "qty":         _to_float(kv.get("Shares", "0")),
                    "entry":       _to_float(kv.get("Avg Entry Price", "0")),
                    "exit":        _to_float(kv.get("Avg Exit Price", "0")),
                    "pnl":         pnl_val,
                    "hold_days":   hold_days,
                    "exit_reason": kv.get("Exit Reason", ""),
                })
        else:
            idx += 1

    return {"stats": stats, "daily": daily, "trades": trades}


def parse_research_log() -> list[dict]:
    """
    Parse memory/research/YYYY-MM-DD.md files into a list of research sessions.
    Each file may contain multiple ## date — routine session blocks.
    Falls back to the legacy memory/RESEARCH-LOG.md if the research/ dir is empty.
    Returns sessions sorted newest-first.

    Each session = { date, title, sections: [{heading, body}] }
    """
    research_dir = MEMORY_DIR / "research"

    # Collect source files: all *.md from memory/research/, sorted by name (ISO date = alpha order)
    files: list[Path] = []
    if research_dir.exists():
        files = sorted(research_dir.glob("*.md"))

    # Legacy fallback: read old monolithic file if no per-day files found
    legacy = MEMORY_DIR / "RESEARCH-LOG.md"
    if not files and legacy.exists():
        files = [legacy]

    if not files:
        return []

    def _parse_text(text: str) -> list[dict]:
        """
        Handle two header formats written by different routine versions:

        OLD FORMAT (multi-session files):
          # Research Log — 2026-05-20          ← file header, ignored
          ## 2026-05-20 (Wed) — Pre-Market     ← H2 = session header
          ### Account Snapshot                  ← H3 = section header

        NEW FORMAT (single-session files written by newer routines):
          # 2026-06-09 (Tue) — Pre-Market …    ← H1 with date = session header
          ## Account Snapshot                   ← H2 = section header
          ### Sub-section                       ← H3 = body (folded into section)
        """
        _DATE = re.compile(r"(\d{4}-\d{2}-\d{2})(?:\s+\([^)]+\))?\s*[—–-]\s*(.+)")

        sessions: list[dict] = []
        current: dict | None = None

        for line in text.splitlines():

            # ── NEW FORMAT: H1 line containing a date (e.g. "# 2026-06-09 … — …")
            if line.startswith("# ") and not line.startswith("## "):
                m = _DATE.match(line[2:].strip())
                if m:
                    if current:
                        sessions.append(current)
                    current = {
                        "date":     m.group(1),
                        "title":    m.group(2).strip(),
                        "sections": [],
                        "_cur_sec": None,
                        "_h2_is_section": True,   # H2 → section, H3 → body
                    }
                    continue
                # H1 without a date = file-level title → skip
                continue

            # ── OLD FORMAT: H2 session header (e.g. "## 2026-05-18 … — …")
            if line.startswith("## ") and not (current and current.get("_h2_is_section")):
                m = _DATE.match(line[3:].strip())
                if m:
                    if current:
                        sessions.append(current)
                    current = {
                        "date":     m.group(1),
                        "title":    m.group(2).strip(),
                        "sections": [],
                        "_cur_sec": None,
                        "_h2_is_section": False,  # H3 → section
                    }
                    continue

            if current is None:
                continue

            h2_is_sec = current.get("_h2_is_section", False)

            # ── Section header
            if h2_is_sec and line.startswith("## "):
                # New format: H2 opens a section
                heading = line[3:].strip()
                sec: dict = {"heading": heading, "lines": []}
                current["sections"].append(sec)
                current["_cur_sec"] = sec
                continue

            if (not h2_is_sec) and line.startswith("### "):
                # Old format: H3 opens a section
                heading = line.lstrip("# ").strip()
                sec = {"heading": heading, "lines": []}
                current["sections"].append(sec)
                current["_cur_sec"] = sec
                continue

            # ── Body: accumulate into current section (both formats)
            if current["_cur_sec"] is not None:
                current["_cur_sec"]["lines"].append(line)

        if current:
            sessions.append(current)

        for s in sessions:
            s.pop("_cur_sec", None)
            s.pop("_h2_is_section", None)
            for sec in s["sections"]:
                sec["body"] = "\n".join(sec["lines"]).strip()
                del sec["lines"]

        return sessions

    all_sessions: list[dict] = []
    for f in files:
        try:
            all_sessions.extend(_parse_text(f.read_text(encoding="utf-8")))
        except Exception:
            pass

    # Sort newest-first; secondary sort by title to keep same-day sessions stable
    all_sessions.sort(key=lambda s: (s["date"], s["title"]), reverse=True)
    return all_sessions


def parse_journal_today() -> str:
    """Return today's journal markdown as a string, or empty string."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = JOURNAL_DIR / f"{today}.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _to_float(s: str) -> float:
    try:
        return float(re.sub(r"[^\d.\-+]", "", s))
    except Exception:
        return 0.0


def _to_int(s: str) -> int:
    try:
        return int(re.sub(r"[^\d]", "", s))
    except Exception:
        return 0


def _pnl_class(val: float) -> str:
    return "positive" if val > 0 else "negative" if val < 0 else "neutral"


def build_overview_data() -> dict:
    account  = get_account()
    perf     = parse_performance()
    clock    = get_clock()
    positions = get_positions()

    total_unrealized = sum(p["unrealized_pl"] for p in positions)
    total_realized   = sum(t["pnl"] for t in perf["trades"])

    # Chart series: dates and cumulative portfolio values from daily log
    chart_labels = [d["date"] for d in perf["daily"]]
    chart_values = [d["end"]  for d in perf["daily"]]

    # If no history yet, show starting value as flat line placeholder
    if not chart_labels:
        chart_labels = [datetime.now(timezone.utc).strftime("%Y-%m-%d")]
        chart_values = [account.get("portfolio_value", 100000)]

    return {
        "account":          account,
        "clock":            clock,
        "positions_count":  len(positions),
        "total_unrealized": total_unrealized,
        "total_realized":   total_realized,
        "total_pnl":        total_unrealized + total_realized,
        "stats":            perf["stats"],
        "chart_labels":     chart_labels,
        "chart_values":     chart_values,
        "last_updated":     datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ---------------------------------------------------------------------------
# Routes — pages
# ---------------------------------------------------------------------------

@app.route("/")
def overview():
    data = build_overview_data()
    return render_template("overview.html", **data)


@app.route("/positions")
def positions_page():
    positions = get_positions()
    account   = get_account()
    clock     = get_clock()
    for p in positions:
        p["pl_class"]  = _pnl_class(p["unrealized_pl"])
        p["pct_class"] = _pnl_class(p["unrealized_plpc"])
    return render_template(
        "positions.html",
        positions=positions,
        account=account,
        clock=clock,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/research")
def research_page():
    sessions = parse_research_log()
    journal  = parse_journal_today()
    clock    = get_clock()
    return render_template(
        "research.html",
        sessions=sessions,
        journal=journal,
        clock=clock,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/trades")
def trades_page():
    perf    = parse_performance()
    account = get_account()
    clock   = get_clock()
    trades  = perf["trades"]
    for t in trades:
        t["pl_class"] = _pnl_class(t["pnl"])
    total_pnl  = sum(t["pnl"] for t in trades)
    win_count  = sum(1 for t in trades if t["pnl"] > 0)
    loss_count = sum(1 for t in trades if t["pnl"] < 0)
    win_rate   = round(win_count / len(trades) * 100, 1) if trades else 0
    return render_template(
        "trades.html",
        trades=list(reversed(trades)),
        account=account,
        clock=clock,
        stats=perf["stats"],
        total_pnl=total_pnl,
        win_count=win_count,
        loss_count=loss_count,
        win_rate=win_rate,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


# ---------------------------------------------------------------------------
# Routes — JSON API (polled by frontend every 60 s)
# ---------------------------------------------------------------------------

@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(build_overview_data())


@app.route("/api/positions")
def api_positions():
    positions = get_positions()
    account   = get_account()
    for p in positions:
        p["pl_class"]  = _pnl_class(p["unrealized_pl"])
        p["pct_class"] = _pnl_class(p["unrealized_plpc"])
    return jsonify({
        "positions": positions,
        "account":   account,
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    })


@app.route("/api/clock")
def api_clock():
    return jsonify(get_clock())


# ---------------------------------------------------------------------------
# Personal portfolio — tickers, signals, regime, news
# ---------------------------------------------------------------------------

HOLDINGS_FILE = MEMORY_DIR / "portfolio_holdings.json"


def _load_holdings() -> list[dict]:
    """Read holdings from JSON file; returns [] if file missing or corrupt."""
    try:
        with open(HOLDINGS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_holdings(holdings: list[dict]) -> None:
    """Persist holdings list to JSON file, pretty-printed."""
    HOLDINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HOLDINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(holdings, f, indent=2, ensure_ascii=False)


def _fetch_ticker_name(ticker: str) -> str:
    """Try to fetch a human-readable name from yfinance; fall back to ticker."""
    try:
        info = yf.Ticker(ticker).info
        return info.get("shortName") or info.get("longName") or ticker
    except Exception:
        return ticker

def _git_push_holdings() -> tuple[bool, str]:
    """Commit and push portfolio_holdings.json to GitHub so changes survive Render restarts.

    Works in two environments:
    - Local dev: existing git clone, uses whatever remote is already configured.
    - Render: deployed zip with no .git dir; initialises a repo from scratch using
      GITHUB_TOKEN + GITHUB_REPO env vars.
    """
    repo = str(ROOT)
    token = os.getenv("GITHUB_TOKEN", "")
    gh_repo = os.getenv("GITHUB_REPO", "101Larz/trading-bot")  # e.g. "owner/repo"

    if not token:
        return False, "GITHUB_TOKEN not set — skipping push."

    remote_url = f"https://{token}@github.com/{gh_repo}.git"

    def run(cmd):
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=repo)

    # ── 1. Ensure a git repo exists ──────────────────────────────────────────
    git_dir = Path(repo) / ".git"
    if not git_dir.exists():
        r = run(["git", "init", "-b", "main"])
        if r.returncode != 0:
            # Older git without -b; init then rename
            run(["git", "init"])
            run(["git", "checkout", "-b", "main"])

    # ── 2. Set identity (required in CI/cloud) ────────────────────────────────
    run(["git", "config", "user.email", "bot@trading-dashboard"])
    run(["git", "config", "user.name",  "Trading Dashboard"])

    # ── 3. Set / update remote with token ────────────────────────────────────
    check = run(["git", "remote", "get-url", "origin"])
    if check.returncode == 0:
        run(["git", "remote", "set-url", "origin", remote_url])
    else:
        run(["git", "remote", "add", "origin", remote_url])

    # ── 4. Pull latest main to avoid non-fast-forward rejects ────────────────
    run(["git", "fetch", "origin", "main"])
    run(["git", "reset", "--mixed", "origin/main"])

    # ── 5. Stage, commit, push ────────────────────────────────────────────────
    r1 = run(["git", "add", "memory/portfolio_holdings.json"])
    if r1.returncode != 0:
        return False, f"git add failed: {r1.stderr[:120]}"

    r2 = run(["git", "commit", "-m", "chore: update portfolio holdings via dashboard"])
    if r2.returncode != 0 and "nothing to commit" not in (r2.stdout + r2.stderr):
        return False, f"git commit failed: {r2.stderr[:120]}"

    r3 = run(["git", "push", "origin", "main"])
    if r3.returncode != 0:
        return False, f"git push failed: {r3.stderr[:200]}"

    return True, "Saved and pushed to GitHub."


_CCY_SYMBOL = {"USD": "$", "EUR": "€", "GBP": "£", "GBX": "p"}


def _classify_signal(rsi, mas: dict) -> tuple[str, str]:
    """Return (signal_label, css_class) based on RSI and MA alignment."""
    if rsi is None or mas.get("ma20") is None:
        return "UNKNOWN", "neutral"
    price = mas.get("current_price") or 0
    ma20  = mas["ma20"]
    ma50  = mas.get("ma50")
    if rsi > 70:
        return "SELL", "negative"   # overbought
    if price > ma20 and (ma50 is None or ma20 > ma50):
        return "BUY", "positive"    # uptrend + RSI in range
    if price < ma20 and ma50 is not None and ma20 < ma50:
        return "SELL", "negative"   # downtrend
    return "HOLD", "neutral"


def _classify_regime(bars: list[dict]) -> tuple[str, str]:
    """
    Label the current Markov regime by looking at the majority of return-day
    classifications over the last 20 trading sessions.
    Bull >+0.5% | Bear <-0.5% | Sideways otherwise
    """
    if len(bars) < 5:
        return "Unknown", "neutral"
    window = bars[-21:]
    bull = bear = side = 0
    for i in range(1, len(window)):
        ret = (window[i]["c"] - window[i - 1]["c"]) / window[i - 1]["c"]
        if ret > 0.005:
            bull += 1
        elif ret < -0.005:
            bear += 1
        else:
            side += 1
    total = bull + bear + side
    if total == 0:
        return "Unknown", "neutral"
    if bull / total > 0.55:
        return "Bull", "positive"
    if bear / total > 0.40:
        return "Bear", "negative"
    return "Sideways", "neutral"


def _parse_news_item(article: dict) -> dict:
    """Handle both old yfinance (flat) and new yfinance 1.5+ (nested content) formats."""
    content   = article.get("content") or {}
    title     = content.get("title") or article.get("title", "")
    canonical = content.get("canonicalUrl") or {}
    link      = (canonical.get("url", "") if isinstance(canonical, dict) else "") \
                or article.get("link", "")
    provider  = content.get("provider") or {}
    publisher = (provider.get("displayName", "") if isinstance(provider, dict) else "") \
                or article.get("publisher", "")
    raw_time  = content.get("pubDate") or article.get("providerPublishTime") or ""
    if isinstance(raw_time, (int, float)):
        pub_date = datetime.fromtimestamp(raw_time).strftime("%Y-%m-%d")
    else:
        pub_date = str(raw_time)[:10]
    return {"title": title, "link": link, "publisher": publisher, "date": pub_date}


def _get_fx_rates() -> dict:
    """
    Fetch live EUR conversion rates via yfinance.
    EURUSD=X  → how many USD per 1 EUR  (e.g. 1.08)  → 1 USD = 1/1.08 EUR
    GBPEUR=X  → how many EUR per 1 GBP  (e.g. 1.17)  → 1 GBP = 1.17 EUR
    GBX is pence (1/100 of GBP), so GBX→EUR = GBPEUR / 100.
    Falls back to reasonable defaults if yfinance is unavailable.
    """
    rates = {"EUR": 1.0, "USD": 0.926, "GBP": 1.165, "GBX": 0.01165}
    try:
        eurusd = float(yf.Ticker("EURUSD=X").fast_info.last_price or 0)
        if eurusd > 0:
            rates["USD"] = round(1.0 / eurusd, 6)
    except Exception:
        pass
    try:
        gbpeur = float(yf.Ticker("GBPEUR=X").fast_info.last_price or 0)
        if gbpeur > 0:
            rates["GBP"] = round(gbpeur, 6)
            rates["GBX"] = round(gbpeur / 100.0, 6)
    except Exception:
        pass
    return rates


def _fetch_ticker_data(symbol: str, name: str, shares: float,
                        buy_price: float, buy_currency: str,
                        fx_rates: dict) -> dict:
    """Fetch price, indicators, signal, regime, news, and P&L (all in EUR)."""
    from market_data import get_bars, compute_moving_averages, compute_rsi

    buy_to_eur     = fx_rates.get(buy_currency, 1.0)
    cost_basis_eur = round(shares * buy_price * buy_to_eur, 2)

    base: dict = {
        "symbol": symbol, "name": name,
        "shares": shares,
        "buy_price": buy_price, "buy_currency": buy_currency,
        "buy_symbol": _CCY_SYMBOL.get(buy_currency, buy_currency),
        "cost_basis_eur": cost_basis_eur,
        "current_price": None,
        "current_price_currency": "USD", "current_price_symbol": "$",
        "current_value_eur": None,
        "pnl_eur": None, "pnl_pct": None, "pnl_class": "neutral",
        "daily_change_pct": None, "daily_change_class": "neutral",
        "ma20": None, "ma50": None, "rsi": None, "rsi_class": "neutral",
        "signal": "UNKNOWN", "signal_class": "neutral",
        "regime": "Unknown", "regime_class": "neutral",
        "source": "—", "news": [], "error": None,
    }
    try:
        bars, source = get_bars(symbol, limit=60)
        base["source"] = source

        mas = compute_moving_averages(bars)
        rsi = compute_rsi(bars)
        base["ma20"] = mas.get("ma20")
        base["ma50"] = mas.get("ma50")
        base["rsi"]  = rsi
        if rsi is not None:
            base["rsi_class"] = "positive" if 35 <= rsi <= 70 else "negative"

        base["signal"], base["signal_class"] = _classify_signal(rsi, mas)
        base["regime"], base["regime_class"] = _classify_regime(bars)

        # Current price via yfinance fast_info; detect native currency for FX conversion
        ticker_obj  = yf.Ticker(symbol)
        yf_currency = "USD"
        try:
            fi = ticker_obj.fast_info
            yf_currency = (fi.currency or "USD").upper()
            lp, pc = fi.last_price, fi.previous_close
            # GBX (pence) → convert to GBP for display and maths
            if yf_currency == "GBX":
                lp = (lp or 0) / 100.0
                pc = (pc or 0) / 100.0
                yf_currency = "GBP"
            if lp and pc:
                base["current_price"]    = round(float(lp), 4)
                base["daily_change_pct"] = round((lp - pc) / pc * 100, 2)
        except Exception:
            pass
        # Bar fallback if fast_info gave nothing
        if base["current_price"] is None and bars:
            base["current_price"] = bars[-1]["c"]
            if len(bars) >= 2:
                base["daily_change_pct"] = round(
                    (bars[-1]["c"] - bars[-2]["c"]) / bars[-2]["c"] * 100, 2
                )
        base["current_price_currency"] = yf_currency
        base["current_price_symbol"]   = _CCY_SYMBOL.get(yf_currency, yf_currency)

        if base["daily_change_pct"] is not None:
            base["daily_change_class"] = "positive" if base["daily_change_pct"] >= 0 else "negative"

        # P&L in EUR
        if base["current_price"] is not None:
            curr_to_eur = fx_rates.get(yf_currency, 1.0)
            cv_eur  = round(shares * base["current_price"] * curr_to_eur, 2)
            pnl_eur = round(cv_eur - cost_basis_eur, 2)
            base["current_value_eur"] = cv_eur
            base["pnl_eur"]           = pnl_eur
            base["pnl_pct"]           = round(pnl_eur / cost_basis_eur * 100, 2) if cost_basis_eur else None
            base["pnl_class"]         = "positive" if pnl_eur >= 0 else "negative"

        # News — top 4 via yfinance
        try:
            raw_news = ticker_obj.news or []
            parsed   = [_parse_news_item(a) for a in raw_news[:4]]
            base["news"] = [n for n in parsed if n["title"]]
        except Exception:
            pass

    except Exception as exc:
        base["error"] = str(exc)

    return base


def get_personal_portfolio_data() -> tuple[list[dict], dict]:
    """
    1. Fetch live FX rates (USD→EUR, GBP→EUR).
    2. Fetch all 12 holdings in parallel (6 workers).
    3. Compute EUR totals and return (holdings, totals).
    """
    raw      = _load_holdings()
    fx_rates = _get_fx_rates()
    order    = {h["ticker"]: i for i, h in enumerate(raw)}
    results  = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {
            pool.submit(
                _fetch_ticker_data,
                h["ticker"], h["name"], h["shares"],
                h["buy_price"], h["currency"], fx_rates,
            ): h["ticker"]
            for h in raw
        }
        for future in as_completed(futures):
            data = future.result()
            results[data["symbol"]] = data

    holdings = sorted(results.values(), key=lambda d: order.get(d["symbol"], 99))

    total_invested_eur = sum(h["cost_basis_eur"] for h in holdings)
    total_value_eur    = sum(h["current_value_eur"] for h in holdings
                             if h["current_value_eur"] is not None)
    total_pnl_eur      = round(total_value_eur - total_invested_eur, 2)
    total_pnl_pct      = round(total_pnl_eur / total_invested_eur * 100, 2) if total_invested_eur else 0
    totals = {
        "total_invested_eur": round(total_invested_eur, 2),
        "total_value_eur":    round(total_value_eur, 2),
        "total_pnl_eur":      total_pnl_eur,
        "total_pnl_pct":      total_pnl_pct,
        "total_pnl_class":    "positive" if total_pnl_eur >= 0 else "negative",
        "fx_usd_eur":         round(fx_rates["USD"], 4),
        "fx_gbp_eur":         round(fx_rates["GBP"], 4),
    }
    return holdings, totals


def _rolling_ma(closes: list, period: int) -> list:
    result: list = [None] * len(closes)
    for i in range(period - 1, len(closes)):
        result[i] = round(sum(closes[i - period + 1:i + 1]) / period, 4)
    return result


def _fetch_ticker_detail(symbol: str, name: str, shares: float,
                         buy_price: float, buy_currency: str,
                         fx_rates: dict) -> dict:
    """Like _fetch_ticker_data but fetches 200 bars for 6-month chart,
    rolling MA arrays, 52-week high/low, and up to 10 news items."""
    from market_data import get_bars, compute_moving_averages, compute_rsi

    buy_to_eur     = fx_rates.get(buy_currency, 1.0)
    cost_basis_eur = round(shares * buy_price * buy_to_eur, 2)

    base: dict = {
        "symbol": symbol, "name": name,
        "shares": shares,
        "buy_price": buy_price, "buy_currency": buy_currency,
        "buy_symbol": _CCY_SYMBOL.get(buy_currency, buy_currency),
        "cost_basis_eur": cost_basis_eur,
        "current_price": None,
        "current_price_currency": "USD", "current_price_symbol": "$",
        "current_value_eur": None,
        "pnl_eur": None, "pnl_pct": None, "pnl_class": "neutral",
        "daily_change_pct": None, "daily_change_class": "neutral",
        "ma20": None, "ma50": None, "rsi": None, "rsi_class": "neutral",
        "signal": "UNKNOWN", "signal_class": "neutral",
        "regime": "Unknown", "regime_class": "neutral",
        "chart_dates": [], "chart_prices": [],
        "chart_ma20": [], "chart_ma50": [],
        "buy_price_chart": None,
        "week52_high": None, "week52_low": None,
        "source": "—", "news": [], "error": None,
    }

    try:
        bars, source = get_bars(symbol, limit=200)
        base["source"] = source

        mas = compute_moving_averages(bars)
        rsi = compute_rsi(bars)
        base["ma20"] = mas.get("ma20")
        base["ma50"] = mas.get("ma50")
        base["rsi"]  = rsi
        if rsi is not None:
            base["rsi_class"] = "positive" if 35 <= rsi <= 70 else "negative"

        base["signal"], base["signal_class"] = _classify_signal(rsi, mas)
        base["regime"], base["regime_class"] = _classify_regime(bars)

        # Build rolling MA arrays for the chart (last 130 bars ≈ 6 months)
        closes   = [b["c"] for b in bars]
        dates    = [b["t"] for b in bars]
        ma20_arr = _rolling_ma(closes, 20)
        ma50_arr = _rolling_ma(closes, 50)
        N = min(130, len(bars))
        base["chart_dates"]  = dates[-N:]
        base["chart_prices"] = closes[-N:]
        base["chart_ma20"]   = ma20_arr[-N:]
        base["chart_ma50"]   = ma50_arr[-N:]

        ticker_obj  = yf.Ticker(symbol)
        yf_currency = "USD"
        raw_ccy     = "USD"
        try:
            fi      = ticker_obj.fast_info
            raw_ccy = (fi.currency or "USD").upper()
            yf_currency = raw_ccy
            lp, pc  = fi.last_price, fi.previous_close
            if raw_ccy == "GBX":
                lp = (lp or 0) / 100.0
                pc = (pc or 0) / 100.0
                yf_currency = "GBP"
            if lp and pc:
                base["current_price"]    = round(float(lp), 4)
                base["daily_change_pct"] = round((lp - pc) / pc * 100, 2)
            # 52-week high / low (convert GBX → GBP if needed)
            wh = getattr(fi, "year_high", None)
            wl = getattr(fi, "year_low",  None)
            if raw_ccy == "GBX":
                if wh: wh = wh / 100.0
                if wl: wl = wl / 100.0
            base["week52_high"] = round(float(wh), 4) if wh else None
            base["week52_low"]  = round(float(wl), 4) if wl else None
        except Exception:
            pass

        if base["current_price"] is None and bars:
            base["current_price"] = bars[-1]["c"]
            if len(bars) >= 2:
                base["daily_change_pct"] = round(
                    (bars[-1]["c"] - bars[-2]["c"]) / bars[-2]["c"] * 100, 2)

        base["current_price_currency"] = yf_currency
        base["current_price_symbol"]   = _CCY_SYMBOL.get(yf_currency, yf_currency)

        if base["daily_change_pct"] is not None:
            base["daily_change_class"] = "positive" if base["daily_change_pct"] >= 0 else "negative"

        # Buy-price in chart's native currency (for the dashed horizontal line)
        buy_price_eur = buy_price * fx_rates.get(buy_currency, 1.0)
        curr_to_eur   = fx_rates.get(yf_currency, 1.0)
        if curr_to_eur:
            base["buy_price_chart"] = round(buy_price_eur / curr_to_eur, 4)

        # P&L in EUR
        if base["current_price"] is not None:
            curr_to_eur = fx_rates.get(yf_currency, 1.0)
            cv_eur  = round(shares * base["current_price"] * curr_to_eur, 2)
            pnl_eur = round(cv_eur - cost_basis_eur, 2)
            base["current_value_eur"] = cv_eur
            base["pnl_eur"]           = pnl_eur
            base["pnl_pct"]           = round(pnl_eur / cost_basis_eur * 100, 2) if cost_basis_eur else None
            base["pnl_class"]         = "positive" if pnl_eur >= 0 else "negative"

        # News — top 10
        try:
            raw_news = ticker_obj.news or []
            parsed   = [_parse_news_item(a) for a in raw_news[:10]]
            base["news"] = [n for n in parsed if n["title"]]
        except Exception:
            pass

    except Exception as exc:
        base["error"] = str(exc)

    return base


@app.route("/portfolio")
def portfolio_page():
    holdings, totals = get_personal_portfolio_data()
    clock = get_clock()
    return render_template(
        "portfolio.html",
        holdings=holdings,
        totals=totals,
        clock=clock,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/portfolio/manage", methods=["GET", "POST"])
def portfolio_manage():
    clock = get_clock()

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "add":
            ticker    = request.form.get("ticker", "").strip().upper()
            name      = request.form.get("name", "").strip()
            shares    = request.form.get("shares", "").strip()
            buy_price = request.form.get("buy_price", "").strip()
            currency  = request.form.get("currency", "USD").strip().upper()
            if ticker and shares and buy_price:
                try:
                    holdings = _load_holdings()
                    if not any(h["ticker"] == ticker for h in holdings):
                        if not name:
                            name = _fetch_ticker_name(ticker)
                        holdings.append({
                            "ticker":    ticker,
                            "name":      name or ticker,
                            "shares":    float(shares),
                            "buy_price": float(buy_price),
                            "currency":  currency,
                        })
                        _save_holdings(holdings)
                        ok, push_msg = _git_push_holdings()
                        msg = f"Added {ticker}. {push_msg}"
                    else:
                        msg = f"{ticker} already exists — edit shares/price in the table below."
                except ValueError:
                    msg = "Invalid shares or buy price — must be numbers."
            else:
                msg = "Ticker, shares, and buy price are required."
            return redirect(url_for("portfolio_manage", msg=msg))

        if action == "delete":
            ticker = request.form.get("ticker", "").strip().upper()
            if ticker:
                holdings = [h for h in _load_holdings() if h["ticker"] != ticker]
                _save_holdings(holdings)
                ok, push_msg = _git_push_holdings()
                return redirect(url_for("portfolio_manage", msg=f"Deleted {ticker}. {push_msg}"))
            return redirect(url_for("portfolio_manage", msg=f"Deleted {ticker}."))

        if action == "save":
            tickers   = request.form.getlist("ticker")
            shares_l  = request.form.getlist("shares")
            prices_l  = request.form.getlist("buy_price")
            holdings  = _load_holdings()
            lookup    = {}
            for t, s, p in zip(tickers, shares_l, prices_l):
                try:
                    lookup[t] = {"shares": float(s), "buy_price": float(p)}
                except ValueError:
                    pass
            for h in holdings:
                if h["ticker"] in lookup:
                    h["shares"]    = lookup[h["ticker"]]["shares"]
                    h["buy_price"] = lookup[h["ticker"]]["buy_price"]
            _save_holdings(holdings)
            ok, push_msg = _git_push_holdings()
            return redirect(url_for("portfolio_manage", msg=f"Holdings saved. {push_msg}"))

        return redirect(url_for("portfolio_manage"))

    msg      = request.args.get("msg")
    holdings = _load_holdings()
    return render_template(
        "portfolio_manage.html",
        holdings=holdings,
        msg=msg,
        clock=clock,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/portfolio/<ticker>")
def portfolio_detail(ticker: str):
    ticker = ticker.upper()
    meta = next((h for h in _load_holdings() if h["ticker"] == ticker), None)
    if meta is None:
        abort(404)
    fx_rates = _get_fx_rates()
    data = _fetch_ticker_detail(
        meta["ticker"], meta["name"], meta["shares"],
        meta["buy_price"], meta["currency"], fx_rates,
    )
    clock = get_clock()
    return render_template(
        "portfolio_detail.html",
        h=data,
        clock=clock,
        last_updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/api/my-portfolio")
def api_my_portfolio():
    holdings, totals = get_personal_portfolio_data()
    return jsonify({
        "holdings":     holdings,
        "totals":       totals,
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    })


# ---------------------------------------------------------------------------
# Template filters
# ---------------------------------------------------------------------------

@app.template_filter("money")
def money_filter(val):
    try:
        f = float(val)
        sign = "+" if f > 0 else ""
        return f"{sign}${f:,.2f}"
    except Exception:
        return str(val)


@app.template_filter("pct")
def pct_filter(val):
    try:
        f = float(val)
        sign = "+" if f > 0 else ""
        return f"{sign}{f:.2f}%"
    except Exception:
        return str(val)


@app.template_filter("pl_class")
def pl_class_filter(val):
    return _pnl_class(float(val)) if val else "neutral"


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")

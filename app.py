"""
Trading Bot Dashboard — Flask web server.
Serves four pages (overview, positions, research, trades) and JSON API
endpoints that the frontend polls every 60 seconds for live data.
"""

import os
import re
import sys
import json
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import yfinance as yf
from flask import Flask, render_template, jsonify
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

PERSONAL_HOLDINGS = [
    {"ticker": "WDC",     "name": "Western Digital",          "shares": 0.43003312,  "buy_price": 268.82},
    {"ticker": "ASML",    "name": "ASML Holding",             "shares": 0.13747919,  "buy_price": 1252.60},
    {"ticker": "MU",      "name": "Micron Technology",        "shares": 0.20603656,  "buy_price": 163.62},
    {"ticker": "AMAT",    "name": "Applied Materials",        "shares": 0.16546614,  "buy_price": 350.34},
    {"ticker": "LRCX",    "name": "Lam Research",             "shares": 0.26794250,  "buy_price": 240.61},
    {"ticker": "SNDK",    "name": "SanDisk",                  "shares": 0.05929092,  "buy_price": 644.45},
    {"ticker": "STX",     "name": "Seagate Technology",       "shares": 0.05853506,  "buy_price": 419.58},
    {"ticker": "SPY",     "name": "S&P 500 ETF",              "shares": 5.37787128,  "buy_price": 101.743},
    {"ticker": "PANW",    "name": "Palo Alto Networks",       "shares": 1.00000000,  "buy_price": 174.83},
    {"ticker": "VFEM.L",  "name": "Vanguard FTSE EM ETF",    "shares": 1.33739782,  "buy_price": 61.044},
    {"ticker": "VEUR.L",  "name": "Vanguard FTSE Europe ETF","shares": 1.04178269,  "buy_price": 49.98},
    {"ticker": "XNAS.DE", "name": "Xtrackers NASDAQ 100",    "shares": 0.24306270,  "buy_price": 43.322},
]


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


def _fetch_ticker_data(symbol: str, name: str, shares: float, buy_price: float) -> dict:
    """Fetch price, indicators, signal, regime, news, and P&L for one ticker."""
    from market_data import get_bars, compute_moving_averages, compute_rsi

    cost_basis = round(shares * buy_price, 2)
    base: dict = {
        "symbol": symbol, "name": name,
        "shares": shares, "buy_price": buy_price, "cost_basis": cost_basis,
        "current_price": None, "current_value": None,
        "pnl": None, "pnl_pct": None, "pnl_class": "neutral",
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

        # Current price + daily change via yfinance fast_info; fall back to bars
        try:
            fi = yf.Ticker(symbol).fast_info
            lp, pc = fi.last_price, fi.previous_close
            if lp and pc:
                base["current_price"]    = round(float(lp), 4)
                base["daily_change_pct"] = round((lp - pc) / pc * 100, 2)
        except Exception:
            pass
        if base["current_price"] is None and bars:
            base["current_price"] = bars[-1]["c"]
            if len(bars) >= 2:
                base["daily_change_pct"] = round(
                    (bars[-1]["c"] - bars[-2]["c"]) / bars[-2]["c"] * 100, 2
                )
        if base["daily_change_pct"] is not None:
            base["daily_change_class"] = "positive" if base["daily_change_pct"] >= 0 else "negative"

        # P&L (requires a valid current price)
        if base["current_price"] is not None:
            cv  = round(shares * base["current_price"], 2)
            pnl = round(cv - cost_basis, 2)
            base["current_value"] = cv
            base["pnl"]           = pnl
            base["pnl_pct"]       = round(pnl / cost_basis * 100, 2) if cost_basis else None
            base["pnl_class"]     = "positive" if pnl >= 0 else "negative"

        # News — top 4 headlines via yfinance
        try:
            raw_news = yf.Ticker(symbol).news or []
            parsed   = [_parse_news_item(a) for a in raw_news[:4]]
            base["news"] = [n for n in parsed if n["title"]]
        except Exception:
            pass

    except Exception as exc:
        base["error"] = str(exc)

    return base


def get_personal_portfolio_data() -> tuple[list[dict], dict]:
    """Fetch all 12 personal holdings in parallel. Returns (holdings, totals)."""
    order   = {h["ticker"]: i for i, h in enumerate(PERSONAL_HOLDINGS)}
    results = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {
            pool.submit(_fetch_ticker_data, h["ticker"], h["name"], h["shares"], h["buy_price"]): h["ticker"]
            for h in PERSONAL_HOLDINGS
        }
        for future in as_completed(futures):
            data = future.result()
            results[data["symbol"]] = data

    holdings = sorted(results.values(), key=lambda d: order.get(d["symbol"], 99))

    total_invested     = sum(h["cost_basis"] for h in holdings)
    total_value        = sum(h["current_value"] for h in holdings if h["current_value"] is not None)
    total_pnl          = round(total_value - total_invested, 2)
    total_pnl_pct      = round(total_pnl / total_invested * 100, 2) if total_invested else 0
    totals = {
        "total_invested":  round(total_invested, 2),
        "total_value":     round(total_value, 2),
        "total_pnl":       total_pnl,
        "total_pnl_pct":   total_pnl_pct,
        "total_pnl_class": "positive" if total_pnl >= 0 else "negative",
    }
    return holdings, totals


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

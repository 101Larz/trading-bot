"""
Trading Bot Dashboard — Flask web server.
Serves four pages (overview, positions, research, trades) and JSON API
endpoints that the frontend polls every 60 seconds for live data.
"""

import os
import re
import json
from datetime import datetime, timezone
from pathlib import Path

import requests
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ROOT = Path(__file__).parent
MEMORY_DIR = ROOT / "memory"
JOURNAL_DIR = ROOT / "journal"

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

    # ── Closed trade log ─────────────────────────────────────────────────────
    trades = []
    in_trades = False
    for line in text.splitlines():
        if "## Closed Trade Log" in line:
            in_trades = True
            continue
        if in_trades:
            if line.startswith("## "):
                break
            # | Date | Symbol | Side | Qty | Entry | Exit | P&L | Hold Days | Exit Reason |
            cols = [c.strip() for c in line.split("|") if c.strip()]
            if (
                len(cols) >= 7
                and cols[0] not in ("Date", "---", "—")
                and not cols[0].startswith("---")
            ):
                try:
                    trades.append({
                        "date":        cols[0],
                        "symbol":      cols[1],
                        "side":        cols[2],
                        "qty":         _to_float(cols[3]),
                        "entry":       _to_float(cols[4]),
                        "exit":        _to_float(cols[5]),
                        "pnl":         _to_float(cols[6]),
                        "hold_days":   _to_int(cols[7]) if len(cols) > 7 else 0,
                        "exit_reason": cols[8] if len(cols) > 8 else "",
                    })
                except Exception:
                    pass

    return {"stats": stats, "daily": daily, "trades": trades}


def parse_research_log() -> list[dict]:
    """
    Parse memory/RESEARCH-LOG.md into a list of research sessions.
    Each session = { date, title, sections: [{heading, body}] }
    """
    path = MEMORY_DIR / "RESEARCH-LOG.md"
    if not path.exists():
        return []

    text = path.read_text(encoding="utf-8")
    sessions = []
    current = None

    for line in text.splitlines():
        # Match headers like:
        #   ## 2026-05-17 — Pre-Market Research
        #   ## 2026-05-18 (Monday) — Pre-Market
        #   ## 2026-05-18 (Monday) — Pre-Market (session: keen-wright)
        m = re.match(r"^## (\d{4}-\d{2}-\d{2})(?:\s+\([^)]+\))?\s*[—–-]\s*(.+)", line)
        if m:
            if current:
                sessions.append(current)
            current = {
                "date":     m.group(1),
                "title":    m.group(2).strip(),
                "sections": [],
                "_cur_sec": None,
            }
            continue

        if current is None:
            continue

        # Sub-section header: ### Symbol or heading
        if line.startswith("### "):
            heading = line.lstrip("# ").strip()
            sec = {"heading": heading, "lines": []}
            current["sections"].append(sec)
            current["_cur_sec"] = sec
            continue

        # Accumulate body lines into current section
        if current["_cur_sec"] is not None:
            current["_cur_sec"]["lines"].append(line)

    if current:
        sessions.append(current)

    # Clean up internal cursor and join body lines
    for s in sessions:
        s.pop("_cur_sec", None)
        for sec in s["sections"]:
            sec["body"] = "\n".join(sec["lines"]).strip()
            del sec["lines"]

    return list(reversed(sessions))  # newest first


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

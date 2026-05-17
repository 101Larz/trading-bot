"""
Research module: fetches news from Alpaca, account status, and positions.
Claude uses WebSearch for web-based news research; this script handles
structured API data (Alpaca news feed, account, positions).
"""

import os
import sys
import json
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
BROKER_BASE = os.getenv("APCA_BASE_URL", "https://paper-api.alpaca.markets")
DATA_BASE = "https://data.alpaca.markets"


def _headers():
    return {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }


def get_account() -> dict:
    r = requests.get(f"{BROKER_BASE}/v2/account", headers=_headers(), timeout=10)
    r.raise_for_status()
    data = r.json()
    return {
        "buying_power": float(data["buying_power"]),
        "cash": float(data["cash"]),
        "portfolio_value": float(data["portfolio_value"]),
        "equity": float(data["equity"]),
        "long_market_value": float(data.get("long_market_value", 0)),
        "short_market_value": float(data.get("short_market_value", 0)),
        "status": data["status"],
    }


def get_positions() -> list[dict]:
    r = requests.get(f"{BROKER_BASE}/v2/positions", headers=_headers(), timeout=10)
    r.raise_for_status()
    positions = r.json()
    return [
        {
            "symbol": p["symbol"],
            "qty": float(p["qty"]),
            "side": p["side"],
            "market_value": float(p["market_value"]),
            "avg_entry_price": float(p["avg_entry_price"]),
            "current_price": float(p["current_price"]),
            "unrealized_pl": float(p["unrealized_pl"]),
            "unrealized_plpc": float(p["unrealized_plpc"]),
            "change_today": float(p.get("change_today", 0)),
        }
        for p in positions
    ]


def get_news(symbol: str, limit: int = 5) -> list[dict]:
    """Fetch recent news from Alpaca for a symbol."""
    url = f"{DATA_BASE}/v1beta1/news"
    params = {"symbols": symbol, "limit": limit, "sort": "desc"}
    r = requests.get(url, headers=_headers(), params=params, timeout=10)
    r.raise_for_status()
    articles = r.json().get("news", [])
    return [
        {
            "headline": a.get("headline", ""),
            "summary": a.get("summary", "")[:300],
            "source": a.get("source", ""),
            "created_at": a.get("created_at", ""),
            "url": a.get("url", ""),
        }
        for a in articles
    ]


def get_open_orders() -> list[dict]:
    r = requests.get(f"{BROKER_BASE}/v2/orders?status=open", headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def full_research_snapshot(symbols: list[str]) -> dict:
    """Compile account + positions + news for all watchlist symbols."""
    account = get_account()
    positions = get_positions()
    position_map = {p["symbol"]: p for p in positions}

    symbol_snapshots = {}
    for sym in symbols:
        news = get_news(sym, limit=3)
        pos = position_map.get(sym)
        symbol_snapshots[sym] = {
            "news": news,
            "position": pos,
        }

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "account": account,
        "positions": positions,
        "symbols": symbol_snapshots,
    }


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "account"
    symbol = sys.argv[2] if len(sys.argv) > 2 else None

    if action == "account":
        print(json.dumps(get_account(), indent=2))
    elif action == "positions":
        print(json.dumps(get_positions(), indent=2))
    elif action == "news" and symbol:
        print(json.dumps(get_news(symbol), indent=2))
    elif action == "orders":
        print(json.dumps(get_open_orders(), indent=2))
    elif action == "snapshot":
        watchlist_path = os.path.join(os.path.dirname(__file__), "..", "watchlist.json")
        with open(watchlist_path) as f:
            wl = json.load(f)
        symbols = [s["symbol"] for s in wl["watchlist"] if s.get("active")]
        print(json.dumps(full_research_snapshot(symbols), indent=2))
    else:
        print(f"Usage: python research.py [account|positions|news TICKER|orders|snapshot]")

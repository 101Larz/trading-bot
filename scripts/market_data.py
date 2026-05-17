"""
Market data fetching: price bars, latest quotes, moving averages, RSI.
All functions return plain dicts suitable for JSON serialization.
"""

import os
import sys
import json
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
DATA_BASE = "https://data.alpaca.markets"


def _headers():
    return {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }


def get_bars(symbol: str, timeframe: str = "1Day", limit: int = 60) -> dict:
    url = f"{DATA_BASE}/v2/stocks/{symbol}/bars"
    params = {"timeframe": timeframe, "limit": limit, "adjustment": "raw", "sort": "asc"}
    r = requests.get(url, headers=_headers(), params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def get_latest_quote(symbol: str) -> dict:
    url = f"{DATA_BASE}/v2/stocks/{symbol}/quotes/latest"
    r = requests.get(url, headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def compute_moving_averages(bars: list[dict]) -> dict:
    """Compute 20-day and 50-day simple moving averages from bar data."""
    closes = [b["c"] for b in bars]
    if len(closes) < 50:
        return {"ma20": None, "ma50": None, "note": "Insufficient data"}
    ma20 = sum(closes[-20:]) / 20
    ma50 = sum(closes[-50:]) / 50
    current = closes[-1]
    return {
        "ma20": round(ma20, 2),
        "ma50": round(ma50, 2),
        "current_price": round(current, 2),
        "above_ma20": current > ma20,
        "above_ma50": current > ma50,
        "trend": "bullish" if current > ma20 > ma50 else ("bearish" if current < ma20 < ma50 else "mixed"),
    }


def compute_rsi(bars: list[dict], period: int = 14) -> float | None:
    """Compute RSI-14 from bar data."""
    closes = [b["c"] for b in bars]
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains = [max(d, 0) for d in deltas[-period:]]
    losses = [abs(min(d, 0)) for d in deltas[-period:]]
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def get_market_clock() -> dict:
    url = f"{os.getenv('APCA_BASE_URL')}/v2/clock"
    r = requests.get(url, headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def full_snapshot(symbol: str) -> dict:
    """Return bars, MAs, RSI and latest quote for a symbol in one call."""
    bars_data = get_bars(symbol, timeframe="1Day", limit=60)
    bars = bars_data.get("bars", [])
    quote_data = get_latest_quote(symbol)
    mas = compute_moving_averages(bars)
    rsi = compute_rsi(bars)
    return {
        "symbol": symbol,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "latest_quote": quote_data.get("quote", {}),
        "moving_averages": mas,
        "rsi_14": rsi,
        "bar_count": len(bars),
    }


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "snapshot"
    symbol = sys.argv[2] if len(sys.argv) > 2 else "SPY"

    if action == "bars":
        print(json.dumps(get_bars(symbol)))
    elif action == "quote":
        print(json.dumps(get_latest_quote(symbol)))
    elif action == "clock":
        print(json.dumps(get_market_clock()))
    else:
        print(json.dumps(full_snapshot(symbol), indent=2))

"""
Market data fetching: price bars, latest quotes, moving averages, RSI.

Bar data source priority:
  1. Alpaca IEX feed (free, real-time quotes but no historical bars on free plan)
  2. yfinance (fallback for historical OHLCV bars, MAs, RSI)
"""

import os
import sys
import json
import time
from datetime import datetime, date, timedelta, timezone

import pandas as pd
import requests
import yfinance as yf
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


# ---------------------------------------------------------------------------
# Bar data
# ---------------------------------------------------------------------------

def get_bars_alpaca(symbol: str, limit: int = 60) -> list[dict]:
    """Fetch daily bars from Alpaca IEX. Returns [] on free-plan null response."""
    url = f"{DATA_BASE}/v2/stocks/{symbol}/bars"
    params = {"timeframe": "1Day", "limit": limit, "adjustment": "raw", "sort": "asc", "feed": "iex"}
    r = requests.get(url, headers=_headers(), params=params, timeout=10)
    r.raise_for_status()
    return r.json().get("bars") or []


def get_bars_yfinance(symbol: str, limit: int = 60) -> list[dict]:
    """Fetch daily bars from yfinance (uses curl_cffi TLS in v1.5+).

    Uses explicit start/end dates so that today's incomplete intraday session
    is never counted as a daily bar — the bug that caused only 1 bar to be
    returned during market hours when period="Nd" was used.
    """
    end = date.today()
    # Request 3× calendar days so weekends + holidays still yield `limit` bars
    start = end - timedelta(days=limit * 3)
    df = yf.download(
        symbol,
        start=start.isoformat(),
        end=end.isoformat(),   # end is exclusive in yfinance, so today is not included
        interval="1d",
        auto_adjust=True,
        progress=False,
        multi_level_index=False,  # yfinance 1.5+ option: flat columns for single ticker
    )
    if df.empty:
        return []
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    # Drop rows where Close is NaN — yfinance sometimes returns a partial bar for
    # the current intraday session (volume present but OHLC not yet finalized).
    nan_count = int(df["Close"].isna().sum())
    if nan_count:
        print(
            f"[WARN market_data] {symbol}: dropped {nan_count} bar(s) with NaN Close"
            " (partial intraday session discarded)",
            file=sys.stderr,
        )
    df = df.dropna(subset=["Close"])
    df = df.tail(limit)
    return [
        {
            "t": str(idx.date() if hasattr(idx, "date") else idx),
            "o": round(float(row["Open"]), 4),
            "h": round(float(row["High"]), 4),
            "l": round(float(row["Low"]), 4),
            "c": round(float(row["Close"]), 4),
            "v": int(row["Volume"]),
        }
        for idx, row in df.iterrows()
    ]


_YF_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
_YF_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_bars_yahoo_direct(symbol: str, limit: int = 60) -> list[dict]:
    """Fetch daily bars via raw Yahoo Finance v8 chart JSON API.

    Used as a fallback when yfinance itself fails (TLS/network issue in cloud).
    Makes a plain requests.get with browser headers — avoids yfinance's internal
    session handling entirely.
    """
    # Request extra history so we always have `limit` trading bars after filtering
    calendar_days = limit * 3
    end_ts = int(time.time())
    start_ts = end_ts - calendar_days * 86400
    url = _YF_CHART_URL.format(symbol=symbol)
    params = {
        "interval": "1d",
        "period1": str(start_ts),
        "period2": str(end_ts),
        "events": "div,splits",
    }
    try:
        r = requests.get(url, headers=_YF_HEADERS, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        result = data.get("chart", {}).get("result") or []
        if not result:
            return []
        chart = result[0]
        timestamps = chart.get("timestamp", [])
        quotes = chart.get("indicators", {}).get("quote", [{}])[0]
        adj_close = chart.get("indicators", {}).get("adjclose", [{}])[0].get("adjclose", [])
        bars = []
        for i, ts in enumerate(timestamps):
            c = (adj_close[i] if adj_close else None) or (quotes.get("close") or [None])[i]
            o = (quotes.get("open") or [None])[i]
            h = (quotes.get("high") or [None])[i]
            l = (quotes.get("low") or [None])[i]
            v = (quotes.get("volume") or [0])[i]
            if c is None or o is None:
                continue
            bars.append({
                "t": str(date.fromtimestamp(ts)),
                "o": round(float(o), 4),
                "h": round(float(h), 4) if h is not None else round(float(o), 4),
                "l": round(float(l), 4) if l is not None else round(float(o), 4),
                "c": round(float(c), 4),
                "v": int(v) if v else 0,
            })
        # Exclude today's incomplete bar (same date as today)
        today_str = str(date.today())
        bars = [b for b in bars if b["t"] != today_str]
        return bars[-limit:]
    except Exception as exc:
        print(f"[ERROR market_data] {symbol}: yahoo-direct fallback failed — {exc}", file=sys.stderr)
        return []


def get_bars(symbol: str, limit: int = 60) -> tuple[list[dict], str]:
    """Returns (bars, source) with a 3-tier fallback chain.

    1. Alpaca IEX — skipped if <20 bars (free plan has no history)
    2. yfinance — uses curl_cffi TLS (v1.5+) to avoid Yahoo Finance bot-blocks
    3. Yahoo Finance v8 chart API (direct requests, browser headers) — used when
       yfinance itself is blocked at the TLS/network layer in cloud environments
    """
    bars = get_bars_alpaca(symbol, limit)
    if len(bars) >= 20:
        return bars, "alpaca"

    for attempt in range(1, 3):
        try:
            bars = get_bars_yfinance(symbol, limit)
        except Exception as exc:
            print(
                f"[WARN market_data] {symbol}: yfinance raised exception"
                f" (attempt {attempt}/2): {exc}",
                file=sys.stderr,
            )
            bars = []
        if len(bars) >= 20:
            return bars, "yfinance"
        if attempt == 1:
            print(
                f"[WARN market_data] {symbol}: yfinance returned only {len(bars)} bars"
                f" (attempt {attempt}/2) — retrying in 2 s",
                file=sys.stderr,
            )
            time.sleep(2)

    if len(bars) < 20:
        print(
            f"[WARN market_data] {symbol}: yfinance gave {len(bars)} bars — trying"
            " yahoo-direct fallback",
            file=sys.stderr,
        )
        direct_bars = get_bars_yahoo_direct(symbol, limit)
        if len(direct_bars) >= 20:
            return direct_bars, "yahoo-direct"
        bars = direct_bars or bars  # use whichever has more data

    if len(bars) < 20:
        print(
            f"[ERROR market_data] {symbol}: only {len(bars)} bars after all 3 sources."
            " MA20/RSI will be unreliable.",
            file=sys.stderr,
        )
    return bars, "yfinance"


# ---------------------------------------------------------------------------
# Latest quote
# ---------------------------------------------------------------------------

def get_latest_quote(symbol: str) -> dict:
    """Fetch latest bid/ask from Alpaca IEX."""
    url = f"{DATA_BASE}/v2/stocks/{symbol}/quotes/latest"
    r = requests.get(url, headers=_headers(), params={"feed": "iex"}, timeout=10)
    r.raise_for_status()
    return r.json().get("quote", {})


# ---------------------------------------------------------------------------
# Indicators
# ---------------------------------------------------------------------------

def compute_moving_averages(bars: list[dict]) -> dict:
    if not bars:
        return {"ma20": None, "ma50": None, "trend": None, "note": "No bar data"}
    closes = [float(b["c"]) for b in bars]
    # Guard: filter out any NaN values that slipped through (should be caught upstream,
    # but this prevents silent NaN propagation into MA calculations).
    import math
    nan_in_closes = sum(1 for c in closes if math.isnan(c))
    if nan_in_closes:
        print(
            f"[WARN market_data] {nan_in_closes} NaN close(s) in bar data — dropping before MA calc",
            file=sys.stderr,
        )
        closes = [c for c in closes if not math.isnan(c)]
    if len(closes) < 20:
        return {"ma20": None, "ma50": None, "trend": None, "note": f"Only {len(closes)} bars — need 20+"}
    current = closes[-1]
    ma20 = round(sum(closes[-20:]) / 20, 2)
    ma50 = round(sum(closes[-50:]) / 50, 2) if len(closes) >= 50 else None
    trend = None
    if ma50 is not None:
        trend = "bullish" if current > ma20 > ma50 else ("bearish" if current < ma20 < ma50 else "mixed")
    return {
        "current_price": round(current, 2),
        "ma20": ma20,
        "ma50": ma50,
        "above_ma20": bool(current > ma20),
        "above_ma50": bool(current > ma50) if ma50 else None,
        "trend": trend,
    }


def compute_rsi(bars: list[dict], period: int = 14) -> float | None:
    if not bars:
        return None
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
    return round(100 - (100 / (1 + avg_gain / avg_loss)), 2)


# ---------------------------------------------------------------------------
# Market clock
# ---------------------------------------------------------------------------

def get_market_clock() -> dict:
    url = f"{os.getenv('APCA_BASE_URL')}/v2/clock"
    r = requests.get(url, headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


# ---------------------------------------------------------------------------
# Full snapshot
# ---------------------------------------------------------------------------

def full_snapshot(symbol: str) -> dict:
    """
    Return a complete picture of a symbol: latest quote, MAs, RSI, bar source.
    Bars come from Alpaca if available, yfinance otherwise.
    """
    bars, bar_source = get_bars(symbol)
    quote = get_latest_quote(symbol)
    mas = compute_moving_averages(bars)
    rsi = compute_rsi(bars)

    # Derive a clean last price: prefer IEX ask, fall back to MA current_price
    last_price = quote.get("ap") or quote.get("bp") or mas.get("current_price")

    return {
        "symbol": symbol,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "last_price": last_price,
        "bar_source": bar_source,
        "bar_count": len(bars),
        "latest_quote": {"bid": quote.get("bp"), "ask": quote.get("ap")},
        "moving_averages": mas,
        "rsi_14": rsi,
        "rsi_signal": (
            "overbought" if rsi and rsi > 80
            else "oversold" if rsi and rsi < 30
            else "neutral" if rsi
            else None
        ),
    }


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "snapshot"
    symbol = sys.argv[2] if len(sys.argv) > 2 else "SPY"

    if action == "bars":
        bars, source = get_bars(symbol)
        print(json.dumps({"source": source, "count": len(bars), "bars": bars[-5:]}, indent=2))
    elif action == "quote":
        print(json.dumps(get_latest_quote(symbol), indent=2))
    elif action == "clock":
        print(json.dumps(get_market_clock(), indent=2))
    else:
        print(json.dumps(full_snapshot(symbol), indent=2))

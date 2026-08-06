"""
Order placement, cancellation, and market-status checks.
All orders go through risk.py validation before submission.
"""

import os
import sys
import json
import time
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv

load_dotenv()

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
BROKER_BASE = os.getenv("APCA_BASE_URL", "https://paper-api.alpaca.markets")
PAPER_MODE = os.getenv("PAPER_MODE", "true").lower() == "true"


def _headers():
    return {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
        "Content-Type": "application/json",
    }


def get_market_clock() -> dict:
    r = requests.get(f"{BROKER_BASE}/v2/clock", headers=_headers(), timeout=10)
    r.raise_for_status()
    return r.json()


def is_market_open() -> bool:
    clock = get_market_clock()
    return clock.get("is_open", False)


def place_limit_order(
    symbol: str,
    qty: float,
    side: str,
    limit_price: float,
    time_in_force: str = "day",
) -> dict:
    """
    Place a limit order. Side must be 'buy' or 'sell'.
    Always use limit orders — never market orders.
    """
    if PAPER_MODE:
        print(f"[PAPER] Would place {side} limit order: {qty} {symbol} @ ${limit_price:.2f}")

    payload = {
        "symbol": symbol,
        "qty": str(qty),
        "side": side,
        "type": "limit",
        "time_in_force": time_in_force,
        "limit_price": f"{limit_price:.2f}",
    }

    r = requests.post(
        f"{BROKER_BASE}/v2/orders",
        headers=_headers(),
        json=payload,
        timeout=10,
    )
    r.raise_for_status()
    result = r.json()
    result["_paper_mode"] = PAPER_MODE
    return result


def cancel_order(order_id: str) -> int:
    r = requests.delete(f"{BROKER_BASE}/v2/orders/{order_id}", headers=_headers(), timeout=10)
    return r.status_code


def cancel_all_orders() -> int:
    r = requests.delete(f"{BROKER_BASE}/v2/orders", headers=_headers(), timeout=10)
    return r.status_code


def close_position(symbol: str) -> dict:
    """Close an entire position by symbol."""
    r = requests.delete(
        f"{BROKER_BASE}/v2/positions/{symbol}",
        headers=_headers(),
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def get_orders(status: str = "open") -> list[dict]:
    r = requests.get(
        f"{BROKER_BASE}/v2/orders",
        headers=_headers(),
        params={"status": status},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def safe_buy(
    symbol: str,
    qty: float,
    ask_price: float,
    account: dict,
    positions: list[dict],
    daily_pnl: float = 0.0,
) -> dict:
    """
    Full validated buy: runs risk checks, then places a limit order
    at 0.25% above ask to ensure fill.
    """
    from risk import validate_order

    limit_price = round(ask_price * 1.0025, 2)
    ok, messages = validate_order(symbol, "buy", qty, limit_price, account, positions, daily_pnl)

    if not ok:
        return {"status": "rejected", "symbol": symbol, "reasons": messages}

    if not is_market_open():
        return {"status": "rejected", "symbol": symbol, "reasons": ["Market is closed"]}

    order = place_limit_order(symbol, qty, "buy", limit_price)

    # Attempt trailing stop after fill (poll up to 30 s)
    fill_status, _ = _wait_for_fill(order["id"], max_wait=30)
    stop_result: dict = {}
    if fill_status == "filled":
        try:
            stop_result = place_trailing_stop(symbol, qty)
        except Exception as exc:
            stop_result = {
                "error": str(exc),
                "note": f"Buy filled but trailing stop FAILED — fix manually: python trade.py trail {symbol} {qty}",
            }
    else:
        stop_result = {
            "note": f"Order status '{fill_status}' at 30 s — trailing stop not placed yet. "
                    f"Run once filled: python trade.py trail {symbol} {qty}",
        }

    return {"status": "submitted", "order": order, "risk_checks": messages, "trailing_stop": stop_result}


def safe_sell(
    symbol: str,
    qty: float,
    bid_price: float,
) -> dict:
    """Place a limit sell at 0.25% below bid."""
    if not is_market_open():
        return {"status": "rejected", "symbol": symbol, "reasons": ["Market is closed"]}

    limit_price = round(bid_price * 0.9975, 2)
    order = place_limit_order(symbol, qty, "sell", limit_price)
    return {"status": "submitted", "order": order}


# ---------------------------------------------------------------------------
# Buy-side constants (stricter than the global risk.py defaults)
# ---------------------------------------------------------------------------

MAX_BUY_POSITIONS = 8        # max concurrent long positions
MAX_WEEKLY_BUYS = 3          # max buy-side executions Mon–Sun
MAX_POSITION_EQUITY_PCT = 0.20  # max 20% of equity per position
TRAILING_STOP_PCT = 15.0     # trailing stop percentage (GTC) — widened from 10% to survive pullbacks
MIN_HOLD_DAYS = 5            # minimum days to hold before signal-based exits (hard stop bypasses this)


def days_held(symbol: str) -> int:
    """Return the number of calendar days since the most recent filled buy for `symbol`.

    Used to enforce MIN_HOLD_DAYS: signal-based sells are blocked until a position
    has been held for at least MIN_HOLD_DAYS days. Hard stop-loss (-7%) bypasses this.
    Returns 0 if no filled buy is found (treat as just-entered).
    """
    try:
        r = requests.get(
            f"{BROKER_BASE}/v2/orders",
            headers=_headers(),
            params={"status": "filled", "symbols": symbol, "limit": 50},
            timeout=10,
        )
        r.raise_for_status()
        buys = [o for o in r.json() if o.get("side") == "buy" and o.get("symbol") == symbol]
        if not buys:
            return 0
        # Most recent filled buy
        latest = max(buys, key=lambda o: o.get("filled_at") or o.get("created_at") or "")
        fill_ts = latest.get("filled_at") or latest.get("created_at")
        if not fill_ts:
            return 0
        fill_dt = datetime.fromisoformat(fill_ts.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - fill_dt).days
    except Exception:
        return 0


def count_trades_this_week() -> int:
    """Count filled buy orders placed since Monday 00:00 UTC this week."""
    today = datetime.now(timezone.utc)
    monday = today - timedelta(days=today.weekday())
    week_start = monday.replace(hour=0, minute=0, second=0, microsecond=0)
    r = requests.get(
        f"{BROKER_BASE}/v2/orders",
        headers=_headers(),
        params={"status": "filled", "after": week_start.isoformat(), "limit": 100},
        timeout=10,
    )
    r.raise_for_status()
    return sum(1 for o in r.json() if o.get("side") == "buy")


def place_trailing_stop(symbol: str, qty: float, trail_percent: float = TRAILING_STOP_PCT) -> dict:
    """Place a trailing stop sell order (GTC) against an existing position."""
    payload = {
        "symbol": symbol,
        "qty": str(qty),
        "side": "sell",
        "type": "trailing_stop",
        "trail_percent": str(trail_percent),
        "time_in_force": "gtc",
    }
    r = requests.post(f"{BROKER_BASE}/v2/orders", headers=_headers(), json=payload, timeout=10)
    r.raise_for_status()
    return r.json()


def _wait_for_fill(order_id: str, max_wait: int = 30) -> tuple[str, dict]:
    """Poll order status until filled, canceled, expired, rejected, or timeout.

    Returns (status_string, order_dict). status is one of:
      "filled" | "canceled" | "expired" | "rejected" | "timeout"
    """
    deadline = time.time() + max_wait
    while time.time() < deadline:
        r = requests.get(f"{BROKER_BASE}/v2/orders/{order_id}", headers=_headers(), timeout=10)
        r.raise_for_status()
        order = r.json()
        status = order.get("status", "")
        if status in ("filled", "canceled", "expired", "rejected"):
            return status, order
        time.sleep(1)
    return "timeout", {}


def _log_trade_to_performance(symbol: str, shares: float, est_price: float, order_id: str) -> None:
    """Append a buy-entry block to memory/performance.md."""
    perf_path = os.path.join(os.path.dirname(__file__), "..", "memory", "performance.md")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n### Trade Entry — {ts}\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| Symbol | {symbol} |\n"
        f"| Side | BUY |\n"
        f"| Shares | {shares} |\n"
        f"| Est. Price | ${est_price:.2f} |\n"
        f"| Est. Value | ${shares * est_price:.2f} |\n"
        f"| Order ID | {order_id} |\n"
        f"| Trailing Stop | {TRAILING_STOP_PCT:.0f}% GTC placed immediately after fill |\n"
    )
    with open(perf_path, "a", encoding="utf-8") as f:
        f.write(entry)


def buy(symbol: str, shares: float) -> dict:
    """Validated market buy with immediate 15% trailing stop (GTC).

    Rules enforced here (independent of risk.py):
      1. Max 6 concurrent long positions.
      2. Max 3 buy-side executions Mon–Sun (calendar week).
      3. Max 20% of current equity per position.

    On success: places market buy, waits 2 s, places trailing stop, logs to
    memory/performance.md.
    """
    # Lazy imports to avoid circular dependency at module load time
    sys.path.insert(0, os.path.dirname(__file__))
    from research import get_account, get_positions
    from market_data import get_latest_quote, get_bars

    account = get_account()
    positions = get_positions()
    equity = account["equity"]

    # Rule 1 — position count
    if len(positions) >= MAX_BUY_POSITIONS:
        return {
            "status": "rejected",
            "symbol": symbol,
            "reason": f"Already at max {MAX_BUY_POSITIONS} positions ({len(positions)} open)",
        }

    # Rule 2 — weekly trade count
    weekly_buys = count_trades_this_week()
    if weekly_buys >= MAX_WEEKLY_BUYS:
        return {
            "status": "rejected",
            "symbol": symbol,
            "reason": f"Weekly buy limit reached ({weekly_buys}/{MAX_WEEKLY_BUYS})",
        }

    # Rule 3 — position size vs equity
    quote = get_latest_quote(symbol)
    est_price = quote.get("ap") or quote.get("bp")
    if not est_price:
        bars, _ = get_bars(symbol, limit=5)
        est_price = bars[-1]["c"] if bars else None
    if not est_price:
        return {"status": "rejected", "symbol": symbol, "reason": "Could not determine current price"}

    order_value = shares * est_price
    position_pct = order_value / equity
    if position_pct > MAX_POSITION_EQUITY_PCT:
        return {
            "status": "rejected",
            "symbol": symbol,
            "reason": (
                f"Order ${order_value:.2f} is {position_pct:.1%} of equity "
                f"— exceeds {MAX_POSITION_EQUITY_PCT:.0%} limit"
            ),
        }

    # Market-hours check
    if not is_market_open():
        return {"status": "rejected", "symbol": symbol, "reason": "Market is closed"}

    # Place market buy
    if PAPER_MODE:
        print(f"[PAPER] Market buy: {shares} {symbol} @ market (est. ${est_price:.2f})")
    buy_payload = {
        "symbol": symbol,
        "qty": str(shares),
        "side": "buy",
        "type": "market",
        "time_in_force": "day",
    }
    r = requests.post(f"{BROKER_BASE}/v2/orders", headers=_headers(), json=buy_payload, timeout=10)
    r.raise_for_status()
    buy_order = r.json()
    buy_order["_paper_mode"] = PAPER_MODE

    # Poll until the buy order fills (up to 30 s), then place trailing stop.
    # A fixed sleep is unreliable — paper fills can take 3–10 s depending on load.
    fill_status, _ = _wait_for_fill(buy_order["id"], max_wait=30)
    stop_result: dict = {}
    if fill_status == "filled":
        try:
            stop_result = place_trailing_stop(symbol, shares)
            if PAPER_MODE:
                print(f"[PAPER] Trailing stop placed: {shares} {symbol}, {TRAILING_STOP_PCT:.0f}% trail GTC")
        except Exception as exc:
            stop_result = {
                "error": str(exc),
                "note": f"Buy filled but trailing stop FAILED — fix manually: python trade.py trail {symbol} {shares}",
            }
    else:
        stop_result = {
            "error": f"Buy order status '{fill_status}' before trailing stop could be placed",
            "note": f"Run manually if order fills: python trade.py trail {symbol} {shares}",
        }

    _log_trade_to_performance(symbol, shares, est_price, buy_order.get("id", "unknown"))

    return {
        "status": "submitted",
        "symbol": symbol,
        "shares": shares,
        "est_price": est_price,
        "buy_order_id": buy_order.get("id"),
        "trailing_stop": stop_result,
        "weekly_buys_used": weekly_buys + 1,
        "weekly_buys_remaining": MAX_WEEKLY_BUYS - weekly_buys - 1,
        "paper_mode": PAPER_MODE,
    }


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "clock"

    if action == "clock":
        print(json.dumps(get_market_clock(), indent=2))
    elif action == "open":
        print("Market is open" if is_market_open() else "Market is closed")
    elif action == "orders":
        print(json.dumps(get_orders(), indent=2))
    elif action == "cancel-all":
        code = cancel_all_orders()
        print(f"Cancel all orders — HTTP {code}")
    elif action == "close" and len(sys.argv) > 2:
        # Liquidate an entire position via Alpaca's DELETE endpoint (market order).
        # Use only for emergency cut-loser exits when a limit-close is not practical.
        print(json.dumps(close_position(sys.argv[2]), indent=2))
    elif action == "limit-close" and len(sys.argv) == 5:
        # Preferred exit: limit sell at bid − 0.25%.
        # Usage: python trade.py limit-close SYMBOL SHARES BID_PRICE
        sym = sys.argv[2].upper()
        shares = float(sys.argv[3])
        bid = float(sys.argv[4])
        print(json.dumps(safe_sell(sym, shares, bid), indent=2))
    elif action == "trail" and len(sys.argv) >= 4:
        # Place a 10% trailing-stop GTC on an existing position.
        # Usage: python trade.py trail SYMBOL SHARES [TRAIL_PCT]
        sym = sys.argv[2].upper()
        shares = float(sys.argv[3])
        pct = float(sys.argv[4]) if len(sys.argv) > 4 else TRAILING_STOP_PCT
        print(json.dumps(place_trailing_stop(sym, shares, pct), indent=2))
    elif action == "buy" and len(sys.argv) == 4:
        sym = sys.argv[2].upper()
        shares = float(sys.argv[3])
        print(json.dumps(buy(sym, shares), indent=2))
    elif action == "safe-buy" and len(sys.argv) >= 4:
        # Usage: python trade.py safe-buy SYMBOL SHARES [ASK_PRICE]
        # ASK_PRICE is informational; buy() fetches live price internally.
        sym = sys.argv[2].upper()
        shares = float(sys.argv[3])
        print(json.dumps(buy(sym, shares), indent=2))
    elif action == "days-held" and len(sys.argv) > 2:
        print(days_held(sys.argv[2].upper()))
    else:
        print(
            "Usage: python trade.py "
            "[clock|open|orders|cancel-all"
            "|close SYMBOL"
            "|limit-close SYMBOL SHARES BID"
            "|trail SYMBOL SHARES [TRAIL_PCT]"
            "|buy SYMBOL SHARES"
            "|safe-buy SYMBOL SHARES [ASK_PRICE]"
            "|days-held SYMBOL]"
        )

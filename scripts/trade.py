"""
Order placement, cancellation, and market-status checks.
All orders go through risk.py validation before submission.
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
    return {"status": "submitted", "order": order, "risk_checks": messages}


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
        print(json.dumps(close_position(sys.argv[2]), indent=2))
    else:
        print("Usage: python trade.py [clock|open|orders|cancel-all|close SYMBOL]")

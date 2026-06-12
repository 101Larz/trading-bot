"""
Risk validation: all orders must pass these checks before execution.
Returns (ok: bool, reason: str). Never raises — callers check the bool.
"""

import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

MAX_POSITION_PCT = float(os.getenv("MAX_POSITION_PCT", "0.08"))
CASH_RESERVE_PCT = float(os.getenv("CASH_RESERVE_PCT", "0.20"))
STOP_LOSS_PCT = float(os.getenv("STOP_LOSS_PCT", "0.08"))
DAILY_LOSS_LIMIT_PCT = float(os.getenv("DAILY_LOSS_LIMIT_PCT", "0.03"))
MAX_POSITIONS = int(os.getenv("MAX_POSITIONS", "8"))


def check_position_size(
    qty: float,
    price: float,
    portfolio_value: float,
    symbol: str = "",
) -> tuple[bool, str]:
    order_value = qty * price
    allocation = order_value / portfolio_value
    if allocation > MAX_POSITION_PCT:
        return False, (
            f"Position size {allocation:.1%} exceeds max {MAX_POSITION_PCT:.1%} "
            f"for {symbol} (${order_value:.2f} of ${portfolio_value:.2f})"
        )
    return True, "Position size OK"


def check_cash_reserve(
    order_value: float,
    cash: float,
    portfolio_value: float,
) -> tuple[bool, str]:
    cash_after = cash - order_value
    reserve_required = portfolio_value * CASH_RESERVE_PCT
    if cash_after < reserve_required:
        return False, (
            f"Order would leave ${cash_after:.2f} cash, below required reserve "
            f"${reserve_required:.2f} ({CASH_RESERVE_PCT:.0%} of portfolio)"
        )
    return True, "Cash reserve OK"


def check_max_positions(
    current_position_count: int,
    side: str,
) -> tuple[bool, str]:
    if side == "buy" and current_position_count >= MAX_POSITIONS:
        return False, f"Already at max {MAX_POSITIONS} concurrent positions"
    return True, "Position count OK"


def check_daily_loss_limit(
    daily_pnl: float,
    portfolio_value: float,
) -> tuple[bool, str]:
    if daily_pnl < 0:
        loss_pct = abs(daily_pnl) / portfolio_value
        if loss_pct >= DAILY_LOSS_LIMIT_PCT:
            return False, (
                f"Daily loss limit breached: down {loss_pct:.1%} "
                f"(limit {DAILY_LOSS_LIMIT_PCT:.1%}). ALL TRADING HALTED."
            )
    return True, "Daily loss OK"


def check_stop_loss(
    current_price: float,
    entry_price: float,
    symbol: str = "",
) -> tuple[bool, str]:
    """Returns True if we should trigger a stop-loss close."""
    drop_pct = (entry_price - current_price) / entry_price
    if drop_pct >= STOP_LOSS_PCT:
        return True, (
            f"Stop-loss triggered on {symbol}: down {drop_pct:.1%} "
            f"from entry ${entry_price:.2f} (current ${current_price:.2f})"
        )
    return False, "No stop-loss"


def validate_order(
    symbol: str,
    side: str,
    qty: float,
    price: float,
    account: dict,
    positions: list[dict],
    daily_pnl: float = 0.0,
) -> tuple[bool, list[str]]:
    """
    Run all risk checks for an order. Returns (all_ok, list_of_messages).
    Callers should abort if all_ok is False.
    """
    portfolio_value = account["portfolio_value"]
    cash = account["cash"]
    order_value = qty * price
    messages = []

    checks = [
        check_daily_loss_limit(daily_pnl, portfolio_value),
        check_position_size(qty, price, portfolio_value, symbol),
        check_cash_reserve(order_value, cash, portfolio_value),
        check_max_positions(len(positions), side),
    ]

    all_ok = True
    for ok, msg in checks:
        messages.append(msg)
        if not ok:
            all_ok = False

    return all_ok, messages


def check_all_stop_losses(positions: list[dict]) -> list[dict]:
    """Return list of positions that have breached the stop-loss threshold."""
    to_close = []
    for p in positions:
        if p["side"] == "long":
            triggered, msg = check_stop_loss(
                p["current_price"], p["avg_entry_price"], p["symbol"]
            )
            if triggered:
                to_close.append({"symbol": p["symbol"], "qty": p["qty"], "reason": msg})
    return to_close


if __name__ == "__main__":
    print("Risk module loaded. Use validate_order() from other scripts.")
    print(f"  MAX_POSITION_PCT  = {MAX_POSITION_PCT:.0%}")
    print(f"  CASH_RESERVE_PCT  = {CASH_RESERVE_PCT:.0%}")
    print(f"  STOP_LOSS_PCT     = {STOP_LOSS_PCT:.0%}")
    print(f"  DAILY_LOSS_LIMIT  = {DAILY_LOSS_LIMIT_PCT:.0%}")
    print(f"  MAX_POSITIONS     = {MAX_POSITIONS}")

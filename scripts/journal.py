"""
Journal writer: creates and appends to daily markdown journal files.
Journals live in journal/YYYY-MM-DD.md.
"""

import os
import sys
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
JOURNAL_DIR = ROOT / "journal"


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def journal_path(date: str | None = None) -> Path:
    return JOURNAL_DIR / f"{date or _today()}.md"


def init_journal(date: str | None = None, account: dict | None = None) -> Path:
    """Create a fresh journal file for the given date if it doesn't exist."""
    JOURNAL_DIR.mkdir(exist_ok=True)
    path = journal_path(date)
    if path.exists():
        return path

    d = date or _today()
    header = f"# Trade Journal — {d}\n\n"
    header += "## Portfolio Status\n"
    if account:
        header += f"- Cash: ${account.get('cash', 0):,.2f}\n"
        header += f"- Portfolio Value: ${account.get('portfolio_value', 0):,.2f}\n"
        header += f"- Buying Power: ${account.get('buying_power', 0):,.2f}\n"
    else:
        header += "- Cash: _pending_\n- Portfolio Value: _pending_\n"

    header += "\n## Market Research\n_Populated during pre-market routine._\n"
    header += "\n## Trades Executed\n| Time (ET) | Symbol | Side | Qty | Price | Reasoning |\n"
    header += "|-----------|--------|------|-----|-------|-----------|\n"
    header += "\n## Positions Closed\n_None yet._\n"
    header += "\n## End-of-Day Reflection\n_Populated during end-of-day routine._\n"

    path.write_text(header, encoding="utf-8")
    return path


def append_research(symbol: str, notes: str, date: str | None = None):
    path = journal_path(date)
    if not path.exists():
        init_journal(date)
    entry = f"\n### {symbol}\n{notes.strip()}\n"
    _insert_after_section(path, "## Market Research", entry)


def append_trade(
    symbol: str,
    side: str,
    qty: float,
    price: float,
    reasoning: str,
    date: str | None = None,
):
    path = journal_path(date)
    if not path.exists():
        init_journal(date)
    now_et = datetime.now().strftime("%H:%M")
    row = f"| {now_et} | {symbol} | {side.upper()} | {qty} | ${price:.2f} | {reasoning} |\n"
    _insert_after_section(path, "| Time (ET) | Symbol | Side | Qty | Price | Reasoning |", row)


def append_reflection(text: str, date: str | None = None):
    path = journal_path(date)
    if not path.exists():
        init_journal(date)
    content = path.read_text(encoding="utf-8")
    content = content.replace(
        "\n## End-of-Day Reflection\n_Populated during end-of-day routine._\n",
        f"\n## End-of-Day Reflection\n{text.strip()}\n",
    )
    path.write_text(content, encoding="utf-8")


def _insert_after_section(path: Path, marker: str, text: str):
    content = path.read_text(encoding="utf-8")
    idx = content.find(marker)
    if idx == -1:
        content += f"\n{text}"
    else:
        insert_at = idx + len(marker)
        newline_after = content.find("\n", insert_at)
        content = content[: newline_after + 1] + text + content[newline_after + 1 :]
    path.write_text(content, encoding="utf-8")


def update_heartbeat(
    routine: str,
    status: str,
    trades_placed: int = 0,
    positions_count: int = 0,
    cash_balance: float | None = None,
    portfolio_value: float | None = None,
    daily_pnl: float | None = None,
    error: str | None = None,
):
    hb_path = ROOT / "heartbeat.json"
    data = {
        "last_run": datetime.now(timezone.utc).isoformat(),
        "routine": routine,
        "status": status,
        "trades_placed": trades_placed,
        "positions_count": positions_count,
        "cash_balance": cash_balance,
        "portfolio_value": portfolio_value,
        "daily_pnl": daily_pnl,
        "error": error,
    }
    hb_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "init"

    if action == "init":
        p = init_journal()
        print(f"Initialized journal: {p}")
    elif action == "path":
        print(journal_path())
    elif action == "trade":
        append_trade("SPY", "buy", 10, 520.50, "Test entry from CLI")
        print("Test trade appended.")
    else:
        print("Usage: python journal.py [init|path|trade]")

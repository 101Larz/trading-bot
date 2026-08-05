"""
Backtest the trading strategy on historical OHLCV data.

Strategy rules tested
---------------------
Entry (ALL must be true on day T; enter at day T+1 open):
  - RSI-14 in [35, 70]
  - Close > MA20
  - Close > MA50
  - 1-month momentum > 0%  (close > close 20 bars ago)

Exit (checked at day T close; exit at T close):
  - Hard stop-loss  : close ≤ entry × (1 − 0.07)
  - Trailing stop   : close ≤ running_high × (1 − 0.10)
  - Signal sell     : RSI > 70  OR  (close < MA20 AND MA20 < MA50)

Portfolio constraints:
  - Max 8 concurrent positions
  - 8% of initial capital per trade (fixed dollar size)
  - Cash earns nothing (conservative)

Usage:
    python scripts/backtest.py [--years 3] [--capital 100000]

Output:
    memory/backtest_results.md
"""

import sys
import math
import argparse
from datetime import date, timedelta, datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import numpy as np
import yfinance as yf

# ── Paths ───────────────────────────────────────────────────────────────────────
ROOT       = Path(__file__).parent.parent
MEMORY_DIR = ROOT / "memory"

# ── 95-ticker universe ──────────────────────────────────────────────────────────
UNIVERSE = [
    # Technology (20)
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "INTC",
    "CRM",  "ADBE", "QCOM", "TXN",   "NFLX", "AVGO", "ORCL", "INTU", "ACN",
    "IBM",  "ADP",
    # Semis / Storage (10)
    "AMAT", "LRCX", "KLAC", "MRVL", "ARM",  "ASML", "MU",   "WDC",  "SNDK", "STX",
    # Financials (18)
    "JPM",  "V",    "MA",   "BAC",  "GS",   "MS",   "BLK",  "SCHW", "SPGI",
    "MCO",  "ICE",  "CME",  "AON",  "MMC",  "AIG",  "MET",  "PYPL", "BRK-B",
    # Healthcare (16)
    "UNH",  "JNJ",  "ABBV", "LLY",  "MRK",  "PFE",  "TMO",  "ABT",  "DHR",
    "AMGN", "ISRG", "GILD", "ELV",  "REGN", "ZTS",  "SYK",
    # Consumer (12)
    "WMT",  "HD",   "PG",   "KO",   "PEP",  "COST", "DIS",  "MCD",  "NKE",
    "SBUX", "MDLZ", "PM",
    # Energy (2)
    "XOM",  "CVX",
    # Industrials (7)
    "HON",  "UPS",  "CAT",  "BA",   "RTX",  "GE",   "MMM",
    # Materials / Utilities (2)
    "LIN",  "NEE",
    # ETFs / Broad Market (8)
    "QQQ",  "IWM",  "EEM",  "VGK",  "GLD",  "XLE",  "XLF",  "XLV",
]

# ── Strategy parameters ─────────────────────────────────────────────────────────
STOP_LOSS_PCT     = 0.07    # hard stop: -7% from entry
TRAILING_STOP_PCT = 0.10    # trailing stop: -10% from running high
RSI_LOW           = 35
RSI_HIGH          = 70
MAX_POSITIONS     = 8
POSITION_SIZE_PCT = 0.08    # 8% of initial capital per trade
BENCHMARK         = "SPY"


# ── Data download ───────────────────────────────────────────────────────────────

def _download_one(ticker: str, start: str, end: str) -> tuple[str, pd.DataFrame | None]:
    try:
        df = yf.download(
            ticker,
            start=start,
            end=end,
            interval="1d",
            auto_adjust=True,
            progress=False,
            multi_level_index=False,
        )
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.dropna(subset=["Close"])
        return ticker, df if len(df) >= 60 else None
    except Exception as exc:
        print(f"  [WARN] {ticker}: {exc}", file=sys.stderr)
        return ticker, None


def download_all(tickers: list[str], start: str, end: str) -> dict[str, pd.DataFrame]:
    """Parallel download for all tickers. Prints progress."""
    results: dict[str, pd.DataFrame] = {}
    total = len(tickers)
    done  = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(_download_one, t, start, end): t for t in tickers}
        for fut in as_completed(futs):
            ticker, df = fut.result()
            done += 1
            if df is not None:
                results[ticker] = df
                print(f"  [{done:3d}/{total}] {ticker}: {len(df)} bars", flush=True)
            else:
                print(f"  [{done:3d}/{total}] {ticker}: skipped", flush=True)
    return results


# ── Indicators ──────────────────────────────────────────────────────────────────

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Return df with MA20, MA50, RSI14 (simple), MOM20 added; NaN rows dropped."""
    df = df.copy()
    c  = df["Close"]

    df["MA20"] = c.rolling(20).mean()
    df["MA50"] = c.rolling(50).mean()

    # Simple 14-period RSI (matches compute_rsi in market_data.py)
    delta = c.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta).clip(lower=0).rolling(14).mean()
    rs    = gain / loss.replace(0.0, float("nan"))
    df["RSI"] = (100 - (100 / (1 + rs))).round(2)

    # 1-month momentum
    df["MOM20"] = c / c.shift(20) - 1

    return df.dropna(subset=["MA20", "MA50", "RSI", "MOM20"])


# ── Signal helpers ──────────────────────────────────────────────────────────────

def _buy_signal(row: dict) -> bool:
    try:
        return (
            RSI_LOW <= row["RSI"] <= RSI_HIGH
            and row["Close"] > row["MA20"]
            and row["Close"] > row["MA50"]
            and row["MOM20"] > 0
        )
    except (TypeError, KeyError):
        return False


def _sell_signal(row: dict, entry_price: float, running_high: float) -> tuple[bool, str]:
    """Returns (should_exit, reason)."""
    close = row["Close"]

    hard_stop     = entry_price  * (1 - STOP_LOSS_PCT)
    trailing_stop = running_high * (1 - TRAILING_STOP_PCT)
    exit_floor    = max(hard_stop, trailing_stop)
    if close <= exit_floor:
        reason = "stop-loss" if close <= hard_stop else "trailing-stop"
        return True, reason

    rsi, ma20, ma50 = row.get("RSI"), row.get("MA20"), row.get("MA50")
    if rsi is not None and not math.isnan(rsi) and rsi > RSI_HIGH:
        return True, "signal-rsi"
    if (ma20 is not None and ma50 is not None
            and not math.isnan(ma20) and not math.isnan(ma50)
            and close < ma20 and ma20 < ma50):
        return True, "signal-trend"

    return False, ""


# ── Portfolio simulation ────────────────────────────────────────────────────────

def simulate(all_data: dict[str, pd.DataFrame], initial_capital: float) -> tuple[list, list, list]:
    """
    Day-by-day portfolio simulation across all tickers.

    Returns:
        equity_curve  : list[float]  — portfolio value at end of each day
        date_list     : list[str]
        all_trades    : list[dict]   — one dict per closed trade
    """
    position_size = initial_capital * POSITION_SIZE_PCT

    # Pre-compute indicator rows keyed by (ticker, date_str) for O(1) lookup
    ind: dict[str, dict[str, dict]] = {}   # ind[ticker][date_str] = row dict
    opn: dict[str, dict[str, float]] = {}  # opn[ticker][date_str] = open price

    all_dates_set: set[str] = set()

    for ticker, df in all_data.items():
        df_ind = add_indicators(df)
        ind[ticker] = {}
        for idx, row in df_ind.iterrows():
            d = str(idx.date() if hasattr(idx, "date") else idx)
            ind[ticker][d] = row.to_dict()
            all_dates_set.add(d)
        opn[ticker] = {}
        for idx, row in df.iterrows():
            d = str(idx.date() if hasattr(idx, "date") else idx)
            opn[ticker][d] = float(row["Open"])

    all_dates = sorted(all_dates_set)

    # Simulation state
    cash       = initial_capital
    positions  : dict[str, dict] = {}   # ticker → position dict
    all_trades : list[dict]      = []
    equity_curve: list[float]    = []
    date_list  : list[str]       = []
    prev_date  : str | None      = None

    for day_str in all_dates:

        # ── 1. ENTRIES at today's open (signal from yesterday) ──────────────
        if prev_date and len(positions) < MAX_POSITIONS and cash >= position_size:
            for ticker in UNIVERSE:
                if ticker in positions:
                    continue
                if ticker not in ind or prev_date not in ind[ticker]:
                    continue
                if not _buy_signal(ind[ticker][prev_date]):
                    continue
                if day_str not in opn.get(ticker, {}):
                    continue

                entry_price = opn[ticker][day_str]
                if entry_price <= 0:
                    continue
                shares = position_size / entry_price
                cash  -= shares * entry_price

                positions[ticker] = {
                    "entry_date":   day_str,
                    "entry_price":  entry_price,
                    "running_high": entry_price,
                    "shares":       shares,
                    "cost":         shares * entry_price,
                    "last_close":   entry_price,
                    "days":         0,
                }
                if len(positions) >= MAX_POSITIONS or cash < position_size:
                    break

        # ── 2. EXITS at today's close ────────────────────────────────────────
        for ticker in list(positions.keys()):
            if ticker not in ind or day_str not in ind[ticker]:
                continue
            pos  = positions[ticker]
            row  = ind[ticker][day_str]
            close = float(row["Close"])

            pos["running_high"] = max(pos["running_high"], close)
            should_exit, reason = _sell_signal(row, pos["entry_price"], pos["running_high"])

            if should_exit:
                exit_price = close
                pnl_pct    = (exit_price - pos["entry_price"]) / pos["entry_price"] * 100
                cash      += pos["shares"] * exit_price
                all_trades.append({
                    "ticker":       ticker,
                    "entry_date":   pos["entry_date"],
                    "exit_date":    day_str,
                    "entry_price":  round(pos["entry_price"], 4),
                    "exit_price":   round(exit_price, 4),
                    "pnl_pct":      round(pnl_pct, 2),
                    "pnl_dollar":   round(pos["shares"] * exit_price - pos["cost"], 2),
                    "holding_days": pos["days"],
                    "exit_reason":  reason,
                    "win":          pnl_pct > 0,
                })
                del positions[ticker]

        # ── 3. MARK TO MARKET ────────────────────────────────────────────────
        port_value = cash
        for ticker, pos in positions.items():
            if ticker in ind and day_str in ind[ticker]:
                close = float(ind[ticker][day_str]["Close"])
                pos["last_close"] = close
                pos["days"]      += 1
                port_value       += pos["shares"] * close
            else:
                port_value += pos["shares"] * pos["last_close"]

        equity_curve.append(port_value)
        date_list.append(day_str)
        prev_date = day_str

    # ── Close any remaining open positions at last known price ───────────────
    last_day = date_list[-1] if date_list else "?"
    for ticker, pos in list(positions.items()):
        exit_price = pos["last_close"]
        pnl_pct    = (exit_price - pos["entry_price"]) / pos["entry_price"] * 100
        all_trades.append({
            "ticker":       ticker,
            "entry_date":   pos["entry_date"],
            "exit_date":    last_day + " (open)",
            "entry_price":  round(pos["entry_price"], 4),
            "exit_price":   round(exit_price, 4),
            "pnl_pct":      round(pnl_pct, 2),
            "pnl_dollar":   round(pos["shares"] * exit_price - pos["cost"], 2),
            "holding_days": pos["days"],
            "exit_reason":  "end-of-data",
            "win":          pnl_pct > 0,
        })

    return equity_curve, date_list, all_trades


# ── Statistics ──────────────────────────────────────────────────────────────────

def compute_stats(equity_curve: list, trades: list, benchmark_df: pd.DataFrame | None,
                  initial_capital: float) -> dict:
    if not equity_curve or not trades:
        return {}

    equity = np.array(equity_curve, dtype=float)
    daily_ret = np.diff(equity) / equity[:-1]

    total_return_pct = (equity[-1] / equity[0] - 1) * 100

    sharpe = (
        float(daily_ret.mean() / daily_ret.std() * math.sqrt(252))
        if len(daily_ret) > 1 and daily_ret.std() > 0 else 0.0
    )

    running_max  = np.maximum.accumulate(equity)
    drawdowns    = (equity - running_max) / running_max * 100
    max_drawdown = float(drawdowns.min())

    wins   = [t for t in trades if t["win"]]
    losses = [t for t in trades if not t["win"]]
    win_rate  = len(wins) / len(trades) * 100 if trades else 0
    avg_win   = sum(t["pnl_pct"] for t in wins)   / len(wins)   if wins   else 0.0
    avg_loss  = sum(t["pnl_pct"] for t in losses) / len(losses) if losses else 0.0
    total_gain = sum(t["pnl_pct"] for t in wins)
    total_loss = abs(sum(t["pnl_pct"] for t in losses))
    pf = round(total_gain / total_loss, 2) if total_loss > 0 else float("inf")

    avg_hold = sum(t["holding_days"] for t in trades) / len(trades) if trades else 0

    exit_counts: dict[str, int] = {}
    for t in trades:
        exit_counts[t["exit_reason"]] = exit_counts.get(t["exit_reason"], 0) + 1

    bm_return = None
    if benchmark_df is not None and not benchmark_df.empty:
        bm_close = benchmark_df["Close"].dropna()
        if len(bm_close) >= 2:
            bm_return = float((bm_close.iloc[-1] / bm_close.iloc[0] - 1) * 100)

    return {
        "initial_capital":      initial_capital,
        "final_equity":         round(float(equity[-1]), 2),
        "total_return_pct":     round(total_return_pct, 2),
        "benchmark_return_pct": round(bm_return, 2) if bm_return is not None else None,
        "sharpe_ratio":         round(sharpe, 3),
        "max_drawdown_pct":     round(max_drawdown, 2),
        "total_trades":         len(trades),
        "winning_trades":       len(wins),
        "losing_trades":        len(losses),
        "win_rate_pct":         round(win_rate, 1),
        "avg_win_pct":          round(avg_win, 2),
        "avg_loss_pct":         round(avg_loss, 2),
        "profit_factor":        pf if pf != float("inf") else "inf",
        "avg_holding_days":     round(avg_hold, 1),
        "exit_counts":          exit_counts,
    }


# ── Report ──────────────────────────────────────────────────────────────────────

def save_report(stats: dict, trades: list, start: str, end: str) -> Path:
    out = MEMORY_DIR / "backtest_results.md"
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    run_ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    initial = stats["initial_capital"]
    bm      = stats.get("benchmark_return_pct")
    bm_str  = f"{bm:+.2f}%" if bm is not None else "N/A"
    alpha   = (
        f"{stats['total_return_pct'] - bm:+.2f}%" if bm is not None else "N/A"
    )

    # Per-ticker summary
    by_ticker: dict[str, list] = {}
    for t in trades:
        by_ticker.setdefault(t["ticker"], []).append(t)
    ticker_rows = sorted(
        [
            {
                "ticker":    tk,
                "n":         len(ts),
                "wins":      sum(1 for t in ts if t["win"]),
                "avg_pnl":   round(sum(t["pnl_pct"] for t in ts) / len(ts), 2),
                "total_pnl": round(sum(t["pnl_pct"] for t in ts), 2),
            }
            for tk, ts in by_ticker.items()
        ],
        key=lambda x: x["total_pnl"],
        reverse=True,
    )

    sorted_trades = sorted(trades, key=lambda t: t["pnl_pct"], reverse=True)
    best10  = sorted_trades[:10]
    worst10 = sorted_trades[-10:][::-1]

    def trade_row(t: dict) -> str:
        sign = "+" if t["pnl_pct"] >= 0 else ""
        return (
            f"| {t['ticker']} | {t['entry_date']} | {t['exit_date']} "
            f"| ${t['entry_price']:.2f} | ${t['exit_price']:.2f} "
            f"| **{sign}{t['pnl_pct']:.2f}%** | {t['holding_days']}d "
            f"| {t['exit_reason']} |"
        )

    lines = [
        "# Backtest Results",
        "",
        f"**Run:** {run_ts}  ",
        f"**Period:** {start} to {end}  ",
        f"**Universe:** {len(UNIVERSE)} tickers  ",
        f"**Capital:** ${initial:,.0f} · {POSITION_SIZE_PCT*100:.0f}% per trade (${initial*POSITION_SIZE_PCT:,.0f}) · max {MAX_POSITIONS} positions  ",
        "",
        "---",
        "",
        "## Summary Statistics",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total return | **{stats['total_return_pct']:+.2f}%** |",
        f"| SPY benchmark | {bm_str} |",
        f"| Alpha vs SPY | **{alpha}** |",
        f"| Final equity | ${stats['final_equity']:,.2f} |",
        f"| Sharpe ratio | {stats['sharpe_ratio']} |",
        f"| Max drawdown | {stats['max_drawdown_pct']:.2f}% |",
        f"| Total trades | {stats['total_trades']} |",
        f"| Win rate | {stats['win_rate_pct']:.1f}% ({stats['winning_trades']}/{stats['total_trades']}) |",
        f"| Avg win | +{stats['avg_win_pct']:.2f}% |",
        f"| Avg loss | {stats['avg_loss_pct']:.2f}% |",
        f"| Profit factor | {stats['profit_factor']} |",
        f"| Avg holding period | {stats['avg_holding_days']} days |",
        "",
        "### Exit Reasons",
        "",
        "| Reason | Count |",
        "|--------|-------|",
        *[f"| {r} | {c} |" for r, c in sorted(stats["exit_counts"].items())],
        "",
        "---",
        "",
        "## Per-Ticker Summary",
        "",
        "| Ticker | Trades | Wins | Win Rate | Avg P&L% | Total P&L% |",
        "|--------|--------|------|----------|----------|------------|",
        *[
            f"| {r['ticker']} | {r['n']} | {r['wins']} "
            f"| {round(r['wins']/r['n']*100):.0f}% "
            f"| {r['avg_pnl']:+.2f}% | {r['total_pnl']:+.2f}% |"
            for r in ticker_rows
        ],
        "",
        "---",
        "",
        "## 10 Best Trades",
        "",
        "| Ticker | Entry | Exit | Entry $ | Exit $ | P&L% | Hold | Reason |",
        "|--------|-------|------|---------|--------|------|------|--------|",
        *[trade_row(t) for t in best10],
        "",
        "## 10 Worst Trades",
        "",
        "| Ticker | Entry | Exit | Entry $ | Exit $ | P&L% | Hold | Reason |",
        "|--------|-------|------|---------|--------|------|------|--------|",
        *[trade_row(t) for t in worst10],
        "",
        "---",
        "",
        "## Strategy Rules Tested",
        "",
        "**Entry** (all must be true; signal on day T, enter at day T+1 open):",
        f"- RSI-14 between {RSI_LOW} and {RSI_HIGH}",
        "- Close > MA20",
        "- Close > MA50",
        "- 1-month momentum > 0%  (close > close 20 bars ago)",
        "",
        "**Exit** (checked at day close; first trigger wins):",
        f"- Hard stop-loss: −{STOP_LOSS_PCT*100:.0f}% from entry price",
        f"- Trailing stop: −{TRAILING_STOP_PCT*100:.0f}% from running high",
        "- Signal sell: RSI > 70  OR  (close < MA20 AND MA20 < MA50)",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    return out


# ── Main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Backtest the 95-ticker trading strategy.")
    parser.add_argument("--years",   type=int,   default=3,         help="Lookback years (default: 3)")
    parser.add_argument("--capital", type=float, default=100_000.0, help="Starting capital (default: 100000)")
    args = parser.parse_args()

    initial_capital = args.capital
    end_date   = date.today()
    # Extra 30-day buffer so MA50 / RSI warmup bars are available at the start date
    start_date = end_date - timedelta(days=args.years * 365 + 90)
    start_str  = start_date.isoformat()
    end_str    = end_date.isoformat()

    print(f"\n{'='*62}")
    print(f"  BACKTEST — {args.years}-year period")
    print(f"  Data range : {start_str} to {end_str}")
    print(f"  Universe   : {len(UNIVERSE)} tickers")
    print(f"  Capital    : ${initial_capital:,.0f}  |  "
          f"${initial_capital*POSITION_SIZE_PCT:,.0f}/trade  |  "
          f"max {MAX_POSITIONS} positions")
    print(f"{'='*62}\n")

    # Download -----------------------------------------------------------------
    print("Step 1/4 — Downloading market data...")
    all_data = download_all(UNIVERSE, start_str, end_str)
    print(f"\n  Fetched data for {len(all_data)}/{len(UNIVERSE)} tickers.\n")

    print("Step 2/4 — Downloading SPY benchmark...")
    _, benchmark_df = _download_one(BENCHMARK, start_str, end_str)

    # Simulate -----------------------------------------------------------------
    print("\nStep 3/4 — Running portfolio simulation...")
    equity_curve, date_list, all_trades = simulate(all_data, initial_capital)
    print(f"  Simulation complete: {len(all_trades)} trades over {len(date_list)} trading days.\n")

    if not all_trades:
        print("ERROR: No trades were generated. Check data or signal parameters.")
        sys.exit(1)

    # Statistics ---------------------------------------------------------------
    print("Step 4/4 — Computing statistics...")
    stats = compute_stats(equity_curve, all_trades, benchmark_df, initial_capital)

    bm_pct = stats.get("benchmark_return_pct")
    alpha  = (
        f"{stats['total_return_pct'] - bm_pct:+.2f}%"
        if bm_pct is not None else "N/A"
    )

    print(f"\n{'='*62}")
    print(f"  Total return  : {stats['total_return_pct']:+.2f}%  "
          f"(SPY: {bm_pct:+.2f}%  alpha: {alpha})" if bm_pct else
          f"  Total return  : {stats['total_return_pct']:+.2f}%")
    print(f"  Final equity  : ${stats['final_equity']:,.2f}")
    print(f"  Sharpe ratio  : {stats['sharpe_ratio']}")
    print(f"  Max drawdown  : {stats['max_drawdown_pct']:.2f}%")
    print(f"  Win rate      : {stats['win_rate_pct']:.1f}%  "
          f"({stats['winning_trades']}/{stats['total_trades']} trades)")
    print(f"  Avg win       : +{stats['avg_win_pct']:.2f}%")
    print(f"  Avg loss      : {stats['avg_loss_pct']:.2f}%")
    print(f"  Profit factor : {stats['profit_factor']}")
    print(f"  Avg hold      : {stats['avg_holding_days']} days")
    print(f"{'='*62}\n")

    # Save report --------------------------------------------------------------
    out_path = save_report(stats, all_trades, start_str, end_str)
    print(f"  Report saved -> {out_path.relative_to(ROOT)}\n")


if __name__ == "__main__":
    main()

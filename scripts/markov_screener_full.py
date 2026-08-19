#!/usr/bin/env python3
"""
Full 95-ticker Markov + momentum + technical screener.

Self-contained — no local skills required. Uses market_data.py for bar
fetching (yfinance / yahoo-direct fallback) and implements all Markov
maths inline with numpy.

Usage:
    python scripts/markov_screener_full.py
    python scripts/markov_screener_full.py --years 3 --top 10 --workers 16

Output:
    memory/screener_results.md  — top N candidates + full pass/fail tables
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

# Allow importing bar/indicator helpers from the same scripts/ directory
sys.path.insert(0, str(Path(__file__).parent))
from market_data import get_bars, compute_moving_averages, compute_rsi

ROOT = Path(__file__).parent.parent
OUTPUT_FILE = ROOT / "memory" / "screener_results.md"

# ---------------------------------------------------------------------------
# Screening universe — 95 tickers
# ---------------------------------------------------------------------------

UNIVERSE: list[str] = [
    # Mega-cap tech (10)
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AMD", "AVGO", "CRM",
    # Additional tech / software (9)
    "ADBE", "ORCL", "INTU", "IBM", "ACN", "NFLX", "DIS", "INTC", "PYPL",
    # Semis (10)
    "AMAT", "LRCX", "KLAC", "MRVL", "ARM", "ASML", "MU", "WDC", "SNDK", "STX",
    "QCOM",  # note: adds 1 more semi
    # Communications / interactive (0 — already covered above)
    # Financials — banks & brokers (7)
    "JPM", "V", "MA", "GS", "BAC", "MS", "BLK",
    # Financials — exchanges & data (5)
    "SCHW", "SPGI", "MCO", "ICE", "CME",
    # Financials — insurance (4)
    "AON", "MMC", "AIG", "MET",
    # Berkshire (1)
    "BRK-B",
    # Healthcare — pharma & biotech (10)
    "UNH", "LLY", "ABBV", "TMO", "AMGN", "JNJ", "MRK", "PFE", "GILD", "REGN",
    # Healthcare — devices & services (6)
    "ABT", "DHR", "ISRG", "SYK", "ELV", "ZTS",
    # Consumer staples (7)
    "WMT", "PG", "COST", "KO", "PEP", "MDLZ", "PM",
    # Consumer discretionary (5)
    "HD", "MCD", "NKE", "SBUX", "TXN",
    # Energy (2)
    "XOM", "CVX",
    # Industrials (6)
    "HON", "CAT", "GE", "UPS", "BA", "RTX",
    # Materials / utilities (3)
    "LIN", "NEE", "MMM",
    # Other business services (1)
    "ADP",
    # ETFs / broad market (8)
    "QQQ", "IWM", "EEM", "VGK", "GLD", "XLE", "XLF", "XLV",
]

# ---------------------------------------------------------------------------
# Markov maths
# ---------------------------------------------------------------------------

# Regime indices: 0 = Bull, 1 = Bear, 2 = Sideways
_REGIME_NAMES = {0: "Bull", 1: "Bear", 2: "Sideways"}
_BULL_THRESHOLD  =  0.005   # daily return >+0.5% → Bull
_BEAR_THRESHOLD  = -0.005   # daily return < -0.5% → Bear


def _label_regimes(closes: list[float]) -> list[int]:
    """Convert a close-price series into daily regime labels (0/1/2)."""
    labels: list[int] = []
    for i in range(1, len(closes)):
        ret = (closes[i] - closes[i - 1]) / closes[i - 1]
        if ret > _BULL_THRESHOLD:
            labels.append(0)
        elif ret < _BEAR_THRESHOLD:
            labels.append(1)
        else:
            labels.append(2)
    return labels


def _build_transition_matrix(labels: list[int]) -> np.ndarray:
    """Build a 3×3 row-stochastic transition matrix from regime labels."""
    T = np.zeros((3, 3), dtype=float)
    for i in range(len(labels) - 1):
        T[labels[i], labels[i + 1]] += 1.0
    row_sums = T.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0   # avoid zero-division on unseen states
    return T / row_sums


def _stationary_distribution(T: np.ndarray) -> np.ndarray:
    """Find the stationary distribution π via power iteration (π @ T = π)."""
    pi = np.ones(3, dtype=float) / 3.0
    for _ in range(2000):
        pi_next = pi @ T
        if np.allclose(pi, pi_next, atol=1e-12):
            break
        pi = pi_next
    return pi


def _walk_forward_sharpe(closes: list[float], split: float = 0.60) -> float:
    """
    Estimate strategy Sharpe via a train/test split.

    Train: first `split` fraction → build transition matrix.
    Test:  remainder → hold next day if P(Bull|regime) > P(Bear|regime), else cash.
    Returns annualised Sharpe ratio of the strategy.
    """
    n = len(closes)
    if n < 60:
        return 0.0
    split_idx = max(30, int(n * split))

    # Train
    train_labels = _label_regimes(closes[:split_idx])
    T = _build_transition_matrix(train_labels)

    # Test
    test = closes[split_idx:]
    if len(test) < 20:
        return 0.0
    test_rets = [(test[i] - test[i - 1]) / test[i - 1] for i in range(1, len(test))]
    test_labels = _label_regimes(test)

    strat: list[float] = []
    for i, regime in enumerate(test_labels[:-1]):
        signal = float(T[regime, 0] - T[regime, 1])
        next_ret = test_rets[i + 1] if i + 1 < len(test_rets) else 0.0
        strat.append(next_ret if signal > 0 else 0.0)

    if len(strat) < 10:
        return 0.0
    arr = np.array(strat)
    std = float(arr.std())
    return 0.0 if std == 0 else float(arr.mean() / std * math.sqrt(252))


# ---------------------------------------------------------------------------
# Per-ticker analysis
# ---------------------------------------------------------------------------

def analyze_ticker(ticker: str, years: int = 10) -> dict:
    """Run the full Markov + technical analysis for one ticker."""
    result: dict = {
        "ticker": ticker,
        "regime": "Unknown",
        "markov_signal": None,
        "stat_bull_pct": None,
        "sharpe": None,
        "rsi": None,
        "ma_alignment": "unknown",
        "momentum_1m": None,
        "above_ma20": False,
        "above_ma50": False,
        "error": None,
        # phase gates
        "phase_b": False,
        "phase_c": False,
        "phase_d": False,
    }
    try:
        bars, _ = get_bars(ticker, limit=years * 260)  # ~260 trading days/year
        if len(bars) < 60:
            result["error"] = f"only {len(bars)} bars (need 60+)"
            return result

        closes = [b["c"] for b in bars]

        # ── Markov model ────────────────────────────────────────────────────
        labels = _label_regimes(closes)
        T = _build_transition_matrix(labels)
        pi = _stationary_distribution(T)

        current_regime = labels[-1] if labels else 2
        result["regime"]        = _REGIME_NAMES[current_regime]
        result["markov_signal"] = round(float(T[current_regime, 0] - T[current_regime, 1]), 4)
        result["stat_bull_pct"] = round(float(pi[0]) * 100, 1)
        result["sharpe"]        = round(_walk_forward_sharpe(closes), 3)

        # ── Phase B: Markov filter ───────────────────────────────────────────
        result["phase_b"] = (
            result["regime"] == "Bull"
            and (result["markov_signal"] or 0) > 0
            and (result["stat_bull_pct"] or 0) >= 40.0
            and (result["sharpe"] or 0) > 0.20
        )

        # ── Phase C: Momentum filter (1-month = 20 bars) ─────────────────────
        if len(closes) >= 21:
            mom = (closes[-1] - closes[-21]) / closes[-21] * 100
            result["momentum_1m"] = round(mom, 2)
        result["phase_c"] = result["phase_b"] and (result["momentum_1m"] or 0) > 0

        # ── Technical indicators ─────────────────────────────────────────────
        indicator_bars = bars[-60:]
        mas = compute_moving_averages(indicator_bars)
        rsi = compute_rsi(indicator_bars)
        result["rsi"]          = round(rsi, 1) if rsi is not None else None
        result["above_ma20"]   = bool(mas.get("above_ma20"))
        result["above_ma50"]   = bool(mas.get("above_ma50"))
        result["ma_alignment"] = mas.get("trend") or "unknown"

        # ── Phase D: Technical filter (RSI 35–70, above MA20 and MA50) ───────
        rsi_ok = rsi is not None and 35 <= rsi <= 70
        result["phase_d"] = (
            result["phase_c"]
            and result["above_ma20"]
            and result["above_ma50"]
            and rsi_ok
        )

    except Exception as exc:
        result["error"] = str(exc)[:150]

    return result


# ---------------------------------------------------------------------------
# Screener runner
# ---------------------------------------------------------------------------

def run_screener(tickers: list[str], years: int = 10, workers: int = 8) -> list[dict]:
    print(f"[screener] Analysing {len(tickers)} tickers | {years}y history | {workers} workers",
          flush=True)
    order = {t: i for i, t in enumerate(tickers)}
    results: dict[str, dict] = {}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(analyze_ticker, t, years): t for t in tickers}
        done = 0
        for fut in as_completed(futures):
            done += 1
            r = fut.result()
            results[r["ticker"]] = r
            gate = "D" if r["phase_d"] else "C" if r["phase_c"] else "B" if r["phase_b"] else "."
            err  = f"  ERR: {r['error']}" if r["error"] else ""
            if done % 10 == 0 or r["error"]:
                print(f"  [{done:2d}/{len(tickers)}] {r['ticker']:8s} [{gate}]{err}", flush=True)

    return sorted(results.values(), key=lambda r: order.get(r["ticker"], 99))


# ---------------------------------------------------------------------------
# Output writer
# ---------------------------------------------------------------------------

def write_results(all_results: list[dict], top_n: int = 10) -> None:
    passed  = sorted(
        [r for r in all_results if r["phase_d"]],
        key=lambda r: r["sharpe"] or 0, reverse=True,
    )
    top = passed[:top_n]

    b_c_only = sorted(
        [r for r in all_results if r["phase_c"] and not r["phase_d"]],
        key=lambda r: r["sharpe"] or 0, reverse=True,
    )
    phase_b_fails = [r["ticker"] for r in all_results if not r["phase_b"] and not r["error"]]
    phase_c_fails = [r["ticker"] for r in all_results if r["phase_b"] and not r["phase_c"]]
    errors        = [f"{r['ticker']}({r['error']})" for r in all_results if r["error"]]

    now      = datetime.now(timezone.utc)
    cest_str = (now + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M") + " CEST"

    def _mom(r: dict) -> str:
        m = r.get("momentum_1m")
        return f"+{m:.1f}%" if m is not None and m >= 0 else f"{m:.1f}%" if m is not None else "?"

    def _sig(r: dict) -> str:
        s = r.get("markov_signal")
        return f"+{s:.3f}" if s is not None and s >= 0 else f"{s:.3f}" if s is not None else "?"

    lines: list[str] = [
        "# Nightly Screener Results",
        "",
        f"**Run:** {cest_str}",
        f"**Universe:** {len(all_results)} tickers",
        f"**Phase B survivors (Markov):** {sum(1 for r in all_results if r['phase_b'])}",
        f"**Phase C survivors (Momentum):** {sum(1 for r in all_results if r['phase_c'])}",
        f"**Phase D survivors (Technical):** {len(passed)}",
        "",
        "---",
        "",
        f"## Top {min(top_n, len(top))} Candidates (ranked by Sharpe)",
        "",
    ]

    if top:
        lines += [
            "| Rank | Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | RSI | MA Alignment | Momentum 1M |",
            "|------|--------|--------|---------------|------------|--------|-----|--------------|-------------|",
        ]
        for i, r in enumerate(top, 1):
            lines.append(
                f"| {i} | {r['ticker']} | {r['regime']} | {_sig(r)} "
                f"| {r['stat_bull_pct']:.1f}% | +{r['sharpe']:.3f} "
                f"| {r['rsi'] or 'N/A'} | {r['ma_alignment']} | {_mom(r)} |"
            )
    else:
        lines.append("_No tickers passed all four gates today._")

    lines += [
        "",
        "---",
        "",
        "## Full Phase B+C Pass List (Markov+Momentum qualifiers — failed Technical gate)",
        "",
    ]
    if b_c_only:
        lines += [
            "| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | Momentum 1M | RSI | Tech Gate |",
            "|--------|--------|---------------|------------|--------|-------------|-----|-----------|",
        ]
        for r in b_c_only:
            lines.append(
                f"| {r['ticker']} | {r['regime']} | {_sig(r)} "
                f"| {r['stat_bull_pct']:.1f}% | {r['sharpe']:.3f} "
                f"| {_mom(r)} | {r['rsi'] or 'N/A'} | TECH:FAIL |"
            )
    else:
        lines.append("_None._")

    lines += [
        "",
        "---",
        "",
        "## Phase B Failures (Markov filter — not traded today)",
        "",
        (", ".join(phase_b_fails) if phase_b_fails else "_None._"),
        "",
        "## Phase C Failures (Momentum filter)",
        "",
        (", ".join(phase_c_fails) if phase_c_fails else "_None._"),
    ]

    if errors:
        lines += ["", "## Data Errors (skipped)", "", ", ".join(errors)]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[screener] Written → {OUTPUT_FILE}", flush=True)
    print(f"[screener] Top candidates: {[r['ticker'] for r in top]}", flush=True)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Nightly Markov screener — 95-ticker universe")
    ap.add_argument("--years",   type=int, default=3,  help="Years of price history (default 3)")
    ap.add_argument("--top",     type=int, default=10, help="Top N candidates to save (default 10)")
    ap.add_argument("--workers", type=int, default=16, help="Parallel download workers (default 16)")
    args = ap.parse_args()

    all_results = run_screener(UNIVERSE, years=args.years, workers=args.workers)
    write_results(all_results, top_n=args.top)


if __name__ == "__main__":
    main()

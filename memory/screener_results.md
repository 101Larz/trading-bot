# Nightly Screener Results

**Run:** 2026-10-19 02:08 CEST
**Universe:** 95 tickers
**Phase B survivors (Markov):** 0
**Phase C survivors (Momentum):** 0
**Phase D survivors (Technical):** 0

---

## Top 0 Candidates (ranked by Sharpe)

_No tickers passed all four gates today._

---

## Full Phase B+C Pass List (Markov+Momentum qualifiers — failed Technical gate)

_None._

---

## Phase B Failures (Markov filter — not traded today)

AAPL, MSFT, NVDA, GOOGL, AMZN, META, TSLA, AMD, AVGO, CRM, ADBE, ORCL, INTU, IBM, ACN, NFLX, DIS, INTC, PYPL, AMAT, LRCX, KLAC, MRVL, ARM, ASML, MU, WDC, SNDK, STX, QCOM, JPM, V, MA, GS, BAC, MS, BLK, SCHW, SPGI, MCO, ICE, CME, AON, AIG, MET, BRK-B, UNH, LLY, ABBV, TMO, AMGN, JNJ, MRK, PFE, GILD, REGN, ABT, DHR, ISRG, SYK, ELV, ZTS, WMT, PG, COST, KO, PEP, MDLZ, PM, HD, MCD, NKE, SBUX, TXN, XOM, CVX, HON, CAT, GE, UPS, BA, RTX, LIN, NEE, MMM, ADP, QQQ, IWM, EEM, VGK, GLD, XLE, XLF, XLV

## Phase C Failures (Momentum filter)

_None._

## Data Errors (skipped)

MMC(only 0 bars (need 60+))

---

## Diagnostics — why zero survivors (2nd consecutive run)

Markov Phase B is a 4-gate AND. Per-gate pass counts across 94 analyzable tickers:

| Gate                       | Pass count |
|----------------------------|-----------:|
| Current regime = Bull      | 31 / 94    |
| Markov signal > 0          | 90 / 94    |
| Stat Bull% ≥ 40%           | **15 / 94** |
| Walk-forward Sharpe > 0.20 | 78 / 94    |

Regime distribution across the 94 analyzable tickers: Bull 31, Bear 41, Sideways 22.

**Blocking gate: Stat Bull% ≥ 40%.** 23 tickers pass the other three gates
(Bull regime + Markov signal > 0 + Sharpe > 0.20) and ALL 23 fail only on
stationary Bull%. Max stat_bull_pct across the entire universe is 49.6%,
and strong uptrenders like COST, V, JPM, XLE, XOM, ABBV sit in the 34–38%
range.

The ±0.5% daily bull/bear threshold used to label regimes classifies most
daily returns as Sideways, which structurally caps the stationary Bull
probability for US equities around the 35–40% range. The 40% gate is
therefore filtering out well-behaved uptrenders, not noise.

### Near-miss tickers (passing 3 of 4 Phase B gates — only failing stat_bull% ≥ 40%)

Sorted by stat Bull% (closest to the 40% threshold first):

| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe  | Momentum 1M | RSI  |
|--------|--------|---------------|-----------:|--------:|------------:|-----:|
| BA     | Bull   | +0.004        | 38.0%      | +0.276  | −4.03%      | 59.1 |
| ABBV   | Bull   | +0.090        | 37.0%      | +1.025  | +8.79%      | 72.2 |
| CVX    | Bull   | +0.061        | 37.0%      | +0.611  | +7.39%      | 77.0 |
| XLE    | Bull   | +0.066        | 37.0%      | +0.783  | +6.74%      | 79.0 |
| AIG    | Bull   | +0.011        | 36.8%      | +0.646  | +7.18%      | 85.4 |
| BLK    | Bull   | +0.037        | 36.4%      | +0.709  | +6.04%      | 69.5 |
| XOM    | Bull   | +0.057        | 36.1%      | +0.849  | +9.44%      | 83.8 |
| SPGI   | Bull   | +0.058        | 36.0%      | +0.374  | +6.00%      | 75.5 |
| JPM    | Bull   | +0.062        | 35.8%      | +1.353  | −2.36%      | 58.9 |
| PM     | Bull   | +0.057        | 35.3%      | +1.105  | +9.72%      | 65.9 |
| ADP    | Bull   | +0.026        | 35.3%      | +0.375  | +6.52%      | 78.7 |
| V      | Bull   | +0.029        | 35.0%      | +0.961  | +9.32%      | 78.6 |
| COST   | Bull   | +0.091        | 34.7%      | +0.880  | +10.48%     | 79.0 |
| SBUX   | Bull   | +0.016        | 34.6%      | +0.344  | +1.76%      | 56.5 |
| CME    | Bull   | +0.049        | 34.5%      | +0.818  | +6.47%      | 85.0 |

Notes for the pre-market routine:
- Many of these show RSI > 75 (overbought) — not immediate buy candidates
  even if the Markov gate were loosened.
- Operator decision pending: whether to recalibrate the `stat_bull_pct ≥ 40%`
  gate (e.g. 35%) or widen the daily regime thresholds. **No autonomous
  threshold change made by this routine.**
- MMC remains delisted/missing; universe-replacement decision still outstanding.

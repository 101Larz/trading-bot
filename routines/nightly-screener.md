# Routine: Nightly Markov Screener
# Schedule: 02:00 CEST, Monday–Friday (runs overnight before pre-market)
# Purpose: Run the full 95-ticker Markov + momentum + technical screen.
#          Save top 10 ranked candidates to memory/screener_results.md so
#          the 9:00 AM pre-market routine can read results instantly instead
#          of spending 20–30 minutes running 95 tickers.
#
# Output file: memory/screener_results.md  (committed to GitHub after each run)

You are the autonomous trading agent for the 101Larz portfolio. It is 02:00 CEST and the US market is closed. Run the nightly screener now.

---

## Step 1 — Phase A: Run Markov Analysis on All 95 Tickers

Change to the skill directory and run every ticker. Record all four output values for each.

```
cd ~/.claude/skills/markov-hedge-fund-method
```

Run all 95 tickers:

```
uv run python -m markov_hedge_fund_method.run --ticker AAPL --years 10
uv run python -m markov_hedge_fund_method.run --ticker MSFT --years 10
uv run python -m markov_hedge_fund_method.run --ticker NVDA --years 10
uv run python -m markov_hedge_fund_method.run --ticker GOOGL --years 10
uv run python -m markov_hedge_fund_method.run --ticker AMZN --years 10
uv run python -m markov_hedge_fund_method.run --ticker META --years 10
uv run python -m markov_hedge_fund_method.run --ticker TSLA --years 10
uv run python -m markov_hedge_fund_method.run --ticker JPM --years 10
uv run python -m markov_hedge_fund_method.run --ticker V --years 10
uv run python -m markov_hedge_fund_method.run --ticker MA --years 10
uv run python -m markov_hedge_fund_method.run --ticker UNH --years 10
uv run python -m markov_hedge_fund_method.run --ticker JNJ --years 10
uv run python -m markov_hedge_fund_method.run --ticker XOM --years 10
uv run python -m markov_hedge_fund_method.run --ticker CVX --years 10
uv run python -m markov_hedge_fund_method.run --ticker WMT --years 10
uv run python -m markov_hedge_fund_method.run --ticker HD --years 10
uv run python -m markov_hedge_fund_method.run --ticker BAC --years 10
uv run python -m markov_hedge_fund_method.run --ticker PG --years 10
uv run python -m markov_hedge_fund_method.run --ticker ABBV --years 10
uv run python -m markov_hedge_fund_method.run --ticker LLY --years 10
uv run python -m markov_hedge_fund_method.run --ticker MRK --years 10
uv run python -m markov_hedge_fund_method.run --ticker PFE --years 10
uv run python -m markov_hedge_fund_method.run --ticker KO --years 10
uv run python -m markov_hedge_fund_method.run --ticker PEP --years 10
uv run python -m markov_hedge_fund_method.run --ticker COST --years 10
uv run python -m markov_hedge_fund_method.run --ticker NFLX --years 10
uv run python -m markov_hedge_fund_method.run --ticker AMD --years 10
uv run python -m markov_hedge_fund_method.run --ticker INTC --years 10
uv run python -m markov_hedge_fund_method.run --ticker DIS --years 10
uv run python -m markov_hedge_fund_method.run --ticker BA --years 10
uv run python -m markov_hedge_fund_method.run --ticker PYPL --years 10
uv run python -m markov_hedge_fund_method.run --ticker CRM --years 10
uv run python -m markov_hedge_fund_method.run --ticker ADBE --years 10
uv run python -m markov_hedge_fund_method.run --ticker QCOM --years 10
uv run python -m markov_hedge_fund_method.run --ticker TXN --years 10
uv run python -m markov_hedge_fund_method.run --ticker HON --years 10
uv run python -m markov_hedge_fund_method.run --ticker UPS --years 10
uv run python -m markov_hedge_fund_method.run --ticker CAT --years 10
uv run python -m markov_hedge_fund_method.run --ticker GS --years 10
uv run python -m markov_hedge_fund_method.run --ticker MS --years 10
uv run python -m markov_hedge_fund_method.run --ticker BLK --years 10
uv run python -m markov_hedge_fund_method.run --ticker SCHW --years 10
uv run python -m markov_hedge_fund_method.run --ticker SPGI --years 10
uv run python -m markov_hedge_fund_method.run --ticker MCO --years 10
uv run python -m markov_hedge_fund_method.run --ticker ICE --years 10
uv run python -m markov_hedge_fund_method.run --ticker CME --years 10
uv run python -m markov_hedge_fund_method.run --ticker AON --years 10
uv run python -m markov_hedge_fund_method.run --ticker MMC --years 10
uv run python -m markov_hedge_fund_method.run --ticker AIG --years 10
uv run python -m markov_hedge_fund_method.run --ticker MET --years 10
uv run python -m markov_hedge_fund_method.run --ticker AMAT --years 10
uv run python -m markov_hedge_fund_method.run --ticker LRCX --years 10
uv run python -m markov_hedge_fund_method.run --ticker KLAC --years 10
uv run python -m markov_hedge_fund_method.run --ticker MRVL --years 10
uv run python -m markov_hedge_fund_method.run --ticker ARM --years 10
uv run python -m markov_hedge_fund_method.run --ticker ASML --years 10
uv run python -m markov_hedge_fund_method.run --ticker MU --years 10
uv run python -m markov_hedge_fund_method.run --ticker WDC --years 10
uv run python -m markov_hedge_fund_method.run --ticker SNDK --years 10
uv run python -m markov_hedge_fund_method.run --ticker STX --years 10
uv run python -m markov_hedge_fund_method.run --ticker QQQ --years 10
uv run python -m markov_hedge_fund_method.run --ticker IWM --years 10
uv run python -m markov_hedge_fund_method.run --ticker EEM --years 10
uv run python -m markov_hedge_fund_method.run --ticker VGK --years 10
uv run python -m markov_hedge_fund_method.run --ticker GLD --years 10
uv run python -m markov_hedge_fund_method.run --ticker XLE --years 10
uv run python -m markov_hedge_fund_method.run --ticker XLF --years 10
uv run python -m markov_hedge_fund_method.run --ticker XLV --years 10
uv run python -m markov_hedge_fund_method.run --ticker BRK-B --years 10
uv run python -m markov_hedge_fund_method.run --ticker AVGO --years 10
uv run python -m markov_hedge_fund_method.run --ticker TMO --years 10
uv run python -m markov_hedge_fund_method.run --ticker ACN --years 10
uv run python -m markov_hedge_fund_method.run --ticker MCD --years 10
uv run python -m markov_hedge_fund_method.run --ticker ABT --years 10
uv run python -m markov_hedge_fund_method.run --ticker DHR --years 10
uv run python -m markov_hedge_fund_method.run --ticker NKE --years 10
uv run python -m markov_hedge_fund_method.run --ticker LIN --years 10
uv run python -m markov_hedge_fund_method.run --ticker ORCL --years 10
uv run python -m markov_hedge_fund_method.run --ticker PM --years 10
uv run python -m markov_hedge_fund_method.run --ticker NEE --years 10
uv run python -m markov_hedge_fund_method.run --ticker RTX --years 10
uv run python -m markov_hedge_fund_method.run --ticker AMGN --years 10
uv run python -m markov_hedge_fund_method.run --ticker SBUX --years 10
uv run python -m markov_hedge_fund_method.run --ticker IBM --years 10
uv run python -m markov_hedge_fund_method.run --ticker GE --years 10
uv run python -m markov_hedge_fund_method.run --ticker INTU --years 10
uv run python -m markov_hedge_fund_method.run --ticker ISRG --years 10
uv run python -m markov_hedge_fund_method.run --ticker GILD --years 10
uv run python -m markov_hedge_fund_method.run --ticker MDLZ --years 10
uv run python -m markov_hedge_fund_method.run --ticker ADP --years 10
uv run python -m markov_hedge_fund_method.run --ticker SYK --years 10
uv run python -m markov_hedge_fund_method.run --ticker MMM --years 10
uv run python -m markov_hedge_fund_method.run --ticker ELV --years 10
uv run python -m markov_hedge_fund_method.run --ticker REGN --years 10
uv run python -m markov_hedge_fund_method.run --ticker ZTS --years 10
```

Collect results into an internal table:

| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe |
|--------|--------|---------------|------------|--------|
| ...    | ...    | ...           | ...        | ...    |

---

## Step 2 — Phase B: Markov Filter

Keep only tickers passing **all four** gates:

| Gate | Threshold |
|------|-----------|
| Current regime | = Bull |
| Markov signal | > 0 |
| Stat Bull% | ≥ 40% |
| Walk-forward Sharpe | > 0.20 |

Discard all failures. Continue with passing tickers only.

---

## Step 3 — Phase C: Momentum Filter

For each Phase B survivor, fetch the last 25 bars:

```
python scripts/market_data.py snapshot [TICKER]
```

Compute 1-month momentum:
```
momentum_1m = (close_today - close_20_bars_ago) / close_20_bars_ago × 100
```

Keep only tickers where **momentum_1m > 0%**. Discard the rest.

---

## Step 4 — Phase D: Technical Filter

For each Phase C survivor (already have data from Step 3):

| Check | Requirement |
|-------|-------------|
| Price > MA20 | Required |
| Price > MA50 | Required |
| RSI-14 | 35 ≤ RSI ≤ 70 |

Record RSI, MA20, MA50, and MA alignment for each passing ticker.

Do **not** check the earnings calendar here — that changes daily and will be checked in the pre-market routine.

---

## Step 5 — Phase E: Rank and Select Top 10

Rank all Phase D survivors by **Sharpe score descending**. Take the top 10 (or all if fewer than 10 pass).

---

## Step 6 — Write Results to memory/screener_results.md

Overwrite `memory/screener_results.md` with the following structure (replace placeholders with actual values):

```markdown
# Nightly Screener Results

**Run:** YYYY-MM-DD HH:MM CEST
**Universe:** 95 tickers
**Phase B survivors (Markov):** N
**Phase C survivors (Momentum):** N
**Phase D survivors (Technical):** N

---

## Top 10 Candidates (ranked by Sharpe)

| Rank | Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | RSI | MA Alignment | Momentum 1M |
|------|--------|--------|---------------|------------|--------|-----|--------------|-------------|
| 1    | XXX    | Bull   | +0.xx         | xx%        | +0.xx  | xx  | bullish      | +x.x%       |
| 2    | XXX    | Bull   | +0.xx         | xx%        | +0.xx  | xx  | bullish      | +x.x%       |
| 3    | XXX    | Bull   | +0.xx         | xx%        | +0.xx  | xx  | bullish      | +x.x%       |
| ...  | ...    |        |               |            |        |     |              |             |

**MA Alignment key:** bullish = price > MA20 > MA50 | neutral = price > MA20 but MA20 < MA50 | mixed = other

---

## Full Phase B+C Pass List (all Markov+Momentum qualifiers, unsorted)

| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | Momentum 1M | RSI | Tech Gate |
|--------|--------|---------------|------------|--------|-------------|-----|-----------|
| ...    |        |               |            |        |             |     | PASS / TECH:FAIL |

---

## Phase B Failures (Markov filter — do not trade today)

Tickers failing Markov gates: [comma-separated list]

## Phase C Failures (Momentum filter)

Tickers failing momentum gate: [comma-separated list]
```

---

## Step 7 — Commit and Push Results to GitHub

Run these commands to persist results:

```
git add memory/screener_results.md
git commit -m "chore: nightly screener results YYYY-MM-DD"
git push origin main
```

If the push fails due to a non-fast-forward conflict:
```
git pull origin main --rebase
git push origin main
```

---

## Step 8 — Update Heartbeat

Write to `heartbeat.json`:
```json
{
  "last_run": "[ISO timestamp]",
  "routine": "Nightly Screener",
  "status": "success",
  "screener_candidates": [N],
  "screener_run_date": "YYYY-MM-DD"
}
```

**Nightly screener complete. Results will be read by the 09:00 AM ET pre-market routine.**

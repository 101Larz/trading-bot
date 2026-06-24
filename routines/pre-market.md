# Routine: Pre-Market Research
# Schedule: 9:00 AM ET, Monday–Friday
# Purpose: Gather intelligence before trading begins. No trades are placed in this routine.
#
# RESEARCH LOG: Append all findings to memory/research/YYYY-MM-DD.md (today's date).
# Do NOT write to memory/RESEARCH-LOG.md — that file is deprecated.
# Use this header format:
#   ## YYYY-MM-DD (Weekday) — Pre-Market (session: <session-name>)

You are the autonomous trading agent for the 101Larz portfolio. It is now pre-market (9:00 AM ET).

## Step 1 — Session Startup

Read the following files before doing anything else:
1. `memory/strategy.md`
2. `memory/lessons.md`
3. `memory/performance.md`
4. `heartbeat.json`

If `heartbeat.json` shows `"status": "error"` from the last run, investigate the error before proceeding. Write a note about it in today's journal.

## Step 2 — Initialize Today's Journal

Run: `python scripts/journal.py init`

This creates `journal/YYYY-MM-DD.md` for today if it doesn't exist.

## Step 3 — Pull Account & Position Status

Run: `python scripts/research.py account`
Run: `python scripts/research.py positions`

Record the portfolio value, cash balance, and all open positions in the journal's Portfolio Status section.

## Step 3B — Dynamic Markov Screen (60-Stock Universe → Top 3 Candidates)

This step replaces the fixed watchlist with a live daily screen. It runs every pre-market session and produces the ranked candidate list for Step 6.

### Phase A — Markov Scan (all 50 tickers)

Run the Markov regime analysis on every ticker in the screening universe. Execute from the skill directory:

```
cd ~/.claude/skills/markov-hedge-fund-method
```

**Screening universe (run all 60 in order):**
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
```

For each ticker, record these four values:
| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe |
|--------|--------|---------------|------------|--------|
| ...    | ...    | ...           | ...        | ...    |

Where:
- **Regime** = current state (Bull / Bear / Sideways)
- **Markov signal** = P(Bull | current state) − P(Bear | current state)
- **Stat Bull%** = stationary distribution weight on Bull regime
- **Sharpe** = walk-forward backtest Sharpe ratio

### Phase B — Markov Filter

Keep only tickers passing **all four** of these gates:

| Gate | Threshold | Reason |
|------|-----------|--------|
| Current regime | = Bull | Only ride confirmed uptrends |
| Markov signal | > 0 | Next-state probability favours Bull over Bear |
| Stat Bull% | ≥ 40% | Long-run regime mix has a Bull majority |
| Walk-forward Sharpe | > 0.20 | Signal adds value over a 10-year backtest |

Tickers failing any gate → mark **MARKOV:FAIL** in the journal. Do not trade them today regardless of any other signal.

### Phase C — Technical Filter (on Markov-qualified candidates only)

For each ticker that passed Phase B, run:
```
python scripts/market_data.py snapshot [TICKER]
```

Apply the technical entry filter:

| Check | Requirement | If fails |
|-------|-------------|----------|
| Price vs MA20 | price > MA20 | TECH:FAIL |
| Price vs MA50 | price > MA50 | TECH:FAIL |
| RSI-14 | 35 ≤ RSI ≤ 70 | TECH:FAIL (RSI > 70 = chasing; RSI < 35 = falling knife) |
| Earnings window | No earnings in next 5 trading days | EARNINGS:BLOCKED |

Check the earnings calendar via WebSearch: `"[TICKER] earnings date"`

### Phase D — Rank and Select Top 3

From the candidates that passed both Phase B and Phase C, rank by **Sharpe score descending**. Take the top 3. These are today's trade candidates.

Build a summary table in the journal:

```
### Screened Candidates (YYYY-MM-DD)

| Rank | Ticker | Regime | Signal | Stat Bull% | Sharpe | RSI | Trend | Action |
|------|--------|--------|--------|------------|--------|-----|-------|--------|
| 1    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx  | bullish | CANDIDATE |
| 2    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx  | bullish | CANDIDATE |
| 3    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx  | bullish | CANDIDATE |
```

If fewer than 3 candidates pass all filters, record how many passed and note **NO_TRADE** as the pre-market default for the missing slots. If zero pass, the session is NO_TRADE — stop here and skip Step 6.

**These top 3 candidates replace any fixed watchlist for today's Step 6 research.**

## Step 4 — Check Stop-Losses on Open Positions

For each open position, check if it is down ≥8% from entry price. If so, flag it in the journal with: "⚠️ STOP-LOSS CANDIDATE: [SYMBOL] — down [X]% from entry."

Do not close positions yet — execution happens in the market-open routine.

## Step 5 — Macro Research via WebSearch

Search for current macro context using **WebSearch** (not Perplexity):

1. Search: `"S&P 500 market outlook today [current date]"`
2. Search: `"US stock market pre-market futures today"`
3. Search: `"Federal Reserve news this week"`

Summarize findings in 2–3 sentences under a "## Macro Context" section in today's journal.

## Step 6 — Per-Symbol Deep Research (Top 3 Screened Candidates Only)

**Use only the top 3 candidates produced by Step 3B.** Do not pull data on tickers outside that list. If Step 3B produced zero candidates, skip this step entirely.

For each of the top 3 candidates:

**A. Market data is already pulled** (from Phase C of Step 3B — no need to re-run). Confirm you have: current price, MA20, MA50, RSI-14, trend direction.

**B. Pull Alpaca news:**
`python scripts/research.py news [SYMBOL]`

**C. WebSearch for recent news:**
Search: `"[SYMBOL] stock news today"`
Search: `"[SYMBOL] analyst rating"`

**D. Write a symbol summary in the journal:**
- Current price, trend, and Markov regime
- RSI level and interpretation
- Key news items (max 3 bullets)
- Preliminary action: **LIKELY BUY** (all gates passed) / **AVOID** (news/fundamental concern found)

**E. Calculate sizing for each LIKELY BUY:**
```
limit_price = ask × 1.0025
max_shares  = floor((portfolio_value × 0.08) / limit_price)
stop_price  = limit_price × 0.92   (8% hard stop)
target_price = limit_price × 1.15  (15% profit target)
```

Record the full trade plan (limit, stop, target, shares, est. value) in the journal so market-open can execute without recalculating.

## Step 7 — Update Heartbeat

Run: `python scripts/journal.py` (or write directly)

Update `heartbeat.json`:
```json
{
  "last_run": "[ISO timestamp]",
  "routine": "Pre-Market Research",
  "status": "success",
  "trades_placed": 0,
  "positions_count": [N],
  "cash_balance": [value],
  "portfolio_value": [value]
}
```

## Step 8 — Write Research Session to Dated File

Open `memory/research/YYYY-MM-DD.md` (create it if it doesn't exist — replace YYYY-MM-DD with today's actual date).

Append a complete session block:

```
## YYYY-MM-DD (Weekday) — Pre-Market (session: <session-name>)

### Account Snapshot
[table]

### Market Context
[bullet list]

### Markov Screen Results
| Ticker | Regime | Signal | Stat Bull% | Sharpe | RSI | Tech | Decision |
|--------|--------|--------|------------|--------|-----|------|----------|
[one row per screened ticker — PASS or reason for FAIL]

### Screened Candidates
[ranked top 3 table with full entry/stop/target plan]

### Decision: HOLD / TRADE
[rationale — reference specific filter gates that produced this candidate list]

### Sources
[links]
```

Then write a one-paragraph summary at the bottom:
- Overall market tone (risk-on / risk-off / neutral)
- Top 2–3 opportunities identified
- Any symbols to AVOID today and why
- Any open positions flagged for stop-loss review

**Pre-market routine complete. No trades placed. Market-open routine runs at 9:45 AM ET.**

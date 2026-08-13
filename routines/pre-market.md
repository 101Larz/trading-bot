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

## Step 3B — Read Nightly Screener Results

The full 95-ticker Markov + momentum + technical screen runs at 02:00 CEST each weekday night as a separate routine (`routines/nightly-screener.md`). Pre-market reads the saved output instead of re-running the screen.

### 3B-1: Load screener results

Read `memory/screener_results.md`.

Check the **Run:** timestamp at the top. It should be dated **today** (or last night — within 12 hours). If the file is missing or more than 24 hours old:
- Log a warning: "Nightly screener results stale or missing — running emergency Phase A-E screen now" then run the full screen from `routines/nightly-screener.md` inline before continuing.

### 3B-2: Apply the earnings gate (daily check — changes every day)

From the "Top 10 Candidates" table in `memory/screener_results.md`, take the top candidates in Sharpe order. For each, check the earnings calendar via WebSearch:

```
Search: "[TICKER] earnings date"
```

| Check | Requirement | If fails |
|-------|-------------|----------|
| Earnings window | No earnings in next 5 trading days | EARNINGS:BLOCKED — drop from today's list |

### 3B-3: Refresh RSI for market-open context (live price check)

Markov and momentum data from the nightly run is still valid. RSI can shift at the open, so run a quick snapshot on the top 5 survivors (earnings-cleared only):

```
python scripts/market_data.py snapshot [TICKER]
```

Apply the RSI gate with today's live reading:

| Check | Requirement |
|-------|-------------|
| RSI-14 | 35 ≤ RSI ≤ 70 at entry |

Update the candidate list: drop any ticker whose live RSI now fails the gate, and mark the reason (TECH:FAIL-RSI).

### 3B-4: Select today's Top 3

From the earnings-cleared, RSI-confirmed survivors, take the **top 3 by Sharpe** (already ranked in the screener results). These are today's trade candidates.

Build a summary table in the journal:

```
### Screened Candidates (YYYY-MM-DD)

| Rank | Ticker | Regime | Signal | Stat Bull% | Sharpe | RSI (live) | Trend | Action |
|------|--------|--------|--------|------------|--------|------------|-------|--------|
| 1    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx         | bullish | CANDIDATE |
| 2    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx         | bullish | CANDIDATE |
| 3    | ...    | Bull   | +0.xx  | xx%        | +0.xx  | xx         | bullish | CANDIDATE |
```

If fewer than 3 candidates survive after earnings + RSI gates, note **NO_TRADE** for the missing slots. If zero survive, the session is NO_TRADE — skip Step 6.

**These top 3 candidates drive today's Step 6 research.**

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

**A. Market data is already available** from the Step 3B-3 live snapshot. Confirm you have: current price, MA20, MA50, RSI-14 (live), trend direction. If any value is missing, re-run: `python scripts/market_data.py snapshot [SYMBOL]`

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
limit_price  = ask × 1.0025
max_shares   = floor((portfolio_value × 0.08) / limit_price)
stop_price   = limit_price × 0.93   (–7% hard stop — fires immediately, no hold-period bypass)
trail_stop   = running_high × 0.85  (–15% trailing stop from running high)
target_price = limit_price × 1.15   (15% profit target)
min_hold     = 5 trading days        (signal exits blocked until day 5; hard stop always active)
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
| Ticker | Regime | Signal | Stat Bull% | Sharpe | Momentum 1M | RSI | Tech | Decision |
|--------|--------|--------|------------|--------|-------------|-----|------|----------|
[one row per screened ticker — PASS or reason for FAIL (MARKOV:FAIL / MOMENTUM:FAIL / TECH:FAIL)]

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

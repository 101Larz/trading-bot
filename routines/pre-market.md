# Routine: Pre-Market Research
# Schedule: 9:00 AM ET, Monday–Friday
# Purpose: Gather intelligence before trading begins. No trades are placed in this routine.

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

## Step 3B — Markov Regime Check

Run the Markov regime analysis on each primary watchlist ticker. Execute from the skill directory:

```
cd ~/.claude/skills/markov-hedge-fund-method
uv run python -m markov_hedge_fund_method.run --ticker NVDA --years 10
uv run python -m markov_hedge_fund_method.run --ticker AAPL --years 10
uv run python -m markov_hedge_fund_method.run --ticker GOOGL --years 10
uv run python -m markov_hedge_fund_method.run --ticker COST --years 10
uv run python -m markov_hedge_fund_method.run --ticker AMD --years 10
```

For each ticker, record in today's journal:
- **Current regime** (Bull / Bear / Sideways)
- **Markov signal** = P(Bull | current state) − P(Bear | current state) — positive means long bias, negative means short bias
- **Bull persistence** from the transition matrix diagonal

**Gate rule: only proceed to Step 6 per-symbol research for a ticker if BOTH conditions hold:**
1. Current regime = Bull
2. Markov signal is positive (P→Bull > P→Bear from current state)

If either condition fails, mark the ticker as **AVOID (Markov)** in the journal and skip its Step 6 research for today. Do not place trades on tickers that fail this gate regardless of other signals.

## Step 4 — Check Stop-Losses on Open Positions

For each open position, check if it is down ≥8% from entry price. If so, flag it in the journal with: "⚠️ STOP-LOSS CANDIDATE: [SYMBOL] — down [X]% from entry."

Do not close positions yet — execution happens in the market-open routine.

## Step 5 — Macro Research via WebSearch

Search for current macro context using **WebSearch** (not Perplexity):

1. Search: `"S&P 500 market outlook today [current date]"`
2. Search: `"US stock market pre-market futures today"`
3. Search: `"Federal Reserve news this week"`

Summarize findings in 2–3 sentences under a "## Macro Context" section in today's journal.

## Step 6 — Per-Symbol Research

For each active symbol in `watchlist.json`, do the following:

**A. Pull market data:**
`python scripts/market_data.py snapshot [SYMBOL]`

Note: current price, 20-day MA, 50-day MA, RSI-14, trend direction.

**B. Pull Alpaca news:**
`python scripts/research.py news [SYMBOL]`

**C. WebSearch for recent news:**
Search: `"[SYMBOL] stock news today"`
Search: `"[SYMBOL] analyst rating"`

**D. Write a symbol summary in the journal:**
- Current price and trend (bullish/bearish/mixed)
- RSI level and interpretation
- Key news items (max 3 bullets)
- Preliminary action: WATCH / LIKELY BUY / LIKELY SELL / AVOID

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

## Step 8 — Pre-Market Summary

At the end of the journal's Research section, write a one-paragraph summary:
- Overall market tone (risk-on / risk-off / neutral)
- Top 2–3 opportunities identified
- Any symbols to AVOID today and why
- Any open positions flagged for stop-loss review

**Pre-market routine complete. No trades placed. Market-open routine runs at 9:45 AM ET.**

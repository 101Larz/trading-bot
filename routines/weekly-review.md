# Routine: Weekly Review
# Schedule: Friday 5:00 PM ET
# Purpose: Reflect on the full trading week, update strategy if warranted, plan for next week.

You are the autonomous trading agent for the 101Larz portfolio. The trading week has ended.

## Step 1 — Weekly Performance Calculation

Read all journal files for this week (Monday–Friday): `journal/YYYY-MM-DD.md`

Compile:
- Total trades placed this week
- Winning trades (count and total P&L)
- Losing trades (count and total P&L)
- Weekly win rate
- Week's net P&L ($) and (%)
- SPY weekly return (benchmark comparison) — use WebSearch: `"SPY weekly return this week [date]"`
- Maximum intraday drawdown this week
- Any daily loss limit events?

## Step 2 — Position Review

Run: `python scripts/research.py positions`

For each open position:
- How long has it been held?
- Is the thesis still intact?
- Is it approaching a profit target (up ≥15%) or stop-loss (down ≥8%)?
- Any weekend risk (earnings Monday AM, geopolitical events)?

Flag any positions to close **before the weekend** if weekend risk is high. Execute if warranted.

## Step 3 — Watchlist Review via WebSearch

For each symbol in `watchlist.json`, search for the week's highlights:
- `"[SYMBOL] stock week in review [date]"`
- `"[SYMBOL] next week catalyst earnings"`

Update `memory/watchlist-notes.md` with any significant thesis changes.

## Step 4 — Macro Review

Search:
- `"S&P 500 weekly performance [date]"`
- `"stock market outlook next week [date]"`
- `"economic data releases next week"`

Note upcoming macro events that could impact the portfolio (Fed meetings, CPI, jobs report, major earnings).

## Step 5 — Strategy Review

Read `memory/strategy.md` and `memory/lessons.md`.

Answer these questions:
1. Is the core strategy working? (Win rate ≥45% over ≥10 trades?)
2. Are there any rules that were broken this week? If so, why, and what's the fix?
3. Are there any new patterns worth adding to the strategy?
4. Should any symbols be removed from or added to the watchlist?

If any **rule changes** are warranted, update `memory/strategy.md` with the change and the reasoning.

## Step 6 — Update Performance Log

Open `memory/performance.md` and update the Summary Statistics table with the latest cumulative numbers.

## Step 7 — Write Weekly Review Journal Entry

Create a weekly summary file: `journal/week-YYYY-WW.md`

Structure:
```
# Weekly Review — Week of [Monday date]

## Performance Summary
[Table with weekly stats vs SPY benchmark]

## Best Trade
[Symbol, entry/exit, reasoning, P&L]

## Worst Trade
[Symbol, entry/exit, what went wrong, lesson]

## Open Positions at Week End
[Table of current holdings]

## Next Week Preview
[Top 3 symbols to watch, key macro events, any strategy adjustments]

## Strategy Health Check
[Win rate, rule compliance, any changes made]
```

## Step 8 — Send Weekly Digest

Run: `python scripts/notify.py digest` (or directly send the weekly review file)

## Step 9 — Update Heartbeat

Update `heartbeat.json`:
- routine: "Weekly Review"
- status: "success"
- Include final weekly portfolio value

**Weekly review complete. See you Monday at 9:00 AM ET.**

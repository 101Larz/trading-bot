# /weekly-review — Run the Weekly Review Routine On-Demand

Trigger the full weekly review outside of the scheduled Friday 5 PM ET routine.

## Usage
`/weekly-review`

## Steps

Follow the complete weekly review routine defined in `routines/weekly-review.md`.

Key steps:
1. Read all journal files for the current week
2. Calculate weekly P&L and compare to SPY via WebSearch
3. Review all open positions for weekend risk
4. Search for next week's macro events and earnings calendar
5. Update `memory/performance.md` with the week's stats
6. Update `memory/lessons.md` if applicable
7. Update `memory/watchlist-notes.md` with any thesis changes
8. Create `journal/week-YYYY-WW.md` with the weekly summary
9. Send digest via `python scripts/notify.py digest`
10. Update heartbeat

For the full step-by-step procedure, read `routines/weekly-review.md` and follow it completely.

## WebSearch Queries to Include
- `"S&P 500 weekly return [current week]"`
- `"stock market earnings next week [date]"`
- `"economic calendar next week [date]"`
- Per-symbol: `"[SYMBOL] week in review [date]"`

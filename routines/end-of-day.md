# Routine: End of Day
# Schedule: 4:15 PM ET, Monday–Friday (15 minutes after close)
# Purpose: Close the trading day — final positions, journal reflection, performance update, digest email.

You are the autonomous trading agent for the 101Larz portfolio. The market has just closed (4:15 PM ET).

## Step 1 — Final Portfolio Snapshot

Run: `python scripts/research.py account`
Run: `python scripts/research.py positions`

Record:
- Final cash balance
- Final portfolio value
- All open positions (symbol, qty, market value, unrealized P&L)
- Today's total realized P&L (sum of closed trade P&L)
- Today's unrealized P&L (sum of open position unrealized_pl)

Update the journal's **Portfolio Status** section with final end-of-day numbers.

## Step 2 — Close Any Day-Trade Orders Still Open

Run: `python scripts/trade.py orders`

Any `day` orders that are still `open` should have been auto-cancelled by Alpaca at market close. Confirm and log.

## Step 3 — Trades Summary

In the journal's **Trades Executed** table, verify all trades from today are recorded. Fill in any gaps.

## Step 4 — Positions Closed Today

In the **Positions Closed** section, list any positions fully exited today:
| Symbol | Entry Price | Exit Price | Qty | P&L | Exit Reason |

## Step 5 — End-of-Day Reflection (Required — Even on Zero-Trade Days)

Write a reflection in the **End-of-Day Reflection** section covering:

1. **What happened today:** Market tone, major moves, key events.
2. **Trade review:** For each trade placed, was the decision correct in hindsight? Why?
3. **What I'd do differently:** Be honest. One specific lesson if applicable.
4. **Tomorrow's watchlist:** Which symbols to prioritize in pre-market? Any catalysts (earnings, Fed speakers, economic data)?
5. **Thesis check on open positions:** Are all open positions still valid? Flag any to consider closing tomorrow.

## Step 6 — Update Performance Log

Open `memory/performance.md` and append a row to the Daily P&L Log:

| [today's date] | [start value] | [end value] | [daily P&L $] | [daily P&L %] | [trades count] | [notes] |

Update the Summary Statistics section if any values have changed materially.

## Step 7 — Update Lessons (If Applicable)

If today produced a notable lesson (good or bad), append it to `memory/lessons.md` using the format defined in that file.

## Step 8 — Send Daily Digest

Run: `python scripts/notify.py digest`

This emails/Slacks/Discords today's full journal to all configured notification channels.

## Step 9 — Update Heartbeat

Update `heartbeat.json`:
```json
{
  "last_run": "[ISO timestamp]",
  "routine": "End of Day",
  "status": "success",
  "trades_placed": [total trades today],
  "positions_count": [open positions at close],
  "cash_balance": [final cash],
  "portfolio_value": [final portfolio value],
  "daily_pnl": [today's total P&L]
}
```

**End-of-day routine complete. All done for today. Pre-market resumes tomorrow at 9:00 AM ET.**

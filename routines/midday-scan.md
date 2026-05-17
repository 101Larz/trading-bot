# Routine: Midday Scan
# Schedule: 12:30 PM ET, Monday–Friday
# Purpose: Mid-session health check. Manage open positions. No new entries unless exceptional.

You are the autonomous trading agent for the 101Larz portfolio. It is 12:30 PM ET.

## Step 1 — Verify Market Is Open

Run: `python scripts/trade.py open`

If closed, update heartbeat with status "skipped" and stop.

## Step 2 — Portfolio Snapshot

Run: `python scripts/research.py account`
Run: `python scripts/research.py positions`

Calculate daily P&L so far: `(current_portfolio_value - opening_portfolio_value)`

**Check daily loss limit:** If daily P&L is a loss of ≥3% of portfolio value:
- Log "DAILY LOSS LIMIT BREACHED" in journal
- Cancel all open orders: `python scripts/trade.py cancel-all`
- Send risk alert: `python scripts/notify.py risk "Daily loss limit breached — all trading halted for today"`
- Update heartbeat with status "halted"
- **STOP — do not place any more trades today**

## Step 3 — Check Stop-Losses on All Positions

For each open position, recalculate current P&L vs entry:
`python scripts/market_data.py quote [SYMBOL]`

If any position is down ≥8% from entry:
1. Close immediately: `python scripts/trade.py close [SYMBOL]`
2. Log stop-loss execution in journal
3. Send notification: `python scripts/notify.py risk "Stop-loss: [SYMBOL] closed midday"`

## Step 4 — Quick Market Pulse via WebSearch

Search: `"stock market news midday today [date]"`
Search: `"S&P 500 performance today"`

If market conditions have materially changed since open (e.g., unexpected Fed announcement, major index down >1.5%):
- Consider whether any open positions are still valid
- If thesis is broken, close the position and log reasoning
- Do not place new buys in deteriorating conditions

## Step 5 — Review Open Orders

Run: `python scripts/trade.py orders`

If any buy orders from this morning are still open (unfilled):
- Check if the limit price is still reasonable vs current ask
- If current ask has moved >1% above your limit, cancel and reassess: `python scripts/trade.py cancel [ORDER_ID]`
- Log cancellation in journal

## Step 6 — Midday Journal Note

Append a "## Midday Check" section to today's journal:
- Current portfolio value and daily P&L
- Any stop-losses triggered
- Any orders cancelled
- Market conditions (1–2 sentences)
- Any new opportunities spotted (for market-open routine only — no new entries at midday unless exceptional and all 5 checklist items pass)

## Step 7 — Update Heartbeat

Update `heartbeat.json`:
- routine: "Midday Scan"
- status: "success" (or "halted" if daily loss limit hit)
- positions_count: [current]
- cash_balance: [current]
- portfolio_value: [current]
- daily_pnl: [current daily P&L]

**Midday scan complete. Next: End-of-Day routine at 4:15 PM ET.**

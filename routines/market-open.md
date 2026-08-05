# Routine: Market Open Execution
# Schedule: 9:45 AM ET, Monday–Friday (15 minutes after open — avoid the 9:30 spike)
# Purpose: Execute trades based on pre-market research. This is the primary trading window.
#
# RESEARCH LOG: Append all findings to memory/research/YYYY-MM-DD.md (today's date).
# Do NOT write to memory/RESEARCH-LOG.md — that file is deprecated.
# Use this header format:
#   ## YYYY-MM-DD (Weekday) — Market-Open (session: <session-name>)

You are the autonomous trading agent for the 101Larz portfolio. It is now 9:45 AM ET and the market is open.

## Step 1 — Verify Market Is Open

Run: `python scripts/trade.py open`

If the market is closed (holiday, early close), write "Market closed — no trades placed" in the journal and update heartbeat with status "skipped". Stop here.

## Step 2 — Read Pre-Market Research

Read today's journal file: `journal/YYYY-MM-DD.md`

Extract:
- The preliminary action for each symbol (WATCH / LIKELY BUY / LIKELY SELL / AVOID)
- Any stop-loss candidates flagged in pre-market
- Current cash balance and portfolio value

## Step 3 — Handle Stop-Loss Exits First

For each position flagged as a stop-loss candidate in pre-market:

1. Get the current bid price: `python scripts/market_data.py quote [SYMBOL]`
2. Run: `python scripts/risk.py` (validate the close makes sense)
3. Place the close: `python scripts/trade.py close [SYMBOL]`
4. Log the trade in the journal with reasoning "Stop-loss triggered — down [X]% from entry"
5. Send notification: `python scripts/notify.py risk "Stop-loss closed [SYMBOL] — down [X]%"`

## Step 4 — Evaluate Buy Opportunities

For each symbol with preliminary action "LIKELY BUY":

### Decision Checklist (answer all 5 before trading):
1. Is price above both 20-day MA and 50-day MA? (required)
2. Is RSI-14 between 40 and 65? (required — avoid overbought)
3. Is there no negative news catalyst in the last 48h? (required)
4. Is SPY above its own 20-day MA? (required — macro filter)
5. Would this position fit within all risk rules in CLAUDE.md? (required)

If all 5 are YES → proceed to place order.
If any are NO → log reasoning and skip, mark as NO_TRADE.

### Placing a Buy Order:
1. Get current ask: `python scripts/market_data.py quote [SYMBOL]`
2. Calculate position size: `floor((portfolio_value * 0.05) / ask_price)` shares
3. Validate: `python scripts/risk.py` checks (position size, cash reserve, daily loss, max positions)
4. Place order: `python scripts/trade.py safe-buy [SYMBOL] [QTY] [ASK_PRICE]`
   - Limit price = ask + 0.25%
5. Log the trade in the journal
6. Send alert: `python scripts/notify.py trade "[SYMBOL] BUY [QTY] @ [PRICE]"`

## Step 5 — Evaluate Sell / Exit Opportunities

For each open position with preliminary action "LIKELY SELL":

### 5A — Hard Stop (always exits immediately, no hold requirement)
- Position down ≥7% from entry → close now, no questions asked

### 5B — Signal Exits (minimum 5-day hold required)

**Check hold duration first:**
`python scripts/trade.py days-held [SYMBOL]`

If held < 5 calendar days → skip signal exits. Log "HOLD — minimum hold period (5 days) not yet reached." Hard stop in 5A still applies.

If held ≥5 days, exit if ANY of the following are true:

| Check | Threshold | Reason |
|-------|-----------|--------|
| RSI-14 overbought | RSI > 80 | Winner has run its course — lock in gain |
| Trend breakdown | price < MA20 AND MA20 < MA50 | Bullish structure broken |
| Profit target | position up ≥15% | Consider trimming 50% |
| Earnings window | earnings in < 5 trading days | Exit unless high-conviction |

Note: a 15% GTC trailing stop is already placed at time of purchase — Alpaca will auto-close if price drops 15% from the running high without any manual action needed.

If exit triggered:
1. Get current bid: `python scripts/market_data.py quote [SYMBOL]`
2. Place sell: `python scripts/trade.py safe-sell [SYMBOL] [QTY] [BID_PRICE]`
3. Log trade and exit reason in journal

## Step 6 — Decision Log for NO_TRADE Symbols

For every symbol reviewed where you decided NO_TRADE, write one line in the journal:
`- [SYMBOL]: NO_TRADE — [reason in one sentence]`

## Step 7 — Post-Trade State

After all orders are placed:
1. Run: `python scripts/research.py positions` — log updated positions
2. Run: `python scripts/research.py account` — log updated cash/portfolio value

## Step 8 — Update Heartbeat

Update `heartbeat.json` with:
- routine: "Market Open Execution"
- status: "success"
- trades_placed: [number of orders submitted]
- positions_count: [current open position count]
- cash_balance: [current cash]
- portfolio_value: [current total]

## Step 9 — Write Market-Open Session to Dated File

Append a session block to `memory/research/YYYY-MM-DD.md`:

```
## YYYY-MM-DD (Weekday) — Market-Open (session: <session-name>)

### Account Snapshot (live, 9:45 ET)
[table]

### Live Quotes
[table]

### Buy-Rule Check
[checklist]

### Decision: NO_TRADE / TRADE
[rationale]
```

**Market-open routine complete. Next: Midday Scan at 12:30 PM ET.**

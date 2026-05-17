# /status — Portfolio Status Dashboard

Show a quick overview of the current portfolio state, open positions, and bot health.

## Usage
`/status`

## Steps

1. **Check heartbeat:**
   Read `heartbeat.json` and report:
   - Last routine run, timestamp, status
   - If status is "error" → highlight prominently

2. **Account snapshot:**
   ```
   python scripts/research.py account
   ```
   Report:
   - Total portfolio value
   - Cash balance
   - Buying power
   - Equity

3. **Open positions:**
   ```
   python scripts/research.py positions
   ```
   Display as a table:
   | Symbol | Qty | Entry | Current | Unrealized P&L | % |

4. **Open orders:**
   ```
   python scripts/trade.py orders
   ```
   List any pending orders.

5. **Risk check on all positions:**
   Flag any positions currently down ≥6% from entry (approaching stop-loss).
   Flag any positions up ≥12% (approaching profit target).

6. **Daily P&L so far:**
   If today's journal exists, extract starting portfolio value and compute daily change.

7. **Market status:**
   ```
   python scripts/trade.py clock
   ```
   Report: market open/closed, time to next open or close.

8. **Output a clean dashboard:**

   ```
   === PORTFOLIO STATUS — [datetime] ===
   Portfolio Value : $XX,XXX.XX
   Cash            : $XX,XXX.XX
   Daily P&L       : +/- $XXX.XX (+/-X.X%)
   Market          : [OPEN/CLOSED]
   Last Routine    : [name] at [time] — [status]

   OPEN POSITIONS ([N])
   [table]

   ALERTS
   [any stop-loss or profit-target flags]
   ```

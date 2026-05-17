# /risk-check — Run a Full Risk Audit

Audit all open positions and pending orders against risk rules. Report any violations.

## Usage
`/risk-check`

## Steps

1. **Read risk rules** from `CLAUDE.md` and `memory/strategy.md`.

2. **Get current state:**
   ```
   python scripts/research.py account
   python scripts/research.py positions
   python scripts/trade.py orders
   ```

3. **Run risk checks:**

   **a. Daily loss limit:**
   - Get today's starting portfolio value from today's journal
   - Calculate: (current_portfolio_value - start_value) / start_value
   - Flag if daily loss ≥ 3%

   **b. Position size check** (each position):
   - Is each position ≤ 5% of current portfolio value?
   - Flag any position > 5%

   **c. Cash reserve:**
   - Is cash ≥ 20% of portfolio value?
   - Flag if below

   **d. Max positions:**
   - Is open position count ≤ 10?
   - Flag if exceeded

   **e. Stop-loss proximity:**
   - For each position, calculate % below entry
   - Flag any position down ≥ 6% (approaching 8% stop-loss)
   - Immediately flag any position down ≥ 8% (stop-loss should be triggered)

   **f. Total exposure:**
   - Sum of all position market values / portfolio value
   - Flag if > 80%

   **g. Market hours:**
   - `python scripts/trade.py clock`
   - Flag if any open orders exist outside market hours

4. **Output risk report:**

   ```
   === RISK AUDIT — [datetime] ===

   ✅ Daily Loss Limit  : [OK / ⚠️ BREACHED at X%]
   ✅ Cash Reserve      : [OK $X / ⚠️ LOW at X%]
   ✅ Max Positions     : [OK N/10 / ⚠️ EXCEEDED]
   ✅ Total Exposure    : [OK X% / ⚠️ HIGH at X%]

   POSITION DETAILS
   [SYMBOL]: X% of portfolio | P&L: [%] | [OK / ⚠️ NEAR STOP / 🚨 STOP TRIGGERED]
   ...

   VERDICT: [ALL CLEAR / N ISSUES FOUND — ACTION REQUIRED]
   ```

5. If any stop-loss is triggered (≥8% down), offer to close it immediately.

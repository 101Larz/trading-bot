# /positions — Detailed Position Analysis

Show detailed analysis of all open positions including thesis check and exit signals.

## Usage
- `/positions` — analyze all open positions
- `/positions NVDA` — analyze a specific position

## Steps

1. **Get positions:**
   ```
   python scripts/research.py positions
   ```
   If `$ARGUMENTS` specifies a symbol, filter to that position only.

2. **For each position, pull current data:**
   ```
   python scripts/market_data.py snapshot [SYMBOL]
   ```
   ```
   python scripts/research.py news [SYMBOL]
   ```

3. **WebSearch for current status:**
   `"[SYMBOL] stock news today"`

4. **For each position, output a full analysis:**

   ```
   ### [SYMBOL] — [qty] shares @ avg entry $[price]
   Current Price   : $[price]
   Market Value    : $[value]
   Unrealized P&L  : $[amount] ([%])
   Held Since      : [date if in journal]

   Technicals:
   - RSI-14: [value]
   - vs 20MA: [above/below by X%]
   - vs 50MA: [above/below by X%]
   - Trend: [bullish/bearish/mixed]

   Recent News: [1–2 key headlines]

   Exit Signals:
   - Stop-loss (down 8%): [triggered YES/NO — currently at X%]
   - Profit target (up 15%): [triggered YES/NO — currently at X%]
   - RSI overbought (>75): [YES/NO]
   - Thesis intact: [YES/NO — brief reason]

   Recommendation: [HOLD / TRIM 50% / CLOSE / MONITOR]
   ```

5. **Summary at the end:**
   - Total unrealized P&L across all positions
   - Number of positions with active exit signals
   - Any immediate action items

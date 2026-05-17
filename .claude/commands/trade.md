# /trade — Evaluate and Place a Trade

Evaluate a symbol for a trade and execute if criteria are met.

## Usage
- `/trade NVDA buy` — evaluate and attempt to buy NVDA
- `/trade NVDA sell` — evaluate and attempt to sell NVDA
- `/trade NVDA buy 10` — attempt to buy 10 shares of NVDA

## Arguments
`$ARGUMENTS` = "[SYMBOL] [side] [optional qty]"

## Steps

1. Parse arguments: symbol, side (buy/sell), optional qty.

2. **Read strategy and rules:**
   - `memory/strategy.md` (entry/exit criteria)
   - `CLAUDE.md` (risk rules)

3. **Verify market is open:**
   ```
   python scripts/trade.py open
   ```
   If closed, stop and report.

4. **Get current account state:**
   ```
   python scripts/research.py account
   python scripts/research.py positions
   ```

5. **Check daily loss limit:**
   If already down ≥3% today, refuse to trade and explain why.

6. **Run the 5-item decision checklist** (for buys):
   - Price above 20MA and 50MA?
   - RSI between 40–65?
   - No negative news catalyst?
   - SPY above its 20MA?
   - Position fits within risk rules?

   WebSearch: `"[SYMBOL] stock news today"` to check news.
   `python scripts/market_data.py snapshot [SYMBOL]` for technicals.

7. **If all criteria pass → calculate position size:**
   - qty = floor((portfolio_value × 0.05) / ask_price) unless overridden by argument
   - Run risk validation: `python scripts/risk.py`

8. **Place order:**
   - Buy: `python scripts/trade.py safe-buy [SYMBOL] [QTY] [ASK_PRICE]`
   - Sell: `python scripts/trade.py safe-sell [SYMBOL] [QTY] [BID_PRICE]`

9. **Log to journal and update heartbeat.**

10. If any check fails, output a clear NO_TRADE decision with the specific reason(s).

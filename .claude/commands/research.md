# /research — Run Research for a Symbol or Full Watchlist

Run comprehensive market research for one symbol or the entire active watchlist.

## Usage
- `/research` — research all active symbols in watchlist.json
- `/research NVDA` — research a specific symbol

## Steps

1. If a symbol argument was provided (`$ARGUMENTS`), research only that symbol. Otherwise load `watchlist.json` and research all active symbols.

2. For each symbol:

   **a. Pull market data snapshot:**
   ```
   python scripts/market_data.py snapshot [SYMBOL]
   ```
   Note: current price, 20-day MA, 50-day MA, RSI-14, trend.

   **b. Pull Alpaca news:**
   ```
   python scripts/research.py news [SYMBOL]
   ```

   **c. WebSearch for current news and analyst sentiment:**
   - `"[SYMBOL] stock news today"`
   - `"[SYMBOL] analyst rating"`

3. For each symbol, output a structured summary:
   ```
   ### [SYMBOL] — [current price]
   - Trend: [bullish/bearish/mixed] (price vs 20MA/50MA)
   - RSI-14: [value] ([interpretation])
   - Key News: [1–3 bullets]
   - Preliminary Action: [WATCH / LIKELY BUY / LIKELY SELL / AVOID]
   - Reasoning: [1–2 sentences]
   ```

4. End with a one-paragraph macro context summary using WebSearch:
   - `"S&P 500 market outlook today"`

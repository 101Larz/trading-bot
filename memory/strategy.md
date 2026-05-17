# Core Trading Strategy

**READ THIS AT THE START OF EVERY SESSION.**

---

## Philosophy

This bot is a disciplined, trend-following momentum trader. We do not predict the future — we ride confirmed trends with strict risk controls. Capital preservation comes before profit generation.

---

## Entry Criteria (all must be true)

1. **Trend confirmed**: Current price is above both the 20-day MA and 50-day MA (bullish alignment).
2. **Momentum not overextended**: RSI-14 is between 40 and 65 at entry. Avoid chasing overbought setups (RSI > 70).
3. **News sentiment**: No significant negative catalysts in the last 48 hours (check via WebSearch + Alpaca news).
4. **Macro context**: S&P 500 (SPY) is not in a confirmed downtrend (SPY above its own 20-day MA).
5. **Risk budget available**: Position would not violate any rule in the Non-Negotiable Risk Rules table in CLAUDE.md.

---

## Exit Criteria

| Trigger | Action |
|---------|--------|
| Stop-loss: position down 8% from entry | CLOSE immediately, no exceptions |
| Profit target: position up 15% | Consider trimming 50% |
| RSI > 75 (overbought) | Consider full exit |
| Macro reversal: SPY breaks below 50-day MA | Reduce all positions to 50% |
| Earnings in < 5 trading days | Exit entirely unless high-conviction thesis |

---

## Order Execution Rules

- **Always use limit orders.** Never place market orders.
- Buy limit: ask price + 0.25% (to ensure fill without overpaying).
- Sell limit: bid price − 0.25%.
- Time-in-force: `day` (cancel unfilled orders at close).
- Do not chase fills — if an order expires unfilled, reassess next session.

---

## Position Sizing Formula

```
Max shares = floor((portfolio_value × 0.05) / limit_price)
```

Never exceed this, even if confidence is HIGH.

---

## Research Sources (in priority order)

1. `python scripts/research.py snapshot` — Alpaca news + account state
2. `python scripts/market_data.py snapshot TICKER` — price bars, MAs, RSI
3. **WebSearch** for macro context and breaking news:
   - `"[TICKER] stock news today"`
   - `"S&P 500 market outlook this week"`
   - `"[TICKER] analyst upgrade downgrade"`

Do **not** use Perplexity. Use the built-in WebSearch tool.

---

## Model in Use

- **Claude claude-opus-4-7** (`claude-opus-4-7`) for all trading decisions.
- Use extended thinking for ambiguous setups.
- The model ID for API calls is `claude-opus-4-7`.

---

## Paper Trading Phase

Stay in paper trading until:
- [ ] 30 trading days completed with journals for all
- [ ] Win rate ≥ 45% over at least 20 closed trades
- [ ] No daily loss limit breaches
- [ ] All risk rules validated in production simulation

Set `PAPER_MODE=false` and `APCA_BASE_URL=https://api.alpaca.markets` to go live.

# Core Trading Strategy

**READ THIS AT THE START OF EVERY SESSION.**

---

## Philosophy

This bot is a disciplined, trend-following momentum trader. We do not predict the future — we ride confirmed trends with strict risk controls. Capital preservation comes before profit generation.

---

## Dynamic Screening Universe (50 stocks — re-screened every pre-market session)

There is no fixed watchlist. Every pre-market session runs a live Markov + technical screen across 50 large-cap stocks and selects the top 3 candidates ranked by Sharpe. This ensures the bot always trades the best current opportunity rather than a stale list.

### Screening Universe

| Sector | Tickers |
|--------|---------|
| Technology | AAPL, MSFT, NVDA, GOOGL, AMZN, META, TSLA, AMD, INTC, CRM, ADBE, QCOM, TXN, NFLX |
| Financials | JPM, V, MA, BAC, GS, MS, BLK, SCHW, SPGI, MCO, ICE, CME, AON, MMC, AIG, MET, PYPL |
| Healthcare | UNH, JNJ, ABBV, LLY, MRK, PFE |
| Consumer | WMT, HD, PG, KO, PEP, COST, DIS |
| Energy | XOM, CVX |
| Industrials | HON, UPS, CAT, BA |

### Screen Criteria (all four must pass)

| Gate | Threshold | What it tests |
|------|-----------|---------------|
| Current regime | = Bull | Confirms the stock is in an uptrend regime right now |
| Markov signal | > 0 | P(Bull\|current) > P(Bear\|current) — forward-looking bias is positive |
| Stationary Bull% | ≥ 40% | Long-run regime mix favours Bull (structural, not just recent) |
| Walk-forward Sharpe | > 0.20 | The Markov signal generated real alpha over a 10-year backtest |

### Technical Entry Filter (applied after Markov screen)

All Markov-qualified candidates are then checked against:
- Price > MA20 **and** Price > MA50 (bullish alignment)
- RSI-14 between 35 and 70 (momentum not overextended)
- No earnings within the next 5 trading days

### Output: Top 3 by Sharpe

Candidates passing both screens are ranked by walk-forward Sharpe (descending). The top 3 are today's trade candidates. Step 6 of the pre-market routine performs deep research only on these three.

### Last Screen Results

The screener re-runs every session — check today's `memory/research/YYYY-MM-DD.md` for the current ranked candidates. The table below is a historical reference only.

| Date | Rank 1 | Rank 2 | Rank 3 | Notes |
|------|--------|--------|--------|-------|
| 2026-05-21 | MSFT (Sharpe ~0.69 proxy) | GOOGL | — | Pre-dynamic-screen era; inferred from session logs |
| 2026-05-26 | NVDA (RSI 62.5, Sharpe est.) | — | — | First session with NVDA post-earnings clear |

---

## Entry Criteria (all must be true)

1. **Trend confirmed**: Current price is above both the 20-day MA and 50-day MA (bullish alignment).
2. **Momentum not overextended**: RSI-14 is between 35 and 70 at entry. Avoid chasing overbought setups (RSI > 70).
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
Max shares = floor((portfolio_value × 0.08) / limit_price)
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

## Research Log File Structure

Research sessions are stored as **one markdown file per trading day**:

```
memory/research/YYYY-MM-DD.md
```

- Each routine (pre-market, market-open, midday) **appends** a `## date — Routine` block to that day's file.
- Multiple routines on the same day write to the **same file** — no conflicts.
- Different calendar days never share a file — git merges are clean.
- The dashboard reads all `memory/research/*.md` files automatically.
- **Do not write to `memory/RESEARCH-LOG.md`** — that file is deprecated.

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

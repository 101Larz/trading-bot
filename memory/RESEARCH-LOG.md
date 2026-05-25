# Pre-Market Research Log — 2026-05-25 (for 2026-05-26 open)

> US markets are **closed Mon 2026-05-25 (Memorial Day)**. Next session opens Tue 2026-05-26 09:30 ET. This research targets that open.

---

## 1. Account Snapshot

| Field | Value |
|-------|-------|
| Portfolio Value | $99,972.74 |
| Equity | $99,972.74 |
| Cash | $95,068.28 |
| Long Market Value | $4,904.46 |
| Buying Power | $195,041.02 |
| Exposure | 4.9% (well within ≥20% cash rule) |
| Open Positions | 2 / 10 |
| Trades This Week (rolling) | 2 / 3 |
| Daily-loss-limit breaches | 0 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | RSI-14 | Status |
|--------|-----|-----------|---------|----------------|--------|--------|
| AAPL | 1 | $301.88 | $308.82 | +$6.94 (+2.30%) | **91.1** | **EXIT — RSI > 75 rule triggered** |
| GOOGL | 12 | $385.82 | $382.97 | -$34.20 (-0.74%) | 49.8 | Hold (price just below MA20 $385.48, above MA50 $341.14) |

Both positions carry 10% trailing-stop GTC orders.

---

## 2. Market Context

- **Holiday session:** US cash equities closed today. Futures trading thin; sentiment skewed positive on reported US/Iran progress easing oil/inflation risk.
- **SPY:** $745.64, above MA20 ($731.58) and MA50 ($696.49) — macro filter **PASSES**. But RSI-14 = **71.84 (overbought)** — broader market is extended.
- **Tape:** S&P 500 EW + Dow at fresh ATHs; "Magnificent 7" earnings gap to the rest of the S&P is narrowing — broadening rally.
- **Sector momentum:** Semis dominant — PHLX SOX +65% YTD, 22 of 23 up-sessions. Tech / Comm Services / Healthcare leading May. Veteran analysts flagging 1999-style froth + 25–30% drawdown risk.
- **Watchlist regime check (Markov primary candidates):**

| Ticker | Price | MA20 | MA50 | Trend | RSI-14 | Entry-rule status |
|--------|-------|------|------|-------|--------|-------------------|
| NVDA | $215.33 | $214.75 | $196.81 | Bullish | 62.51 | **OK** — RSI in 40–65 band, MAs aligned |
| AAPL | $308.82 | $289.22 | $270.36 | Bullish | 91.10 | **Blocked** — already held, RSI > 75 |
| GOOGL | $382.97 | $385.48 | $341.14 | Mixed | 49.80 | Hold (just under MA20) |
| COST | $1,028.24 | $1,026.25 | $1,007.01 | Bullish | 53.61 | **Blocked** — fiscal Q3 earnings May 28–29 (< 5 trading days) |
| AMD | $467.51 | $405.90 | $303.19 | Bullish | 75.22 | **Blocked** — RSI > 70 (overextended) |

---

## 3. Trade Ideas — for Tue 2026-05-26 open

### Idea A (priority): SELL AAPL — RSI-exit rule

- **Symbol / Side:** AAPL / SELL
- **Qty:** 1 (full position)
- **Rationale:** RSI-14 = 91.1, far above the strategy's RSI > 75 exit trigger. Position is +2.3% unrealized; lock the gain rather than wait for the 10% trailing stop to bleed it.
- **Limit:** bid − 0.25% (bid ref ~$304 → limit ~$303.20; re-quote at open).
- **Post-fill:** cancel companion 10% trailing-stop GTC.

### Idea B: BUY NVDA — Markov primary, clean entry

- **Symbol / Side:** NVDA / BUY (new)
- **Entry limit:** ask + 0.25% on Tuesday's open — current ask reference $215.33 → limit ~$215.87 (re-quote at open).
- **Sizing:** floor(($99,972 × 0.05) / $215.87) = **23 shares** (~$4,965 ≈ 5.0% cap; round to **20 sh** for headroom against intraday drift).
- **Stop:** 10% trailing GTC immediately after fill (initial stop ~$194.30).
- **Target:** +15% (~$248) → trim 50%.
- **Rationale:** Markov primary (Bull stat 59.4%, persistence 91.7%, Sharpe +0.307). MA20/50 aligned bullish; RSI 62.5 sits at the top edge of the 40–65 band — confirm sub-65 at open. Sector tailwind strong but SPY RSI 71.8 says don't oversize.
- **Risk:** ~$430 max loss at 10% stop on 20 sh (~0.43% of portfolio).

### Idea C (contingent): GOOGL — HOLD

- **Action:** No add. Price ($382.97) sits **just under MA20** ($385.48) — entry rule #1 (price > MA20) currently fails for new adds. Existing position is small (-0.74%, -$34) and protected by 10% trailing stop.
- **Watch:** If GOOGL prints back over MA20 with RSI still 40–65, eligible for re-evaluation. Otherwise hold and let the trailing stop manage downside.

---

## 4. Decision

**TRADE on 2026-05-26 open:**
1. **SELL AAPL 1 sh** at limit (bid − 0.25%) — RSI-exit rule.
2. **BUY NVDA 20 sh** at limit (ask + 0.25%) — Markov primary, entry criteria pass.
3. **HOLD GOOGL** — let trailing stop manage; no add until back over MA20.

### Pre-trade gate (re-run at 09:30 ET Tue):
- [ ] Re-fetch live quote + bar snapshot for AAPL, NVDA, SPY
- [ ] Confirm SPY still > MA20 (macro filter)
- [ ] Confirm NVDA RSI-14 still in 40–65 band (live, not stale)
- [ ] Confirm no overnight negative catalyst on NVDA/AAPL
- [ ] Re-compute NVDA share count from live portfolio value
- [ ] Cancel AAPL trailing-stop GTC after AAPL exit fills

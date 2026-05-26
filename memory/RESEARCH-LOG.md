# Pre-Market Research Log

## 2026-05-26 (Tuesday) — Pre-Market

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $95,068.28 |
| Portfolio Value | $100,013.27 |
| Equity | $100,013.27 |
| Buying Power | $195,081.55 |
| Long Market Value | $4,944.99 |
| Open Positions | 2 / 10 |
| Trades This Week | 0 / 3 (new week) |
| Account Status | ACTIVE |

Open positions:
| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $310.35 | +$8.47 (+2.81%) |
| GOOGL | 12 | $385.82 | $386.22 | +$4.80 (+0.10%) |

Both protected by 10% trailing-stop GTC orders. Cash 95.1% of equity — well above 20% reserve rule. First trading day after Memorial Day; weekly trade counter reset.

### Market Context
- **Macro / events**: New Fed Chair Kevin Warsh expected to take the oath today. US-Iran signaling progress on de-escalation — risk-on tilt. May consumer-confidence print due; AutoZone (AZO) and Zscaler (ZS) report earnings.
- **S&P 500**: SPY $745.64, above MA20 ($731.58) and MA50 ($696.49) — confirmed bullish trend. RSI-14 **71.84 → overbought**. Macro filter PASSES, but extension argues against chasing here.
- **Sector momentum**: Semis re-asserting leadership — PHLX Semi outperforming SPX by most in over a year. AMD +267% TTM and Data Center revenue $5.8B (+57% YoY). NVDA Q1 print landed May 20 (EPS $1.76 est, rev $78.5B est). YTD leadership still tilts to Industrials/Energy/Consumer Defensive, but May has rotated back to Tech + Comm Services.
- **Held names**:
  - **AAPL** $310.35; +2.81% unrealized. RSI-14 **91.10** (extreme overbought — strategy exit rule "RSI > 75 → consider full exit" still triggered). Bullish MA stack (price > MA20 $289 > MA50 $270). Q2 2026 print was strong (rev $111.2B +17%, EPS $2.01); $100B buyback authorized + dividend raise.
  - **GOOGL** $386.22; +0.10% unrealized. Price now **below** MA20 ($385.48), still above MA50 ($341.14) — trend **mixed**. RSI-14 49.80 (neutral). Q1 2026 blowout (rev $109.9B +22%, Cloud +63%); Gemini 3.5 launched at I/O. Headwind: EU antitrust fine (low-9-figure EUR) and $190B capex pace.
- **Earnings calendar (next 5 trading days)**: COST reports May 28 → **rules out new COST entry** (≥5-day buffer). CRM, MRVL, SNOW, SNPS, DKS on May 27. DELL, MDB, BBY, ADSK on May 28.

### Watchlist Technical Scan
| Ticker | Price | MA20 | MA50 | RSI-14 | Status | Verdict |
|--------|-------|------|------|--------|--------|---------|
| NVDA   | 215.33 | 214.75 | 196.81 | 62.51 | bullish, neutral RSI | **ENTRY-ELIGIBLE** |
| AAPL   | 308.82 | 289.22 | 270.36 | 91.10 | overbought | HOLD/TRIM — no add |
| GOOGL  | 382.97 | 385.48 | 341.14 | 49.80 | mixed (below MA20) | HOLD — no add |
| COST   | 1028.24 | 1026.25 | 1007.01 | 53.61 | bullish | **BLOCKED** — earnings May 28 |
| AMD    | 467.51 | 405.90 | 303.19 | 75.22 | overbought | NO ENTRY — RSI > 70 |

### Trade Ideas

1. **NVDA — BUY (PRIMARY)**
   - Thesis: Only watchlist ticker passing all entry criteria post-earnings. Price > MA20 > MA50, RSI 62.51 in the 40–65 band (just inside), bullish persistence 91.7% per Markov screen. Earnings already cleared (May 20) — clean catalyst window.
   - Sizing: floor(($100,013 × 0.05) / ~$228 ask) = **21 shares** max (~$4,788, ~4.79% equity).
   - Entry: limit @ ask + 0.25% — confirm in market-open routine with a live ≥20-bar snapshot.
   - Stop: 10% trailing-stop GTC immediately after fill (hard stop ~$205).
   - Target: trim 50% at +15% ($262); reassess at RSI > 75.

2. **AAPL — TRIM / FULL EXIT (RISK MGMT)**
   - Thesis: RSI 91 is **far beyond** the strategy's "RSI > 75 → consider full exit" trigger. Single share (~$310) so the trim mechanic collapses to a full exit decision. Carrying overbought-flag for the third session in a row.
   - Action at open: exit AAPL 1 sh via limit sell at bid − 0.25%; cancel paired trailing-stop on fill. Frees marginal cash and removes a stale risk flag.

3. **GOOGL — HOLD**
   - Thesis: Just lost MA20 by $2.51; MA50 still well below. RSI neutral. No catalyst exit and trailing stop still well wide (HWM $385.73, stop $347.16). Do not add; do not exit.

### Decision: **TRADE**
- Place NVDA buy (21 sh limit) at market-open routine, contingent on a fresh live-data re-check (MA stack + RSI 40–65 must still hold; SPY must remain above MA20).
- Exit AAPL position concurrently to respect the RSI > 75 rule.
- Net effect: 0/3 → 1/3 weekly trades for the new buy; one closeout (not counted against weekly buy cap).

---

## 2026-05-18 (Monday) — Pre-Market

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Long Market Value | $0.00 |
| Open Positions | 0 |
| Account Status | ACTIVE |

Fresh paper account. No open positions. No prior heartbeat (bot's first run). Performance log empty.

### Market Context
- **S&P 500 ~7,406**, modestly lower; index sank to start the week as Friday's selloff carried over.
- **Inflation/rates risk-off**: accelerating US inflation data, Treasury yields jumped, traders now fully ruling out any Fed rate cuts in 2026. Risk-off tone.
- **Major event-risk week**: NVDA + TGT earnings **Wednesday**, WMT **Thursday**. NVDA is the market's bellwether for the AI rally — binary catalyst mid-week.
- **Geopolitics**: Iran/Middle East conflict; Strait of Hormuz disruption pushing oil higher; energy price shock pressuring consumer spending.
- **Sector momentum**: Energy dominant YTD; recent-month strength in Utilities, Consumer Cyclical, Communication Services. Tech still strong YTD but pulling back with rate fears.
- **M&A movers**: Dominion Energy (D) +14% on NextEra buyout talks; LiveRamp (RAMP) +27% on Publicis all-cash acquisition (deal-driven, not tradeable on trend).

### Trade Ideas (watch only — not actioned today)
These are candidates to evaluate *after* the NVDA print and with confirmed MA/RSI data. No technicals (20/50-day MA, RSI-14) were pulled this run, so none meet the strategy's entry checklist yet.

1. **Energy / oil beneficiary (e.g. XLE or a large-cap integrated name)** — Strongest YTD sector with a live geopolitical catalyst (Hormuz, rising crude).
   - Entry: only on pullback holding above 20- & 50-day MA, RSI 40–65.
   - Stop: 8% below entry (hard rule).
   - Target: +15% (trim 50%).
2. **Utilities (e.g. XLU or NEE)** — Recent-month momentum leader; defensive in a risk-off, rate-fear tape. NEE also tied to the D buyout headline.
   - Entry: confirmed bullish MA alignment, RSI 40–65.
   - Stop: 8% below entry. Target: +15%.
3. **NVDA** — Bellwether but **earnings Wednesday (<5 trading days)** → strategy explicitly bars new entries into earnings. Re-evaluate post-print.

### Decision: **HOLD — NO_TRADE**
Rationale:
- Risk-off open: SPY pulling back two sessions on inflation/rate fears; macro entry criterion (#4) not cleanly satisfied.
- Binary NVDA catalyst Wednesday creates outsized event risk for any new long initiated today.
- No technical data (MA/RSI) pulled this run — strategy entry checklist cannot be satisfied.
- Default action under uncertainty is NO_TRADE. Capital preservation first; reassess at market-open routine and post-NVDA.

Sources:
- [Stock Market Today May 18 2026 — TheStreet](https://www.thestreet.com/latest-news/stock-market-today-may-18-2026-updates)
- [Stock market today: Nasdaq, S&P 500, Dow slip — Yahoo Finance](https://finance.yahoo.com/markets/stocks/live/stock-market-today-monday-may-18-earnings-nvidia-232705005.html)
- [Stock Market News for May 18, 2026 — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/stock-market-news-may-18-120100990.html)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [Best Performing Stocks 2026 YTD — StockTitan](https://www.stocktitan.net/rankings/stock-gains-ytd/2026)

---

## 2026-05-18 (Monday) — Pre-Market (session: keen-wright)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Open Positions | 0 |
| Status | ACTIVE |

Fresh account, all cash, no open positions. No position-specific news to review.

### Market Context
- **S&P 500 futures lower** to start the week. Both S&P 500 and Nasdaq hit record highs last week but pulled back Friday; weakness continuing Monday.
- **Inflation / rates headwind**: US 10Y Treasury yield above 4.60% — highest in a year. Recent data points to accelerating inflation; traders have fully priced out any Fed rate cuts in 2026.
- **Event risk this week**: NVDA earnings Wed 5/20 (KeyBanc PT raised to $300 from $275), TGT Wed, WMT Thu. Market is largely in wait-and-see mode ahead of NVDA.
- **Geopolitical**: US-Iran tensions keeping oil bid; potential Samsung labor strike risk to memory chip supply.
- **Sector momentum**: Semis (SOX) +65% YTD — strongest sector but extended; analysts flagging dot-com parallels and risk of a 25-30% correction.
- **Single-name movers**: LiveRamp (RAMP) +27% (Publicis $2.5B all-cash buyout), Dominion (D) +14% (NextEra buyout talks), Regeneron (REGN) -10.5% (failed Phase 3 melanoma trial).

### Trade Ideas (watch only — not actioned today)
1. **NVDA** — Trend strongly bullish, but **earnings in 2 trading days** (Wed 5/20). Strategy rule: do not enter with earnings < 5 days out. Binary event risk. *No entry.*
2. **AVGO (Broadcom)** — AI/semis leader with strong trend. RSI likely overbought after sector's 65% YTD run; violates RSI 40-65 entry rule and chases an extended move. Watch for a pullback toward the 20-day MA. Indicative: entry on pullback ~ -5% from current with 8% stop, 15% target — *no entry until RSI resets.*
3. **Cash / SPY benchmark** — With rising yields, inflation surprise, and a market-defining NVDA print midweek, the highest-EV action is to preserve capital and reassess post-NVDA.

### Decision: **HOLD / NO_TRADE**

Rationale:
- Macro backdrop is risk-off: yields at 1-year highs, inflation accelerating, Fed cuts off the table, geopolitical oil shock.
- The week's price action is hostage to NVDA earnings Wed — a binary event that violates the "no entry within 5 days of earnings" rule for the strongest-trend names.
- Leading sector (semis) is overbought and historically extended; no setup currently satisfies all five entry criteria (trend + RSI 40-65 + clean news + SPY trend + risk budget).
- Default to NO_TRADE under uncertainty. Reassess at next routine and after the NVDA print.

### Sources
- [Stock Market Today May 18 2026 — TheStreet](https://www.thestreet.com/latest-news/stock-market-today-may-18-2026-updates)
- [Stock market today: inflation fears, Nvidia — Yahoo Finance](https://finance.yahoo.com/markets/stocks/live/stock-market-today-monday-may-18-earnings-nvidia-232705005.html)
- [Stock Market News for May 18, 2026 — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/stock-market-news-may-18-120100990.html)
- [Nvidia's Next Earnings Report on May 20 — Motley Fool](https://www.fool.com/investing/2026/05/18/nvidias-next-earnings-report-on-may-20-could-send/)
- [Semiconductor Leaders SOXX, SMH, FTXL — 24/7 Wall St.](https://247wallst.com/investing/2026/05/06/semiconductor-leaders-soxx-smh-and-ftxl-are-crushing-it-on-ai-infrastructure-demand/)
- [Top Semiconductor Stocks to Watch May 2026 — Intellectia](https://intellectia.ai/blog/semiconductor-stocks-to-watch-may-2026)

---

## 2026-05-19 (Tuesday) — Pre-Market (session: keen-wright)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Fresh account, all cash, no open positions. No position-specific news to review. Max single-position size = 5% = **$5,000**.

### Market Context
- **Tape**: S&P 500 ~7,400 (SPY ~$762 last), down ~0.3%. Second consecutive session of losses, led by tech/semis.
- **Rates**: US 10Y Treasury yield broke above 4.60% — highest in a year. Headwind for equities, especially long-duration tech.
- **Catalyst**: Seagate −7% on CEO factory-capacity remarks; dragged Micron −6% and the broader memory/chip complex. Earnings due: Home Depot, Keysight, Toll Brothers.
- **Rotation**: Out of technology into **Energy, Consumer Staples, Financials**; overall earnings momentum still solid (improving breadth ex-tech).
- **Single-name**: LiveRamp (RAMP) bid on Publicis $2.2B acquisition (deal-driven, not trend-tradeable).
- **Macro filter (strategy criterion 4)**: SPY above its 20-day ($725) and 50-day ($691) MAs — **not in a confirmed downtrend**, longs permitted. Caveat: SPY RSI-14 = 73 (overbought) → index stretched, do not chase.

### Technical Screen (sector ETFs aligned with rotation)
| Symbol | Last | >MA20 | >MA50 | Trend | RSI-14 | Read |
|--------|------|-------|-------|-------|--------|------|
| XLF | 53.15 | yes | yes | bullish | 48.6 | Cleanest setup — RSI mid-range, bullish alignment |
| XLE | 62.26 | yes | yes | mixed | 62.0 | Strong sector; MA20 marginally < MA50 (weaker confirm) |
| XLP | 88.18 | yes | yes | bullish | 68.8 | Defensive bid; RSI elevated, near overbought caution |

> Note: pre-market quotes show wide bid/ask spreads (e.g. XLF bid 49.99 / ask 53.15) — likely stale. Limits below are computed off the ask per strategy; re-validate live spreads at market-open before sending orders.

### Trade Ideas (for market-open execution — not actioned pre-market)
Sizing: floor(($100,000 × 0.05) / limit). Stop = −8% entry, Target = +15% entry.

1. **XLF (primary)** — Financials, RSI 48.6, bullish MA alignment, leading-sector rotation.
   - Entry (buy limit, ask +0.25%): **$53.28** | Stop: **$49.02** | Target: **$61.27**
   - Size: ~93 shares (~$4,955)
2. **XLE (secondary)** — Energy, strong weekly sector momentum, RSI 62 (upper band).
   - Entry (buy limit, ask +0.25%): **$62.42** | Stop: **$57.43** | Target: **$71.78**
   - Size: ~80 shares (~$4,994)
3. **XLP (conditional)** — Consumer Staples, defensive vs. rising-rate/tech-weak tape. RSI 68.8 → only if RSI cools < 65.
   - Entry (buy limit, ask +0.25%): **$88.40** | Stop: **$81.33** | Target: **$101.66**
   - Size: ~56 shares (~$4,950)

### Decision: **HOLD**
Pre-market research only; market closed (no trades outside 9:30–4:00 ET). No positions to manage. SPY overbought (RSI 73) and the 10Y breakout above 4.60% is a fresh macro headwind — do not chase at the open. Queue **XLF** as primary candidate for the market-open routine, contingent on: live spread normalizing, RSI still 40–65, and no negative financials-sector catalyst in prior 48h. XLE secondary; XLP only if RSI < 65. Default remains **NO_TRADE** if conditions are not cleanly met.

### Sources
- [S&P 500 Futures — Investing.com](https://www.investing.com/indices/us-spx-500-futures)
- [Pre-market Stocks — CNN](https://www.cnn.com/markets/premarkets)
- [Stock Market Today May 18 2026 — TheStreet](https://www.thestreet.com/latest-news/stock-market-today-may-18-2026-updates)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [Premarket Movers — Benzinga](https://www.benzinga.com/premarket)

---

## 2026-05-19 (Tuesday) — Pre-Market (session: gallant-lamport)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Long Market Value | $0.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Fresh paper account, all cash, no open positions — no held-position news to review. Max single-position size = 5% = **$5,000**. Heartbeat (2026-05-18) shows last routine `success`, decision HOLD.

### Market Context
- **Tape**: S&P 500 futures little changed after two consecutive down sessions; tech/semis the drag (Seagate −7% on CEO factory-capacity remarks, Micron −6%).
- **Rates**: Treasury yields breaching key levels (2Y > 4.0%, 10Y > 4.50%, 30Y > 5.0%) — risk-off pressure on long-duration tech.
- **Event risk**: NVDA earnings after the bell **Wed 5/20** — market-defining, with "sell-the-news" risk. Today carries options-expiration volatility.
- **Geopolitics**: Middle East / US–Iran headlines still moving the tape.
- **Sector momentum (May)**: Healthcare, Technology, Consumer Cyclical leading.

### SPY Technical Read (macro filter — strategy criterion 4)
| Metric | Value |
|--------|-------|
| Last | ~738.65 |
| MA20 | 725.30 (price above) |
| MA50 | 691.04 (price above) |
| Trend | Bullish alignment |
| RSI-14 | **73.15 — overbought** |

SPY not in a confirmed downtrend (longs technically permitted), but the index is **overbought** into a risk-off, high-event-risk session — do not chase.

### Trade Ideas (watch only — not actioned pre-market)
Watchlist is tech-heavy; sizing = floor(($100,000 × 0.05) / limit), stop −8%, target +15%.

1. **MSFT** — Cloud/Azure AI; less directly exposed to the memory-chip selloff than NVDA/Micron. Candidate only on a confirmed pullback holding above the 20-day MA with RSI 40–65.
2. **GOOGL** — Search + cloud, no imminent earnings catalyst. Candidate on a constructive trend with RSI 40–65, same risk template.
3. **NVDA** — **Excluded.** Earnings in 2 trading days (Wed) violates the "no entry with earnings < 5 trading days" rule and sits at the center of the semi selloff.

### Decision: **HOLD / NO_TRADE**
Rationale:
- Pre-market research only; market closed — no trades outside 9:30–4:00 ET.
- SPY RSI 73 (overbought) — strategy avoids chasing extended momentum.
- Risk-off macro: rising yields + two down sessions + tech/semi weakness.
- Binary NVDA catalyst Wed plus today's OpEx volatility — outsized event risk for any new long.
- Default action under uncertainty is NO_TRADE. Preserve full cash; reassess at the market-open routine and post-NVDA.

### Sources
- [S&P 500 Futures — Investing.com](https://www.investing.com/indices/us-spx-500-futures)
- [Market Wavers Amid Conflicting Reports — Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [Pre-market Stocks — CNN](https://www.cnn.com/markets/premarkets)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [Top Stock Market Movers — Morningstar](https://www.morningstar.com/markets/movers)

---


## 2026-05-19 (Tuesday) — Pre-Market (session: gallant-lamport, run 2)

## 2026-05-19 (Tuesday) — Pre-Market (session: gallant-lamport, 11:04 UTC re-run)


### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Long Market Value | $0.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Fresh paper account, all cash, no open positions — no held-position news to review. Max single-position size = 5% = **$5,000**.

### Market Context

- **Tape**: S&P 500 futures down ~0.4% pre-market; second consecutive session of losses, led by tech/memory-chip weakness.
- **Rates**: 10Y Treasury yield at a one-year high (>4.60%), 30Y >5.0% — broad risk-off tone, headwind for long-duration tech.
- **Event risk**: NVDA earnings after the close **Wed 5/20** (also TGT). Market-defining binary catalyst — avoid initiating tech or earnings-window positions.
- **Geopolitics**: US–Iran tensions; oil supply-shock risk supporting energy.
- **Sector momentum**: Defensives leading — energy, consumer staples, financials, utilities firm; technology the laggard.

- **Tape**: U.S. futures slightly lower (S&P 500 / Nasdaq-100 ≈ −0.1%) after a tech-led selloff. SPY last ≈ $738. Records set last week, but Friday's bond-yield spike triggered the worst Nasdaq-100 day since Mar 27.
- **Rates**: Treasury yields breaching key levels — 2Y > 4.0%, 10Y > 4.50%, 30Y > 5.0%. Headwind for long-duration tech.
- **Geopolitics**: US–Iran tensions keep oil bid — WTI ≈ $108.66 (+3%), Brent ≈ $112.10 (+2%). Direct positive catalyst for energy.
- **Event risk**: NVDA earnings after the bell **Wed 5/20** — market-defining, "sell-the-news" risk; lack of fresh bullish AI catalysts afterward.
- **Sector momentum (May)**: Healthcare, Technology, Consumer Cyclical leading by monthly gains; **Energy** strong on the oil shock; semis (SOX) at all-time high but extended.


### Technical Screen
| Symbol | Last | >MA20 | >MA50 | Trend | RSI-14 | Read |
|--------|------|-------|-------|-------|--------|------|

| SPY | 738.65 | yes | yes | bullish | 73.2 | Macro filter passes (SPY > 20MA) but index overbought |
| XLE | 60.58 | yes | yes | mixed | 62.0 | Only candidate inside the 40–65 RSI entry band |
| XLP | 85.90 | yes | yes | bullish | 68.8 | RSI > 65 entry ceiling — fails momentum filter |

> Pre-market quotes show wide bid/ask spreads (likely stale). Limits computed off the ask per strategy; re-validate live spreads at market-open before any order.

### Trade Ideas (watch only — not actioned pre-market)
Sizing = floor(($100,000 × 0.05) / limit), stop −8%, target +15%.

1. **XLE (Energy SPDR)** — only name meeting all entry criteria (price > MA20/MA50, RSI 62).
   - Entry (buy limit, ask +0.25%): **$62.42** | Stop: **$57.43** | Target: **$71.78** | Size: ~80 sh (~$4,994)
   - Caveat: driver is a fragile geopolitical/oil spike — size conservatively.
2. **XLP (Consumer Staples)** — WATCH. Defensive bid real but RSI 68.8 above the 40–65 band. Revisit on a pullback toward MA20 (~$83.8) with RSI < 65.
3. **SPY** — WATCH. Trend bullish but RSI 73 (overbought) and NVDA catalyst lands tomorrow. No chase into an overbought index ahead of a binary event.

### Decision: **HOLD**
Rationale: pre-market research only; market closed (no trades outside 9:30–4:00 ET). Macro is risk-off (10Y at one-year high, two down sessions, geopolitical/oil overhang), SPY is overbought (RSI 73), and a market-moving NVDA print hits tomorrow after the close. Only XLE cleanly passes entry rules and its driver is a fragile geopolitical spike. Per strategy, default under uncertainty is NO_TRADE. Preserve full cash; queue XLE as the primary candidate for the market-open routine contingent on live spread, RSI still 40–65, and no negative energy catalyst — and reassess post-NVDA.

### Sources
- [S&P 500 Futures — Investing.com](https://www.investing.com/indices/us-spx-500-futures)
- [Stock futures fall as traders monitor U.S.-Iran war — CNBC](https://www.cnbc.com/2026/05/18/stock-market-today-live-updates.html)
- [Stock Market Today May 18 2026 — TheStreet](https://www.thestreet.com/latest-news/stock-market-today-may-18-2026-updates)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [Weekly Trader's Outlook — Charles Schwab](https://www.schwab.com/learn/story/weekly-traders-outlook)

| SPY | 738.65 | yes | yes | bullish | 73.2 | Macro filter OK (not a downtrend) but **overbought** — do not chase |
| XLE | 60.58 | yes | yes | mixed | 62.0 | Energy ETF; oil catalyst; RSI upper-band but ≤65 |
| CVX | 196.12 | yes | yes | mixed | 61.0 | Clean bullish alignment, RSI 61 in-range, oil beneficiary |
| XOM | 160.49 | yes | yes | mixed | 65.5 | Marginal — RSI at the 65 ceiling |
| XLV | 145.72 | yes | no | mixed | 56.6 | **Reject** — below 50-day MA (fails entry criterion 1) |
| UNH | 391.13 | yes | yes | bullish | 69.6 | **Reject** — RSI 70 (fails RSI 40–65 rule) |

> Pre-market quotes show wide/stale bid-ask (e.g. CVX/XLV ask = 0; SPY bid 717 / ask 762). Limits below computed off last/ask per strategy — **re-validate live spreads at market-open before sending any order**.

### Trade Ideas (for market-open execution — not actioned pre-market)
Sizing = floor(($100,000 × 0.05) / limit). Stop = −8% entry, Target = +15% entry.

1. **CVX (primary)** — Energy, clean bullish MA alignment, RSI 61 (in 40–65), live oil catalyst from US–Iran supply risk.
   - Entry (buy limit, ≈ last +0.25%): **$185.95** | Stop: **$171.07** | Target: **$213.84**
   - Size: ~26 shares (~$4,835)
2. **XLE (secondary)** — Energy ETF, diversified oil exposure, RSI 62.
   - Entry (buy limit, ask +0.25%): **$62.42** | Stop: **$57.43** | Target: **$71.78**
   - Size: ~80 shares (~$4,994)
3. **XOM (conditional)** — Integrated oil; only if RSI cools back below 65 (currently 65.5, at the ceiling).
   - Entry (buy limit, ≈ last +0.25%): **$169.02** | Stop: **$155.50** | Target: **$194.37**
   - Size: ~29 shares (~$4,902)

### Decision: **HOLD / NO_TRADE**
Rationale:
- Pre-market research only; market closed — no trades placed outside 9:30–4:00 ET.
- SPY RSI 73 (overbought) into a risk-off tape (yields breaching 10Y > 4.50%, 30Y > 5.0%); strategy avoids chasing extended momentum.
- Binary NVDA print Wed adds outsized cross-market event risk to any new long initiated today.
- Energy is the only sector with both a clean technical setup *and* a positive live catalyst (oil shock) — queue **CVX** as primary for the market-open routine, contingent on: live spread normalized, RSI still 40–65, no negative energy/stock catalyst in prior 48h. XLE secondary; XOM only if RSI < 65.
- Default action under uncertainty remains NO_TRADE; capital preservation first.

### Sources
- [S&P 500 Futures — Investing.com](https://www.investing.com/indices/us-spx-500-futures)
- [Market Wavers Amid Conflicting Reports on War — Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [Stock market news for May 18, 2026 — CNBC](https://www.cnbc.com/2026/05/17/stock-market-today-live-updates.html)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [Best Stocks to Buy Now: May 2026 — Motley Fool](https://www.fool.com/investing/top-stocks-to-buy-and-hold/)
- [Monthly Stock Sector Outlook 2026 — Charles Schwab](https://www.schwab.com/learn/story/stock-sector-outlook)

---

## 2026-05-20 (Wednesday) — Pre-Market (session: gallant-lamport)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Long Market Value | $0.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Fresh paper account, all cash, no held positions — no position-specific news to review. Max single-position size = 5% = **$5,000**.

### Market Context
- **Tape**: ES (June S&P 500 e-mini) ≈ −0.38% pre-market; soft tone into the NVDA print.
- **Today's main catalyst**: **NVDA reports Q1 earnings AFTER the close** — market-defining binary event for AI/semis and the broad tape.
- **This week's other earnings**: HD (Wed AM), WMT (Thu), ROST (Thu) — all within 5 trading days → excluded from new entries per strategy.
- **Sector momentum**: Semis (SOX) +65% YTD continues to lead, but technology now broadly extended; analysts flagging dot-com parallels. Some rotation hints toward financials/staples.
- **Single-name catalysts**: PIII, RXT, AGL leading May monthly momentum (small caps — outside strategy universe).

### SPY Macro Filter (strategy criterion 4)
| Metric | Value |
|--------|-------|
| Last | $733.73 |
| MA20 | $726.78 (price above) |
| MA50 | $692.18 (price above) |
| Trend | Bullish alignment |
| RSI-14 | 67.6 (neutral, slightly elevated) |

SPY is NOT in a confirmed downtrend → longs permitted. RSI slightly above 65 — do not chase.

### Technical Screen
| Symbol | Last | >MA20 | >MA50 | Trend | RSI-14 | Read |
|--------|------|-------|-------|-------|--------|------|
| MSFT | 417.42 | yes | yes | bullish | 45.4 | **Clean setup** — RSI mid-range, bullish alignment, no near earnings |
| V    | 329.91 | yes | yes | bullish | 45.8 | **Clean setup** — defensive payments, decoupled from NVDA event |
| GOOGL| 387.66 | yes | yes | bullish | 68.9 | Reject — RSI > 65 ceiling |
| AAPL | 298.97 | yes | yes | bullish | 84.1 | Reject — overbought |
| AVGO | 411.07 | no  | yes | mixed   | 52.2 | Reject — below 20-day MA |
| JPM  | 295.70 | no  | no  | mixed   | 36.9 | Reject — trend filter fails |
| WMT  | 134.20 | yes | yes | bullish | 67.2 | Reject — earnings Thu (< 5 days) |

> Pre-market quotes show wide/stale spreads (e.g. MSFT/WMT ask = 0). Limits below are computed off last; re-validate live spreads at market-open before any order.

### Trade Ideas (for market-open execution — not actioned pre-market)
Sizing = floor(($100,000 × 0.05) / limit). Stop = −8% entry, Target = +15% entry.

1. **MSFT (primary)** — Cloud/AI mega-cap, RSI 45 (mid-band), no near earnings, less binary than NVDA.
   - Entry (buy limit, last +0.25%): **$418.50** | Stop: **$385.00** | Target: **$481.00**
   - Size: ~11 shares (~$4,604)
2. **V (secondary, defensive complement)** — Payments leader, RSI 46, decoupled from NVDA tonight.
   - Entry (buy limit, last +0.25%): **$330.74** | Stop: **$304.40** | Target: **$380.40**
   - Size: ~15 shares (~$4,961)
3. **Watch only**: GOOGL (RSI too high), AVGO (sub-MA20), WMT (earnings window).

### Decision: **HOLD / NO_TRADE**
Rationale:
- Pre-market research only; market closed — no trades placed outside 9:30–4:00 ET.
- **NVDA earnings TONIGHT** is a binary cross-market event capable of moving SPY ±2–3% tomorrow. Initiating today commits capital to an exogenous binary without edge.
- MSFT and V both remain viable post-print; we lose no setup by waiting one session.
- Per strategy: default under uncertainty is NO_TRADE. Preserve full cash; reassess at market-open routine and again after the NVDA print.
- If, at market-open, conditions still qualify AND the gap is calm, plan: enter ONE position (MSFT preferred) at HALF size (~$2,500) to keep powder dry across the event.

### Sources
- [S&P 500 Futures — Investing.com](https://www.investing.com/indices/us-spx-500-futures)
- [Tech Still Struggling, but Yields, Oil Slip Early — Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [May 2026 Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)
- [5 Leading Semiconductor Stocks Dominating May 2026 — Parameter](https://parameter.io/5-leading-semiconductor-stocks-dominating-may-2026-nvidia-nvda-amd-and-more/)
- [Top Semiconductor Stocks to Watch May 2026 — Intellectia](https://intellectia.ai/blog/semiconductor-stocks-to-watch-may-2026)
- [Best Stocks to Buy Right Now for May — Motley Fool](https://www.fool.com/investing/2026/05/06/the-best-stocks-to-buy-right-now-for-may/)

---

## 2026-05-20 (Wednesday) — Market-Open (session: sweet-shannon)

### Account Snapshot (live, 9:45 ET)
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Week-to-date trade count: **0** (well below 3-trade weekly cap). Position count: **0/6**.

### Live Quotes (9:45 ET)
| Symbol | Last | Bid | Ask | Notes |
|--------|------|-----|-----|-------|
| MSFT | 418.00 | 412.93 | 418.00 | Gap roughly flat vs. pre-market plan ($418.50 entry) |
| V | 329.75 | 329.25 | 329.75 | Tight spread, slightly below pre-market plan ($330.74) |
| SPY | 737.00 | 736.53 | 737.00 | Modestly higher vs. yesterday's $733.73 |

`market_data.py snapshot` returns only **1 bar** for each name at this hour → MA20/MA50/RSI-14 cannot be re-verified live. Pre-market values stand: MSFT RSI 45.4, V RSI 45.8, both above MA20/MA50.

### Buy-Rule Check (per market-open routine)
- Max 6 open positions: ✅ 0 currently
- Max 3 trades this week: ✅ 0 used
- Max 20% equity per position: ✅ candidate sizes ≤ 5%
- Catalyst in today's RESEARCH-LOG: ✅ MSFT (primary) and V (secondary) named

### Decision: **NO_TRADE**
Rationale:
- **NVDA earnings AFTER the close tonight** is a binary cross-market event capable of moving SPY ±2–3% tomorrow. Pre-market plan was conditional on a "calm" gap and explicitly preferred to wait one session.
- Live indicators (MA/RSI) cannot be re-verified at the open (1 bar only). Strategy's default under unverifiable entry criteria is NO_TRADE.
- Capital preservation > opportunity cost: MSFT and V both remain viable post-print. No edge lost by waiting.
- `scripts/trade.py` currently has no `buy` CLI subcommand wired up; `safe_buy()` exists internally only. Not patching during a live routine.

### Plan for next routine (midday / post-NVDA)
- Re-pull MSFT and V snapshots once bar count ≥ 20 to re-verify MA/RSI.
- If NVDA print is benign and SPY holds MA20, consider opening **MSFT at half size (~6 sh ≈ $2,510)** in the midday or Thursday open routine.
- If NVDA disappoints and SPY breaks MA20 (~727), stand down further and re-evaluate the watchlist.

---

## 2026-05-21 (Thursday) — Pre-Market (session: gallant-lamport)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $100,000.00 |
| Portfolio Value | $100,000.00 |
| Equity | $100,000.00 |
| Buying Power | $200,000.00 |
| Long Market Value | $0.00 |
| Open Positions | 0 |
| Status | ACTIVE (paper) |

Fresh paper account, all cash, no held positions — no position-specific news to review. Max single-position size = 5% = **$5,000**. Heartbeat (2026-05-20) shows last routine `success`, decision HOLD.

### Market Context
- **Tape**: ES (S&P 500 e-mini) ≈ 7,440, **+0.24%** pre-market. SPY closed **+1.08%** yesterday (index 7,432.97) as oil and Treasury yields slid on Middle East de-escalation optimism.
- **NVDA earnings (released after close 5/20)**: **Beat** — EPS $1.87 vs $1.77 est; revenue $81.62B (+85% y/y) vs $79.18B est; data-center $75.2B (92% of sales); Q2 guide $89.1–92.8B vs $87.3B Street; dividend raised to $0.25. **But the stock fell >2% after-hours** — third straight post-earnings drop; "sell-the-news" pattern intact despite the beat.
- **Today's earnings calendar**: WMT, DE, ROST, RL, ZM, DECK — all within 5 trading days → excluded from new entries per strategy.
- **Breadth / rotation**: Weak internals — **<50% of S&P 500 stocks above their 200-day MA**; chips just had the worst two-day stretch since October; ongoing rotation-out-of-tech theme. SPY RSI cooled from ~77 last week to ~66.
- **Sector momentum (May)**: Utilities (leader), Healthcare, Technology. Single-name movers HCWB +128%, IMVT +35%, LICN −62% are small-caps outside the strategy universe.

### Technical Screen (`market_data.py`)
| Symbol | Price | >MA20 | >MA50 | Trend | RSI-14 | Read |
|--------|-------|-------|-------|-------|--------|------|
| SPY   | 741.25 | yes | yes | bullish | 67.8 | Macro filter OK (not a downtrend); RSI >65 — do not chase |
| MSFT  | 421.06 | yes | yes | bullish | 60.6 | **Clean setup** — RSI in 40–65 band, bullish alignment |
| GOOGL | 388.91 | yes | yes | bullish | 53.1 | **Clean setup** — RSI mid-band, bullish alignment |
| QQQ   | 713.15 | yes | yes | bullish | 73.1 | Reject — overbought (RSI >65) |
| AAPL  | 302.25 | yes | yes | bullish | 84.8 | Reject — extremely overbought |
| NVDA  | 223.47 | yes | yes | bullish | 69.8 | Reject — RSI >65 + post-earnings volatility |
| AMZN  | 265.01 | no  | yes | mixed   | 49.9 | Reject — below 20-day MA |
| META  | 605.06 | no  | no  | mixed   | 45.6 | Reject — below 20- & 50-day MA |

> **Data caveat**: `market_data.py` reports a `last_price` field that diverges materially from the MA engine's `current_price` (e.g. SPY last_price 713.48 vs current_price 741.25). The MA/RSI engine uses `current_price`, which is consistent with SPY's actual ~$743 close — `last_price` appears stale. Limits below are computed off `current_price`; **re-validate live spreads at market-open before any order.**

### Trade Ideas (for market-open execution — not actioned pre-market)
Sizing = floor(($100,000 × 0.05) / limit). Stop = −8% entry, Target = +15% entry.

1. **MSFT (primary)** — Cloud/Azure AI mega-cap, RSI 60.6 (in 40–65 band), bullish MA alignment, no imminent earnings. Carried over from yesterday's queue.
   - Entry (buy limit, current +0.25%): **$422.11** | Stop: **$388.34** | Target: **$485.43**
   - Size: **11 shares** (~$4,643)
2. **GOOGL (secondary)** — Search/Cloud/Gemini, RSI 53.1 (mid-band — cleanest momentum read), bullish alignment, no imminent earnings.
   - Entry (buy limit, current +0.25%): **$389.88** | Stop: **$358.69** | Target: **$448.36**
   - Size: **12 shares** (~$4,679)
3. **Watch only**: SPY (RSI 67.8 above the 65 ceiling), QQQ/AAPL/NVDA overbought, AMZN/META below their MAs.

### Decision: **HOLD**
Rationale:
- Pre-market research only; market closed — no trades placed outside 9:30–4:00 ET.
- NVDA **beat** but the stock still **fell after-hours** — the tech "sell-the-news" / rotation risk remains live, and S&P breadth is weak (<50% above 200-day MA).
- MSFT and GOOGL both cleanly pass the five-point entry checklist (trend + RSI 40–65 + no near earnings + SPY above 20-day MA + risk budget). Queue both for the **market-open routine**, contingent on: (a) no tech-rotation gap-down, (b) RSI still 40–65 on a ≥20-bar live snapshot, (c) SPY holding above its 20-day MA (~728).
- Given weak breadth, prefer **a single HALF-size entry (MSFT preferred, ~6 sh ≈ $2,530)** at the open rather than opening both. Default remains **NO_TRADE** if conditions do not cleanly hold.

### Sources
- [S&P 500 E-Mini Futures — Barchart](https://www.barchart.com/futures/quotes/ES*0/futures-prices)
- [Stock market news for May 20, 2026 — CNBC](https://www.cnbc.com/2026/05/19/stock-market-today-live-updates.html)
- [Nvidia (NVDA) Q1 2027 earnings report: Live updates — CNBC](https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html)
- [Nvidia tops Q1 estimates, offers upbeat outlook — Yahoo Finance](https://finance.yahoo.com/markets/stocks/article/nvidia-to-report-q1-earnings-as-chip-competition-grows-191200841.html)
- [Weekly Trader's Stock Market Outlook — Charles Schwab](https://www.schwab.com/learn/story/weekly-traders-outlook)
- [May 2026's Top Stocks by Monthly Momentum — StockTitan](https://www.stocktitan.net/rankings/stock-gains-monthly/2026/may)

---

## 2026-05-22 (Friday) — Pre-Market (session: gallant-lamport)

### Account Snapshot
| Metric | Value |
|--------|-------|
| Cash | $99,698.12 |
| Portfolio Value | $100,003.74 |
| Equity | $100,003.74 |
| Buying Power | $199,701.86 |
| Long Market Value | $305.62 |
| Open Positions | 1 |
| Status | ACTIVE (paper) |

Held position: **AAPL 1 sh** @ $301.88 avg, mark $305.62, unrealized **+$3.74 (+1.24%)**; 10% trailing-stop GTC active. Max single-position size = 5% = **$5,000**. Heartbeat (2026-05-21 EOD) shows last routine `success`, decision HOLD.

### Market Context
- **Tape**: S&P 500 futures **+0.34%** pre-market Friday; the benchmark is up ~0.5% week-to-date and on track for its **eighth straight weekly gain** despite elevated volatility. Macro filter is supportive.
- **Today's catalyst**: Final May University of Michigan Consumer Sentiment report.
- **Sector momentum**: Semiconductors remain the dominant leadership ($SOX posted a ~41% four-week advance into late April — best rally since 2000); AI infrastructure / data-center demand still driving tech. Caveat: equal-weight tech has been lagging cap-weight since end of March — strength is concentrated in the mega-caps.
- **Single-name movers**: CAVA +7.5% on strong earnings and raised guidance; MU +3% as a Samsung memory-chip strike threatens ~3% of global supply.
- **Held-position news (AAPL)**: Stock broke above $300, hit $306 on 5/21. Q2 FY26 beat (EPS $2.01 vs $1.95; revenue $111.2B; Services $30.98B; Greater China $20.5B). 28 analysts at Buy consensus, 12-mo target $308.65. Watch: iPhone supply constraints on advanced processor chips. **No negative 48h catalyst** — position thesis intact.

### Technical Screen (`market_data.py`, 60-bar yfinance)
| Symbol | Price | >MA20 | >MA50 | Trend | RSI-14 | Read |
|--------|-------|-------|-------|-------|--------|------|
| SPY   | 742.72 | yes | yes | bullish | 67.5 | Macro filter OK (above 20-day MA); RSI >65 — don't chase SPY |
| GOOGL | 387.66 | yes | yes | bullish | 51.5 | **Clean setup** — RSI mid-band, bullish alignment |
| COST  | 1050.45 | yes | yes | bullish | 60.0 | Clean RSI/trend, but earnings risk (see caveat) |
| NVDA  | 219.51 | yes | yes | bullish | 66.7 | Reject — RSI just above 65 entry ceiling |
| AMD   | 449.59 | yes | yes | bullish | 67.8 | Reject — RSI above 65 entry ceiling |
| AAPL  | 304.99 | yes | yes | bullish | 82.4 | Held — extremely overbought (see exit flag) |

> **Data caveat**: `market_data.py` again reports a `last_price` that diverges from the MA engine's `current_price` (AAPL last_price 285.74 vs current_price 304.99; SPY bid 716.42 / ask 760.80). The MA/RSI engine's `current_price` is consistent with AAPL's actual ~$305 mark. Limits below are off `current_price`; **re-validate live spreads at market-open before any order.**

### Trade Ideas (for market-open execution — not actioned pre-market)
Sizing = floor(($100,003.74 × 0.05) / limit). Stop = −8% entry, Target = +15% entry.

1. **GOOGL (primary)** — Search/Cloud/Gemini mega-cap, RSI 51.5 (cleanest mid-band read), bullish MA alignment, no imminent earnings. Passes all five entry criteria.
   - Entry (buy limit, current +0.25%): **$388.63** | Stop: **$357.54** | Target: **$446.92**
   - Size: **12 shares** (~$4,664)
2. **COST (secondary)** — Consumer-staples momentum, RSI 60.0 (in band), bullish alignment.
   - Entry (buy limit, current +0.25%): **$1,053.08** | Stop: **$968.83** | Target: **$1,211.04**
   - Size: **4 shares** (~$4,212)
   - **Caveat**: Costco fiscal Q3 typically reports late May — verify the earnings date at market-open; if within 5 trading days, exclude per strategy.
3. **Watch only**: NVDA (RSI 66.7) and AMD (RSI 67.8) both just above the 40–65 entry band — re-check for a pullback into band.

### Position Management Flag — AAPL
AAPL RSI-14 is **82.4** (extremely overbought). Strategy exit criteria: "RSI > 75 → consider full exit." Position is tiny (1 sh, ~$306) with a 10% trailing stop active, so risk is contained — but the **market-open routine should consider trimming/closing AAPL** to lock the +1.2% gain rather than ride an overbought name.

### Decision: **TRADE**
Rationale:
- Macro supportive: futures +0.34%, eighth straight weekly gain, SPY above its 20- and 50-day MAs.
- **GOOGL** cleanly passes the five-point entry checklist (trend + RSI 51.5 in 40–65 band + no near earnings + SPY above 20-day MA + risk budget available). Queue as the **primary market-open entry**.
- **COST** is a clean secondary, contingent on confirming its earnings date is >5 trading days out.
- Pre-market research only — no orders placed outside 9:30–4:00 ET. Execution at the market-open routine is contingent on live re-validation: (a) no gap-down, (b) RSI still 40–65 on a ≥20-bar live snapshot, (c) SPY holding above its 20-day MA (~730). Default to **NO_TRADE** if conditions do not cleanly hold.
- Separately, evaluate trimming/closing the overbought AAPL position at the open.

### Sources
- [Stock futures rise as S&P 500 looks toward another winning week — CNBC](https://www.cnbc.com/2026/05/21/stock-market-today-live-updates.html)
- [Nvidia, Fed Minutes on Marquee as Stocks Up Early — Charles Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [7 Best-Performing Semiconductor Stocks for May 2026 — NerdWallet](https://www.nerdwallet.com/investing/learn/best-semiconductor-stocks)
- [Apple AAPL Stock Reaches $306 — FX Leaders](https://www.fxleaders.com/news/2026/05/21/apple-aapl-stock-reaches-306-as-strong-fundamentals-offset-growing-supply-concerns/)
- [NVIDIA (NVDA) Stock Forecast & Analyst Price Targets — StockAnalysis](https://stockanalysis.com/stocks/nvda/forecast/)


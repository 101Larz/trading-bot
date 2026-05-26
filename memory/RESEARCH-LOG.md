# Pre-Market Research Log — 2026-05-25 (for 2026-05-26 open)

 claude/gallant-lamport-53nWG
> US markets are **closed Mon 2026-05-25 (Memorial Day)**. Next session opens Tue 2026-05-26 09:30 ET. This research targets that open.

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

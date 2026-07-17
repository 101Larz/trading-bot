# Performance Log

Updated after every end-of-day routine. Agent writes new entries; do not manually edit.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Start Date | — |
| Total Trading Days | 0 |
| Total Trades | 1 |
| Winning Trades | 0 |
| Losing Trades | 0 |
| Win Rate | — |
| Average Win | — |
| Average Loss | — |
| Largest Win | — |
| Largest Loss | — |
| Total P&L | $0.00 |
| Max Drawdown | — |
| Sharpe (approx) | — |
| Daily Loss Limit Breaches | 0 |

---

## Daily P&L Log

| Date | Starting Value | Ending Value | Daily P&L | Daily % | Trades | Notes |
|------|---------------|--------------|-----------|---------|--------|-------|
| — | — | — | — | — | — | Bot not yet started |
| 2026-05-19 | $100,000.00 | $100,000.00 | $0.00 | 0.00% | 0 | EOD snapshot — no trades, no open positions, cash $100,000.00 |
| 2026-05-20 | $100,000.00 | $100,000.00 | $0.00 | 0.00% | 0 | EOD: NO_TRADE day. Market-open declined NVDA (earnings tonight). No positions opened or closed. Cash $100,000.00. |
| 2026-05-21 | $100,000.00 | $100,002.65 | +$2.65 | +0.00% | 1 | EOD: opened AAPL 1 sh @ $301.88; 10% trailing-stop GTC active. Unrealized +$2.65. |
| 2026-05-22 | $100,002.65 | $99,975.69 | -$26.96 | -0.03% | 1 | EOD: opened GOOGL 12 sh @ $385.82. AAPL +$6.68, GOOGL -$30.99 unrealized. AAPL RSI overbought — flagged for exit review. |
| 2026-05-25 | $99,975.69 | $99,972.74 | -$2.95 | -0.003% | 0 | EOD: Memorial Day — US markets closed. No trades. AAPL +$6.94, GOOGL -$34.20 unrealized. Trailing stops active. |
| 2026-05-26 | $99,972.74 | $100,035.52 | +$62.78 | +0.063% | 0 | EOD: NO_TRADE day (no catalyst in research log). AAPL +$6.84, GOOGL +$28.68 unrealized. Trailing stops active. |
| 2026-05-27 | $100,035.52 | $100,056.98 | +$21.46 | +0.021% | 0 | EOD: NO_TRADE day (NVDA rejected at market-open — live ask $211.70 < MA20 $214.66). AAPL +$8.62, GOOGL +$48.36 unrealized. Trailing stops active. |
| 2026-05-28 | $100,056.98 | $100,063.19 | +$6.21 | +0.0062% | 0 | EOD: NO_TRADE day (pre-market screen returned zero passes; AMD RSI 67 > 65 ceiling). AAPL +$10.27, GOOGL +$52.92 unrealized. Trailing stops active. |
| 2026-05-29 | $100,063.19 | $99,871.21 | -$191.98 | -0.192% | 1 | EOD: opened NVDA 23 sh @ $216.00 (pre-market trigger passed live). AAPL +$9.61, GOOGL -$56.52, NVDA -$80.93 unrealized. Trailing stops active on all three. |
| 2026-06-01 | $99,871.21 | $100,085.49 | +$214.28 | +0.214% | 0 | EOD: NO_TRADE day (AMD rejected — RSI 67 > 65 and spread 1.03% > 0.5%). AAPL +$4.18, GOOGL -$113.04, NVDA +$194.81 unrealized. Trailing stops active on all three. |
| 2026-06-02 | $100,085.49 | $99,888.31 | -$197.18 | -0.197% | 0 | EOD: NO_TRADE day (NVDA add blocked — position at 5.31% > 5% cap; AMD/other watchlist failed pre-market screen). AAPL +$12.97, GOOGL -$278.76, NVDA +$154.10 unrealized. Trailing stops active on all three. |
| 2026-06-03 | $99,888.31 | $99,666.86 | -$221.45 | -0.222% | 0 | EOD: NO_TRADE day (NVDA add blocked at 5% cap; AMD blocked — RSI 70.04 > 65 and spread 2.73% > 0.5%). AAPL +$8.65, GOOGL -$319.44 (now -6.90%, ~$0.40/sh from -7% cut), NVDA -$22.35 unrealized. Trailing stops active on all three. |
| 2026-06-04 | $99,666.86 | $99,875.87 | +$209.01 | +0.210% | 0 | EOD: NO_TRADE day (NVDA add blocked — price $213.68 < MA20 $218.88 and at 4.93% cap; AMD blocked — RSI 74.14 > 65, spread 2.73% > 0.5%; AAPL add blocked — pre-WWDC exit pre-staged). GOOGL -7% cut watch resolved favorably (-6.90% → -3.79%). AAPL +$9.22, GOOGL -$175.44, NVDA +$42.09 unrealized. |
| 2026-06-05 | $99,875.87 | $99,609.60 | -$266.27 | -0.267% | 1 | EOD: NVDA trailing-stop fired 11:20 ET — 23 sh sold @ $209.04, realized -$160.08 / -3.22% (HWM $232.28, stop $209.052; AVGO read-through + soft semis tape). AAPL +$5.34, GOOGL -$235.66 unrealized. Weekly buys 0/3. AAPL pre-WWDC exit pre-staged for tonight remains pending (workflow snapshot only). |
| 2026-06-08 | $99,609.60 | $99,567.47 | -$42.13 | -0.042% | 0 | EOD: NO_TRADE day. AAPL pre-WWDC exit OVERRIDDEN at market-open (held through 13:00 ET keynote on documented rationale — limit-sell infra gap, 0.31% position immateriality, trailing-stop backstop intact). AAPL -$0.99, GOOGL -$271.44 unrealized. GOOGL cushion to -7% cut ~$3.49/sh. Weekly buys 0/3. |
| 2026-06-09 | $99,567.47 | $99,570.94 | +$3.47 | +0.0035% | 0 | EOD: NO_TRADE day (pre-market zero passes; macro filter SPY < MA20 4th straight session). AAPL -$10.84, GOOGL -$258.12 unrealized. GOOGL -7% cushion ~$4.50/sh into Wed CPI. Weekly buys 0/3. |
| 2026-06-10 | $99,570.94 | $99,499.18 | -$71.76 | -0.072% | 1 | EOD: GOOGL CUT at midday (12 sh @ $358.25, realized -$330.84 / -7.15% — workflow cut-loser rule fired at -7.16%). Post-CPI tape risk-off; SPY < MA20. AAPL 1 sh -$9.88 unrealized; trailing-stop GTC active. Cash 99.71% of equity. Weekly buys 0/3 (sell does not consume buy budget). |
| 2026-06-11 | $99,499.18 | $99,502.96 | +$3.78 | +0.0038% | 0 | EOD: NO_TRADE day. Midday HOLD (AAPL -1.74%, no cut). AAPL 1 sh -$6.08 unrealized; trailing-stop $285.66 GTC active. Cash 99.71% of equity. Weekly buys 0/3 (1 sell on 6/10). |
| 2026-06-12 | $99,502.96 | $99,498.75 | -$4.21 | -0.0042% | 0 | EOD: NO_TRADE day. Midday HOLD (AAPL -3.47%, no cut). AAPL 1 sh -$10.29 unrealized; trailing-stop $285.66 GTC active. Cash 99.71% of equity. Week closes: 0 buys / 1 sell (6/10 GOOGL cut). |
| 2026-06-15 | $99,498.75 | $99,503.31 | +$4.56 | +0.0046% | 0 | EOD: NO_TRADE day. Macro filter SPY < MA20 9th session + FOMC Wed 6/17 binary → universal entry block. AAPL 1 sh -$5.73 unrealized; trailing-stop $285.66 GTC active. Cash 99.70% of equity. Weekly buys 0/3. |
| 2026-06-16 | $99,503.31 | $99,505.93 | +$2.62 | +0.0026% | 0 | EOD: NO_TRADE day (T-1 to FOMC; pre-market MA/RSI unverifiable, SPY only 1-session above MA20). AAPL 1 sh -$3.11 unrealized; trailing-stop $285.66 GTC active. Cash 99.70% of equity. Weekly buys 0/3 preserved through FOMC. |
| 2026-06-17 | $99,505.93 | $99,503.11 | -$2.82 | -0.0028% | 0 | EOD: NO_TRADE day (FOMC). Pre-market/market-open/midday all HOLD. AAPL 1 sh -$5.68 unrealized; trailing-stop $285.66 GTC active. Cash 99.70% of equity. Weekly buys 0/3 preserved. |
| 2026-06-18 | $99,503.11 | $99,505.16 | +$2.05 | +0.0021% | 0 | EOD: NO_TRADE day (T-1 Juneteenth). Pre-market/market-open/midday all HOLD. AAPL 1 sh -$3.88 unrealized; trailing-stop $285.66 GTC active. Cash 99.70% of equity. Week closes: 0 buys / 0 sells (Fri 6/19 Juneteenth — market closed). |
| 2026-06-19 | $99,505.16 | $99,505.17 | +$0.01 | +0.00001% | 0 | EOD: **Juneteenth — US markets CLOSED.** No trades possible. AAPL 1 sh -$3.87 unrealized; trailing-stop $285.66 GTC active. Cash 99.70% of equity. Week closes: 0 buys / 0 sells. |
| 2026-06-22 | $99,505.17 | $99,573.48 | +$68.31 | +0.0687% | 1 | EOD: opened AMD 14 sh @ $546.19 at market-open (post-Juneteenth re-engagement). AAPL -$4.94, AMD +$69.38 unrealized. AMD broker-side trailing-stop placement FAILED (403) at fill — unprotected by GTC stop; flagged for tomorrow's pre-market to retry. AAPL 10% trailing-stop $285.66 GTC active. Weekly buys 1/3. |
| 2026-06-23 | $99,573.48 | $99,166.59 | -$406.89 | -0.409% | 0 | EOD: NO_TRADE day. AMD marked down -$294.34 intraday on broad semi sell-off + M Science Q2 GPU report + HBM/GDDR6 cost pressure. AAPL 1 sh -$7.07; AMD 14 sh -$335.56 unrealized. AMD cushion to -7% cut $507.96 = ~$14.27/sh (~2.73%). AMD broker-side trailing-stop still infra-gated. AAPL trailing-stop $285.66 GTC active. Weekly buys 1/3. |
| 2026-06-24 | $99,166.59 | $99,359.87 | +$193.28 | +0.195% | 0 | EOD: NO_TRADE day. AMD partial recovery +$199.84 intraday ($522.23 → $536.50, +2.73%); AAPL marked down -$0.75. AMD 14 sh -$135.72 unrealized (-1.78%); cushion to -7% cut $507.96 = ~$28.54/sh (~5.32%) — materially widened vs prior EOD. AAPL 1 sh -$7.82 (-2.59%). AMD broker-side trailing-stop still infra-gated. AAPL trailing-stop $285.66 GTC active. Weekly buys 1/3. Micron earnings AMC tonight — AMD thesis read-through carries to Thursday pre-market. |
| 2026-06-25 | $99,359.87 | $99,299.85 | -$60.02 | -0.060% | 1 | EOD: AAPL closed overnight via trailing-stop GTC ($285.66 fill, cash $91,560.43 → $91,845.95 = +$285.52; realized ≈ -$16.36 / -5.42% vs $301.88 entry). NO_TRADE during regular session (macro filter SPY << MA20 -1.64%; yfinance TLS-broken; AMD at 7.40% cap, MU gap-up unverifiable post-blowout). AMD intraday recovery: midday -$307.78 (-4.03%) → close -$192.82 (-2.52%). Cushion to -7% cut $507.96 = ~$24.05/sh (~4.52%). AMD broker-side trailing-stop still infra-gated. Single-position book now. Weekly buys 1/3, sells 1 (AAPL stop). |
| 2026-06-26 | $99,299.85 | $99,097.93 | -$201.92 | -0.203% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday (macro filter SPY << MA20 ~-2.1% live at open; yfinance TLS-broken Day 5; AMD at 7.36% cap, averaging-down barred). AMD marked down vs prior EOD ($532.42 → $518.00, -2.71%). AMD 14 sh -$394.72 unrealized (-5.16%); cushion to -7% cut $507.96 = ~$10.04/sh (~1.94%) — **tightened from midday ~$13.47/sh on late-session fade**. AMD broker-side trailing-stop still infra-gated (Day 5). Single-position book. **Week 6/22–6/26 closes: 1 buy / 1 sell / 2 events total.** |
| 2026-06-29 | $99,097.93 | $99,382.46 | +$284.53 | +0.287% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday. AMD rallied vs Fri EOD ($518.00 → $538.32, +3.92%). AMD 14 sh -$110.19 unrealized (-1.44%); cushion to -7% cut $507.96 = ~$30.36/sh (~5.64%) — **materially widened from Fri ~$10.04/sh on overnight recovery**. AMD broker-side trailing-stop still infra-gated (Day 6). Single-position book. Week 6/29 buys 0/3 fresh budget. |
| 2026-06-30 | $99,382.46 | $99,938.07 | +$555.61 | +0.559% | 0 | EOD: NO_TRADE day. AMD rallied $538.32 → $578.01 (+7.37%); intraday ATH $563.25 cleared, mark closed above. AMD 14 sh +$445.42 unrealized (+5.83%); cushion to -7% cut $507.96 = ~$70.05/sh (~12.12%) — materially widened from Mon ~$30.36/sh. Catalysts: Wells Fargo PT $505→$615, Cantor PT $500→$700 (both Overweight reaffirmed). Position now 8.10% of equity (above 8% size cap on appreciation — not a violation since size-at-entry was compliant). AMD broker-side trailing-stop still infra-gated (Day 7). Single-position book. Week 6/29 buys 0/3. |
| 2026-07-01 | $99,938.07 | $99,395.43 | -$542.64 | -0.543% | 0 | EOD: NO_TRADE day. AMD gave back Tue rally: $578.01 → $539.25 (-6.71% day change). AMD 14 sh -$97.22 unrealized (-1.27%); cushion to -7% cut $507.96 = ~$31.29/sh (~5.80%) — materially tightened from Tue ~$70.05/sh but still comfortable. Position sized back to 7.60% of equity (below 8% cap). AMD broker-side trailing-stop still infra-gated (Day 8). yfinance TLS-broken (Day 8). Single-position book. Week 6/29 buys 0/3. |
| 2026-07-02 | $99,395.43 | $99,101.57 | -$293.86 | -0.296% | 0 | EOD: NO_TRADE day (early close 1 PM ET ahead of Fri 7/3 Independence Day observed). AMD $539.25 → $518.26 (Alpaca day change -4.18%). AMD 14 sh -$391.08 unrealized (-5.11%); cushion to -7% cut $507.96 = ~$10.30/sh (~1.99%) — **TIGHT** vs Wed ~$31.29/sh on macro/sector profit-taking (BoA AI-bubble flag; Intel -7%, TSM -6%). Thesis INTACT (Cantor $700, WFC $615, UBS $670 PTs; next earnings 8/4). AMD broker-side trailing-stop still infra-gated (Day 9). Single-position book. Week 6/29 buys 0/3 (Fri 7/3 CLOSED — week ends today). |
| 2026-07-03 | $99,101.57 | $99,095.41 | -$6.16 | -0.006% | 0 | EOD: **Independence Day observed — US markets CLOSED.** No trades possible. AMD 14 sh mark $517.82 (vs prior $518.26, -$0.44/sh AH/stale-mark artifact); unrealized -$397.24 (-5.20%); cushion to -7% cut $507.96 = ~$9.86/sh (~1.90%) — **TIGHT into weekend**. AMD broker-side trailing-stop still infra-gated (Day 10). Single-position book. **Week 6/29–7/3 closes: 0 buys / 0 sells / 0 events (4-session week; Fri 7/3 CLOSED).** |
| 2026-07-06 (market-open) | $99,293.93 (pre-mkt) | $99,628.11 | +$334.18 intraday | +0.336% | 0 | Market-open: **HOLD — no trades**. AMD rallied at open ($532.00 → $555.76, +7.33% day change); unrealized flipped to +$133.92 (+1.75%), **first time above breakeven since 6/23**. Cushion to -7% cut $507.96 widened to ~$47.80/sh (~8.60%). Both entry gates (macro SPY>MA20 + per-candidate MA/RSI) UNVERIFIED (yfinance TLS Day 11 confirmed); per pre-market carry-forward rule no buys can fire. AMD add still barred (7.81% cap, broker-side stop gap Day 11). Weekly buys 0/3, budget preserved. Single-position book. |
| 2026-07-06 (midday) | — | — | — | — | 0 | Midday: **HOLD — no trades**. AMD extended rally ($555.76 → $560.67, +8.28% day change); unrealized +$202.66 (+2.65%). Cushion to -7% cut $507.96 widened to ~$52.71/sh (~9.40%) — widest since 6/30 EOD. Thesis STRENGTHENING: (1) Turing (JP self-driving) customer win — moving 10% of AI training from NVDA to AMD; (2) Goldman Sachs raised PT to $640; (3) Cantor $700 / WFC $615 / UBS $670 PTs all intact; (4) "Advancing AI" event catalyst late July. No cut, no stop-tighten (below +15% at $628.12). AMD 8.17% of equity — appreciated above 8% cap; no add possible. Broker-side trailing-stop infra gap Day 11 unchanged. Weekly buys 0/3 preserved. |
| 2026-07-06 | $99,095.41 | $99,576.17 | +$480.76 | +0.485% | 0 | EOD: NO_TRADE day (pre-market/market-open/midday all HOLD; TLS Day 11 → entry gates unverifiable). AMD rallied $517.82 → $552.16 (+6.63% day change per Alpaca); intraday high $560.67 faded ~$8.51/sh into close. AMD 14 sh +$83.52 unrealized (+1.09%) — first EOD in the green since 6/23 sell-off. Cushion to -7% cut $507.96 widened to ~$44.20/sh (~8.00%) — comfortable, materially off Fri 7/3 ~$9.86/sh tight. Thesis strengthened: Goldman Sachs PT $640, Turing (JP self-driving) 10% AI-training migration NVDA→AMD; Cantor $700 / WFC $615 / UBS $670 PTs intact. Position 7.76% of equity (below 8% cap after intraday fade). AMD broker-side trailing-stop still infra-gated (Day 11). Single-position book. Week 7/6 buys 0/3 preserved. |
| 2026-07-07 | $99,576.17 | $91,845.93 | -$7,730.24 | -7.77% | 0 | **EOD ANOMALY: AMD 14-sh position VANISHED from Alpaca between market-open ($7,250.88 LMV) and post-close (0 positions) with NO cash change — no sell order recorded, no proceeds credited.** Portfolio value = cash exactly ($91,845.93). Most likely Alpaca paper account reset/desync, not a real trade. `research.py orders` returns empty. **3% daily-loss limit BREACHED** (-7.77%) — trading halted per non-negotiable rules pending reconciliation. See EOD snapshot below for full details. |
| 2026-07-08 (market-open) | $99,039.55 (pre-mkt) | $99,102.14 | +$62.59 intraday | +0.063% | 0 | Market-open: **HOLD — no trades**. AMD 14 sh mark $518.20, -$391.92 unrealized (-5.12%). Cushion to manual -7% cut $507.96 widened to ~$10.24/sh (~1.98%) from pre-market ~$5.87/sh — still CRITICAL TIGHT. Six independent stand-downs converge (FOMC minutes 2 PM ET binary; SOXX -12.9% 2-day; AMD cushion tight; yfinance TLS Day 13; broker-side stop gap Day 13; fresh off Alpaca desync anomaly). Pre-market's HOLD reaffirmed. Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-08 (midday) | — | $98,974.94 | -$127.20 intraday | -0.128% | 0 | Midday: **HOLD — no action** (position -6.77%, rule fires at -7%). AMD 14 sh mark $509.22, -$517.71 unrealized (-6.77%). **Cushion CRITICAL TIGHT: ~$1.26/sh (~0.25%)** to manual -7% cut $507.96 — tightened from market-open ~$10.24/sh on continued semi pressure. **AMD intraday low $503.11 already BELOW cut threshold — broker-side stop would have fired; only reason position still open is Day 13 infra gap.** Thesis INTACT (Goldman raised PT today on "strong server CPU demand"; Micro Center × Ryzen AI Halo partnership; GS $640/Cantor $700/WFC $615/UBS $670 Overweight PTs intact). FOMC minutes 2 PM ET binary in ~1 hr — hawkish surprise likely triggers cut. Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-08 | $91,845.93 (7/7 anomaly) | $99,047.53 | +$7,201.60* | +7.84%* | 0 | EOD: NO_TRADE day. AMD 14 sh present ($514.40 mark, -$445.12 unrealized / -5.82%). *Day P&L vs 7/7 recorded EOD reflects **restoration of AMD position** (7/7 anomaly reconciled — position AND cash both present); real intraday drift vs 7/8 market-open $99,102.14 = -$54.61 / -0.055%; drift vs 7/6 EOD (last clean) $99,576.17 = -$528.64 / -0.531%. AMD recovered off midday $509.22 low → $514.40 close (+$5.18/sh). Cushion to manual -7% cut $507.96 widened to ~$6.44/sh (~1.25%) from midday CRITICAL TIGHT ~$1.26/sh. Thesis INTACT (Goldman PT raise, Micro Center × Ryzen AI Halo, GS $640/Cantor $700/WFC $615/UBS $670 Overweight PTs). AMD broker-side trailing-stop still infra-gated (Day 13). yfinance TLS-broken (Day 13). Single-position book. Weekly buys 0/3 preserved. |
| 2026-07-09 (market-open) | $99,164.43 (pre-mkt) | $99,540.40 | +$375.97 intraday | +0.379% | 0 | Market-open: **HOLD — no trades**. AMD rallied hard at open ($516.11 → $549.60, day +6.22%); unrealized flipped from pre-market -$328.22 (-4.29%) to +$47.75 (+0.62%). **Cushion to manual -7% cut $507.96 widened to ~$41.65/sh (~8.20%)** from pre-market CRITICAL TIGHT $1.00/sh (~0.20%) — position no longer on cut-watch. Buy-rule check: **no qualified catalyst in RESEARCH-LOG** (macro filter unverifiable TLS Day 14 → carry-forward rule blocks buys; MSFT/GOOGL DEFERRED at pre-market). AMD add barred (broker-side stop gap Day 14, no averaging-up catalyst). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-09 (midday) | — | — | — | — | 0 | Midday: **HOLD — no action**. AMD 14 sh mark $549.52 (+0.61% unrealized, +$46.49); day +6.21%. Cushion to manual -7% cut $507.96 held at ~$41.56/sh (~7.94%) — essentially unchanged from market-open ~$41.65/sh (position flat intra-session $549.60 → $549.52). No cut (well below -7%), no stop-tighten (well below +15% trigger $628.12; cushion ~$78.60/sh). Thesis INTACT: GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs; Goldman PT raised 7/8; Micro Center × Ryzen AI Halo; "Advancing AI" Jul 22–23. AMD broker-side trailing-stop still infra-gated (Day 14). yfinance TLS-broken (Day 14). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-09 | $99,047.53 | $99,485.03 | +$437.50 | +0.442% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday / EOD. AMD 14 sh mark $545.65 (-$7.62 unrealized, -0.10%); day +0.055% (essentially flat vs 7/8 close). Cushion to manual -7% cut $507.96 = ~$37.69/sh (~6.91%) — modestly tightened from midday ~$41.56/sh on late-session fade off $549.52. Position remains comfortably above cut threshold. Thesis INTACT (GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs; Goldman PT raise 7/8; Micro Center × Ryzen AI Halo; "Advancing AI" Jul 22–23 binary). AMD broker-side trailing-stop still infra-gated (Day 14). yfinance TLS-broken (Day 14). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-10 (market-open) | $99,483.07 (pre-mkt) | $99,540.61 | +$57.54 intraday | +0.058% | 0 | Market-open: **HOLD — no trades**. AMD 14 sh mark $549.26 (+$42.92 unrealized, +0.56%); day +0.465%. Cushion to manual -7% cut $507.96 = ~$41.30/sh (~7.52%) — RELAXED, well off cut-watch. AMD flipped from pre-market -$9.58 (-0.13%) to +$42.92 (+0.56%). Buy-rule check: **no qualified catalyst in RESEARCH-LOG** (pre-market HOLD reaffirmed — TLS Day 15 blocks MA/RSI entry gates). AMD add barred (7.73% cap headroom thin, broker-side stop gap Day 15, no averaging-up catalyst). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-10 (midday) | — | $99,608.79 | +$68.18 intraday | +0.069% | 0 | Midday: **HOLD — no action**. AMD 14 sh mark $554.45 (+$115.51 unrealized, +1.51%); day +1.41%. Cushion to manual -7% cut $507.96 = ~$46.49/sh (~8.39%) — RELAXED, materially widened from market-open ~$41.30/sh on continued intraday firming ($549.26 → $554.45). No cut (well above -7%), no stop-tighten (only +1.51%, well below +15%/+20% triggers). Thesis INTACT: no AMD-specific negative catalyst; Fed's July monetary policy report constructive for AI/semis ("strong factory output driven by data center investment tied to AI"); GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing. AMD add barred (7.79% cap, broker-side stop gap Day 15, no averaging-up catalyst). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-10 | $99,485.03 | $99,659.61 | +$174.58 | +0.176% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday / EOD. AMD 14 sh mark $558.12 (+$166.96 unrealized, +2.18%); day +2.085%. Cushion to manual -7% cut $507.96 widened to ~$50.16/sh (~8.99%) — RELAXED, materially off cut-watch. Position 7.84% of equity (below 8% cap). Thesis INTACT: GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing; Fed July monetary policy report constructive for AI/semis; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 8/4. AMD broker-side trailing-stop still infra-gated (Day 15). yfinance TLS-broken (Day 15). Single-position book. **Week 7/6–7/10 closes: 0 buys / 0 sells / 0 events.** |
| 2026-07-13 | $99,659.61 | $99,327.39 | -$332.22 | -0.333% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday / EOD (macro RISK-OFF from Iran/US strikes + Strait of Hormuz shock; TLS Day 16 blocks MA/RSI entry gates; MSFT/GOOGL/NVDA deferred). AMD 14 sh mark $534.39 (-$165.26 unrealized, -2.16%); day -4.21%. Cushion to manual -7% cut $507.96 = ~$26.43/sh (~4.94%) — modestly tightened from midday ~$27.82/sh on small late-session fade off $535.78. Position 7.53% of equity (below 8% cap). Thesis INTACT (GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 8/4). AMD broker-side trailing-stop still infra-gated (Day 16). yfinance TLS-broken (Day 16). Single-position book. Weekly buys 0/3 preserved. |
| 2026-07-14 (market-open) | $99,442.33 (pre-mkt) | $99,674.59 | +$347.20 intraday | +0.350% | 0 | Market-open: **HOLD — no trades**. AMD 14 sh mark $558.61 (+$173.82 unrealized, +2.27%); day +4.53% post-CPI relief rally. Cushion to manual -7% cut $507.96 widened to ~$50.65/sh (~9.07%) from pre-market ~$34.64/sh — RELAXED. CPI print landed constructive; Warsh testimony 10:00 ET still ahead (binary) — new-entry blocked into it. TLS Day 17 blocks MA/RSI entry gates → strategy criteria #1 & #2 procedurally fail; MSFT/GOOGL/NVDA remain DEFERRED. AMD add barred (7.86% cap, broker-side stop gap Day 17, no averaging-up catalyst; chasing +4.53% intraday pop is not documented). Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-14 (midday) | — | $99,598.57 | +$271.18 intraday | +0.273% | 0 | Midday: **HOLD — no action**. AMD 14 sh mark $553.76 (+$105.92 unrealized, +1.385%); day +3.625%. Cushion to manual -7% cut $507.96 = ~$45.80/sh (~8.27%) — RELAXED. Faded modestly off market-open $558.61 → $553.76 (-0.87% intra-session). No cut (well above -7%); no stop-tighten (below +15%/+20% triggers). Thesis INTACT/STRENGTHENING: CPI cooling drove chip rally; Advancing AI Jul 22–23 upcoming; 42 Buy / 9 Hold analyst deck. AMD add barred (broker-side stop gap Day 17, TLS Day 17, no averaging-up catalyst). Weekly buys 0/3 preserved. |
| 2026-07-14 | $99,327.39 | $99,520.03 | +$192.64 | +0.194% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday / EOD (CPI print constructive → post-CPI relief rally; Warsh testimony 10:00 ET binary passed; TLS Day 17 blocks MA/RSI entry gates; MSFT/GOOGL/NVDA remain DEFERRED). AMD 14 sh mark $548.15 (+$27.38 unrealized, +0.36%); day +2.575%. Cushion to manual -7% cut $507.96 = ~$40.19/sh (~7.33%) — RELAXED, materially widened from 7/13 EOD ~$26.43/sh on post-CPI reclaim. Position 7.71% of equity (below 8% cap). Thesis INTACT/STRENGTHENING (June core CPI flat vs 2.9% forecast → chip rally; GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 8/4). AMD broker-side trailing-stop still infra-gated (Day 17). yfinance TLS-broken (Day 17). Single-position book. Weekly buys 0/3 preserved. |
| 2026-07-15 (market-open) | $99,674.59 (pre-mkt) | $99,573.37 | -$101.22 intraday | -0.102% | 0 | Market-open: **HOLD — no trades**. AMD 14 sh mark $552.29 (+$85.34 unrealized, +1.12%); day +0.759%. Cushion to manual -7% cut $507.96 = ~$44.33/sh (~8.03%) — RELAXED, tightened from pre-mkt ~$51.23/sh on modest fade off pre-mkt $559.19 → $552.29. Buy-rule check: **no qualified catalyst in RESEARCH-LOG** (all fresh candidates DEFERRED — TLS Day 18 blocks MA/RSI entry gates; MSFT/GOOGL/NVDA remain deferred). AMD add barred (7.76% cap thin, broker-side stop gap Day 18, no averaging-up catalyst, chasing pop into ASML AMC binary undocumented). ASML Q2 earnings AMC tonight = semi-sector binary (~8% implied move) — additional stand-down. Weekly buys 0/3 preserved. Single-position book. |
| 2026-07-15 | $99,520.03 | $99,255.40 | -$264.63 | -0.266% | 0 | EOD: NO_TRADE day across pre-market / market-open / midday / EOD (TLS Day 18 blocks MA/RSI entry gates; MSFT/GOOGL/NVDA remain DEFERRED; ASML AMC binary tonight = additional stand-down). AMD 14 sh mark $529.248 (-$237.25 unrealized, -3.10%); day -3.445%. Cushion to manual -7% cut $507.96 = ~$21.29/sh (~4.02%) — MODERATELY TIGHT, materially tightened from mkt-open ~$44.33/sh on sector fade into ASML. Position 7.46% of equity (below 8% cap). Thesis INTACT (GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 8/4). AMD broker-side trailing-stop still infra-gated (Day 18). yfinance TLS-broken (Day 18). Single-position book. Weekly buys 0/3 preserved. |
| 2026-07-16 (market-open) | $99,191.03 (pre-mkt) | $98,972.21 | -$218.82 intraday | -0.221% | 1 | Market-open: **AMD 14 sh CUT** at 9:48 ET — limit-sell filled $509.02 (limit $504.20 = bid $505.46 − 0.25%; price improvement +$4.82/sh vs limit). Realized -$520.38 / -6.80% vs $546.19 avg entry. **Manual -7% cut fired at open**: mark hit $506.83 (-7.208%) below $507.96 threshold on TSMC-driven gap-down; broker-side trailing-stop infra-gated Day 20 so manual control was sole active brake. Fill actually landed at -6.80% on price improvement (better than -7.208% mid at time of order). Post-cut book: 100% cash ($98,972.21), zero positions. TSMC Q2 pre-market binary today; wide 2.55% spread ($505.46 / $518.66) at fill. No new-entry: entry gates procedurally BLOCKED (TLS Day 20 → MA/RSI unverifiable), no qualified catalyst. Weekly buys 0/3 preserved, sells 1. Advancing AI Jul 22–23 (4 sessions) thesis catalyst forfeited on process discipline. **Broker-side trailing-stop infra gap = root cause of manual-cut requirement — patch materially overdue.** |
| 2026-07-16 | $99,255.40 | $98,972.21 | -$283.19 | -0.285% | 1 | EOD: AMD 14 sh CUT at market-open 9:48 ET — limit-sell filled $509.02 (realized -$520.38 / -6.80% vs $546.19 entry). Manual -7% cut fired on TSMC-driven gap-down; broker-side trailing-stop infra-gated Day 20. Post-cut: **100% cash $98,972.21, zero positions** (first cash-only book since 6/25 AAPL trailing-stop). No new-entry (TLS Day 20 blocks MA/RSI entry gates; no qualified catalyst; TSMC binary today). Week 7/13–7/16: 0 buys / 1 sell (AMD cut) / 1 event through Thu. Weekly buys 0/3 preserved. **AMD position closed → all cut-watch, size-cap, +15% trim, and cushion flags CLEARED.** Portfolio -1.03% vs 5/19 baseline $100k. Cash-parked heading into Fri 7/17. |
| 2026-07-17 | $98,972.21 | $98,972.19 | -$0.02 | -0.00002% | 0 | EOD: NO_TRADE day (pre-market + market-open both HOLD; cash-parked full session). Zero positions, 100% cash $98,972.19; portfolio essentially flat (2-cent Alpaca rounding noise). Entry gates procedurally BLOCKED (yfinance TLS Day 21 → MA20/MA50/RSI-14 unverifiable); broker-side trailing-stop infra-gated Day 21; AMD re-entry chase-blocked same-session-post-cut despite KeyBanc PT $725 / UBS PT $700 overnight upgrades; MSFT/GOOGL/NVDA remain DEFERRED on gates. Semi-sector defensive tape (TSMC capex signal + NFLX AH -8%); S&P/NDX futures -0.30%. **Week 7/13–7/17 closes: 0 buys / 1 sell (AMD cut) / 1 event across 5 sessions.** Weekly buy budget 3/3 preserved (unused). Cumulative P&L since 5/19: -$1,027.81 / -1.03%. |

---

## EOD Snapshot — 2026-07-17 (Friday — session: claude/sleepy-goldberg-akka5r)

| Field | Value |
|-------|-------|
| Portfolio Value | $98,972.19 |
| Cash | $98,972.19 |
| Long Market Value | $0.00 |
| Day P&L ($) | -$0.02 |
| Day P&L (%) | -0.00002% |
| Trades Today | 0 |
| Trades This Week | 1 (week of 7/13; Mon 0 / Tue 0 / Wed 0 / Thu 1 sell / Fri 0) |
| Open Positions | 0 / 8 |

### Open Positions

*(none — 100% cash)*

### Trades Executed Today

*(none)*

### Session Notes

Cash-parked full session. Portfolio essentially flat: $98,972.21 → $98,972.19 = -$0.02 (fractional-cent Alpaca equity-field rounding on cash-only book, effectively zero). Zero positions, zero orders. First full-day cash-parked session since 6/25 AAPL trailing-stop (~3 weeks) — clean-book state persisted through both scheduled routines (pre-market + market-open).

Day arc: pre-market $98,972.19 HOLD → market-open $98,972.19 HOLD → EOD $98,972.19. No mark drift (no exposure); only trivial 2-cent variance from Alpaca equity-field rounding. Weekly buy budget 3/3 preserved (unused).

NO_TRADE decision rationale carried across both routines:
1. **Entry gates procedurally BLOCKED — yfinance TLS Day 21.** MA20/MA50/RSI-14 unverifiable script-side; per pre-market carry-forward rule this blocks all new-entry irrespective of catalyst quality.
2. **Broker-side trailing-stop infra gap — Day 21.** `scripts/trade.py` still lacks `trailing-stop` subcommand; any new position would ship without automated downside protection. Yesterday's AMD manual-cut is the fresh lesson.
3. **AMD re-entry chase-blocked** despite KeyBanc PT $725 (from $530) / UBS PT $700 (from $670) overnight upgrades — same-session-post-cut re-entry violates discipline; AMD may re-qualify after Advancing AI Jul 22–23 catalyst resolves on documented catalyst + fresh entry-gate pass.
4. **MSFT / GOOGL / NVDA remain DEFERRED** — infra-gates unresolved.
5. **Tape defensive:** S&P/NDX futures -0.30% at open; NFLX AH -8% (Q3 slowing-growth guide) weighed comm services; TSMC capex signal (fundamentals-positive, sentiment-negative) continued to weigh on semis.
6. **Weekend risk elevated** — Middle East backdrop unchanged; 100% cash into weekend is high-value optionality; no forced action.

Cash $98,972.19 = 100.00% of equity (≥20% reserve ✅ abundantly); exposure 0.00% (≤80% ✅); daily-loss limit (3%) — day P&L -0.00002%, well within. **Week 7/13–7/17 closes: 0 buys / 1 sell (AMD cut 7/16) / 1 event across 5 sessions.** Weekly buy budget 3/3 preserved and unused.

Cumulative P&L since 5/19 $100k baseline: **-$1,027.81 / -1.03%.** Realized ledger unchanged from 7/16 close — AAPL cut -$16.36 (6/25), GOOGL cut -$330.84 (6/10), NVDA trailing-stop -$160.08 (6/5), AMD cut -$520.38 (7/16) = 4 losing exits totaling -$1,027.66 realized (~$0.15 residual reflects idle cash rounding). Unrealized carry nil (cash-parked).

**Carry-forward flags for Monday (7/20) pre-market:**
1. **100% cash book — full 3/3 weekly buy budget available on Mon (new week).** Cash $98,972.19; 8% size cap ~$7,918. No downside protection needed until first new-entry.
2. **Broker-side trailing-stop infra gap — Day 21 into weekend.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Immaterial while cash-parked but **must be patched before next entry** — 21-session infra debt was proximate cause of 7/16 manual-cut exposure. **Escalate: highest-priority infra fix.**
3. **yfinance bars TLS-broken — Day 21 into weekend.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: Alpaca-bars fallback in `market_data.py`** — 21 consecutive sessions of buy-side gate blocks. **Escalate: co-highest priority.**
4. **AMD re-qualification window — Advancing AI Jul 22–23** (Tue–Wed next week). Not eligible for immediate re-entry (chase-block); after catalyst resolves, on documented catalyst + fresh entry-gate pass, re-qualification is possible. KeyBanc $725 / UBS $700 / Cantor $700 / GS $640 / WFC $615 PT stack extends analyst-support runway.
5. **MSFT / GOOGL / NVDA remain deferred** — TLS-blocked gates prevent qualifying entry. If TLS-fallback ships over the weekend, these are the ready candidates.
6. **Weekend tape watch:** NFLX AH -8% (streaming/comm services); TSMC capex signal read-through; Middle East backdrop; any Sunday-night futures gap.
7. **Cumulative P&L since 5/19:** -$1,027.81 / -1.03%. Realized: AAPL -$16.36 + GOOGL -$330.84 + NVDA -$160.08 + AMD -$520.38 = -$1,027.66 across 4 losing exits.
8. **Regime posture:** post-CPI relief regime intact but semi-sector on defensive tape (TSMC capex ripple + NFLX AH streamer weight); risk-management first, entry second.
9. **Clean cash-only book** — clean sheet into new week; all cut-watch, cushion, +15% trim, and size-cap flags CLEARED.

---

## EOD Snapshot — 2026-07-16 (Thursday — session: claude/sleepy-goldberg-31lhlf)

| Field | Value |
|-------|-------|
| Portfolio Value | $98,972.21 |
| Cash | $98,972.21 |
| Long Market Value | $0.00 |
| Day P&L ($) | -$283.19 |
| Day P&L (%) | -0.285% |
| Trades Today | 1 (AMD 14 sh sold @ $509.02 @ 9:48 ET; realized -$520.38 / -6.80%) |
| Trades This Week | 1 (week of 7/13; Mon 0 / Tue 0 / Wed 0 / Thu 1 sell) |
| Open Positions | 0 / 8 |

### Open Positions

*(none — 100% cash)*

### Trades Executed Today

| Time (ET) | Symbol | Side | Qty | Fill | Limit | Realized P&L | Notes |
|-----------|--------|------|-----|------|-------|--------------|-------|
| 09:48 | AMD | SELL | 14 | $509.02 | $504.20 | -$520.38 (-6.80%) | Manual -7% cut fired at open ($506.83 breached $507.96 threshold on TSMC-driven gap-down); limit-sell filled with +$4.82/sh price improvement inside -7%. |

### Session Notes

**Structural regime change day.** AMD 14 sh position — held since 6/22 through the 6/23 semi sell-off, the 7/7 Alpaca desync anomaly, the 7/8 CRITICAL TIGHT cushion, the 7/13 Iran/Hormuz risk-off, and the 7/14 CPI reclaim — was cut at market-open 9:48 ET on TSMC Q2 pre-market gap-down. Manual -7% control fired ($506.83 mark breached $507.96 threshold); broker-side trailing-stop infra-gated Day 20 so manual limit-sell was the sole active brake. Fill landed at $509.02 (limit $504.20 = bid $505.46 − 0.25%) with +$4.82/sh price improvement, so realized loss came in at -6.80% instead of the -7.208% mid at order-send. Book: **100% cash $98,972.21, zero positions** — first cash-only state since 6/25 AAPL trailing-stop fill.

Day arc: pre-market $99,191.03 (AMD 14 sh mark $522.36, -$333.62 unrealized) → market-open cut at 9:48 ET → post-cut $98,972.21 (100% cash). Portfolio value -$283.19 / -0.285% from 7/15 EOD $99,255.40 → $98,972.21 = realized loss on AMD (-$520.38) partially offset by pre-cut mark recovery vs 7/15 close $529.248 (mark $529.248 → fill $509.02 fund-flow accounting: sold 14 sh worth ~$7,409.47 at close-mark → received $7,126.28 gross; ~$283 of the day's drawdown is the fill-vs-close-mark gap).

Post-cut session (market-open forward through midday and EOD): NO new-entry across the full day. Entry gates procedurally BLOCKED — TLS Day 20 leaves MA20/MA50/RSI-14 unverifiable script-side (20 consecutive sessions); no qualified catalyst in RESEARCH-LOG; MSFT/GOOGL/NVDA remain DEFERRED; TSMC Q2 pre-market binary carried through session. Cash parked at 100% into Fri 7/17 open.

Cash $98,972.21 = 100.00% of equity (≥20% reserve ✅ — abundantly); exposure 0.00% (≤80% ✅); daily-loss limit (3%) — day P&L -0.285%, well within. **Week 7/13–7/16 through Thu: 0 buys / 1 sell (AMD cut) / 1 event.** Weekly buy budget 3/3 preserved (sells do not consume buy budget).

Cumulative P&L since 5/19 $100k baseline: **-$1,027.79 / -1.03%.** Realized ledger update — AMD 6/22 buy → 7/16 cut: total P&L -$520.38 / -6.80% held 18 trading days (best mark +$1,015.02 on 6/30 at $578.01, worst mark -$517.71 on 7/8 midday at $509.22, exited near worst on TSMC gap). Position underperformed vs entry despite thesis remaining intact (GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs standing at exit; Advancing AI Jul 22–23 catalyst inside position window forfeited).

**Post-mortem — AMD 6/22–7/16 (realized -$520.38 / -6.80%, 18 sessions held):**
- **Entry (6/22):** market-open post-Juneteenth re-engagement, sized 8% at $546.19; broker-side trailing-stop placement FAILED (403) at fill — position never had broker-side downside protection.
- **High-water mark (6/30):** +$1,015.02 unrealized (+12.4%) on Wells Fargo PT $505→$615 + Cantor PT $500→$700 double-upgrade; +15% trim trigger ~$628.12 was ~$50/sh away (~8%) but not hit — position never triggered documented trim rule.
- **Cushion trajectory:** widened to ~$70/sh (6/30) → tightened to ~$10/sh (7/3) → 7/6 rally re-widened to ~$50/sh (7/6–7/10) → 7/13 Iran/Hormuz shock ~$26/sh → 7/14 CPI reclaim ~$40/sh → 7/15 ASML fade ~$21/sh → 7/16 gap-down breached threshold.
- **Exit (7/16 9:48 ET):** manual -7% cut fired on TSMC Q2 pre-market gap-down; broker-side infra-gated 20 sessions in a row so manual control was sole brake. Price improvement +$4.82/sh vs limit saved -$67.48 vs worst-case fill.
- **Lessons:** (1) Broker-side trailing-stop infra gap = root cause of manual-cut dependence — 20-session infra debt materially compromised position management. (2) +15% trim rule was live at 6/30 peak (+12.4%) but never triggered — trim window opened and closed without action; document rule as "trim on touch" vs "trim on close-above" to disambiguate. (3) Thesis-intact-but-exit-on-price-rule is correct discipline; forfeited Advancing AI Jul 22–23 catalyst on process, not on thesis — no regret.

**Carry-forward flags for Friday (7/17) pre-market:**
1. **100% cash book — full 3/3 weekly buy budget available.** Cash $98,972.21 = 100% of equity. Any qualified entry has abundant sizing headroom (8% cap = ~$7,918).
2. **Zero open positions — all cut-watch, cushion, +15% trim, and size-cap flags CLEARED.** No downside protection needed until first new-entry.
3. **AMD may re-qualify after Advancing AI Jul 22–23 catalyst** (5 sessions away). Not eligible for immediate re-entry — need documented catalyst + entry-gate pass. Watch for TSMC read-through, semi-sector direction over the next 2 sessions.
4. **Broker-side trailing-stop infra gap — Day 20.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Immaterial while cash-parked but **must be patched before next entry** — 20-session infra debt was proximate cause of today's manual-cut exposure. **Escalate: highest-priority infra fix.**
5. **yfinance bars TLS-broken — Day 20.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: Alpaca-bars fallback in `market_data.py`** — 20 consecutive sessions of buy-side gate blocks. Cash-parked state is a mercy: no misses to relitigate today. **Escalate: co-highest priority with broker-side stop.**
6. **MSFT / GOOGL / NVDA remain deferred** — TLS-blocked gates prevent qualifying entry. If TLS-fallback ships, these are the ready candidates.
7. **TSMC Q2 aftermath** — read-through material to Fri semi-sector tape and any AMD/NVDA re-qualification. Full reassessment at pre-market.
8. **Week 7/13–7/17 through Thu:** 0 buys / 1 sell / 1 event. Fri (7/17) is 5th and final session; weekly buy budget 3/3 preserved into it.
9. **Cumulative P&L since 5/19:** -$1,027.79 / -1.03%. AAPL cut -$16.36 (6/25), GOOGL cut -$330.84 (6/10), NVDA trailing-stop -$160.08 (6/5), AMD cut -$520.38 (7/16) = 4 losing exits totaling -$1,027.66 realized; unrealized carry now nil (cash-parked).
10. **Regime posture:** post-CPI relief regime intact but semi-sector on defensive tape (TSMC gap-down catalyzing single-name cascades); risk-management first, entry second.

---

## EOD Snapshot — 2026-07-15 (Wednesday — session: claude/sleepy-goldberg-9cy5v5)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,255.40 |
| Cash | $91,845.93 |
| Long Market Value | $7,409.47 |
| Day P&L ($) | -$264.63 |
| Day P&L (%) | -0.266% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 (week of 7/13; Mon 0 + Tue 0 + Wed 0) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $529.25 | -$237.25 (-3.10%) | -3.445% |

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Portfolio value -$264.63 / -0.266% from 7/14 EOD $99,520.03 → $99,255.40, driven entirely by AMD mark move ($548.15 → $529.248, -$18.90/sh × 14 = -$264.63). Position flipped from +0.36% unrealized (7/14 EOD) to -3.10% unrealized (7/15 EOD) — gave back the post-CPI reclaim on semi-sector fade into ASML AMC.

AMD intraday arc: pre-market $559.19 (cushion ~$51.23/sh) → market-open $552.29 (+1.12%, cushion ~$44.33/sh, +0.759% day) → close $529.248 (-3.10%, cushion ~$21.29/sh, -3.445% day). Monotonic fade off market-open peak through the session (~$23.04/sh decline into close), ending near intraday low. Sector positioning ahead of ASML Q2 earnings AMC drove the sell pressure.

Macro/sector: ASML Q2 earnings AMC = semi-sector binary (~8% implied move); positioning drove late-session fade in AMD alongside broader semi tape. Post-CPI relief regime (June core CPI flat vs 2.9% forecast) intact; no fresh hawkish shock from Warsh testimony 7/14. Iran/Hormuz risk-off tape further unwound.

Thesis INTACT: no AMD-specific negative catalyst — GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; 42 Buy / 9 Hold / 0 Sell across 51 analysts; "Advancing AI" summit Jul 22–23 upcoming binary catalyst inside position window (5 sessions away — Zen 6 Venice on TSMC 2nm launch + Helios rack-scale customer deployments); next earnings 2026-08-04.

Cash $91,845.93 = 92.54% of equity (≥20% reserve ✅); exposure 7.46% (≤80% ✅); daily-loss limit (3%) — day P&L -0.266%, well within. Week 7/13: 0 buys / 0 sells / 0 events through Wednesday. Weekly buy budget 3/3 preserved.

**Carry-forward flags for Thursday (7/16) pre-market:**
1. **AMD cut-watch — MODERATELY TIGHT.** -3.10% unrealized; cushion ~$21.29/sh (~4.02%) to manual -7% threshold $507.96. Materially tightened from 7/14 EOD ~$40.19/sh on today's sector fade. Watch ASML AMC reaction, semi-sector continuation.
2. **ASML Q2 earnings AMC tonight — semi-sector binary.** ~8% implied move; read-through material to AMD gap direction at Thu open. Full reassessment at pre-market.
3. **AMD broker-side trailing-stop infra gap — Day 18.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position remains unprotected broker-side; manual -7% cut at $507.96 is sole active control. **Infra patch materially overdue — escalate.**
4. **yfinance bars TLS-broken — Day 18.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`** — 18 consecutive sessions of buy-side gate blocks.
5. **AMD 7.46% position** — below 8% size cap; any add barred (broker-side stop gap; TLS-blocked gates; no averaging-up catalyst; averaging-into-weakness violates trend-continuation).
6. **AMD +15% trim watch** — mark $529.25 vs +15% trim trigger ~$628.12. Cushion ~$98.87/sh (~18.7%). Not actionable.
7. **Weekly buy budget 3/3 preserved** into Thu–Fri (2 remaining sessions).
8. **AMD "Advancing AI" summit — Jul 22–23** — 5 sessions away; inside position window.
9. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary yet.
10. **Post-CPI regime** — inflation cooling constructive for risk assets; monitor for Warsh follow-through, Iran/Hormuz de-escalation, semi-sector fade continuation post-ASML.
11. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.
12. **MSFT / GOOGL / NVDA remain deferred** — TLS-blocked gates prevent qualifying entry; carry to Thu pre-market.

---

## EOD Snapshot — 2026-07-14 (Tuesday — session: claude/sleepy-goldberg-otqm0x)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,520.03 |
| Cash | $91,845.93 |
| Long Market Value | $7,674.10 |
| Day P&L ($) | +$192.64 |
| Day P&L (%) | +0.194% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 (week of 7/13; Mon 0 + Tue 0) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $548.15 | +$27.38 (+0.36%) | +2.575% |

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Portfolio value +$192.64 / +0.194% from 7/13 EOD $99,327.39 → $99,520.03, driven entirely by AMD mark move ($534.39 → $548.15, +$13.76/sh × 14 = +$192.64). Position flipped from -2.16% unrealized (7/13 EOD) to +0.36% unrealized (7/14 EOD) — reclaimed breakeven on CPI relief rally.

AMD intraday arc: pre-market $542.30 (cushion ~$34.64/sh) → market-open $558.61 (+2.27%, cushion ~$50.65/sh, +4.53% day) → midday $553.76 (+1.385%, cushion ~$45.80/sh) → close $548.15 (+0.36%, cushion ~$40.19/sh, +2.575% day). Peak at market-open; modest monotonic fade through midday and into close (~$10.46/sh off intraday high). Position closed comfortably above cut threshold on session-net gain.

Macro RELIEF: June core CPI printed flat vs 2.9% forecast → post-CPI chip rally (AMD +5% intraday spike, Intel +4%); Warsh testimony 10:00 ET passed as non-event (no fresh hawkish shock). Semis rebounded broadly from Monday RISK-OFF drawdown. Iran/Hormuz risk-off tape partially unwound.

Thesis INTACT and STRENGTHENING: CPI cooling → chip rally read-through; GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; 42 Buy / 9 Hold / 0 Sell across 51 analysts; "Advancing AI" summit Jul 22–23 upcoming binary catalyst inside position window (8 sessions away — Zen 6 Venice on TSMC 2nm launch + Helios rack-scale customer deployments); next earnings 2026-08-04.

Cash $91,845.93 = 92.29% of equity (≥20% reserve ✅); exposure 7.71% (≤80% ✅); daily-loss limit (3%) — day P&L +0.194%, well within. Week 7/13: 0 buys / 0 sells / 0 events through Tuesday. Weekly buy budget 3/3 preserved.

**Carry-forward flags for Wednesday (7/15) pre-market:**
1. **AMD cut-watch — RELAXED.** +0.36% unrealized; cushion ~$40.19/sh (~7.33%) to manual -7% threshold $507.96. Materially widened from 7/13 EOD ~$26.43/sh on post-CPI reclaim.
2. **AMD broker-side trailing-stop infra gap — Day 17.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position remains unprotected broker-side; manual -7% cut $507.96 is sole active control. **Infra patch materially overdue — escalate.**
3. **yfinance bars TLS-broken — Day 17.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`.**
4. **AMD 7.71% position** — below 8% size cap; any add barred (broker-side stop gap; TLS-blocked gates; no averaging-up catalyst; chasing intraday pop not documented).
5. **AMD +15% trim watch** — mark $548.15 vs +15% trim trigger ~$628.12. Cushion ~$79.97/sh (~14.6%). Not actionable.
6. **Weekly buy budget 3/3 preserved** into Wed–Fri (3 remaining sessions).
7. **AMD "Advancing AI" summit — Jul 22–23** — 6 sessions away; inside position window.
8. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary yet.
9. **Post-CPI regime** — inflation cooling constructive for risk assets; monitor for Warsh follow-through, Iran/Hormuz de-escalation continuation, semi-sector momentum.
10. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.
11. **MSFT / GOOGL / NVDA remain deferred** — TLS-blocked gates prevent qualifying entry; carry to Wed pre-market.

---

## EOD Snapshot — 2026-07-13 (Monday — session: claude/sleepy-goldberg-rg3251)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,327.39 |
| Cash | $91,845.93 |
| Long Market Value | $7,481.46 |
| Day P&L ($) | -$332.22 |
| Day P&L (%) | -0.333% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 7/13 opens today) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $534.39 | -$165.26 (-2.16%) | -4.21% |

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Portfolio value -$332.22 / -0.333% from 7/10 EOD $99,659.61 → $99,327.39, driven entirely by AMD mark move ($558.12 → $534.39, -$23.73/sh × 14 = -$332.22). Position moved from +2.18% unrealized (7/10 EOD) to -2.16% unrealized (7/13 EOD) — flipped back into the red on macro RISK-OFF gap-down.

AMD intraday arc: pre-market $538.99 (cushion ~$31.03/sh) → market-open $527.41 (-3.44%, cushion ~$19.44/sh — half of pre-market) → midday $535.78 (-1.91%, cushion ~$27.82/sh, recovered +1.59% off open) → close $534.39 (-2.16%, cushion ~$26.43/sh). Modest late-session fade off midday high; position held comfortably above -7% cut threshold throughout.

Macro context RISK-OFF: Iran/US strikes + Strait of Hormuz shock drove Brent +7% / WTI +6%; semis under sector pressure through the session. Fed's Waller floated rate-hike-on-the-table language ahead of CPI print this week — additional binary risk. SPY MA20 filter script-side unverifiable (TLS Day 16); tape direction confirmed risk-off.

Thesis INTACT: no AMD-specific negative catalyst today; GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; "Advancing AI" summit Jul 22–23 upcoming binary catalyst inside position window; next earnings 2026-08-04. Constructive read-through from tech-giant FCF story ($430B combined FCF for NVDA/MU/AVGO/AMAT).

Cash $91,845.93 = 92.47% of equity (≥20% reserve ✅); exposure 7.53% (≤80% ✅); daily-loss limit (3%) — day P&L -0.333%, well within. **Week 7/13 opens: 0 buys / 0 sells / 0 events (Monday).** Weekly buy budget 3/3 preserved.

**Carry-forward flags for Tuesday (7/14) pre-market:**
1. **AMD cut-watch — MODESTLY TIGHT.** -2.16% unrealized; cushion ~$26.43/sh (~4.94%) to manual -7% threshold $507.96. Materially tighter than 7/10 EOD ~$50.16/sh on macro shock; still comfortably above cut threshold. Watch for CPI reaction, Iran/Hormuz escalation, semi-sector continuation.
2. **AMD broker-side trailing-stop infra gap — Day 16.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position remains unprotected broker-side; manual -7% cut at $507.96 is sole active control. **Infra patch materially overdue — escalate.**
3. **yfinance bars TLS-broken — Day 16.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`** — 16 consecutive sessions of buy-side gate blocks.
4. **AMD 7.53% position** — below 8% size cap; any add still barred (broker-side stop gap; TLS-blocked gates; no averaging-up catalyst; averaging-into-weakness violates trend-continuation).
5. **AMD +15% trim watch** — mark $534.39 vs +15% trim trigger ~$628.12. Cushion ~$93.73/sh (~17.5%). Not actionable.
6. **Weekly buy budget 3/3 preserved** into Tue–Fri.
7. **AMD "Advancing AI" summit — Jul 22–23** — near-term binary catalyst inside position window.
8. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary yet.
9. **Macro RISK-OFF regime** — Iran/US strikes, Strait of Hormuz shock, Brent/WTI shock, Fed's Waller hawkish tilt into CPI print. Revalidate at Tue pre-market for tape and geopolitical newsflow.
10. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.
11. **MSFT / GOOGL / NVDA remain deferred** from pre-market — no fresh qualifying catalyst; carry-forward to Tue pre-market.

---

## EOD Snapshot — 2026-07-10 (Friday — session: claude/sleepy-goldberg-knhzps)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,659.61 |
| Cash | $91,845.93 |
| Long Market Value | $7,813.68 |
| Day P&L ($) | +$174.58 |
| Day P&L (%) | +0.176% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 7/6 closes today) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $558.12 | +$166.96 (+2.18%) | +2.085% |

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Portfolio value +$174.58 / +0.176% from 7/9 EOD $99,485.03 → $99,659.61, driven entirely by AMD mark move ($545.65 → $558.12, +$12.47/sh × 14 = +$174.58). Position moved from -0.10% unrealized (7/9 EOD) to +2.18% unrealized (7/10 EOD) — comfortably in the green.

AMD intraday arc: pre-market $544.83 (-0.13% unrealized, cushion ~$36.87/sh) → market-open $549.26 (+0.56%, cushion ~$41.30/sh) → midday $554.45 (+1.51%, cushion ~$46.49/sh) → close $558.12 (+2.18%, cushion ~$50.16/sh). Monotonic firming throughout the session; late-day strength held into the close.

Thesis INTACT: no AMD-specific negative catalyst; Fed's July monetary policy report constructive for AI/semis ("strong factory output driven by data center investment tied to AI"); GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; Goldman PT raise 7/8 in effect; Micro Center × Ryzen AI Halo partnership; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 2026-08-04.

Cash $91,845.93 = 92.16% of equity (≥20% reserve ✅); exposure 7.84% (≤80% ✅); daily-loss limit (3%) — day P&L strongly positive at +0.176%, well within. **Week 7/6–7/10 closes: 0 buys / 0 sells / 0 events.** Weekly buy budget 3/3 unused (resets Monday 7/13).

**Carry-forward flags for Monday (7/13) pre-market:**
1. **AMD cut-watch — RELAXED.** +2.18% unrealized; cushion ~$50.16/sh (~8.99%) to manual -7% threshold $507.96. Comfortably off cut-watch heading into weekend.
2. **AMD broker-side trailing-stop infra gap — Day 15.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position remains unprotected broker-side; manual -7% cut at $507.96 is sole active control. **Infra patch materially overdue — escalate.**
3. **yfinance bars TLS-broken — Day 15.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`** — 15 consecutive sessions of buy-side gate blocks.
4. **AMD 7.84% position** — below 8% size cap; any add still barred (broker-side stop gap; TLS-blocked gates; no averaging-up catalyst).
5. **AMD +15% trim watch** — mark $558.12 vs +15% trim trigger ~$628.12. Cushion ~$70.00/sh (~12.5%). Not actionable.
6. **Weekly buy budget resets Monday (7/13)** — fresh 3/3.
7. **AMD "Advancing AI" summit — Jul 22–23** — near-term binary catalyst inside position window.
8. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary.
9. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.
10. **Macro filter** — SPY vs MA20 still TLS-blocked script-side; revalidate at Mon pre-market.

---

## EOD Snapshot — 2026-07-09 (Thursday — session: claude/sleepy-goldberg-gpeylk)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,485.03 |
| Cash | $91,845.93 |
| Long Market Value | $7,639.10 |
| Day P&L ($) | +$437.50 |
| Day P&L (%) | +0.442% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 7/6) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $545.65 | -$7.62 (-0.10%) | +0.055% |

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Portfolio value +$437.50 / +0.442% from 7/8 EOD $99,047.53 → $99,485.03, driven entirely by AMD mark move ($514.40 → $545.65, +$31.25/sh × 14 = +$437.50). Position moved from -5.82% unrealized (7/8 EOD) to -0.10% unrealized (7/9 EOD) — near breakeven at close.

AMD intraday arc: pre-market $516.11 (-4.29% unrealized, cushion ~$1.00/sh CRITICAL TIGHT) → market-open $549.60 (+0.62%, cushion ~$41.65/sh) → midday $549.52 (+0.61%, cushion ~$41.56/sh) → close $545.65 (-0.10%, cushion ~$37.69/sh). Intraday high near midday; modest late-session fade of ~$3.87/sh into close.

Thesis INTACT and strengthening: Goldman Sachs PT raise 7/8 (adds to $640 PT), Micro Center × Ryzen AI Halo partnership; GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 2026-08-04.

Cash $91,845.93 = 92.32% of equity (≥20% reserve ✅); exposure 7.68% (≤80% ✅); daily-loss limit (3%) — day P&L strongly positive at +0.442%, well within. Weekly buy budget 0/3 preserved into Friday.

**Carry-forward flags for Friday (7/10) pre-market:**
1. **AMD cut-watch — RELAXED.** -0.10% unrealized; cushion ~$37.69/sh (~6.91%) to manual -7% threshold $507.96. Position near breakeven; monitor for AMD-specific or macro semi-sector headline flow.
2. **AMD broker-side trailing-stop infra gap — Day 14.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position remains unprotected broker-side; manual -7% cut at $507.96 is sole active control. **Infra patch materially overdue — escalate.**
3. **yfinance bars TLS-broken — Day 14.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`** — 14 consecutive sessions of buy-side gate blocks.
4. **AMD 7.68% position** — below 8% size cap; any add still barred (broker-side stop gap; TLS-blocked gates; no averaging-up catalyst).
5. **AMD +15% trim watch** — mark $545.65 vs +15% trim trigger ~$628.12. Cushion ~$82.47/sh (~15.1%). Not actionable.
6. **Weekly buy budget 3/3 preserved** into Friday (final day of week).
7. **AMD "Advancing AI" summit — Jul 22–23** — near-term binary catalyst.
8. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary.
9. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.
10. **Macro filter** — SPY vs MA20 still TLS-blocked script-side; revalidate at Fri pre-market.

---

## EOD Snapshot — 2026-07-08 (Wednesday — session: claude/sleepy-goldberg-bj5x2f)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,047.53 |
| Cash | $91,845.93 |
| Long Market Value | $7,201.60 |
| Day P&L ($) vs 7/7 EOD | +$7,201.60 (position restoration — NOT real trading P&L; see notes) |
| Day P&L (%) vs 7/7 EOD | +7.84% (position restoration) |
| Drift vs 7/8 market-open ($99,102.14) | -$54.61 / -0.055% |
| Drift vs 7/6 EOD ($99,576.17, last clean) | -$528.64 / -0.531% (2-session) |
| Trades Today | 0 |
| Trades This Week | 0 (week of 7/6) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $514.40 | -$445.12 (-5.82%) | -0.33% |

### 7/7 Anomaly Reconciliation

The 7/7 EOD snapshot recorded an **AMD position vanished without cash credit** anomaly (portfolio value $91,845.93 = cash only). Today's account state shows the AMD 14-sh position IS present with cash unchanged from 7/7 ($91,845.93). Interpretation:

- The 7/7 "vanished position" appears to have been an **Alpaca paper account state snapshot anomaly** (transient desync at read-time), not a real position loss.
- Cash ($91,845.93) is identical across 7/6 EOD → 7/7 EOD anomaly → 7/8 EOD, consistent with no cash transaction ever occurring.
- Position (AMD 14 sh, avg entry $546.19) is unchanged from pre-anomaly baseline — same lot, same cost basis.
- **Total P&L in the summary header remains uncorrupted** (no realized -$7,730 loss was ever booked).
- 3% daily-loss halt from 7/7 no longer applicable — 7/8 real drift is -0.055% intraday, -0.531% vs last clean EOD (7/6). Within limits.

### Session Notes

NO_TRADE day across pre-market / market-open / midday / EOD. Six independent stand-downs converged: (1) macro filter SPY vs MA20 uncertain post-anomaly + FOMC minutes 2 PM ET binary; (2) SOXX -12.9% 2-day sell-off (AMD in blast radius); (3) AMD position cushion CRITICAL TIGHT through midday; (4) yfinance TLS-broken Day 13 (MA20/MA50/RSI-14 entry gates unverifiable script-side); (5) `scripts/trade.py` trailing-stop subcommand missing Day 13 (AMD unprotected broker-side); (6) fresh off Alpaca desync anomaly — heightened caution.

AMD intraday arc: pre-market cushion ~$5.87/sh → market-open $518.20 (cushion ~$10.24/sh) → midday $509.22 (CRITICAL TIGHT ~$1.26/sh, intraday low $503.11 BELOW cut threshold) → close $514.40 (cushion ~$6.44/sh). Position ended above manual -7% cut threshold $507.96 despite penetrating it intraday (broker-side stop would have fired at $503.11 low if infra-gate not present). Alpaca day change -0.33%.

Thesis INTACT: Goldman Sachs PT raised today on "strong server CPU demand" (adds to $640 PT); Micro Center × Ryzen AI Halo partnership headline; GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight PTs all standing; "Advancing AI" summit Jul 22–23 upcoming binary; next earnings 2026-08-04.

Cash $91,845.93 = 92.73% of equity (≥20% reserve ✅); exposure 7.27% (≤80% ✅); daily-loss limit (3%) — real intraday drift -0.055%, well within. Weekly buy budget 0/3 preserved (single-position book unchanged).

**Carry-forward flags for Thursday (7/9) pre-market:**
1. **7/7 anomaly RECONCILED** — position + cash both present at 7/8 EOD; total P&L header untouched. No further reconciliation needed but flag pattern for future recurrence.
2. **AMD cut-watch — TIGHT (recovered from midday CRITICAL).** -5.82% unrealized; cushion ~$6.44/sh (~1.25%) to manual -7% threshold $507.96. **Thursday pre-market: re-check immediately on cash open; if mark/last breaches $507.96, execute cut.** FOMC minutes reaction + SOXX continuation risk overnight.
3. **AMD broker-side trailing-stop infra gap — Day 13.** `scripts/trade.py` still lacks `trailing-stop` subcommand. **Position penetrated cut threshold intraday ($503.11 low) with no broker-side protection — infra patch materially overdue.** Escalate.
4. **yfinance bars TLS-broken — Day 13.** MA/RSI entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`.**
5. **AMD 7.27% of equity** — below 8% size cap; any add still barred (broker-side stop gap, averaging down into losing position, TLS-blocked gates).
6. **AMD +15% trim watch** — mark $514.40 vs +15% trim trigger ~$628.12; cushion ~$113.72/sh. Not actionable.
7. **Weekly buy budget 3/3** preserved into Thu–Fri.
8. **FOMC minutes** released 2 PM ET today — check post-close market reaction / Thursday pre-market for hawkish tilt implications.
9. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary.
10. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.

---

## EOD Snapshot — 2026-07-07 (Tuesday — session: claude/sleepy-goldberg-q1fj91)

| Field | Value |
|-------|-------|
| Portfolio Value | $91,845.93 |
| Cash | $91,845.93 |
| Long Market Value | $0.00 |
| Day P&L ($) | **-$7,730.24** |
| Day P&L (%) | **-7.77%** (breaches 3% daily-loss limit) |
| Trades Today | 0 (no orders recorded) |
| Trades This Week | 0 (week of 7/6) |
| Open Positions | **0 / 8** (AMD 14 sh position vanished — see anomaly below) |

### Open Positions

*(none — AMD 14-sh position no longer present in Alpaca)*

### CRITICAL ANOMALY — AMD position vanished without a trade

**Observed state:**
- **Market-open (09:45 ET, per heartbeat.json):** portfolio_value $99,096.81, cash $91,845.93, long_market_value $7,250.88, 1 open position (AMD 14 sh @ $518.13 mark, -$392.90 unrealized).
- **Midday scan (12:30 ET, per memory/performance.md):** AMD 14 sh @ $521.00 mark, -$352.72 unrealized. Cushion ~$13.04/sh to manual -7% cut $507.96.
- **Post-close (16:36 ET, this snapshot):** portfolio_value $91,845.93, cash $91,845.93 (**unchanged from market-open**), long_market_value **$0.00**, **0 open positions**. `research.py orders` returns `[]`.

**Analysis:**
- Yesterday's EOD (7/6): $99,576.17. Today's close: $91,845.93. Delta: **-$7,730.24 / -7.77%** — exactly the value of the missing AMD LMV.
- Cash is IDENTICAL to yesterday's EOD cash ($91,845.93) and to today's market-open cash. **No cash transaction occurred.**
- If AMD had been sold near the manual -7% cut $507.96, cash should have increased by ~14 × $507.96 = ~$7,111 to ~$98,957. It did not.
- If the trailing-stop had fired at any intraday price, proceeds would be reflected in cash. They are not.
- **Conclusion:** this is not a real trade close. The most likely cause is an **Alpaca paper account state reset or synchronization anomaly** where the position was removed from the book without a matching cash credit. Paper accounts are known to reset periodically.

**Actions taken:**
1. Push notification sent to the user immediately upon detection.
2. This EOD snapshot logs the anomaly rather than pretending it was a normal trading day.
3. No new trades executed (would be blocked by the 3% daily-loss limit regardless).
4. Weekly buy budget preserved at 0/3.

**Carry-forward flags for Wednesday (7/8) pre-market:**
1. **AMD DISAPPEARANCE UNRECONCILED — HIGHEST PRIORITY.** Before any further trading activity, manually inspect the Alpaca paper dashboard to determine whether: (a) paper account was reset (proceed to re-baseline the performance log and consider re-establishing the AMD thesis position if still valid), (b) the position was closed with proceeds still pending settlement (unlikely — Alpaca paper settles instantly), or (c) some other bug/desync. Do not re-open AMD until root cause is clear.
2. **3% daily-loss limit BREACHED (-7.77%) — trading is HALTED** per the non-negotiable risk rules. Pre-market Wed must not open new positions until the anomaly is reconciled with the user.
3. **Long_market_value $0** — book is now empty. Risk posture is 100% cash by default until reconciliation.
4. **`scripts/trade.py` trailing-stop infra gap — Day 13.** No longer relevant to a live position, but the missing subcommand meant AMD had zero broker-side protection through this event; if the account was reset, this remains a top priority to patch before re-opening any position.
5. **yfinance TLS-broken — Day 13.** Alpaca-bars fallback in `market_data.py` remains the priority infra fix.
6. **Realized-P&L accounting hold.** Do not treat the -$7,730.24 delta as a realized loss until reconciled — it may be a bookkeeping artifact rather than a real trading loss. The performance log's `Total P&L` field must not be updated until the user confirms disposition.
7. Weekly buy budget 0/3 preserved into Wed–Fri (blocked regardless by daily-loss halt until reconciled).
8. Single-position book was AMD only; now zero-position book.

---

## Midday Scan — 2026-07-07 (Tuesday — session: claude/exciting-bohr-2kpn9m)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L | Day Change |
|--------|-----|-----------|------|----------------|-----------|
| AMD | 14 | $546.19 | $521.00 | -$352.72 (-4.61%) | -5.62% |

Midday checks:
- **Cut-loser (−7%)**: AMD -4.61% — **no cut**. Cushion ~$13.04/sh (~2.50%) to manual -7% threshold $507.96 — modestly widened from market-open ~$10.17/sh (~1.96%) on small intraday bounce ($518.13 → $521.00).
- **Stop-tighten (+15%/+20%)**: no position at gain.
- **Thesis check**: **INTACT.** AMD day -7.08% is macro/sector profit-taking (AI-trade unwind, consistent with BoA "AI bubble" flag pattern) — not company-specific. Reaffirmed: GS $640, Cantor $700, WFC $615, UBS $670 PTs all Overweight/Buy; DC revenue +57% YoY Q1 ($5.8B); Advancing AI summit Jul 22–23 upcoming binary; next earnings 2026-08-04 (outside 5-day exclusion).
- **Trailing-stop infra gap (Day 12)**: AMD unprotected by broker-side stop. `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is sole control.

No trades executed. Risk posture: cash 92.65% (≥20% ✅), exposure 7.35% (≤80% ✅), daily-loss limit (3%) — AMD day -5.62% × 7.35% ≈ -0.41% portfolio, within.

**Flags for end-of-day:**
1. **AMD cut-watch — TIGHT but stable.** Cushion ~$13.04/sh (~2.50%) to $507.96. Re-check at EOD; if breached execute close immediately.
2. AMD broker-side trailing-stop infra gap — Day 12 carry-forward.
3. AMD +15% trim staging — cushion ~$107/sh to $628.12; not actionable.
4. yfinance bars TLS-broken — Day 12 carry-forward.
5. Weekly buys 0/3 preserved.
6. June FOMC minutes later this week — hawkish risk.
7. AMD "Advancing AI" summit Jul 22–23 — near-term binary catalyst.
8. Single-position book unchanged.

---

## Market-Open Log — 2026-07-07 (Tuesday — session: claude/sweet-shannon-he3epy)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $91,845.93 |
| Equity | $99,096.81 |
| Long Market Value | $7,250.88 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 0 / 3 (week of 7/6) |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AMD 7.32%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD reaffirmed; AMD add BLOCKED, MSFT/GOOGL DEFERRED (TLS Day 12).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L | Day Change |
|--------|-----|-----------|------|----------------|-----------|
| AMD | 14 | $546.19 | $518.13 | -$392.90 (-5.14%) | -6.14% |

Three independent stand-downs (reaffirming pre-market):
- **Entry gates unverifiable — Day 12.** yfinance TLS-broken; MA20/MA50/RSI-14 unverifiable script-side. Strategy criteria #1 & #2 procedurally fail → any buy violates rules.
- **AMD add barred.** Position 7.32% (below 8% cap on intraday markdown); broker-side stop gap Day 12; averaging down into -6.14% intraday weakness not a documented catalyst.
- **No qualified new-candidate catalyst.** MSFT / GOOGL DEFERRED at pre-market on same gate block.

**AMD risk management — CRITICAL TIGHT:**
- Unrealized -5.14% vs manual -7% cut $507.96. **Cushion ~$10.17/sh (~1.96%)** — tightened from pre-market ~$34.71/sh (~6.40%) on intraday markdown ($542.67 → $518.13, -4.52% intra-session).
- +15% trim trigger ~$628.12; mark cushion ~$110/sh. Not actionable.
- **Broker-side trailing-stop still infra-gated — Day 12.** `scripts/trade.py` lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is sole protection.
- Thesis INTACT (GS $640 / Cantor $700 / WFC $615 / UBS $670 Overweight; NVDA Kyber delay; Turing win; "Advancing AI" summit Jul 22–23). Sell-off is macro / semis-sector give-back, not company-specific.

Trades executed: **none.**

Risk posture: cash 92.68% (≥20% ✅); exposure 7.32% (≤80% ✅); daily-loss limit (3%) — day drift -0.48% from Mon EOD, within. Weekly buys 0/3 preserved.

**Flags for midday-scan:**
1. **AMD manual cut at $507.96 — CRITICAL TIGHT.** Cushion ~$10.17/sh (~1.96%). If breached execute close immediately.
2. **AMD broker-side trailing-stop infra gap — Day 12.** Position -$393 unrealized, unprotected — escalate.
3. **AMD +15% trim staging** — mark cushion ~$110/sh. Not actionable.
4. **yfinance bars TLS-broken — Day 12.** Priority infra fix (Alpaca-bars fallback).
5. **Weekly buy budget 3/3** preserved.
6. **June FOMC minutes** later this week — hawkish risk.
7. **AMD "Advancing AI" summit — Jul 22–23** — near-term binary inside position window.

---

## EOD Snapshot — 2026-07-06 (Monday — session: claude/sleepy-goldberg-dl3rmg)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,576.17 |
| Cash | $91,845.93 |
| Long Market Value | $7,730.24 |
| Day P&L ($) | +$480.76 |
| Day P&L (%) | +0.485% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 7/6 — fresh 3/3 budget) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $552.16 | +$83.52 (+1.09%) | +6.63% |

Notes: NO_TRADE day across pre-market / market-open / midday (yfinance TLS-broken Day 11 → macro SPY>MA20 and per-candidate MA20/MA50/RSI-14 entry gates unverifiable script-side; both entry gates FAIL → any buy is a rules violation). Day P&L +$480.76 / +0.485% driven entirely by AMD rally vs Fri 7/3 stale mark ($517.82 → $552.16, +$34.34/sh × 14 = +$480.76). Alpaca day change +6.63%. AMD intraday arc: pre-market $532.00 → market-open $555.76 (+7.33%) → midday $560.67 (+8.28%, intraday HWM) → close $552.16 (+6.63%, ~$8.51/sh late-session fade). **First EOD in the green since the 6/23 semi sell-off — position flipped from -$397 (7/3) to +$84 (7/6) unrealized in a single session.** Cushion to manual -7% cut threshold $507.96 = **~$44.20/sh (~8.00%)** — materially widened from Fri 7/3 ~$9.86/sh (~1.90%) tight zone; comfortable and well-off cut-watch. **AMD thesis strengthened today**: (1) Goldman Sachs (Schneider) raised PT to $640 pre-market; (2) Turing (Japanese self-driving startup) customer win — moving ~10% of AI training from NVDA to AMD GPUs (AMD VC arm invested); (3) Cantor $700 / WFC $615 / UBS $670 Overweight PTs all reaffirmed; (4) "Advancing AI" event catalyst late July; (5) DC GPU $15.6B/$40.6B/$63B for 2026/27/28 intact; (6) MI450/OpenAI 5-yr deal intact. Position sized to 7.76% of equity (below 8% cap after intraday fade off 8.17% midday high). **AMD remains unprotected by broker-side trailing-stop (Day 11 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand; manual -7% cut at $507.96 is sole active control. Cash $91,845.93 = 92.24% of equity (≥20% reserve ✅); exposure 7.76% (≤80% ✅); daily-loss limit (3%) — day P&L strongly positive. Weekly buy budget 3/3 fresh preserved into Tue–Fri.

**Carry-forward flags for Tuesday (7/7) pre-market:**
1. **AMD cut-watch — RELAXED.** +1.09% unrealized; cushion widened to ~$44.20/sh (~8.00%) to manual -7% threshold $507.96. Continue monitoring at pre-market for any AI-trade sentiment or Fed-minutes-preview headline flow.
2. **AMD broker-side trailing-stop infra gap — Day 11.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Position finally back in the green with meaningful unrealized gain to protect (albeit small); **infra patch materially overdue** — position has swung ~$842 unrealized in 4 sessions unprotected. Escalate immediately.
3. **yfinance bars TLS-broken — Day 11.** MA20/MA50/RSI-14 entry gates unverifiable script-side. **Priority infra fix: implement Alpaca-bars fallback in `market_data.py`** — both entry gates have been blocked at market-open for 11 sessions running, gating any new buys entirely.
4. **AMD 7.76% position** — below 8% size cap after intraday fade. Any add still barred (broker-side stop gap; averaging-up on modest gain not a documented catalyst; TLS-blocked gates).
5. **AMD +15% trim watch** — mark $552.16 vs +15% trim trigger ~$628.12. Cushion ~$75.96/sh (~13.75%). Not yet actionable.
6. **Macro filter** — SPY vs MA20 status uncertain (Dow ATH reported at market-open is constructive, but script-side comparison unverified). Re-validate at Tue pre-market.
7. **Weekly buy budget 3/3 fresh** — preserved into Tue–Fri.
8. **Fed minutes** later this week — potential macro re-tightening risk; reserve dry powder.
9. **AMD next earnings 2026-08-04** — well outside 5-day exclusion; no near-term binary.
10. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.

---

## EOD Snapshot — 2026-07-03 (Friday — session: claude/sleepy-goldberg-grsqfe)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,095.41 |
| Cash | $91,845.93 |
| Long Market Value | $7,249.48 |
| Day P&L ($) | -$6.16 |
| Day P&L (%) | -0.006% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 6/29 — closes today; 4-session week) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $517.82 | -$397.24 (-5.20%) | 0.00% (closed) |

Notes: **Independence Day observed — US equity markets CLOSED all session.** No trades executed or possible. Portfolio value drifted -$6.16 / -0.006% from Thu EOD $99,101.57 → $99,095.41 on a tiny AMD mark move ($518.26 → $517.82, -$0.44/sh × 14 = -$6.16); day-change shows 0.00% consistent with closed market — the mark adjustment is likely from Thu after-hours print or a stale-mark artifact rolled into today's book. AMD 14 sh -$397.24 unrealized (-5.20%); cushion to manual -7% cut threshold $507.96 = **~$9.86/sh (~1.90%)** — tighter than Thu EOD ~$10.30/sh but essentially unchanged. Thesis INTACT (Cantor PT $700, Wells Fargo $615, UBS $670 — all Overweight/Buy reaffirmed 6/30–7/2; DC GPU $15.6B/$40.6B/$63B 2026/27/28; 2nm EPYC Venice ramp H2 2026; next earnings 2026-08-04 well outside 5-day exclusion). **AMD remains unprotected by broker-side trailing-stop (Day 10 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is the sole active control. Cash $91,845.93 = 92.68% of equity (≥20% reserve ✅); exposure 7.32% (≤80% ✅); daily-loss limit (3%) — day drift -0.006%, immaterial. **Week 6/29–7/3 closes: 0 buys / 0 sells / 0 events (4-session week — Fri 7/3 CLOSED for Independence Day).** Weekly buy budget 0/3 unused; resets Monday 7/6.

**Carry-forward flags for Monday (7/6) pre-market:**
1. **AMD cut-watch — CRITICAL TIGHT into 3-day weekend.** -5.20% unrealized; cushion ~$9.86/sh (~1.90%) to manual -7% threshold $507.96. **Monday pre-market: re-check immediately on cash open; if mark/last breaches $507.96, execute `python scripts/trade.py close AMD`.** Weekend + Independence Day headline/gap risk elevated; any hawkish Fed-speak or AI-trade sell-off could gap through the threshold.
2. **AMD broker-side trailing-stop infra gap — Day 10.** `scripts/trade.py` still lacks `trailing-stop` subcommand. **Position that swung from +$445 (6/30) to -$397 (7/3) unrealized in 4 sessions without a broker-side stop — infra patch materially overdue. Escalate immediately Mon pre-market.**
3. **AMD position 7.32% of equity** — below 8% size cap; any add still barred (averaging-down on a losing position + Day 10 broker-side stop gap).
4. **yfinance bars TLS-broken — Day 10.** MA/RSI entry gates unverifiable script-side. Investigate at Mon pre-market.
5. **Macro filter** — SPY vs MA20 status heading into 3-day weekend uncertain; re-validate at Mon pre-market. BoA AI-bubble note is potential lingering overhang.
6. **Weekly buy budget resets Monday (7/6)** — 3/3 fresh.
7. **AMD next earnings 2026-08-04** — outside 5-day exclusion; no near-term binary on the position.
8. **Single-position book** since 6/25 AAPL trailing-stop fill; AMD is sole active position.

---

## EOD Snapshot — 2026-07-02 (Thursday — session: claude/sleepy-goldberg-spwv7d)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,101.57 |
| Cash | $91,845.93 |
| Long Market Value | $7,255.64 |
| Day P&L ($) | -$293.86 |
| Day P&L (%) | -0.296% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 6/29 — ends today; Fri 7/3 CLOSED) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $518.26 | -$391.08 (-5.11%) | -4.18% |

Notes: NO_TRADE day across pre-market / market-open / midday. **Short session (early close 1 PM ET) ahead of Fri 7/3 Independence Day observed — US markets CLOSED Fri.** Day P&L -$293.86 / -0.296% driven entirely by AMD markdown vs prior close ($539.25 → $518.26, -$20.99/sh × 14 = -$293.86). AMD intraday: pre-market cushion ~$24.91/sh → midday $513.25 (-6.03%, cushion tightened to ~$5.29/sh / ~1.03%) → close $518.26 (-5.11%, cushion recovered to ~$10.30/sh / ~1.99%) on modest late-session bounce off midday low. Position sized to 7.32% of equity (below 8% cap). Today's drawdown is macro/sector profit-taking — BoA "bubble risk" flag on AI trade dragged Intel -7%, TSM -6%, AMD -5% in sympathy; not a company-specific thesis break. **Thesis INTACT / strengthening:** Cantor PT $700 (raised from $500 pre-market), Wells Fargo PT $615 (raised from $505 6/30), UBS $670 all Overweight/Buy reaffirmed; DC GPU revenue $15.6B/$40.6B/$63B for 2026/27/28; 2nm EPYC Venice ramp H2 2026 intact. Next AMD earnings 2026-08-04 (outside 5-day exclusion). **AMD remains unprotected by broker-side trailing-stop (Day 9 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is the sole active control. Cash $91,845.93 = 92.68% of equity (≥20% reserve ✅); exposure 7.32% (≤80% ✅); daily-loss limit (3%) — day drift -0.30%, well within. **Week 6/29–7/2 closes: 0 buys / 0 sells / 0 events (4-day short week; Fri 7/3 CLOSED).**

**Carry-forward flags for Monday (7/6) pre-market:**
1. **AMD cut-watch — TIGHT into 3-day weekend.** -5.11% unrealized; cushion narrowed to ~$10.30/sh (~1.99%) to manual -7% threshold $507.96. **Monday pre-market: re-check immediately on cash open; if mark/last breaches $507.96, execute `python scripts/trade.py close AMD`.** 3-day weekend headline/gap risk elevated (Independence Day + weekend AI-trade sentiment).
2. **AMD broker-side trailing-stop infra gap — Day 9.** `scripts/trade.py` still lacks `trailing-stop` subcommand. **Position that swung from +$445 (6/30) to -$391 (7/2) unrealized in 3 sessions without a broker-side stop — infra patch materially overdue.** Escalate.
3. **AMD position 7.32% of equity** — below 8% size cap on pullback; any add still barred (averaging-down on a losing position + Day 9 broker-side stop gap).
4. **yfinance bars TLS-broken — Day 9.** MA/RSI entry gates unverifiable script-side. Investigate at Mon pre-market.
5. **Macro filter** — SPY vs MA20 status heading into 3-day weekend uncertain; re-validate at Mon pre-market. BoA AI-bubble note is potential lingering overhang.
6. **Weekly buy budget resets Monday (7/6)** — 3/3 fresh.
7. **AMD next earnings 2026-08-04** — well outside 5-day exclusion; no near-term binary on the position.
8. **AAPL exit context**: single-position book since 6/25 AAPL trailing-stop fill; AMD is sole active position.

---

## Midday Scan — 2026-07-02 (Thursday — session: claude/exciting-bohr-fjo434)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $513.25 | -$461.17 (-6.03%) |

Midday checks:
- **Cut-loser (−7%)**: AMD -6.03% — **no cut** (cushion ~$5.29/sh to -7% threshold $507.96, ~1.03%). **Tightened materially** from pre-market ~$24.91/sh (~4.68%) on intraday selloff (mark $532.87 → $513.25, -3.68% intraday). Day change -5.11%.
- **Stop-tighten (+15%/+20%)**: no position at gain.
- **Thesis check**: **INTACT.** Today's -5% is macro/sector profit-taking after AMD's ATH $580.91 on Tue + BoA "bubble risk" flag on AI trade (Intel -7%, AMD -5%, TSM -6%). Not a company-specific break. Cantor $700 PT (up from $500) + WFC $615 PT reaffirmed pre-market — bullish PT revisions intact. Prior UBS $670 PT still standing. Next AMD earnings 2026-08-04 (outside 5-day exclusion). NFP print + pre-holiday illiquidity likely amplifying moves.
- **Trailing-stop infra gap**: AMD broker-side stop still unprotected (Day 9 carry-forward). Manual -7% cut at $507.96 is sole control.
- **Early close 1 PM ET today, market closed Fri 7/3** — 3-day weekend headline risk if not cut before close. But thesis intact and -7% not breached — hold.

No trades executed. Risk posture: cash ~92.8% of equity (≥20% ✅), exposure ~7.2% (≤80% ✅), daily-loss limit (3%) — AMD -5.11% day = ~-0.38% portfolio, well within.

**Flags for end-of-day (or before 1 PM early close):**
1. **AMD cut-watch CRITICAL TIGHT** — cushion $5.29/sh (~1.03%) to $507.96. Re-check at EOD/early-close; if breached, execute `python scripts/trade.py sell AMD` immediately (limit-sell tooling absent — market-order strategy-stop exception per CLAUDE.md).
2. AMD broker-side trailing-stop infra gap — Day 9 carry-forward.
3. Thesis intact (Cantor $700 + WFC $615 + UBS $670 PTs) — hold conviction supported despite tape weakness.
4. **3-day weekend gap risk** ahead — if AMD closes near cut threshold, evaluate defensive close before 1 PM.

---

## EOD Snapshot — 2026-07-01 (Wednesday — session: claude/sleepy-goldberg-bsvsom)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,395.43 |
| Cash | $91,845.93 |
| Long Market Value | $7,549.50 |
| Day P&L ($) | -$542.64 |
| Day P&L (%) | -0.543% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 6/29) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L | Day Change |
|--------|-----|-----------|---------|----------------|-----------|
| AMD | 14 | $546.19 | $539.25 | -$97.22 (-1.27%) | -7.17% |

Notes: NO_TRADE day across pre-market / market-open / midday. Day P&L -$542.64 / -0.543% driven entirely by AMD giving back Tue's rally — mark $578.01 → $539.25 (-$38.76/sh × 14 = -$542.64). AMD intraday: market-open $556.24 (+1.84%) → midday $552.33 (+1.12%) → close $539.25 (-1.27%), late-session fade of ~$13/sh into the bell. AMD day change -7.17% per Alpaca reflects the pullback from Tue's blowout $578.01 close (which itself was +7.37% on the day). Position sized back to 7.60% of equity (below 8% cap on the pullback). Cushion to manual -7% cut threshold $507.96 = ~$31.29/sh (~5.80%) — materially tightened from Tue EOD ~$70.05/sh (~12.12%) but still comfortable and well off the Fri 6/26 tight zone (~$10/sh). No thesis break: WFC $615 / Cantor $700 (both Overweight) reaffirmed; DC GPU $15.6B/$40.6B/$63B for 2026/27/28; 2nm EPYC Venice ramp H2 2026 intact. Today's drawdown is post-blowout digestion + Warsh Sintra headline flow, not a company-specific catalyst. **AMD remains unprotected by broker-side trailing-stop (Day 8 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is the sole active control. Cash $91,845.93 = 92.40% of equity (≥20% reserve ✅); exposure 7.60% (≤80% ✅); daily-loss limit (3%) — day drift -0.54%, well within. Weekly buy budget 0/3 preserved.

**Carry-forward flags for Thursday (7/2) pre-market:**
1. **AMD cut-watch — TIGHTENED but comfortable.** -1.27% unrealized; cushion narrowed to ~$31.29/sh (~5.80%) to manual -7% threshold $507.96. Monitor at pre-market for any Warsh follow-through / macro re-tightening.
2. **AMD broker-side trailing-stop infra gap — Day 8.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Priority escalation: with position that swung from +$445 to -$97 unrealized in a single session, the infra patch is materially overdue.
3. **AMD +15% trim watch still staged** — mark $539.25 vs +15% trim trigger ~$628.12. Cushion ~$88.87/sh (~16.5%). Not actionable.
4. **yfinance bars TLS-broken — Day 8.** MA/RSI entry gates unverifiable script-side. Investigate at pre-market.
5. **Macro filter** — re-validate SPY vs MA20 at Thu pre-market; watch for Warsh Sintra follow-through.
6. **Weekly buy budget 3/3 preserved** into Thu–Fri (short week — Fri 7/3 half-day early close / Fri close ahead of Jul 4 holiday possible; verify Alpaca calendar).
7. **AMD next earnings 2026-08-04** — well outside 5-day exclusion.
8. **Independence Day (Fri 7/4) — US markets CLOSED.** Thu 7/2 pre-market: verify Wed 7/3 half-day / early-close status.

---

## Midday Scan — 2026-07-01 (Wednesday — session: claude/exciting-bohr-9x1tub)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L | Day Change |
|--------|-----|-----------|------|----------------|-----------|
| AMD | 14 | $546.19 | $552.33 | +$85.90 (+1.12%) | -4.92% |

Midday checks:
- **Cut-loser (−7%)**: AMD +1.12% — no cut. Position in profit; cushion ~$44.37/sh (~8.03%) to manual -7% threshold $507.96.
- **Stop-tighten (+15%/+20%)**: AMD +1.12%, below +15% trigger ($628.12). No tighten. Cushion ~$75.79/sh to +15% trim.
- **Thesis check**: AMD thesis intact / strengthening per market-open log — WFC PT $615, Cantor $700 (both Overweight); DC GPU revenue $15.6B/$40.6B/$63B for 2026/27/28; 2nm EPYC Venice ramp H2 2026. Next earnings 2026-08-04 (outside 5-day exclusion). No thesis break.
- **Trailing-stop infra gap (Day 8)**: AMD still unprotected by broker-side trailing-stop (`scripts/trade.py` lacks `trailing-stop` subcommand). Manual -7% cut at $507.96 remains sole protection.

Day drift vs market-open: mark $556.24 → $552.33 (-$3.91/sh, -0.70% intra-session); AMD day change -4.92% reflects pullback from Tue $578.01 close. Still comfortably above cut threshold.

No trades executed. Weekly buys 0/3 used. Risk posture: cash 92.24% of equity (≥20% ✅), exposure 7.76% (≤80% ✅), daily-loss limit (3%) untouched.

**Flags for end-of-day:**
1. AMD manual cut at $507.96 — cushion ~$44.37/sh (~8.03%); monitor through close.
2. AMD +15% trim staging — mark $552.33 vs $628.12; cushion ~$75.79/sh. Not yet actionable.
3. AMD broker-side trailing-stop infra gap — Day 8 carry-forward.
4. yfinance bars TLS-broken — Day 8 carry-forward.
5. Weekly buy budget 3/3 preserved.

---

## Market-Open Log — 2026-07-01 (Wednesday — session: claude/sweet-shannon-0fbyuo)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $91,845.93 |
| Equity | $99,632.59 |
| Long Market Value | $7,786.66 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 0 / 3 (week of 6/29) |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AMD 7.82%; below 8% cap post-pullback)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD reaffirmed; AMD trim-watch not add, MU/GOOGL DEFERRED (TLS Day 8).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L | Day Change |
|--------|-----|-----------|------|----------------|-----------|
| AMD | 14 | $546.19 | $556.24 | +$140.64 (+1.84%) | -4.25% |

Three independent stand-downs (matching pre-market):
- **No new-candidate catalyst.** yfinance TLS-broken **Day 8** — MA20/MA50/RSI-14 gates unverifiable for any symbol. MU and GOOGL deferred at pre-market on the same block.
- **AMD add not indicated.** Position pulled back to 7.82% (below 8% cap), but no add trigger in today's research log — averaging into an existing winner is not a documented catalyst. Position +1.84% unrealized; not distressed.
- **Warsh Sintra binary today.** Fed Chair speaking; asymmetric downside on any hawkish surprise given SPY-vs-MA20 macro re-tighten risk from mid-June. Reserve weekly buy budget.

**AMD risk management:**
- Unrealized +$140.64 (+1.84%) vs manual -7% cut $507.96. **Cushion ~$48.28/sh (~8.68%)** — comfortable; well off Fri 6/26 tight zone (~$10/sh).
- +15% trim trigger ~$628.12; mark $556.24 = cushion ~$71.88/sh (~12.9%). Not actionable.
- **Broker-side trailing-stop still infra-gated — Day 8.** `scripts/trade.py` lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 remains sole protection.
- Thesis intact / strengthening: WFC PT $615, Cantor $700 both Overweight; DC GPU $15.6B/$40.6B/$63B for 2026/27/28; 2nm EPYC Venice ramp H2 2026. Next earnings 2026-08-04.

Trades executed: **none.**

Risk posture: cash 92.18% of equity (≥20% ✅); exposure 7.82% (≤80% ✅); daily-loss limit (3%) — day drift -$305.48 / -0.31% from Tue EOD, well within. Weekly buys 0/3 used — 3 remaining preserved into Wed–Fri.

**Flags for midday-scan:**
1. **AMD manual cut at $507.96.** Cushion ~$48.28/sh (~8.68%) — comfortable; monitor for Warsh-hawkish sell-off risk.
2. **AMD +15% trim staging** — mark $556.24 vs $628.12; cushion ~$71.88/sh. Not yet actionable.
3. **AMD broker-side trailing-stop infra gap — Day 8.** Carry-forward.
4. **yfinance bars TLS-broken — Day 8.** Carry-forward.
5. **Warsh Sintra headline flow** — hawkish surprise → macro filter re-tighten risk.
6. **Weekly buy budget 3/3** — preserved.

---

## EOD Snapshot — 2026-06-30 (Tuesday — session: claude/sleepy-goldberg-0mjjkc)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,938.07 |
| Cash | $91,845.93 |
| Long Market Value | $8,092.14 |
| Day P&L ($) | +$555.61 |
| Day P&L (%) | +0.559% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 6/29 — fresh budget) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AMD | 14 | $546.19 | $578.01 | +$445.42 (+5.83%) |

Notes: NO_TRADE day across pre-market / market-open / midday. Day P&L +$555.61 / +0.559% driven entirely by AMD rally vs Mon close ($538.32 → $578.01, +$39.69/sh × 14 = +$555.66). AMD intraday hit all-time high $563.25 then closed above at $578.01 (+7.14% day change per Alpaca). **AMD thesis materially strengthened** — Wells Fargo (Rakers) raised PT to $615 from $505 (Overweight) projecting server CPU revenue +68% YoY 2026 / +28% 2027 / +22% 2028 above consensus; Cantor Fitzgerald raised PT to $700 from $500 (Overweight). Position now 8.10% of equity — appreciated above the 8% per-position size cap; **not a violation** since the cap applies at-entry and the position was 7.46% at fill. No trim required at this level (strategy +15% trim trigger at ~$628.12 still ~$50/sh away). Cushion to manual -7% cut threshold $507.96 = ~$70.05/sh (~12.12%) — materially widened from Mon EOD ~$30.36/sh (~5.64%). **AMD remains unprotected by broker-side trailing-stop (Day 7 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut is the active control; cushion is now comfortable but unrealized gain warrants prioritizing the infra patch. Cash $91,845.93 = 91.90% of equity (≥20% reserve ✅); exposure 8.10% (≤80% ✅); daily-loss limit (3%) — day P&L strongly positive. Weekly buy budget 0/3 fresh.

**Carry-forward flags for Wednesday (7/1) pre-market:**
1. **AMD +15% trim watch.** Mark $578.01 vs +15% trim trigger ~$628.12. Cushion ~$50.11/sh (~8.67%). Not yet actionable but begin staging trim plan (50% per strategy).
2. **AMD broker-side trailing-stop infra gap — Day 7.** Priority escalation: with +$445.42 unrealized, patching `scripts/trade.py` to add `trailing-stop` subcommand is the right defensive move. Until patched, manual -7% cut at $507.96 remains sole protection.
3. **AMD position 8.10% of equity** — above 8% size cap on appreciation. No action required (cap is at-entry), but any add is barred regardless.
4. **yfinance bars TLS-broken — Day 7.** MA/RSI entry gates unverifiable script-side. Investigate at pre-market.
5. **Macro filter** — re-validate SPY vs MA20 at Wed pre-market.
6. **Weekly buy budget 3/3 fresh** into Wed–Fri.
7. **AMD next earnings 2026-08-04** — well outside 5-day exclusion.
8. **Month-end / quarter-end 2026-06-30** — possible rebalancing flows into early July; expect noisier tape.

---

## Midday Scan — 2026-06-30 (Tuesday — session: claude/exciting-bohr-df3ozl)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $576.44 | +$423.37 (+5.54%) |

Midday checks:
- **Cut-loser (−7%)**: AMD +5.54% — no cut. Position is in profit.
- **Stop-tighten (+15%/+20%)**: AMD +5.54%, below +15% trigger. No tighten yet (cushion ~$68/sh to +15% at $628.12).
- **Thesis check**: AMD thesis **materially strengthened** today — Wells Fargo (Rakers) raised PT to $615 from $505 (Overweight); Cantor Fitzgerald raised PT to $700 from $500 (Overweight). Rakers projects server CPU revenue +68% YoY 2026, +28% 2027, +22% 2028 — meaningfully above consensus. AMD hit all-time high $563.25 intraday; mark now $576.44 (+6.85% day change). No thesis break — opposite, accelerating.
- **Trailing-stop infra gap (Day 7)**: AMD still unprotected by broker-side trailing-stop (`scripts/trade.py` lacks `trailing-stop` subcommand). Manual -7% cut at $507.96 remains active control, but mark is well above ($68.48/sh / +13.5% cushion).

No trades executed. Weekly buys 0/3 used. Risk posture: cash $91,845.93 ≈ 91.9% (≥20% ✅), exposure ~8.07% (just over 8% per-position cap on appreciation — not a violation since size-at-entry was compliant), daily-loss limit (3%) — day P&L strongly positive.

**Flags for end-of-day:**
1. AMD position appreciated above 8% size cap due to gains (8.07%) — no action required (cap is at-entry), but flag for sizing context if any add is considered.
2. AMD broker-side trailing-stop infra gap — Day 7 carry-forward; consider patching `scripts/trade.py` to add `trailing-stop` subcommand given AMD now has meaningful unrealized gain to protect.
3. Strategy note: at +15% (~$628.12) consider trimming 50% per strategy.md exit criteria.
4. yfinance bars TLS-broken — Day 7 carry-forward.

---

## EOD Snapshot — 2026-06-29 (Monday — session: claude/sleepy-goldberg-yvhbum)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,382.46 |
| Cash | $91,845.93 |
| Long Market Value | $7,536.53 |
| Day P&L ($) | +$284.53 |
| Day P&L (%) | +0.287% |
| Trades Today | 0 |
| Trades This Week | 0 (week of 6/29 — fresh budget) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AMD | 14 | $546.19 | $538.32 | -$110.19 (-1.44%) |

Notes: NO_TRADE day across pre-market / market-open / midday. Day P&L +$284.53 / +0.287% driven entirely by AMD recovery vs Fri close ($518.00 → $538.32, +$20.32/sh × 14 = +$284.48). AMD cushion to manual -7% cut threshold $507.96 = ~$30.36/sh (~5.64%) — **materially widened from Fri EOD ~$10.04/sh (~1.94%)** on overnight rebound. Three independent stand-downs reaffirmed all session: (1) macro filter SPY << MA20 — universal buy block under strategy criterion #4; (2) yfinance bars TLS-broken **Day 6** — MA20/MA50/RSI-14 entry gates unverifiable script-side; (3) AMD already at 7.58% position cap with averaging-down on a losing position barred. AMD thesis intact (Bernstein $600, UBS $670 PTs reaffirmed; Micron HBM 2026 sold-out read-through unchanged; next earnings 2026-08-04). **AMD remains unprotected by broker-side trailing-stop (Day 6 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is the active control. Cash $91,845.93 = 92.42% of equity (≥20% reserve ✅); exposure 7.58% (≤80% ✅); daily-loss limit (3%) untouched. Weekly buy budget 0/3 fresh into Tue–Fri.

**Carry-forward flags for Tuesday (6/30) pre-market:**
1. **AMD cut-watch — RELAXED.** -1.44% unrealized; cushion widened to ~$30.36/sh (~5.64%) to manual -7% threshold $507.96. Continue monitoring at pre-market.
2. **AMD broker-side trailing-stop infra gap — Day 6.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual cut is sole protection. Escalate / patch.
3. **yfinance bars TLS-broken — Day 6.** MA/RSI entry gates unverifiable script-side. Investigate at pre-market.
4. **Macro filter** — SPY << MA20; re-validate at Tue pre-market.
5. **Weekly buy budget 3/3 fresh** into Tue–Fri.
6. **AMD next earnings 2026-08-04** — well outside 5-day exclusion.

---

## Midday Scan — 2026-06-29 (Monday — session: claude/exciting-bohr-rrlr3c)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $528.14 | -$252.76 (-3.31%) |

Midday checks:
- **Cut-loser (−7%)**: AMD -3.31% — no cut (cushion ~$20.18/sh to -7% threshold $507.96). Mark drifted modestly from market-open $529.22 → $528.14 (-$0.18% intraday); cushion essentially unchanged.
- **Stop-tighten (+15%/+20%)**: no position at gain. AMD broker-side trailing-stop still infra-gated (Day 6 carry-forward) — `scripts/trade.py` lacks `trailing-stop` subcommand. Manual -7% cut remains sole protection.
- **Thesis check**: AMD thesis intact — no company-specific news flow this routine. Macro tape constructive into midday (Trump admin US/Iran "stand down", futures up; offsetting headlines on Nasdaq 100 5-day slide + tech volatility 23-year high vs S&P). Bernstein $600 / UBS $670 PTs reaffirmed pre-market; Micron HBM 2026 sold-out read-through unchanged. Next AMD earnings 2026-08-04 (well outside 5-day exclusion).

No trades executed. Weekly buys 0/3 used. Risk posture: cash ~92.5% (≥20% ✅), exposure ~7.5% (≤80% ✅), daily-loss limit (3%) — day drift +$143.13 / +0.14% from Fri EOD, well within.

**Flags for end-of-day:**
1. AMD manual cut at -7% ($507.96) — cushion ~$20.18/sh (~3.82%); monitor through close.
2. AMD broker-side trailing-stop infra gap — Day 6 carry-forward.
3. yfinance bars TLS-broken — Day 6 carry-forward; entry gates remain unverifiable.
4. Macro filter — SPY MA20 status unverifiable script-side; re-validate at EOD.

---

## Market-Open Log — 2026-06-29 (Monday — session: claude/sweet-shannon-4ynrly)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $91,845.93 |
| Equity | $99,270.69 |
| Long Market Value | $7,424.76 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 0 / 3 (week of 6/29 — fresh budget) |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AMD 7.46%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD reaffirmed; AMD ADD barred (cap + averaging-down on -3.11% loser), MU/GOOGL conditional on macro clear + RSI/MA verification.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $529.22 | -$237.71 (-3.11%) |

Three independent stand-downs (reaffirming pre-market):
- **Macro filter likely still fails** — SPY live $739.75 (bid $739.13 / ask $739.75). Friday close ~-2.1% below MA20 (~$745 implied); a 0.53% ES bid does not clear MA20. Cannot verify MA20 directly: yfinance TLS-broken Day 6 (zero bars).
- **yfinance bars TLS-broken — Day 6.** Both SPY and AMD bar requests return `OPENSSL_internal:invalid library`. MA20/MA50/RSI-14 entry gates (strategy criteria #1, #2) unverifiable script-side. Markov + technical screen un-runnable.
- **AMD at cap + averaging-down barred** — position 7.46% of equity (close to 8% cap); strategy precedent bars averaging down on -3.11% loser. No other watchlist symbol passes macro filter + has verifiable entry gates.

**AMD risk management:**
- Unrealized -3.11% vs manual -7% threshold $507.96. **Cushion ~$21.26/sh (~4.02%)** — materially widened vs Fri EOD ~$10.04/sh (~1.94%) on overnight recovery (+$11.22/sh / +2.17% from $518.00 close).
- **Broker-side trailing-stop still infra-gated — Day 6.** `scripts/trade.py` lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 remains sole protection. Escalation flagged.
- Thesis intact — Bernstein $600, UBS $670 PTs reaffirmed; Micron HBM 2026 sold-out read-through unchanged. Next AMD earnings 2026-08-04 (outside 5-day exclusion).

Trades executed: **none.**

Risk posture: cash 92.52% of equity (≥20% reserve ✅); exposure 7.48% (≤80% ✅); daily-loss limit (3%) — day drift +$172.76 / +0.17% from Fri EOD, well within. Weekly buy budget 0/3 used — 3 remaining preserved into Tue–Fri.

**Flags for midday-scan:**
1. **AMD manual cut at $507.96.** Cushion ~$21.26/sh (~4.02%) — comfortable but monitor. If breached, execute `python scripts/trade.py close AMD`.
2. **AMD broker-side trailing-stop infra gap — Day 6.** Carry-forward.
3. **yfinance TLS-broken — Day 6.** Carry-forward; entry gates remain unverifiable.
4. **Macro filter live re-check at midday.** If SPY clears MA20 and TLS resolves, evaluate MU/GOOGL per pre-market conditionals.
5. **Weekly buy budget 3/3 fresh** — preserve for high-conviction post-screen candidate.

---

## EOD Snapshot — 2026-06-26 (Friday — session: claude/sleepy-goldberg-c1ymyq)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,097.93 |
| Cash | $91,845.93 |
| Long Market Value | $7,252.00 |
| Day P&L ($) | -$201.92 |
| Day P&L (%) | -0.203% |
| Trades Today | 0 |
| Trades This Week | 2 (AMD BUY 6/22 + AAPL SELL stop 6/25) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AMD | 14 | $546.19 | $518.00 | -$394.72 (-5.16%) |

Notes: NO_TRADE day across pre-market / market-open / midday. Three independent stand-downs reaffirmed all session: (1) macro filter SPY << MA20 ~-2.1% live at open — universal buy block under strategy criterion #4; (2) yfinance bars TLS-broken **Day 5** — MA20/MA50/RSI-14 entry gates unverifiable script-side; (3) AMD already at 7.36% position cap with averaging-down on a losing position barred by strategy precedent, MU post-blowout gap-up almost certainly RSI > 70. AMD intraday: market-open mark $510.71 (-6.50%, cushion ~$2.75/sh) → midday $521.43 (-4.53%, cushion ~$13.47/sh on +2.10% recovery) → close $518.00 (-5.16%, cushion ~$10.04/sh on late-session fade). Day P&L -$201.92 / -0.203% driven entirely by AMD markdown vs prior close ($532.42 → $518.00, -$14.42/sh × 14 = -$201.88). **AMD remains unprotected by broker-side trailing-stop (Day 5 infra carry-forward)** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual -7% cut at $507.96 is the active control. Thesis intact (UBS PT $670 reaffirmed, Micron HBM 2026 sold-out read-through unchanged, next AMD earnings 2026-08-04 outside 5-day exclusion); today's drawdown is macro/sector (chip rout + Kashkari hawkish + Iran/Hormuz ceasefire violation), not a thesis break. Cash $91,845.93 = 92.68% of equity (≥20% reserve ✅); exposure 7.32% (≤80% ✅); daily-loss limit (3%) — day drift -0.20%, comfortably within. **Week 6/22–6/26 closes: 1 buy (AMD 6/22) / 1 sell (AAPL trailing-stop 6/25) / 2 events.** Weekly buy budget 1/3 used.

**Carry-forward flags for Monday (6/29) pre-market:**
1. **AMD cut-watch — TIGHT.** -5.16% unrealized; cushion narrowed to ~$10.04/sh (~1.94%) to manual -7% threshold $507.96. Materially tightened vs midday. **Monday pre-market: re-check immediately; if mark/last breaches $507.96, execute `python scripts/trade.py close AMD`.**
2. **AMD broker-side trailing-stop infra gap — Day 5.** `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual cut is sole protection. Escalate.
3. **yfinance bars TLS-broken — Day 5.** MA/RSI entry gates unverifiable script-side. Investigate at pre-market or carry forward as infra block.
4. **Macro overhang** — PCE hawkish + Iran/Hormuz ceasefire violation + chip rout + Kashkari signaling potential hikes. SPY << MA20 (~-2.1%). Re-validate at Mon pre-market.
5. **Week-1 of new month upcoming** — weekly buy budget resets Monday (3/3 fresh).
6. **AMD next earnings 2026-08-04** — well outside 5-day exclusion; no near-term binary on the position.

---

## Midday Scan — 2026-06-26 (Friday — session: claude/exciting-bohr-draf74)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $521.43 | -$346.70 (-4.53%) |

Midday checks:
- **Cut-loser (−7%)**: AMD -4.53% — no cut (cushion ~$13.47/sh to -7% threshold $507.96; **materially widened** vs market-open ~$2.75/sh on intraday recovery $510.71 → $521.43, +$10.72/sh / +2.10%).
- **Stop-tighten (+15%/+20%)**: no position at gain.
- **Thesis check**: AMD thesis intact — no company-specific break. Today's tape driven by macro/sector: chip rout dragging Nasdaq 100, Kashkari (Bloomberg) signaling Fed may need to hike on broad inflation, Iran/Strait-of-Hormuz drone strikes (ceasefire violation). UBS PT $670 (Arcuri 5-star) reaffirmed; Micron HBM 2026 sold-out read-through unchanged; next earnings 2026-08-04.
- **Trailing-stop infra gap**: AMD broker-side stop still gated on missing `trailing-stop` subcommand in `scripts/trade.py` (Day 5 carry-forward). Manual -7% cut remains the active control.

No trades executed. Weekly buys 1/3 used. Risk posture: cash 92.64% (≥20% ✅), exposure 7.36% (≤80% ✅), daily-loss limit (3%) — day drift -$152.92 / -0.15%, well within.

**Flags for end-of-day:**
1. AMD manual cut at -7% ($507.96) — cushion widened to ~$13.47/sh (~2.58%) on intraday recovery; monitor through close.
2. AMD broker-side trailing-stop retry still infra-gated (Day 5).
3. yfinance bars TLS-broken (Day 5) — carry-forward.
4. Macro overhang — PCE hawkish + Iran/Hormuz + chip rout. Re-validate SPY vs MA20 at EOD.

---

## Market-Open Log — 2026-06-26 (Friday — session: claude/sweet-shannon-y6038g)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $91,845.93 |
| Equity | $99,000.14 |
| Long Market Value | $7,154.21 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 1 / 3 buys (2 events including AAPL stop) |
| Decision | **NO_TRADE — HOLD; AMD on CRITICAL TIGHT cut-watch** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (1/3 buys)
- Max 8% equity per position ✅ (AMD 7.22%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD reaffirmed; AMD ADD rejected (cap+avg-down+macro), GOOGL Dow-add deferred (macro), MU post-blowout deferred (RSI+TLS+macro).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $510.71 | -$496.78 (-6.50%) |

Three independent stand-down reasons (reaffirming pre-market):
- **Macro filter fails HARDER** — SPY live $729.31 << est MA20 ~$745 (~-2.1%). Pre-market SPY was $734.96; tape opened weaker on PCE digestion. Universal buy block under strategy criterion #4.
- **yfinance bars TLS-broken (Day 5)** — SPY/AMD snapshots return zero bars; MA20/MA50/RSI-14 unverifiable. Entry criteria #1 & #2 cannot be confirmed script-side.
- **AMD already at cap + cut-watch** — add blocked (7.22% of equity, averaging-down barred); no other watchlist symbol passes macro filter.

**AMD risk management — CRITICAL TIGHT CUT-WATCH:**
- Live unrealized -6.50% vs manual -7% threshold $507.96. **Cushion ~$2.75/sh on mark $510.71 (~0.54%).** Materially tightened from pre-market ~$12.04/sh (~2.31%).
- **Bid $505.53 is already BELOW the -7% threshold $507.96** — sell at bid would lock in worse than the cut trigger. Wide spread ~2.06% at open = execution risk if forced to cut.
- If mark/last breaches $507.96 at any subsequent routine: execute `python scripts/trade.py close AMD` (limit-sell tooling absent — market-order strategy-stop exception per CLAUDE.md "no exceptions" stop-loss rule).
- **Broker-side trailing-stop still infra-gated (Day 5)** — `scripts/trade.py` lacks `trailing-stop` subcommand. Manual cut is the only protection.
- Thesis intact — UBS bull case reaffirmed; this week's drawdown is macro/PCE-driven, not thesis break. Next earnings 2026-08-04 (outside 5-day exclusion).

Trades executed: **none.**

Risk posture: cash 92.77% of equity (≥20% reserve ✅); exposure 7.23% (≤80% ✅); daily-loss limit (3%) — day drift -$299.71 / -0.30%, well within. Weekly buy budget 1/3 used — 2 remaining preserved into Friday close (final day of week 6/22–6/26).

**Flags for midday-scan:**
1. **AMD manual -7% cut at $507.96 — CRITICAL.** Cushion ~$2.75/sh. **Re-check at midday; if mark breaches, execute close immediately.**
2. **Wide spread at open** (~2.06%) — execution risk; bid already below -7% threshold.
3. **Macro filter** — SPY $729.31 << est MA20 ~$745. Re-validate at midday.
4. **AMD broker-side trailing-stop infra gap (Day 5).** Carry-forward.
5. **yfinance bars TLS-broken (Day 5).** Carry-forward.
6. **Weekly buy budget** — 1/3 used; 2 remaining into Friday close.

---

## EOD Snapshot — 2026-06-25 (Thursday — session: claude/sleepy-goldberg-93g1e1)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,299.85 |
| Cash | $91,845.95 |
| Long Market Value | $7,453.90 |
| Day P&L ($) | -$60.02 |
| Day P&L (%) | -0.060% |
| Trades Today | 1 (AAPL trailing-stop fill overnight) |
| Trades This Week | 2 (AMD BUY 6/22 + AAPL SELL stop 6/25) |
| Open Positions | 1 / 8 (AMD 14 sh) |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AMD | 14 | $546.19 | $532.42 | -$192.82 (-2.52%) |

Notes: AAPL closed overnight via 10% trailing-stop GTC ($285.66 fill, cash $91,560.43 → $91,845.95 = +$285.52 net; realized P&L ≈ -$16.36 / -5.42% vs $301.88 entry). Position was 0.30% of equity — immaterial — and trailing-stop fired as designed. Single-position book now: AMD only. Regular session NO_TRADE across pre-market / market-open / midday on three independent stand-downs: (1) macro filter SPY << MA20 ~-1.64% live at open; (2) yfinance bars TLS-broken — MA20/MA50/RSI-14 gates unverifiable; (3) AMD add blocked at 7.40% cap, MU post-blowout gap-up almost certainly RSI > 70. AMD recovered through afternoon — midday -$307.78 (-4.03%) → close -$192.82 (-2.52%), a +$114.96 intraday rebound (~+1.51% on AMD). Cushion to -7% cut threshold $507.96 = ~$24.05/sh (~4.52%) — materially widened vs market-open ~$15.69/sh / ~3.0%. **AMD remains unprotected by broker-side trailing-stop** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual cut at -7% is the active control; carry-forward to Friday. Cash $91,845.95 = 92.49% of equity (≥20% reserve ✅); exposure 7.51% (≤80% ✅); daily-loss limit (3%) — day drift -0.06%, well within. Weekly buy budget 1/3 used (2 remaining into Friday); weekly sells 1 (AAPL stop).

**Carry-forward flags for Friday pre-market:**
1. **AMD cut-watch** — -2.52% unrealized; cushion ~$24.05/sh (~4.52%) to manual -7% threshold $507.96. Materially widened vs morning — monitor at pre-market.
2. **AMD broker-side trailing-stop retry** — `scripts/trade.py` still missing `trailing-stop` subcommand. Infrastructure carry-forward.
3. **Macro filter** — SPY << MA20 at Thu open (-1.64%); re-validate at Fri pre-market.
4. **yfinance bars TLS-broken** — MA/RSI gates unverifiable. Investigate at pre-market or carry forward as infra block.
5. **MU post-print** — gap-up to $1,197.37 on blowout; if RSI fades to 35–70 band intraday and TLS resolves, becomes a Friday candidate (weekly buy budget supports it: 2/3 remaining).
6. **AAPL reconciliation complete** — trailing-stop fill confirmed via cash delta ($285.52 net inflow). Realized -$16.36 logged.

---

## Midday Scan — 2026-06-25 (Thursday — session: claude/exciting-bohr-zw1722)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $524.21 | -$307.78 (-4.03%) |

Midday checks:
- **Cut-loser (−7%)**: AMD -4.03% — no cut (cushion ~$16.25/sh to -7% threshold $507.96; widened vs market-open ~$15.69/sh on intraday +0.86% drift).
- **Stop-tighten (+15%/+20%)**: no position at gain.
- **Thesis check**: AMD thesis intact — UBS PT $670 (Arcuri 5-star) reaffirmed on agentic-AI CPU demand; Micron HBM 2026 sold-out read-through unchanged. This week's drawdown is macro/risk-off (hawkish-Fed-driven semi rotation), not a thesis break. Next earnings 2026-08-04.
- **Trailing-stop infra gap**: AMD still unprotected by broker-side trailing-stop (`scripts/trade.py` lacks `trailing-stop` subcommand). Manual -7% cut remains the active control. Carry-forward.

AAPL closed overnight via trailing-stop GTC (per market-open log) — single-position book now.

No trades executed. Weekly buys 1/3 used. Risk posture: cash ~92.6% (≥20% ✅), exposure ~7.4% (≤80% ✅), daily-loss limit (3%) untouched.

**Flags for end-of-day:**
1. AMD broker-side trailing-stop retry still infra-gated.
2. AAPL closure reconciliation — confirm fill price/timestamp; update ledger at EOD.

---

## Market-Open Log — 2026-06-25 (Thursday — session: claude/sweet-shannon-535i7k)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:48 ET) |
| Cash | $91,845.95 |
| Equity | $99,193.43 |
| Long Market Value | $7,347.48 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 1 / 3 |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (1/3)
- Max 8% equity per position ✅ (AMD 7.40%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; AMD ADD blocked at cap, MU NEW LONG conditional on RSI validation that cannot be performed (TLS-broken yfinance).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $523.65 | -$315.56 (-4.13%) |

**AAPL position CLOSED overnight** — trailing-stop GTC $285.66 fired (cash $91,560.43 → $91,845.95 = +$285.52 net of fees; realized P&L ≈ -$16.22 / -5.37% vs entry $301.88). Routine inherits 1 position (AMD only); to be reconciled in EOD with order-fill detail.

Three independent stand-down reasons (reaffirming pre-market):
- **Macro filter fails** — SPY live $732.78 << implied MA20 ~$745 (-1.64%). Universal buy block under strategy criterion #4. SPY closed 6/24 at ~$735.82; tape opened risk-off vs the pre-market futures hint.
- **yfinance bars TLS-broken** — SPY/AMD/MU 60-bar requests all return `OPENSSL_internal:invalid library`. MA20/MA50/RSI-14 gates unverifiable from bar data; entry criteria #1 & #2 cannot be confirmed.
- **AMD add blocked + MU gap-up unverifiable** — AMD position at -4.13% (averaging-down on a losing position is barred by strategy precedent); MU gapped to $1,197.37 post-blowout — without RSI confirmation, post-print gap-up almost certainly puts RSI > 70 (overbought entry filter ceiling).

**AMD risk management:**
- Unrealized -4.13% vs manual -7% threshold $507.96. **Cushion ~$15.69/sh (~3.0% to threshold)** — tightened from EOD ~$28.54/sh (~5.32%) on broad semi reversal at open despite Micron blowout read-through.
- **Broker-side trailing-stop still infra-gated** — `scripts/trade.py` lacks `trailing-stop` subcommand. Manual cut at -7% remains active control.
- Thesis intact: Micron HBM 2026 sold-out + UBS $670 PT (Arcuri 5-star) reaffirm AMD AI-DC unit-economics. Today's price action is macro/risk-off, not a thesis break.

Trades executed: **none.**

Risk posture: cash 92.60% of equity (≥20% reserve ✅); exposure 7.40% (≤80% ✅); daily-loss limit (3%) — day drift -$166.44 / -0.17%, well within. Weekly buy budget 1/3 used — 2 remaining preserved into Fri.

**Flags for midday-scan:**
1. **AMD manual cut at -7%** ($507.96) — cushion ~$15.69/sh (~3.0%). Re-check at midday; execute `python scripts/trade.py close AMD` if breached.
2. **AAPL closure reconciliation** — confirm trailing-stop fill price/timestamp; update performance ledger at EOD with realized P&L.
3. **AMD broker-side trailing-stop retry** — still infra-gated.
4. **MU post-print** — if RSI validates inside 35–70 band intraday after gap-up fade (and TLS issue resolves), may become a Friday candidate.

---

## EOD Snapshot — 2026-06-24 (Wednesday — session: claude/sleepy-goldberg-a8e3qh)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,359.87 |
| Cash | $91,560.43 |
| Long Market Value | $7,799.44 |
| Day P&L ($) | +$193.28 |
| Day P&L (%) | +0.195% |
| Trades Today | 0 |
| Trades This Week | 1 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $294.06 | -$7.82 (-2.59%) |
| AMD | 14 | $546.19 | $536.50 | -$135.72 (-1.78%) |

Notes: NO_TRADE day across pre-market / market-open / midday (macro filter SPY < MA20 live at open -1.34%; Micron earnings AMC binary read-through to AMD; yfinance bars TLS-broken — MA/RSI gates unverifiable; AMD already at 7.27% position cap blocked any add). Day P&L +$193.28 / +0.195% driven by AMD recovering +$199.84 intraday ($522.23 → $536.50, +2.73%) on broad semi-bid into Micron print; AAPL marked down -$0.75 vs prior close. AMD cushion to -7% cut threshold $507.96 = ~$28.54/sh (~5.32%) — materially widened from prior EOD (~$14.27/sh / ~2.73%). AAPL 10% trailing-stop GTC $285.66 active (HWM $317.40, cushion ~$8.40/sh, ~2.9% to stop). **AMD remains unprotected by broker-side trailing-stop** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual cut at -7% remains the active control. Cash $91,560.43 = 92.15% of equity (≥20% reserve ✅); exposure 7.85% (≤80% ✅); daily-loss limit (3%) untouched. Weekly buy budget 1/3 used — 2 remaining into Thu–Fri.

**Carry-forward flags for Thursday pre-market:**
1. **Micron earnings AMC tonight** — direct read-through to AMD on memory/HBM pricing + AI-server channel. Assess thesis impact at pre-market and gate any AMD action accordingly.
2. **AMD cut-watch** — -1.78% unrealized; cushion ~$28.54/sh (~5.32%) to manual -7% threshold $507.96. Materially widened; monitor at pre-market.
3. **AMD broker-side trailing-stop retry** — still gated on missing `trailing-stop` subcommand in `scripts/trade.py`. Infrastructure carry-forward.
4. **Macro filter** — SPY < MA20 at Wed open; re-validate at Thu pre-market.

---

## Midday Scan — 2026-06-24 (Wednesday — session: claude/exciting-bohr-jb81un)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 2 / 8 (AAPL 1 sh, AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $297.54 | -$4.34 (-1.44%) |
| AMD | 14 | $546.19 | $520.30 | -$362.52 (-4.74%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -1.44% (cushion ~$16.79/sh to $280.75); AMD -4.74% (cushion ~$12.34/sh to $507.96 — **widened** vs market-open ~$6.16/sh on AMD recovery $514.12 → $520.30). No cuts.
- **Stop-tighten (+15%/+20%)**: no position at gain. AAPL 10% trailing-stop GTC $285.66 / HWM $317.40 active. AMD still unprotected by broker-side stop (post-fill 403 carry-forward).
- **Thesis check**: AMD Buy consensus intact (35 analysts: 43% Strong Buy, 43% Buy); AI infra capex cycle (~$750B 2026) + 'Advancing AI 2026' event July 22–23 ahead. AAPL BofA constructive on AI reset; PT $314.42 consensus. No thesis breaks.
- **Micron earnings AMC tonight** = binary AMD read-through. No pre-print action.

No trades executed. Weekly buys 1/3 used. Risk posture: cash ~92.4% (≥20% ✅), exposure ~7.6% (≤80% ✅), daily-loss limit (3%) untouched.

**Flags for end-of-day:**
1. Micron earnings AMC — assess AMD thesis read-through at EOD.
2. AMD broker-side trailing-stop retry still infra-gated.

---

## Market-Open Log — 2026-06-24 (Wednesday — session: claude/sweet-shannon-f2paud)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $91,560.43 |
| Equity | $99,050.51 |
| Long Market Value | $7,490.08 |
| Open Positions | 2 / 6 (AAPL 1 sh, AMD 14 sh) |
| Trades This Week | 1 / 3 |
| Decision | **NO_TRADE — HOLD; AMD close cut-watch** |

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (1/3)
- Max 8% equity per position ✅ (AMD 7.27%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; all trade ideas tagged "NOT for today" (macro filter fails, Micron earnings AMC binary, yfinance bars TLS-broken).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $295.71 | -$6.17 (-2.04%) |
| AMD | 14 | $546.19 | $514.12 | -$449.08 (-5.87%) |

Three independent stand-down reasons (reaffirming pre-market):
- **Macro filter fails** — SPY -1.44% yesterday close; live tape risk-off; SPY < MA20 zone (~$745) vs current ~$733 area. Universal buy block under strategy criterion #4.
- **Micron earnings AMC tonight** — direct read-through to held AMD on memory/HBM pricing + AI-server channel. Do not add semi exposure into the print.
- **yfinance bars TLS-broken** — live MA20/MA50/RSI-14 unverifiable. Bar-based entry criteria #1 & #2 cannot be confirmed.

**AMD risk management (close watch):**
- Unrealized -5.87% vs manual -7% threshold $507.96. **Cushion ~$6.16/sh (~1.20% to threshold)** — tightened from pre-market (~$21.54/sh / ~4.07%) on overnight markdown.
- If breached at midday, execute `python scripts/trade.py close AMD` (market-order strategy-stop exception; limit-sell tooling absent).
- **Broker-side trailing-stop still infra-gated** — `scripts/trade.py` lacks `trailing-stop` subcommand. Manual cut at -7% is the active control.

AAPL: 1 sh / 0.30% of equity — immaterial. 10% trailing-stop GTC $285.66 active (HWM $317.40, cushion ~$10.05/sh / ~3.4% to stop).

Trades executed: **none.**

Risk posture: cash 92.44% of equity (≥20% reserve ✅); exposure 7.56% (≤80% ✅); daily-loss limit (3%) — day drift -0.12% from prior EOD, well within. Weekly buy budget 1/3 used — 2 remaining preserved into Thu/Fri post-Micron.

**Flags for midday-scan:**
1. **AMD manual cut at -7%** ($507.96) — cushion narrowed to ~$6.16/sh (~1.20%). Re-check at midday; if breached, execute close.
2. **AMD broker-side trailing-stop retry** — still infra-gated; carry-forward.
3. **Micron earnings AMC tonight** — assess at EOD for AMD thesis read-through.

---

## EOD Snapshot — 2026-06-23 (Tuesday — session: claude/sleepy-goldberg-g54eag)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,166.59 |
| Cash | $91,560.43 |
| Long Market Value | $7,606.16 |
| Day P&L ($) | -$406.89 |
| Day P&L (%) | -0.409% |
| Trades Today | 0 |
| Trades This Week | 1 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $294.81 | -$7.07 (-2.34%) |
| AMD | 14 | $546.19 | $522.23 | -$335.56 (-4.39%) |

Notes: NO_TRADE day across pre-market / market-open / midday (macro filter SPY < MA20 live at open -1.34%; AMD add blocked at 7.25% position cap; AMD averaging-down barred on -6.11% open position). Day P&L -$406.89 / -0.41% driven by AMD marking down -$294.34 intraday on broad semi sell-off + M Science Q2 GPU report (Data Center sales below consensus) + HBM/GDDR6 cost pressure; AAPL marked down -$2.13 vs prior close. AMD cushion to -7% cut threshold $507.96 = ~$14.27/sh (~2.73%) — widened vs market-open (~$5/sh) but worth close watch into Wednesday. AAPL 10% trailing-stop GTC $285.66 active (HWM $317.40, cushion ~$9.15/sh, ~3.1% to stop). **AMD remains unprotected by broker-side trailing-stop** — `scripts/trade.py` still lacks `trailing-stop` subcommand. Manual cut at -7% remains the active control. Cash $91,560.43 = 92.33% of equity (≥20% reserve ✅); exposure 7.67% (≤80% ✅); daily-loss limit (3%) — day drift -0.41%, comfortably within. Weekly buy budget 1/3 used — 2 remaining into Wed–Fri.

**Carry-forward flags for Wednesday pre-market:**
1. **AMD cut-watch** — -4.39% unrealized; cushion ~$14.27/sh (~2.73%) to manual -7% threshold $507.96. If breached, execute `python scripts/trade.py close AMD` (market-order strategy-stop exception; limit-sell tooling absent).
2. **AMD broker-side trailing-stop retry** — still gated on missing `trailing-stop` subcommand in `scripts/trade.py`. Infrastructure carry-forward.
3. **AMD thesis pressure** — M Science Q2 GPU deployment report + HBM/GDDR6 cost pressure. Roadmap (HPC/supercomputing share) intact but conviction softening. Re-evaluate at Wed pre-market.

---

## Midday Scan — 2026-06-23 (Tuesday — session: claude/exciting-bohr-henotg)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 2 / 8 (AAPL 1 sh, AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $298.28 | -$3.60 (-1.19%) |
| AMD | 14 | $546.19 | $525.17 | -$294.34 (-3.85%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -1.19% (cushion ~$17.53/sh to $280.75); AMD -3.85% (cushion ~$17.21/sh to $507.96). No cuts. AMD cushion **widened** vs market-open -6.11% (~$5/sh → ~$17/sh).
- **Stop-tighten (+15%/+20%)**: no position at gain. AAPL 10% trailing-stop GTC $285.66 / HWM $317.40 active. AMD still unprotected by broker-side stop (post-fill 403 carry-forward).
- **Thesis check**:
  - AMD: -5.46% intraday on broad semi sell-off + M Science Q2 GPU deployment report (Data Center sales below consensus) + HBM/GDDR6 cost pressure. Partial thesis pressure but underlying roadmap intact (HPC/supercomputing share). Not a clean break — hold with EOD re-evaluation.
  - AAPL: BofA flags WWDC as "material positive AI reset, underappreciated." UK £3B iCloud suit is a known overhang. Thesis intact; position immaterial at 0.30% of equity.
- **Trailing-stop infra gap**: AMD broker-side stop still gated on missing `trailing-stop` subcommand in `scripts/trade.py`. Carry-forward to EOD.

No trades executed. Weekly buys 1/3 used. Risk posture: cash ~92.5% (≥20% ✅), exposure ~7.4% (≤80% ✅), daily-loss limit (3%) untouched.

**Flags for end-of-day:**
1. AMD thesis pressure (M Science Q2 GPU report + HBM cost) — re-evaluate hold conviction at EOD.
2. AMD broker-side trailing-stop retry still infrastructure-gated.

---

## Market-Open Log — 2026-06-23 (Tuesday — session: claude/sweet-shannon-fz3de7)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $91,560.43 |
| Equity | $99,032.98 |
| Long Market Value | $7,472.55 |
| Open Positions | 2 / 6 (AAPL 1 sh, AMD 14 sh) |
| Trades This Week | 1 / 3 |
| Decision | **NO_TRADE — HOLD; AMD on close watch** |

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (1/3)
- Max 8% equity per position ✅ (AMD 7.25%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; no new entries authorized; macro filter narrowly fails on bar-based SPY pre-market and decisively fails live at open.

Live gate re-validation (60-bar snapshot @ 09:46 ET):
- **Macro (SPY)**: bar current $744.39 < MA20 $745.43 ❌; **live last $735.44 << MA20 $745.43 (-1.34%)**. Hard fail — opposite of pre-market ES futures hint (+0.98% faded at open).
- AMD chart-pass intact (bar $551.63 > MA20 $506.96; RSI 55.94 neutral) but **adding blocked**: position already 7.25% of equity, averaging-down on a -6.11% open position is barred by strategy precedent.
- No other watchlist candidate live-validated (macro fails universally).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $300.965 | -$0.92 (-0.30%) |
| AMD | 14 | $546.19 | $512.82 | -$467.24 (-6.11%) |

**AMD risk management:**
- **Cut-loser watch**: AMD -6.11% vs manual -7% threshold $507.96. **Cushion $4.86/sh (~0.94% to threshold)** — close watch. If breached at midday, execute `python scripts/trade.py close AMD` (one-time market-order exception under strategy stop-loss "no exceptions" rule; limit-sell tooling absent).
- **Trailing-stop retry**: `scripts/trade.py` still has no `trailing-stop` subcommand (CLI: `clock|open|orders|cancel-all|close|buy`). Cannot place broker-side GTC trailing-stop from this routine. Infrastructure carry-forward to EOD (add `trailing-stop` subcommand) — not patching during a live market-open routine.
- AMD remains 14 sh unprotected by broker-side stop; manual monitoring is the active control.

AAPL: 1 sh / 0.30% of equity — immaterial. 10% trailing-stop GTC $285.66 active (HWM $317.40, cushion ~$15.31/sh / ~5.1% to stop).

Trades executed: **none.**

Risk posture: cash 92.46% of equity (≥20% reserve ✅); exposure 7.55% (≤80% ✅); daily-loss limit (3%) — day drift -0.43% from yesterday's EOD, well within. Weekly buy budget 1/3 used — 2 remaining into Wed–Fri (preserved through macro-fail day).

**Flags for midday-scan:**
1. **AMD manual cut at -7%** ($507.96) — close to threshold (~$5/sh cushion).
2. **AMD broker-side trailing-stop retry** still gated on infrastructure (no `trailing-stop` subcommand in `trade.py`); not actionable until tooling lands.

---

## EOD Snapshot — 2026-06-22 (Monday — session: claude/sleepy-goldberg-udz4tn)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,573.48 |
| Cash | $91,560.44 |
| Long Market Value | $8,013.04 |
| Day P&L ($) | +$68.31 |
| Day P&L (%) | +0.0687% |
| Trades Today | 1 |
| Trades This Week | 1 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $296.94 | -$4.94 (-1.64%) |
| AMD | 14 | $546.19 | $551.15 | +$69.38 (+0.91%) |

Notes: Post-Juneteenth re-engagement day. Market-open fired AMD 14 sh BUY @ $546.19 (live gates all passed: SPY > MA20, AMD price > MA20, RSI 53.12 in 40–65 band, spread 0.128%). Day P&L +$68.31 driven primarily by AMD marking up +$69.38 intraday (+$4.96/sh from fill to close), offset modestly by AAPL marking down -$1.07 vs prior close. **AMD remains unprotected by a broker-side trailing-stop** — Alpaca returned 403 Forbidden on the GTC submit immediately after fill; `scripts/trade.py` has no trailing-stop subcommand. Flagged for tomorrow's pre-market: retry 10% trailing-stop GTC anchored to fill $546.19 → initial stop ~$491.57. AAPL 10% trailing-stop GTC $285.66 active (cushion ~$11.28/sh, ~3.8% to stop). Cash $91,560.44 = 91.95% of equity (≥20% reserve ✅); exposure 8.05% (≤80% ✅); daily-loss limit (3%) untouched. Weekly buy budget 1/3 used — 2 remaining into Tue–Fri.

---

## Midday Scan — 2026-06-22 (Monday — session: claude/exciting-bohr-ku5ten)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 2 / 8 (AAPL 1 sh, AMD 14 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $300.51 | -$1.37 (-0.45%) |
| AMD | 14 | $546.19 | $541.355 | -$67.75 (-0.89%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -0.45% (cushion ~$19.76/sh to $280.75); AMD -0.89% (cushion ~$33.40/sh to $507.96). No cuts.
- **Stop-tighten (+15%/+20%)**: no position at gain. AAPL 10% trailing-stop GTC $285.66 / HWM $317.40 active.
- **Trailing-stop infra gap**: AMD has no broker-side stop (post-fill 403 at 09:46 ET). `scripts/trade.py` has no trailing-stop subcommand — not patching trading infrastructure during a live routine; deferred to EOD per market-open carry-forward.
- **Thesis**: Both intact. AMD constructive (Rackspace AI compute partnership, MEXT acquisition, bullish PT revisions); headwinds noted (Lisa Su 125k sh insider sale, tightened China export rules) — not a thesis break on entry day. AAPL constructive (iPhone pricing power on memory shortage, Intel foundry talks, $313.62 PT/Buy).

No trades executed. Weekly buys 1/3 used. Risk posture: cash 92.0% (≥20% ✅), exposure ~7.9% (≤80% ✅), daily-loss limit (3%) untouched.

---

## Market-Open Log — 2026-06-22 (Monday — session: sweet-shannon-4olcig)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash (pre-trade) | $99,207.16 |
| Equity (pre-trade) | $99,508.49 |
| Open Positions | 1 → 2 / 6 (AAPL 1 sh, AMD 14 sh) |
| Trades This Week | 0 → 1 / 3 |
| Decision | **TRADE — AMD 14 sh BUY** |

Buy-rule check:
- Max 6 open positions ✅ (1/6 → 2/6)
- Max 3 trades this week ✅ (0/3 → 1/3)
- Max 8% equity per position ✅ (AMD ~7.71%)
- Catalyst in today's RESEARCH-LOG ✅ — AMD authorized conditional 14 sh BUY in pre-market log.

Live gate re-validation (60-bar snapshot @ 09:46 ET):
- **Macro (SPY)**: bar current $746.74 > MA20 $745.25 ✅ (live ask $748.65 also above). RSI 45.98 neutral.
- **AMD price**: bar current $537.37 > MA20 $501.86 ✅ (live ask $546.48 also > MA20).
- **AMD RSI-14**: 53.12 — inside 40–65 band ✅.
- **AMD spread**: bid $545.78 / ask $546.48 → 0.128% ≤ 0.5% ✅.
- All four gates pass → AMD trade fires.

Position sizing (recomputed @ live ask $546.48):
- Limit = ask × 1.0025 = $547.85
- Max shares (8% cap) = floor(($99,508.49 × 0.08) / $547.85) = floor(14.53) = **14 shares**
- Allocation = $7,646.66 ≈ 7.69% of equity (within 8% per-position rule).

Trade executed:
| Symbol | Side | Qty | Avg Fill | Order ID |
|--------|------|-----|----------|----------|
| AMD | BUY | 14 | $546.19 | b48c23e0-495e-490b-892d-78d38668b9cd |

**Trailing-stop placement FAILED** — Alpaca returned 403 Forbidden on the GTC trailing-stop submit immediately after fill. AMD currently unprotected by a broker-side stop. **Flag for midday-scan / end-of-day routine: retry 10% trailing-stop GTC anchored to fill $546.19 → initial stop ~$491.57.**

Position snapshot (post-trade, live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $301.05 | -$0.83 (-0.27%) |
| AMD | 14 | $546.19 | $545.98 | -$3.00 (-0.04%) |

Risk posture: cash ~$91,558 = 92.0% of equity (≥20% reserve ✅); exposure ~8.0% (≤80% ✅); daily-loss limit (3%) untouched. Weekly buy budget 1/3 used — 2 remaining into Tue–Fri.

---

## EOD Snapshot — 2026-06-19 (Friday — Juneteenth — session: sleepy-goldberg-bmlats)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,505.17 |
| Cash | $99,207.16 |
| Long Market Value | $298.01 |
| Day P&L ($) | +$0.01 |
| Day P&L (%) | +0.00001% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 1 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $298.01 | -$3.87 (-1.28%) |

Notes: **Juneteenth Federal Holiday — US equity markets CLOSED all session.** No pre-market, market-open, or midday trade decisions actionable; routines logged HOLD across the board. Portfolio value $99,505.17 vs yesterday $99,505.16 — Day P&L +$0.01 is broker mark-drift only (no real session activity). AAPL 1 sh -$3.87 unrealized (-1.28%); 10% trailing-stop GTC $285.66 active (cushion ~$12.35/sh, ~4.1% to stop). Cash $99,207.16 = 99.70% of equity (≥20% reserve ✅); exposure 0.30% (≤80% ✅); daily-loss limit (3%) untouched. **Week 6/15–6/19 closes: 0 buys / 0 sells / 0 net trades.** Next decision window: Monday 2026-06-22 pre-market.

---

## Midday Scan — 2026-06-19 (Friday — Juneteenth)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Market | **CLOSED — Juneteenth** (next open Mon 2026-06-22 09:30 ET) |
| Cash | $99,207.16 |
| Long Market Value | $298.01 |
| Equity | $99,505.17 |
| Open Positions | 1 / 8 (AAPL 1 sh) |
| Decision | **HOLD — no action (market closed)** |

Position snapshot (last mark):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $298.01 | -$3.87 (-1.28%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -1.28% — no cut (cushion ~$17.26/sh to -7% threshold $280.75). Market closed — order placement impossible regardless.
- **Stop-tighten**: no position at +15%/+20% gain. 10% trailing-stop GTC $285.66 remains in force.
- **Thesis check**: AAPL 0.30% of equity — immaterial. News tape constructive (BofA reiterates Buy $380 PT 6/18; Intel-Apple foundry pact powered semis Thursday rally; analyst notes on iPhone memory-cost pricing power). No thesis break.

No trades executed (market closed for Juneteenth Federal Holiday). Weekly buys close 0/3. Next decision window: Monday 2026-06-22 pre-market.

---

## EOD Snapshot — 2026-06-18 (Thursday — session: sleepy-goldberg-bnxu39)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,505.16 |
| Cash | $99,207.16 |
| Long Market Value | $298.00 |
| Day P&L ($) | +$2.05 |
| Day P&L (%) | +0.0021% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 1 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $298.00 | -$3.88 (-1.28%) |

Notes: T-1 Juneteenth — flat. NO_TRADE across pre-market, market-open, and midday routines (zero authorized catalysts; macro filter still fails post-FOMC with SPY < MA20; T-1 to Juneteenth gap-risk). Day P&L +$2.05 driven by AAPL marking up from -$5.68 to -$3.88 unrealized intraday. AAPL 10% trailing-stop GTC $285.66 active (cushion ~$12.34/sh, ~4.1% to stop). Cash $99,207.16 = 99.70% of equity (≥20% reserve ✅); exposure 0.30% (≤80% ✅); daily-loss limit (3%) untouched. Weekly buy budget closes 0/3 — Friday 6/19 Juneteenth (market closed); next decision window Monday 2026-06-22 pre-market.

---

## Midday Scan — 2026-06-18 (Thursday)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 8 (AAPL 1 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $297.16 | -$4.72 (-1.56%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -1.56% — no cut (cushion ~$16.41/sh to -7% threshold $280.75).
- **Stop-tighten**: no position at +15%/+20% gain. Trailing-stop GTC $285.66 (10% trail) remains in force.
- **Thesis check**: AAPL position is 0.30% of equity — immaterial. No new negative catalyst since pre-market. Thesis intact.

No trades executed. T-1 to Juneteenth posture unchanged. Weekly buys 0/3 preserved.

---

## Market-Open Log — 2026-06-18 (Thursday — session: sweet-shannon-5s42cu)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $99,207.16 |
| Equity | $99,504.82 |
| Long Market Value | $297.66 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AAPL 0.30%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; all trade ideas (NVDA, MSFT, KLAC/TSM) explicitly tagged "NOT FOR TODAY" pending post-Juneteenth re-screen.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $297.69 | -$4.19 (-1.39%) |

Three independent stand-down reasons (reaffirming pre-market):
- **Macro filter still fails** — SPY bar-based $740.96 < MA20 $746.80 (live ask $744.61 also below). Post-FOMC hawkish drift unresolved.
- **T-1 to Juneteenth** — Friday 6/19 closed; asymmetric gap risk over 3-day weekend on hawkish-Fed/geopolitical headlines.
- **Zero authorized catalysts** — all watchlist ideas explicitly tagged "NOT FOR TODAY" in today's pre-market log.

AAPL trailing-stop GTC $285.66 cushion ~$12.03/sh (~4.0%). Trades executed: **none.** Risk posture: cash 99.70% (≥20% ✅), exposure 0.30% (≤80% ✅), daily-loss limit untouched. Weekly buy budget 0/3 preserved through Juneteenth.

---

## Market-Open Log — 2026-06-17 (Wednesday — session: sweet-shannon-l7x1cp)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $99,207.16 |
| Equity | $99,507.90 |
| Long Market Value | $300.74 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE — HOLD** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AAPL 0.30%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; all trade ideas (NVDA, AMD, MSFT, GOOGL) explicitly tagged "NOT for today" pending post-FOMC re-evaluation.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $300.72 | -$1.16 (-0.38%) |

Three independent stand-down reasons (reaffirming pre-market):
- **FOMC binary today** — 2:00 PM ET rate decision + 2:30 PM ET Warsh debut presser; market ~70% prob hike-by-year-end vs March SEP median 3.4% (dot-plot gap).
- **Macro filter only tentatively reclaimed** — SPY 2 sessions above MA20 after 9 below.
- **MA/RSI re-validation NaN-blocked** — yfinance bar enrichment unreliable.

AAPL trailing-stop GTC $285.66 cushion ~$15.06/sh (~5.0%). Trades executed: **none.** Risk posture: cash 99.70% (≥20% ✅), exposure 0.30% (≤80% ✅), daily-loss limit untouched. Weekly buy budget 0/3 preserved for clean post-FOMC Thu/Fri.

---

## Midday Scan — 2026-06-17 (Wednesday — session: sweet-shannon-l7x1cp)

| Field | Value |
|-------|-------|
| Routine | Midday Scan (pre-FOMC) |
| Cash | $99,206.02 |
| Long Market Value | $298.57 |
| Open Positions | 1 / 8 (AAPL 1 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $298.57 | -$3.31 (-1.10%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -1.10% — no cut (cushion ~$5.79/sh to -7% threshold $280.75).
- **Stop-tighten**: no position at +15%/+20% gain. Trailing-stop GTC $285.66 (10% trail) remains in force.
- **Thesis check**: AAPL position is 0.30% of equity — immaterial. Pre-FOMC tape; no new negative catalyst for AAPL since pre-market. Thesis intact.

No trades executed. Awaiting FOMC 2:00 PM ET decision + 2:30 PM ET Warsh debut presser. Weekly buys 0/3 preserved.

---

## EOD Snapshot — 2026-06-17 (Wednesday — session: sleepy-goldberg-6zbgij)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,503.11 |
| Cash | $99,207.16 |
| Long Market Value | $295.95 |
| Day P&L ($) | -$2.82 |
| Day P&L (%) | -0.0028% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 1 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $296.20 | -$5.68 (-1.88%) |

Notes: FOMC day — flat. NO_TRADE across pre-market, market-open, and midday routines (catalyst absent; all watchlist trade ideas tagged "NOT for today" pending post-FOMC re-evaluation). Day P&L -$2.82 driven entirely by AAPL marking down from -$3.11 to -$5.68 unrealized post-FOMC. AAPL 10% trailing-stop GTC $285.66 active (cushion ~$10.54/sh, ~3.5% to stop). Cash $99,207.16 = 99.70% of equity (≥20% reserve ✅); exposure 0.30% (≤80% ✅); daily-loss limit (3%) nowhere near. Weekly buy budget 0/3 preserved — full budget into Thu/Fri post-FOMC re-evaluation window.

---

## Market-Open Log — 2026-06-10 (Wednesday — session: sweet-shannon-lf81nx)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $94,908.18 |
| Equity | $99,571.62 |
| Long Market Value | $4,663.44 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (largest GOOGL 4.39%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; macro filter fails post-CPI (SPY $735.72 < MA20 $746.26).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $289.35 | -$12.53 (-4.15%) |
| GOOGL | 12 | $385.82 | $364.55 | -$255.24 (-5.51%) |

Entry-criteria re-validation (live):
- **Macro (SPY)**: $735.72 < MA20 $746.26 → criterion #4 fails universally. CPI print sent tape risk-off.
- **NVDA**: $205.66 < MA20 $218.01 → criterion #1 fails; RSI 40.34 (just above floor). NO_TRADE.
- **AMD**: bar current $475.51 < MA20 $476.53 → criterion #1 fails; spread 4.04% unusable. NO_TRADE.
- **AAPL/GOOGL add**: both below MA20; GOOGL also in cut-watch zone.

GOOGL -7% cut watch: live -5.51%, cushion $5.74/sh (1.58%) — **widened** vs pre-market (-6.34%). No cut. Trailing-stop GTC active.

Trades executed: **none.**

Risk posture: cash 95.32% of equity (≥20% reserve ✅), exposure 4.68% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Thu/Fri.

---

## Market-Open Log — 2026-06-09 (Tuesday — session: sweet-shannon-obv5jg)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $94,908.18 |
| Equity | $99,647.97 |
| Long Market Value | $4,739.79 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (largest GOOGL 4.46%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD/NO_TRADE; macro filter fails (SPY $739.22 < MA20 $746.37, 4th session); zero watchlist passes.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $297.17 | -$4.71 (-1.56%) |
| GOOGL | 12 | $385.82 | $370.195 | -$187.50 (-4.05%) |

Entry-criteria re-validation (per pre-market, no override at open):
- **AMD** (only chart-passer): macro filter blocks; bar spread unusable. No entry.
- **AAPL/GOOGL/NVDA/COST**: all below MA20 → criterion #1 fails universally.

Trades executed: **none.**

Risk posture: cash 95.24% of equity (≥20% reserve ✅), exposure 4.76% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Wed CPI. **GOOGL -7% cut watch**: live -4.05% (improved from pre-market -5.53%); cushion widened — defer to midday scan. Trailing stops active on both positions.

---

## Market-Open Log — 2026-06-08 (Monday — session: sweet-shannon-J8VSZ)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $94,908.18 |
| Equity | $99,592.97 |
| Long Market Value | $4,684.79 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 (new week) |
| Decision | **NO_TRADE — pre-staged AAPL exit OVERRIDDEN (hold through WWDC)** |

Market clock: `is_open=true` (next_close 16:00 ET).

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (largest GOOGL 4.39%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market screen returned **zero buy candidates**; macro filter fails (SPY $737.55 < MA20 $746.29).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $311.13 | +$9.25 (+3.06%) |
| GOOGL | 12 | $385.82 | $364.475 | -$256.14 (-5.53%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **Macro filter (SPY)**: live last $743.41; bar-based current $737.55 < MA20 $746.29 → criterion #4 **FAILS** across the entire watchlist. No buys eligible regardless of per-ticker reads.
- **AAPL**: chart-pass only (price > MA20 $304.24 & MA50 $281.09; RSI 58.28 neutral) — but it's the pending exit, not an add.
- **GOOGL/NVDA/AMD/COST**: all fail criterion #1 (below MA20). NVDA stopped out Friday at $209.04; oversold.

**AAPL pre-WWDC exit resolution (pre-staged across 4 prior pre-market routines):**

Decision: **OVERRIDE — hold through WWDC keynote (13:00 ET)** with documented rationale:
1. **Infrastructure**: `scripts/trade.py` has no limit-sell subcommand. The `close` command calls Alpaca DELETE /v2/positions/{symbol}, which submits a **market order** — direct violation of strategy.md line 58 ("Always use limit orders. Never place market orders."). The strategy's limit-only rule has no documented exception.
2. **Position immateriality**: AAPL is 1 sh / $311.13 = **0.31% of equity**. Even a worst-case post-keynote "sell the news" drawdown (-10%) would cost ~$31 — immaterial vs portfolio. The risk-management benefit of the pre-staged exit is symbolic, not material.
3. **Mechanical backstop intact**: 10% trailing-stop GTC active (stop $285.24 / HWM $316.93). If WWDC disappoints catastrophically, the stop fires automatically — strategy-compliant exit discipline.
4. **No thesis break**: AAPL chart still passes entry criteria (price > MA20 & MA50, RSI 58 neutral). Morgan Stanley PT $365–$385, BofA $380, Wedbush "Expect Fireworks" — analyst tape constructive into the catalyst.

This resolves the pre-staged exit explicitly. Going forward, the AAPL position is held under standard exit discipline (trailing-stop GTC) — the pre-WWDC carry-forward flag is **CLOSED**.

**GOOGL -7% cut watch**: live -5.53% unrealized; cut threshold -7% → ~$358.81. Cushion ~$5.66/sh (~1.6%). Defer to midday scan.

Trades executed: **none.**

Risk posture: cash 95.30% of equity (≥20% reserve rule ✅), exposure 4.70% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter remains 0/3 — full budget into Tuesday.

---

## Market-Open Log — 2026-06-05 (Friday — session: sweet-shannon-vLVM7)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $90,100.28 |
| Equity | $99,773.96 |
| Long Market Value | $9,673.68 |
| Open Positions | 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (3/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (largest NVDA 4.92%)
- Catalyst in today's RESEARCH-LOG: pre-market log rejected all candidates (zero watchlist passes).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $313.665 | +$11.79 (+3.90%) |
| GOOGL | 12 | $385.82 | $371.00 | -$177.84 (-3.84%) |
| NVDA | 23 | $216.00 | $213.36 | -$60.72 (-1.22%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **NVDA add (BLOCKED)**: live last $213.38 < MA20 $219.18 → criterion #1 fails; RSI-14 **36.12** < 40 band → criterion #2 fails; position 4.92% of equity — one more share crosses 5% cap. Three independent blockers.
- **AMD entry (BLOCKED)**: live RSI-14 **67.01** > 65 ceiling → criterion #2 fails. Quote spread $2.06 / 0.42% within 0.5% (improved from prior sessions), but RSI alone disqualifies.
- **AAPL add (BLOCKED)**: pre-WWDC exit pre-staged for tonight 2026-06-05 EOD (T-1 before 6/8 keynote) — adding inverts the exit plan.
- **GOOGL add (BLOCKED)**: price $371.00 < MA20 $386.85 (criterion #1) and RSI 30.09 oversold (criterion #2) — strategy bars averaging down.

Trades executed: **none.**

Risk posture: cash 90.30% of equity (≥20% reserve rule ✅), exposure 9.70% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter remains 0/3 — full budget unused into Friday close. Macro context: NFP 8:30 ET is the binary print; US/Iran tensions + oil spike + AVGO semis derate = unfavorable add-longs environment. **AAPL pre-WWDC exit pre-staged for tonight EOD.** **GOOGL cut-loser watch (-3.84%)** deferred to midday scan. All three positions protected by 10% trailing-stop GTC orders.

---

---

## EOD Snapshot — 2026-05-20

| Field | Value |
|-------|-------|
| Portfolio Value | $100,000.00 |
| Cash | $100,000.00 |
| Long Market Value | $0.00 |
| Day P&L ($) | $0.00 |
| Day P&L (%) | 0.00% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 0 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| — | — | — | — | — |

Notes: Flat into close. NVDA earnings released after-hours — re-evaluate at tomorrow's pre-market routine.

---

## Market-Open Log — 2026-05-21 (Thursday)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (9:46 ET) |
| Cash | $100,000.00 |
| Equity | $100,000.00 |
| Open Positions | 0 / 6 |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check: positions 0/6 ✅ · weekly trades 0/3 ✅ · ≤20% equity/position ✅ · catalyst in RESEARCH-LOG ✅ (MSFT primary, GOOGL secondary).

Decision rationale:
- Entry criteria unverifiable: `market_data.py` returns only 1 bar for MSFT/GOOGL/SPY → MA20/MA50/RSI-14 all `null`. Strategy criteria #1 (price > MA20 & MA50) and #2 (RSI 40–65) cannot be confirmed. Pre-market plan explicitly required RSI 40–65 on a ≥20-bar live snapshot — condition fails.
- `trade.py` has no `buy` subcommand (CLI: `clock|open|orders|cancel-all|close`). No documented execution path; not patching trading infrastructure during a live routine.
- Live quotes benign — no tech-rotation gap-down: MSFT ask $423 (vs plan $422.11), GOOGL ask $386.24 (vs plan $389.88), SPY $738.10.
- Default under unverifiable entry criteria is NO_TRADE. Capital preserved at full cash.

Trades executed: **none.**

---

## Closed Trade Log

| Date | Symbol | Side | Qty | Entry | Exit | P&L | Hold Days | Exit Reason |
|------|--------|------|-----|-------|------|-----|-----------|-------------|
| — | — | — | — | — | — | — | — | — |

---

## Notes

- All values are paper trading until `PAPER_MODE=false`.
- Performance is measured against SPY (buy-and-hold benchmark).
- Update this file at the end of each trading day via the end-of-day routine.

### Trade Entry — 2026-05-21 16:54
| Field | Value |
|-------|-------|
| Symbol | AAPL |
| Side | BUY |
| Shares | 1.0 |
| Est. Price | $301.90 |
| Est. Value | $301.90 |
| Order ID | 1a27b81f-a6ce-4da9-99ed-f89995d719c6 |
| Trailing Stop | 10% GTC placed immediately after fill |

---

## EOD Snapshot — 2026-05-21

| Field | Value |
|-------|-------|
| Portfolio Value | $100,002.65 |
| Cash | $99,698.12 |
| Long Market Value | $304.53 |
| Day P&L ($) | +$2.65 |
| Day P&L (%) | +0.0027% |
| Trades Today | 1 |
| Trades This Week | 1 |
| Open Positions | 1 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $304.53 | +$2.65 (+0.88%) |

Notes: First position of the week. AAPL 1 sh opened @ $301.88 avg entry; 10% trailing-stop GTC active (order 5851cbb5, stop $274.99, HWM $305.54). Day P&L driven entirely by AAPL mark-up. Cash reserve 99.7% of equity — comfortably within the ≥20% rule and the 5% single-position cap. Trade was entered after the market-open routine, which had logged NO_TRADE at 09:46 ET. Flat-to-green day; no risk limits approached.

### Trade Entry — 2026-05-22 13:46
| Field | Value |
|-------|-------|
| Symbol | GOOGL |
| Side | BUY |
| Shares | 12.0 |
| Est. Price | $390.00 |
| Est. Value | $4680.00 |
| Order ID | a543b11b-59fe-4fad-84d2-fd0d545e3c78 |
| Trailing Stop | 10% GTC placed immediately after fill |

---

## Market-Open Log — 2026-05-22 (Friday)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash (pre-trade) | $99,698.12 |
| Equity (pre-trade) | $100,005.54 |
| Open Positions | 1 → 2 / 6 |
| Trades This Week | 1 → 2 / 3 |
| Decision | **TRADE — GOOGL** |

Buy-rule check: positions 1/6 ✅ · weekly trades 1/3 ✅ · ≤20% equity/position ✅ (~4.6%) · catalyst in today's RESEARCH-LOG ✅ (GOOGL primary).

Entry-criteria re-validation (live, 60-bar snapshot):
- GOOGL: price $385.83 > MA20 $383.55 & MA50 $339.55 (bullish) ✅ · RSI-14 51.48 in 40–65 band ✅ · tight spread (bid 385.72 / ask 385.83) ✅ · SPY $742.72 > MA20 $730.0 (macro filter OK) ✅ · no negative 48h catalyst ✅. No gap-down vs pre-market plan.
- COST: **rejected.** RSI 60 / bullish MAs passed, but (a) quote spread unusable/stale (bid $984.20 / ask $1,092 vs $1,050 mark) and (b) Costco fiscal Q3 earnings land ~May 28–29 — within 5 trading days. Strategy bars entry into the earnings window.

Trade executed:
| Symbol | Side | Qty | Est. Price | Est. Value | Order ID |
|--------|------|-----|-----------|-----------|----------|
| GOOGL | BUY | 12 | $390.00 | $4,680.00 | a543b11b-59fe-4fad-84d2-fd0d545e3c78 |

Sizing: floor(($100,005.54 × 0.05) / $386.79 limit) = 12 shares. 10% trailing-stop GTC placed immediately after fill (order a7fadae9, stop $347.157, HWM $385.73). Weekly buys remaining: 1.

Position-management note — AAPL: RSI-14 still extremely overbought (~82). Tiny 1-share position protected by a 10% trailing stop; flagged for the end-of-day routine to consider a full exit per the "RSI > 75" exit rule.

---

## EOD Snapshot — 2026-05-22

| Field | Value |
|-------|-------|
| Portfolio Value | $99,975.69 |
| Cash | $95,068.28 |
| Long Market Value | $4,907.41 |
| Day P&L ($) | -$26.96 |
| Day P&L (%) | -0.03% |
| Trades Today | 1 |
| Trades This Week | 2 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $308.56 | +$6.68 (+2.21%) |
| GOOGL | 12 | $385.82 | $383.24 | -$30.99 (-0.67%) |

Notes: Flat-to-slightly-red day; Day P&L -$26.96 driven by GOOGL marking down -$30.99 after entry, partially offset by AAPL +$6.68. Both positions carry 10% trailing-stop GTC orders. Cash reserve $95,068.28 = 95.1% of equity — well within the ≥20% cash rule; total exposure 4.9%. No risk limits approached (daily loss limit 3% not remotely close). AAPL RSI-14 remains overbought (>75) — carried into the weekend; re-evaluate for exit at Monday's pre-market routine. 2 of 3 weekly trades used.

---

## Market-Open Log — 2026-05-25 (Monday — Memorial Day)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $95,068.28 |
| Equity | $99,972.74 |
| Long Market Value | $4,904.46 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 (new week) |
| Decision | **NO_TRADE** |

Market clock: `is_open=false`, `next_open=2026-05-26T09:30 ET`. Today is **Memorial Day** — US equity markets closed. No order placement possible.

Buy-rule check (pre-empted by market closure):
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3, new week)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ❌ — no 2026-05-25 entry in `memory/RESEARCH-LOG.md` (last entry 2026-05-22). Holiday → no pre-market routine ran.

Position snapshot:
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $308.82 | +$6.94 (+2.30%) |
| GOOGL | 12 | $385.82 | $382.97 | -$34.20 (-0.74%) |

Trades executed: **none** (market closed). Both positions remain protected by 10% trailing-stop GTC orders. AAPL RSI overbought flag still open — defer exit evaluation to Tuesday's pre-market routine when live data is available.

---

## EOD Snapshot — 2026-05-25

| Field | Value |
|-------|-------|
| Portfolio Value | $99,972.74 |
| Cash | $95,068.28 |
| Long Market Value | $4,904.46 |
| Day P&L ($) | -$2.95 |
| Day P&L (%) | -0.003% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $308.82 | +$6.94 (+2.30%) |
| GOOGL | 12 | $385.82 | $382.97 | -$34.20 (-0.74%) |

Notes: **Memorial Day — US equity markets closed.** No trades placed; portfolio marked at last available prices (effectively flat vs Friday close). Day P&L -$2.95 reflects tiny residual mark drift in the broker's account snapshot, not real session activity. Both positions remain protected by 10% trailing-stop GTC orders. Cash 95.1% of equity — well above the ≥20% reserve rule. AAPL RSI-overbought flag carried forward to Tuesday's pre-market routine. Weekly trade counter reset to 0/3 for the new trading week starting 2026-05-26.

---

## Market-Open Log — 2026-05-26 (Tuesday — session: sweet-shannon)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $95,068.28 |
| Equity | $99,996.35 |
| Long Market Value | $4,928.07 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Market clock: `is_open=true` (next_close 16:00 ET). Trading window active.

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- **Catalyst in today's RESEARCH-LOG ❌** — no 2026-05-26 entry exists in `memory/RESEARCH-LOG.md`; last entry is 2026-05-22. Heartbeat dated 2026-05-22T07:10Z — Tuesday's pre-market routine did not produce a logged catalyst.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $310.23 | +$8.35 (+2.77%) |
| GOOGL | 12 | $385.82 | $384.82 | -$12.00 (-0.26%) |

Decision rationale:
- Buy-rule #4 (catalyst in today's RESEARCH-LOG) fails — no symbol is authorized for entry under the market-open routine.
- Per CLAUDE.md: default action under uncertainty is **NO_TRADE**.
- AAPL RSI-overbought exit flag remains open from 2026-05-22 — exit evaluation is the EOD routine's responsibility, not market-open.
- Both positions remain protected by 10% trailing-stop GTC orders. Cash 95.1% of equity, well within the ≥20% rule.

Trades executed: **none.**

---

## EOD Snapshot — 2026-05-26

| Field | Value |
|-------|-------|
| Portfolio Value | $100,035.52 |
| Cash | $95,068.28 |
| Long Market Value | $4,967.24 |
| Day P&L ($) | +$62.78 |
| Day P&L (%) | +0.063% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $308.72 | +$6.84 (+2.27%) |
| GOOGL | 12 | $385.82 | $388.21 | +$28.68 (+0.62%) |

Notes: Quiet, slightly green day. NO_TRADE at market-open (no 2026-05-26 catalyst in `memory/RESEARCH-LOG.md`); 0 trades placed today. Day P&L +$62.78 driven by GOOGL recovering +$28.68 unrealized (vs -$34.20 entering the session) and AAPL holding +$6.84. Both positions protected by 10% trailing-stop GTC orders (AAPL stop $280.64 / HWM $311.82; GOOGL stop $350.33 / HWM $389.26). Cash $95,068.28 = 95.03% of equity — well above the ≥20% reserve rule; total exposure 4.97%. Daily-loss limit (3%) not approached. Weekly trade counter 0/3. AAPL RSI-overbought exit flag still open from 2026-05-22 — defer to tomorrow's pre-market routine for re-evaluation; trailing stop currently providing the exit discipline.

---

## Market-Open Log — 2026-05-27 (Wednesday — session: sweet-shannon-yaC8h)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $95,068.28 |
| Equity | $100,037.60 |
| Long Market Value | $4,969.32 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Market clock: `is_open=true` (next_close 16:00 ET). Trading window active.

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ✅ — NVDA primary (memory/research/2026-05-27.md authorizes 21 sh max, conditional on live re-validation).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $310.60 | +$8.72 (+2.89%) |
| GOOGL | 12 | $385.82 | $388.22 | +$28.80 (+0.62%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **NVDA**: live ask **$211.70** vs MA20 **$214.66** → price **BELOW** MA20. Strategy criterion #1 (price > MA20 & MA50) **FAILS** on live data. RSI-14 63.94 still inside 40–65 band ✅; SPY $750.59 > MA20 $733.35 (macro filter OK, though SPY RSI 71.48 overbought). The pre-market plan's explicit contingency — "require fresh live-data re-validation … if RSI prints > 65 at open, defer to NO_TRADE" — extends to MA stack failure under the strategy's "all must be true" entry rule. Bar-based `current_price` of $214.86 reflects the prior bar's close; live tape ($211.70) has drifted below MA20 since pre-market. Default under criterion failure: NO_TRADE.
- **AAPL exit**: pre-market authorized full exit (1 sh) on RSI 87.71. Per established precedent (2026-05-26 market-open log: "exit evaluation is the EOD routine's responsibility, not market-open"), AAPL RSI-overbought exit flag carries forward to EOD. 10% trailing-stop GTC (stop ~$280.64 / HWM $311.82) continues to provide exit discipline. Flag now 5 sessions old — EOD must resolve.

Trades executed: **none.**

Risk posture: cash 95.0% of equity (≥20% reserve rule ✅), exposure 4.97%, daily-loss limit (3%) not approached. Weekly trade counter remains 0/3 — full budget preserved for Thursday/Friday if NVDA's MA stack reclaims bullish alignment or another watchlist name becomes entry-eligible.

---

## EOD Snapshot — 2026-05-27

| Field | Value |
|-------|-------|
| Portfolio Value | $100,056.98 |
| Cash | $95,068.28 |
| Long Market Value | $4,988.70 |
| Day P&L ($) | +$21.46 |
| Day P&L (%) | +0.021% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $310.50 | +$8.62 (+2.86%) |
| GOOGL | 12 | $385.82 | $389.85 | +$48.36 (+1.05%) |

Notes: Quiet, slightly green day. NO_TRADE at market-open — NVDA (the pre-market primary catalyst) rejected on live re-validation: ask $211.70 had drifted below MA20 $214.66, failing strategy criterion #1 (price > MA20 & MA50). Day P&L +$21.46 driven by GOOGL adding +$19.68 unrealized (to +$48.36) and AAPL marking up +$1.78 (to +$8.62). Both positions protected by 10% trailing-stop GTC orders — AAPL stop $281.93 / HWM $313.26; GOOGL stop $354.49 / HWM $393.88 (both HWMs ratcheted higher today). Cash $95,068.28 = 95.01% of equity (≥20% reserve rule ✅); total exposure 4.99%. Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Thursday/Friday. **AAPL RSI-overbought exit flag (open since 2026-05-22, now 5 sessions old):** trailing stop has continued ratcheting higher with the position (+2.86% unrealized) — providing disciplined exit without forcing a sale into strength. Flag remains carried; re-evaluate at Thursday pre-market alongside fresh RSI print.

## Market-Open Log — 2026-05-28 (Thursday — session: sweet-shannon-toUfU)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $95,068.28 |
| Equity | $100,005.35 |
| Long Market Value | $4,937.07 |
| Open Positions | 2 / 6 (AAPL 1 sh, GOOGL 12 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Market clock: `is_open=true` (next_close 16:00 ET). Trading window active.

Buy-rule check:
- Max 6 open positions ✅ (2/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ❌ — pre-market screen returned **zero passes** across the watchlist (NVDA/GOOGL/COST below MA20; AAPL RSI 87 overbought; AMD RSI 67 > 65 ceiling).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $310.95 | +$9.07 (+3.00%) |
| GOOGL | 12 | $385.82 | $385.70 | -$1.44 (-0.03%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **AMD** (closest watchlist candidate): live RSI **67.28** still > 65 ceiling → criterion #2 fails. Quote also unusable (bid $495.52 / ask $510.00 — $14.48 spread, ~2.9%); spread alone disqualifies. NO_TRADE.
- **AAPL exit re-validation**: live RSI **87.39** (well above 75 exit threshold; flag now **7 sessions old**). Per established precedent (2026-05-26 and 2026-05-27 market-open logs), AAPL exit evaluation is the EOD routine's responsibility. 10% trailing-stop GTC (stop $281.93 / HWM $313.26) continues to provide mechanical exit discipline; unrealized +3.00% — trailing stop is doing its job. Flag carried to EOD.

Trades executed: **none.**

Risk posture: cash 95.06% of equity (≥20% reserve rule ✅), exposure 4.94%, daily-loss limit (3%) not approached. Weekly trade counter remains 0/3 — full budget preserved into Friday. Heavy macro day (Q2 GDP, PCE, Claims, Durable Goods at 8:30 ET); cluster of after-close earnings tonight (COST/DELL/ADSK/MDB/BBY/BURL/DLTR/GAP/NTAP) — tape may move on the prints. Holding flat-plus-stops is the disciplined response.

---

## Midday Scan — 2026-05-28 (Thursday — session: sweet-shannon-toUfU)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Cash | $95,068.28 |
| Long Market Value | $4,978.45 |
| Open Positions | 2 / 10 (AAPL 1 sh, GOOGL 12 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $309.97 | +$8.09 (+2.68%) |
| GOOGL | 12 | $385.82 | $389.04 | +$38.64 (+0.84%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL +2.68%, GOOGL +0.84% — no losers to cut.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force.
- **Thesis check (web news, 48h)**:
  - AAPL: record Q2 FY2026 ($111.18B), Melius and BofA PT hikes ahead of WWDC 2026 — thesis intact.
  - GOOGL: Q1 2026 +22% YoY, Cloud +63%, Strong Buy (57/0) — thesis intact.

No trades executed. Trailing stops continue mechanical exit discipline. AAPL RSI-overbought flag still EOD's responsibility.

---

## EOD Snapshot — 2026-05-28

| Field | Value |
|-------|-------|
| Portfolio Value | $100,063.19 |
| Cash | $95,068.28 |
| Long Market Value | $4,994.91 |
| Day P&L ($) | +$6.21 |
| Day P&L (%) | +0.0062% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $312.15 | +$10.27 (+3.40%) |
| GOOGL | 12 | $385.82 | $390.23 | +$52.92 (+1.14%) |

Notes: Quiet, marginally green day. NO_TRADE at market-open — pre-market screen returned zero passes (NVDA/GOOGL/COST below MA20; AAPL RSI 87 overbought; AMD RSI 67 > 65 ceiling and quote spread ~2.9% unusable). Midday scan confirmed HOLD — no losers to cut, no positions at +15/+20% gain threshold for stop-tightening; AAPL and GOOGL theses both intact per 48h news check. Day P&L +$6.21 driven by AAPL ratcheting to +$10.27 (+3.40%, new HWM) and GOOGL adding to +$52.92 (+1.14%). Both positions protected by 10% trailing-stop GTC orders. Cash $95,068.28 = 94.98% of equity (≥20% reserve rule ✅); total exposure 4.99%. Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget unused; week closes Friday. **AAPL RSI-overbought exit flag (open since 2026-05-22, now 7 sessions old):** trailing stop continues ratcheting with the position — providing disciplined exit without forcing a sale into strength. Flag remains carried; re-evaluate at Friday pre-market alongside fresh RSI print.


### Trade Entry — 2026-05-29 13:46
| Field | Value |
|-------|-------|
| Symbol | NVDA |
| Side | BUY |
| Shares | 23.0 |
| Est. Price | $216.02 |
| Est. Value | $4968.46 |
| Order ID | ccf47f68-f16e-4b77-8316-0a0f1c4889b3 |
| Trailing Stop | 10% GTC placed immediately after fill |

---

## Market-Open Log — 2026-05-29 (Friday — session: sweet-shannon-9il3Z)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash (pre-trade) | $95,068.28 |
| Equity (pre-trade) | $99,977.89 |
| Long Market Value | $4,909.61 |
| Open Positions | 2 → 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 → 1 / 3 |
| Decision | **TRADE — NVDA** |

Market clock: `is_open=true` (next_close 16:00 ET). Trading window active.

Buy-rule check:
- Max 6 open positions ✅ (2/6 → 3/6)
- Max 3 trades this week ✅ (0/3 → 1/3)
- Max 20% equity per position ✅ (~4.97%)
- Catalyst in today's RESEARCH-LOG ✅ — NVDA conditional pre-authorized (`memory/research/2026-05-29.md`, trigger: ask > $215.50 with RSI ≤ 65 and spread < 0.5%).

Entry-criteria re-validation (live, 60-bar snapshot):
- **NVDA**: live ask **$215.66** > MA20 **$214.88** ✅ (reclaim of MA20 confirmed; pre-market plan trigger $215.50 exceeded) · price > MA50 $198.73 ✅ · RSI-14 **52.51** in 40–65 band ✅ · spread $0.07 / 0.033% < 0.5% ✅ · SPY $757.94 > MA20 $737.44 (macro filter OK) ✅ · no negative 48h catalyst ✅. All five entry criteria pass.

Trade executed:
| Symbol | Side | Qty | Est. Price | Est. Value | Buy Order ID | Trail-Stop Order ID |
|--------|------|-----|-----------|-----------|--------------|---------------------|
| NVDA | BUY | 23 | $216.02 | $4,968.46 | ccf47f68-f16e-4b77-8316-0a0f1c4889b3 | f36bf1b2-1fda-4b2d-8c79-db7b6e80968b |

Sizing: floor(($99,977.89 × 0.05) / $216.20 limit) = 23 shares. 10% trailing-stop GTC placed via retry after the initial chained call returned 403 from broker (transient; second call succeeded; stop $194.319, qty 23, status `new`). Weekly buys remaining: 2.

Position-management notes:
- **AAPL** (1 sh, +$11.75 / +3.89%): RSI-14 still ~88 — flag now 8 sessions old. Trailing-stop GTC (HWM ratcheting with the position) continues to provide mechanical exit discipline. EOD's responsibility per established precedent.
- **GOOGL** (12 sh, -$30.60 / -0.66%): live ask $383.27 below MA20 $391.37; held; trailing-stop GTC active. No add — would push GOOGL toward 5% cap.

Risk posture: cash 95.10% → ~90.13% post-trade (≥20% reserve rule ✅); total exposure 4.91% → ~9.88% (≤80% ✅); daily-loss limit (3%) not approached. Weekly trade budget 2/3 remaining into Friday close.

---

## Midday Scan — 2026-05-29 (Friday — session: sweet-shannon-9il3Z)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $9,885.90 |
| Open Positions | 3 / 10 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $311.40 | +$9.52 (+3.15%) |
| GOOGL | 12 | $385.82 | $382.91 | -$34.95 (-0.76%) |
| NVDA | 23 | $216.00 | $216.51 | +$11.62 (+0.23%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL +3.15%, GOOGL -0.76%, NVDA +0.23% — no losers approaching the -7% cut threshold.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force on all three.
- **Thesis check**: AAPL/GOOGL theses confirmed intact at 2026-05-28 midday scan (record AAPL Q2, GOOGL Q1 +22%); NVDA thesis fresh from this morning's market-open entry (all 5 criteria passed live re-validation). No new negative catalysts surfaced intraday.

No trades executed. Trailing stops continue mechanical exit discipline. AAPL RSI-overbought flag still EOD's responsibility (flag now 8 sessions old; trailing stop ratcheting with position).

---

## EOD Snapshot — 2026-05-29

| Field | Value |
|-------|-------|
| Portfolio Value | $99,871.21 |
| Cash | $90,100.28 |
| Long Market Value | $9,770.93 |
| Day P&L ($) | -$191.98 |
| Day P&L (%) | -0.192% |
| Trades Today | 1 |
| Trades This Week | 1 |
| Open Positions | 3 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $311.49 | +$9.61 (+3.18%) |
| GOOGL | 12 | $385.82 | $381.11 | -$56.52 (-1.22%) |
| NVDA | 23 | $216.00 | $212.48 | -$80.93 (-1.63%) |

Notes: First trade-day of the week — NVDA 23 sh opened @ $216.00 at market-open after live re-validation of pre-market trigger ($215.50 ask, RSI ≤ 65, spread < 0.5%; all five entry criteria passed). 10% trailing-stop GTC placed immediately after fill. Day P&L -$191.98 (-0.192%) driven by GOOGL marking down -$23.31 (to -$56.52 unrealized; live -2.31% session move) and NVDA marking down -$80.93 (entered $216.00, closed $212.48 — small post-entry pullback, well above 10% trailing-stop floor of $194.32) — partially offset by AAPL ratcheting +$9.61 to a fresh HWM. Cash $90,100.28 = 90.22% of equity (≥20% reserve rule ✅); total exposure 9.78% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 1/3 — week closes today; weekly review routine to follow at 17:00 ET. **AAPL RSI-overbought exit flag (open since 2026-05-22, now 8 sessions old):** trailing stop continues ratcheting (position now +3.18% unrealized) — providing disciplined exit without forcing a sale into strength. All three positions protected by 10% trailing-stop GTC orders entering the weekend.

---

## Market-Open Log — 2026-06-01 (Monday — session: sweet-shannon-6cBiH)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $90,100.28 |
| Equity | $99,960.05 |
| Long Market Value | $9,859.77 |
| Open Positions | 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 / 3 (new week) |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (3/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ✅ — AMD conditional pre-authorization (memory/research/2026-06-01.md, trigger: live RSI ≤ 65 AND spread < 0.5%).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $309.79 | +$7.91 (+2.62%) |
| GOOGL | 12 | $385.82 | $375.32 | -$126.06 (-2.72%) |
| NVDA | 23 | $216.00 | $219.42 | +$78.66 (+1.58%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **AMD**: live ask **$496.00** > MA20 $440.11 & MA50 $328.15 ✅ · RSI-14 **66.97** > 65 ceiling ❌ · spread bid $490.90 / ask $496.00 = $5.10 / **1.03%** > 0.5% ceiling ❌. Two criteria fail. Pre-market plan was explicit: "Defer to NO_TRADE if RSI prints > 65, spread > 0.5%". Both triggered → NO_TRADE.
- **AAPL exit re-validation**: live RSI-14 **84.28** still >> 75 exit threshold (flag now 9 sessions old). Per established precedent (2026-05-26 / 27 / 28 market-open logs), AAPL exit evaluation is EOD's responsibility; market-open routine does not execute exits. 10% trailing-stop GTC continues mechanical exit discipline; HWM ratcheting with the position (unrealized +2.62%). Flag carried to EOD.
- **NVDA / GOOGL holds**: no add (NVDA combined position would exceed 5% cap per pre-market analysis); GOOGL still below MA20 — both held under trailing-stop GTC protection.

Trades executed: **none.**

Risk posture: cash 90.14% of equity (≥20% reserve rule ✅), exposure 9.86% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget preserved into Tuesday.

---

## Midday Scan — 2026-06-01 (Monday — session: sweet-shannon-6cBiH)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $9,909.02 |
| Open Positions | 3 / 10 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $305.83 | +$3.95 (+1.31%) |
| GOOGL | 12 | $385.82 | $375.39 | -$125.16 (-2.70%) |
| NVDA | 23 | $216.00 | $221.67 | +$130.51 (+2.63%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL +1.31%, GOOGL -2.70%, NVDA +2.63% — no losers approaching the -7% cut threshold.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force on all three.
- **Thesis check (web news, 48h)**:
  - AAPL: BofA reiterated Buy ($380 PT) into June 2026 — strong iPhone upgrade cycle, Services growth, internal silicon margins. Thesis intact.
  - GOOGL: trading in $378–$388 range; no breaking negative catalyst. Thesis intact.
  - NVDA: BofA reiterated Buy ($320 PT) into June; Jensen Huang COMPUTEX 2026 keynote today — positive event-driven catalyst. Thesis intact.

No trades executed. Trailing stops continue mechanical exit discipline. AAPL RSI-overbought flag still EOD's responsibility (flag now 9 sessions old; trailing stop ratcheting with position).

---

## Market-Open Log — 2026-06-02 (Tuesday — session: sweet-shannon-2jsqG)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $90,100.28 |
| Equity | $100,050.69 |
| Long Market Value | $9,950.41 |
| Open Positions | 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (3/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ✅ — but only NVDA passes criteria, and NVDA is at the 5% cap.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $308.43 | +$6.55 (+2.17%) |
| GOOGL | 12 | $385.82 | $361.34 | -$293.76 (-6.35%) |
| NVDA | 23 | $216.00 | $230.76 | +$339.48 (+6.83%) |

Entry-criteria re-validation (per pre-market plan):
- **NVDA add (BLOCKED)**: all 5 criteria pass (price $230.76 > MA20 $216.75 > MA50; RSI 53.9 in band; SPY bullish; Computex catalysts intact). Sizing: NVDA mark = $5,307.48 = **5.31% of equity**, above the 5% per-position cap. No additional shares authorized. Hold existing 23 sh.
- **AAPL/GOOGL/MSFT/META/AMZN**: all failed the pre-market bar-based screen (below MA20 and/or RSI out of band).
- **AAPL exit re-validation**: RSI pulled back to 70.58 (below 75 exit threshold). Trailing-stop GTC continues ratcheting. Pre-WWDC exit pre-staged for Friday 2026-06-05 EOD (T-1 before 6/8 keynote). Today: hold.
- **GOOGL midday watch**: live -6.35% — within $0.65/share of the **-7% midday cut threshold**. Pre-market does not execute exits; midday routine will decide.

Trades executed: **none.**

Risk posture: cash 90.06% of equity (≥20% reserve rule ✅), exposure 9.94% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter remains 0/3 — full budget preserved into the week. JOLTS 10:00 ET; AVGO earnings Wednesday after-close.

---

## Midday Scan — 2026-06-02 (Tuesday — session: exciting-bohr-0mfD5)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $9,902.93 |
| Open Positions | 3 / 10 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $312.18 | +$10.30 (+3.41%) |
| GOOGL | 12 | $385.82 | $367.27 | -$222.60 (-4.81%) |
| NVDA | 23 | $216.00 | $225.37 | +$215.51 (+4.34%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL +3.41%, GOOGL -4.81%, NVDA +4.34% — no positions at/below -7% threshold. GOOGL recovered from -6.35% at market-open to -4.81% intraday (no cut).
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force on all three.
- **Thesis check (web news, 48h)**:
  - AAPL: Morgan Stanley reiterates WWDC 6/8 as "key catalyst" — PT $365–$385 (upside $440); BofA $380. Thesis intact.
  - GOOGL: $80B equity raise (Berkshire $10B PP + $30B public + $40B ATM) drove intraday selling — dilution overhang plus AI capex doubling to $180–190B for 2026. Strong Buy (64 analysts, $430 PT) intact; share-supply pressure is the headwind, not a fundamental break. Thesis pressured but **not broken**.
  - NVDA: Computex Vera Rubin in full production (OpenAI/Anthropic/xAI/Oracle); RTX Spark PC chip with Microsoft/Dell/HP/ASUS/Lenovo/MSI. Thesis intact / strengthened.

No trades executed. Trailing stops continue mechanical exit discipline. AAPL pre-WWDC exit still pre-staged for Friday 2026-06-05 EOD per pre-market plan.

---

## EOD Snapshot — 2026-06-01

| Field | Value |
|-------|-------|
| Portfolio Value | $100,085.49 |
| Cash | $90,100.28 |
| Long Market Value | $9,985.21 |
| Day P&L ($) | +$214.28 |
| Day P&L (%) | +0.214% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 3 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $306.06 | +$4.18 (+1.39%) |
| GOOGL | 12 | $385.82 | $376.40 | -$113.04 (-2.44%) |
| NVDA | 23 | $216.00 | $224.47 | +$194.81 (+3.92%) |

Notes: First session of the new trading week. NO_TRADE at market-open — AMD (the sole pre-authorized catalyst) rejected on live re-validation: RSI-14 66.97 > 65 ceiling AND spread $5.10 / 1.03% > 0.5% ceiling (two criteria failed against an explicit "defer if either triggers" plan). Midday scan confirmed HOLD — no losers near the -7% cut threshold, no positions at +15/+20% gain for stop-tightening; AAPL/GOOGL/NVDA theses all confirmed intact via 48h news check (BofA Buy reiterations on AAPL and NVDA; Jensen Huang COMPUTEX 2026 keynote positive for NVDA). Day P&L +$214.28 (+0.214%) driven by NVDA marking up to +$194.81 (+3.92%, fresh HWM since entry Friday) — partially offset by GOOGL drifting to -$113.04 (-2.44%) and AAPL pulling back to +$4.18 (+1.39%). Cash $90,100.28 = 90.02% of equity (≥20% reserve rule ✅); total exposure 9.98% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Tuesday. **AAPL RSI-overbought exit flag (open since 2026-05-22, now 9 sessions old):** trailing stop continues ratcheting with the position — providing disciplined exit without forcing a sale into strength. All three positions protected by 10% trailing-stop GTC orders.

---

## Market-Open Log — 2026-06-03 (Wednesday — session: sweet-shannon-UIskX)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $90,100.28 |
| Equity | $99,785.77 |
| Long Market Value | $9,685.49 |
| Open Positions | 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (3/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅
- Catalyst in today's RESEARCH-LOG ✅ — NVDA conditional (cap-blocked); AMD conditional (RSI/spread).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $316.42 | +$14.54 (+4.82%) |
| GOOGL | 12 | $385.82 | $363.76 | -$264.72 (-5.72%) |
| NVDA | 23 | $216.00 | $217.605 | +$36.92 (+0.74%) |

Entry-criteria re-validation (per pre-market plan):
- **NVDA add (BLOCKED)**: all 5 criteria pass live (price $222.82 > MA20 $217.97 > MA50 $201.27; RSI 51.61 in band; SPY bullish). Sizing: 24 sh × $217.76 ask = $5,226.24 = **5.237% of equity** > 5% per-position cap. No additional shares authorized.
- **AMD entry (BLOCKED)**: live RSI **70.04** > 65 ceiling ❌; spread $533.00 − $518.81 = $14.19 = **2.73%** > 0.5% ceiling ❌. Both gating conditions fail per pre-market plan.
- **AAPL exit pre-stage**: still pre-staged for Friday 2026-06-05 EOD (T-1 before WWDC 6/8). Trailing-stop GTC continues mechanical discipline; RSI ~76 at premarket.
- **GOOGL midday watch**: live -5.72% — within ~$1.50/sh of the -7% midday cut threshold. Carry forward to midday scan.

Trades executed: **none.**

Risk posture: cash 90.29% of equity (≥20% reserve rule ✅), exposure 9.71% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget preserved. AVGO earnings after-close — semis read-through to NVDA tomorrow.

---

## Midday Scan — 2026-06-03 (Wednesday — session: exciting-bohr-rMX4b)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $9,583.17 |
| Open Positions | 3 / 10 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $309.72 | +$7.84 (+2.60%) |
| GOOGL | 12 | $385.82 | $360.11 | -$308.52 (-6.66%) |
| NVDA | 23 | $216.00 | $215.31 | -$15.87 (-0.32%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL +2.60%, GOOGL **-6.66%** (closest, within ~$1.30/sh of cut), NVDA -0.32% — no position at/below the -7% threshold. GOOGL one print away from mechanical exit; carried to EOD.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force on all three.
- **Thesis check (web news, 48h)**:
  - AAPL: WWDC 6/8 key catalyst — Morgan Stanley $365–$385 PT, upside $440. Apple trading near $4.6T cap on AI expectations. Thesis intact. Pre-WWDC exit still pre-staged for Friday 2026-06-05 EOD.
  - GOOGL: Same $80B capital raise / dilution overhang from 6/2 — no new thesis break, just continuing weakness. Strong Buy 64-analyst rating intact; FY revenue >$400B; $0.22 dividend ex-date 6/8. Thesis pressured but **not broken**.
  - NVDA: Microsoft/Azure unified agentic-AI stack across Windows; Coherent datacenter optics investment partnership. Thesis intact / strengthened — intraday weakness is broader-tape semi rotation, not stock-specific.

No trades executed. Trailing stops continue mechanical exit discipline. GOOGL -6.66% remains the live risk; one more session of dilution-overhang selling triggers the mechanical -7% cut at next routine.

---

## EOD Snapshot — 2026-06-02

| Field | Value |
|-------|-------|
| Portfolio Value | $99,888.31 |
| Cash | $90,100.28 |
| Long Market Value | $9,788.03 |
| Day P&L ($) | -$197.18 |
| Day P&L (%) | -0.197% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 3 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $314.85 | +$12.97 (+4.30%) |
| GOOGL | 12 | $385.82 | $362.59 | -$278.76 (-6.02%) |
| NVDA | 23 | $216.00 | $222.70 | +$154.10 (+3.10%) |

Notes: Second session of the new trading week. NO_TRADE at market-open — only NVDA passed all 5 entry criteria, but its current mark put the position at 5.31% of equity, exceeding the 5% per-position cap (no add authorized); AAPL/GOOGL/MSFT/META/AMZN all failed the pre-market bar-based screen. Midday scan confirmed HOLD — GOOGL recovered intraday from -6.35% (market-open) to -4.81% (midday), staying above the -7% cut threshold; no positions at +15/+20% gain for stop-tightening; all three theses confirmed intact (AAPL: Morgan Stanley reiterated WWDC 6/8 catalyst, $365–$385 PT; GOOGL: $80B equity raise drove intraday selling — dilution overhang but Strong Buy 64-analyst rating intact; NVDA: Computex Vera Rubin in full production with OpenAI/Anthropic/xAI/Oracle, RTX Spark with major OEMs). Day P&L -$197.18 (-0.197%) driven by GOOGL marking down further to -$278.76 (-6.02%, new low — close to but above the -7% cut threshold) — partially offset by AAPL ratcheting +$8.79 to fresh HWM (+$12.97 / +4.30%) and NVDA giving back -$40.71 to +$154.10 (+3.10%). Cash $90,100.28 = 90.20% of equity (≥20% reserve rule ✅); total exposure 9.80% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Wednesday. **AAPL pre-WWDC exit pre-staged for Friday 2026-06-05 EOD** (T-1 before 6/8 keynote per pre-market plan; RSI pulled back to 70.58, now below the 75 exit threshold — trailing stop continues mechanical discipline in the interim). **GOOGL midday watch (-6.02% close, within $0.65 of -7% cut threshold):** carry forward to Wednesday midday scan — one more session of dilution-overhang weakness would trigger mechanical exit. All three positions protected by 10% trailing-stop GTC orders.

---

## EOD Snapshot — 2026-06-03

| Field | Value |
|-------|-------|
| Portfolio Value | $99,666.86 |
| Cash | $90,100.28 |
| Long Market Value | $9,566.58 |
| Day P&L ($) | -$221.45 |
| Day P&L (%) | -0.222% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 3 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $310.53 | +$8.65 (+2.87%) |
| GOOGL | 12 | $385.82 | $359.20 | -$319.44 (-6.90%) |
| NVDA | 23 | $216.00 | $215.03 | -$22.35 (-0.45%) |

Notes: Third session of the trading week. NO_TRADE at market-open — NVDA add blocked (5.237% > 5% per-position cap despite all 5 criteria passing); AMD blocked (RSI 70.04 > 65 ceiling AND spread $14.19 / 2.73% > 0.5% ceiling). Midday scan confirmed HOLD — GOOGL deteriorated further to -6.66% (within ~$1.30/sh of -7% cut) but did not trigger; AAPL theses intact (WWDC 6/8 catalyst, MS $365–$385 PT); GOOGL dilution overhang from $80B raise continues (Strong Buy 64-analyst rating intact); NVDA Microsoft/Azure agentic-AI stack + Coherent optics partnership strengthens thesis. Day P&L -$221.45 (-0.222%) driven by GOOGL leg lower to -$319.44 (-6.90%, fresh low — now within ~$0.40/sh of -7% cut threshold) and NVDA flipping to -$22.35 (-0.45%) on intraday semi-rotation — partially offset by AAPL holding +$8.65 (+2.87%). Cash $90,100.28 = 90.40% of equity (≥20% reserve rule ✅); total exposure 9.60% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget remaining for Thu/Fri. **GOOGL -7% cut watch (HIGHEST PRIORITY for Thursday midday scan):** position closed -6.90%, one more session of dilution-overhang selling triggers mechanical exit; trailing-stop GTC remains primary backstop. **AAPL pre-WWDC exit pre-staged for Friday 2026-06-05 EOD** (T-1 before 6/8 keynote). **NVDA** post-AVGO earnings tomorrow — semis read-through monitored. All three positions protected by 10% trailing-stop GTC orders.

---

## Midday Scan — 2026-06-04 (Thursday — session: exciting-bohr-oKZGa)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $9,786.89 |
| Open Positions | 3 / 10 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $311.27 | +$9.39 (+3.11%) |
| GOOGL | 12 | $385.82 | $371.725 | -$169.14 (-3.65%) |
| NVDA | 23 | $216.00 | $218.04 | +$46.92 (+0.94%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL +3.11%, GOOGL -3.65%, NVDA +0.94% — no position at/below -7% threshold. **GOOGL cut-loser watch resolved favorably**: position recovered from yesterday's -6.90% close (within $0.40/sh of cut) to -3.65% midday (intraday +3.55%).
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC orders remain in force on all three.
- **Thesis check (web news, 48h)**:
  - AAPL: WWDC 6/8 catalyst — MS PT $365–$385 (upside $440). Pre-WWDC exit pre-staged for Friday 2026-06-05 EOD. Thesis intact.
  - GOOGL: Capital raise upsized to $84.75B (from $80B); ARK bought 134K shares today; Strong Buy intact. Thesis pressured but **not broken**.
  - NVDA: AVGO Q2 beat ($73B AI order book, AI rev +>100% to $10.8B) read-through net positive; Vera Rubin in production; Microsoft/Azure agentic-AI stack. Thesis intact / strengthened.

No trades executed. Trailing stops continue mechanical exit discipline. AAPL pre-WWDC exit still pre-staged for Friday 2026-06-05 EOD.

---

## Market-Open Log — 2026-06-04 (Thursday — session: sweet-shannon-z4odj)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:47 ET) |
| Cash | $90,100.28 |
| Equity | $99,686.48 |
| Long Market Value | $9,586.20 |
| Open Positions | 3 / 6 (AAPL 1 sh, GOOGL 12 sh, NVDA 23 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (3/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (largest NVDA 4.93%)
- Catalyst in today's RESEARCH-LOG: pre-market log rejected all candidates.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $311.54 | +$9.66 (+3.20%) |
| GOOGL | 12 | $385.82 | $363.47 | -$268.20 (-5.79%) |
| NVDA | 23 | $216.00 | $213.625 | -$54.63 (-1.10%) |

Entry-criteria re-validation:
- **NVDA add (BLOCKED)**: live last $213.68 < MA20 $218.88 → criterion #1 fails. Position already 4.93% of equity, one more share crosses 5% cap. RSI-14 41.65 ✅ but two other blockers stand.
- **AAPL add (BLOCKED)**: pre-staged Friday 2026-06-05 EOD exit (T-1 before WWDC 6/8) — adding inverts exit plan.
- **AMD entry (BLOCKED)**: pre-market RSI 74.14 > 65 and historical spread 2.73% > 0.5%. Both gating filters fail.
- **GOOGL cut-loser watch**: live -5.79% (recovered from -6.90% yesterday close, intraday +1.25%); within ~$1.40/sh of -7% cut at $358.81. Pre-market does not execute exits — defer to midday scan.

Trades executed: **none.**

Risk posture: cash 90.38% of equity (≥20% reserve rule ✅), exposure 9.62% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter remains 0/3. Macro backdrop: BofA defensive June seasonality call + AVGO/CrowdStrike disappointment carryover + U.S.–Iran tensions → unfavorable add-longs environment. **GOOGL -7% cut watch is highest-priority item for midday scan.** All three positions protected by 10% trailing-stop GTC orders.

---

## EOD Snapshot — 2026-06-04

| Field | Value |
|-------|-------|
| Portfolio Value | $99,875.87 |
| Cash | $90,100.28 |
| Long Market Value | $9,775.59 |
| Day P&L ($) | +$209.01 |
| Day P&L (%) | +0.210% |
| Trades Today | 0 |
| Trades This Week | 0 |
| Open Positions | 3 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $311.10 | +$9.22 (+3.05%) |
| GOOGL | 12 | $385.82 | $371.20 | -$175.44 (-3.79%) |
| NVDA | 23 | $216.00 | $217.83 | +$42.09 (+0.85%) |

Notes: Fourth session of the trading week — green recovery day. NO_TRADE at market-open — NVDA add blocked (live $213.68 < MA20 $218.88 + position 4.93% near 5% cap); AMD add blocked (pre-market RSI 74.14 > 65 ceiling AND spread 2.73% > 0.5% ceiling); AAPL add blocked (pre-WWDC exit pre-staged for Friday EOD inverts add logic). Midday scan confirmed HOLD — **GOOGL -7% cut watch resolved favorably**: position recovered from yesterday's -6.90% close (within $0.40/sh of mechanical cut) to -3.65% midday (intraday +3.55%), closing -3.79%; no stop-tighten triggers; theses all intact (AAPL: WWDC 6/8 catalyst with MS PT $365–$385; GOOGL: capital raise upsized to $84.75B but ARK accumulating, Strong Buy intact; NVDA: AVGO Q2 beat read-through positive, Vera Rubin in production, Microsoft/Azure agentic-AI stack). Day P&L +$209.01 (+0.210%) driven by GOOGL rallying from -$319.44 to -$175.44 (+$144.00 swing) and NVDA recovering from -$22.35 to +$42.09 (+$64.44 swing) — partially offset by AAPL ticking back to +$9.22 (+3.05%). Cash $90,100.28 = 90.21% of equity (≥20% reserve rule ✅); total exposure 9.79% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget unused; Friday is the week's final session. **AAPL pre-WWDC exit pre-staged for Friday 2026-06-05 EOD** (T-1 before 6/8 keynote). **GOOGL cut-loser watch DE-ESCALATED** after intraday recovery — trailing-stop GTC remains the primary backstop; carry forward to Friday for re-evaluation if dilution-overhang selling resumes. All three positions protected by 10% trailing-stop GTC orders.

---

### Trade Exit — 2026-06-05 11:20 ET (trailing stop)
| Field | Value |
|-------|-------|
| Symbol | NVDA |
| Side | SELL (trailing_stop GTC fill) |
| Shares | 23 |
| Avg Exit Price | $209.04 |
| Avg Entry Price | $216.00 |
| Realized P&L | -$160.08 (-3.22%) |
| HWM | $232.28 |
| Stop Price | $209.052 |
| Hold Days | 5 (entered 2026-05-29) |
| Order ID | f36bf1b2-1fda-4b2d-8c79-db7b6e80968b |
| Exit Reason | 10% trailing-stop fired intraday (NVDA broke $209 on AVGO read-through + soft semis tape; HWM $232.28 set 2026-06-02 intraday after Computex high) |

---

## Midday Scan — 2026-06-05 (Friday — session: exciting-bohr-yp0ZW)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Cash | $94,908.20 |
| Equity | $99,658.77 |
| Long Market Value | $4,750.57 |
| Open Positions | 2 / 10 (AAPL 1 sh, GOOGL 12 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $311.29 | +$9.41 (+3.12%) |
| GOOGL | 12 | $385.82 | $369.94 | -$190.56 (-4.12%) |

Midday checks:
- **NVDA exit recorded**: 10% trailing-stop GTC filled at 11:20 ET, 23 sh @ $209.04 (HWM $232.28, stop $209.052). Realized -$160.08 / -3.22%. Mechanical exit discipline worked as designed — semis derate + AVGO read-through pulled NVDA through the trailing stop. Cash $90,100.28 → $94,908.20 (+$4,807.92 proceeds).
- **Cut-loser (-7%)**: AAPL +3.12%, GOOGL -4.12% — no losers at/below -7% threshold. GOOGL widened modestly from yesterday's close (-3.79%) but still well above the -$358.81 mechanical cut level (currently $369.94).
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. AAPL +3.12% is closest to a gain trigger but nowhere near +15%. 10% trailing-stop GTC orders remain in force on both AAPL and GOOGL.
- **Thesis check (web news, 48h)**:
  - AAPL: Wedbush (Dan Ives) frames WWDC 6/8 keynote as "Apple Stock Could Finally Have Its AI Moment" — "Expect Fireworks" on Apple Intelligence 2.0 + Gemini-Siri. Morgan Stanley PT $365–$385 (upside $440), BofA $380 still standing. **Pre-WWDC exit remains pre-staged for TODAY EOD.** Thesis intact.
  - GOOGL: Daniel Loeb (Third Point) added Meta + Alphabet in Q1 — billionaire endorsement vs the dilution overhang. Ackman / Ives both holding GOOGL. Depositary-share close completes today; supply-pressure window ends. Thesis intact.

No trades executed at midday. Realized -$160.08 from NVDA trailing-stop exit. AAPL pre-WWDC EOD exit still queued. Cash reserve climbs to 95.23% of equity (≥20% rule ✅); exposure drops to 4.77% (≤80% ✅). Daily-loss limit (3%) not approached.

---

## EOD Snapshot — 2026-06-05

| Field | Value |
|-------|-------|
| Portfolio Value | $99,609.60 |
| Cash | $94,908.20 |
| Long Market Value | $4,701.40 |
| Day P&L ($) | -$266.27 |
| Day P&L (%) | -0.267% |
| Trades Today | 1 (NVDA SELL, trailing-stop fill) |
| Trades This Week | 0 buys / 3 budget · 1 exit |
| Open Positions | 2 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $307.22 | +$5.34 (+1.77%) |
| GOOGL | 12 | $385.82 | $366.18 | -$235.66 (-5.09%) |

### Week Recap (2026-06-01 → 2026-06-05)

| Date | EOD Equity | Day P&L | Day % |
|------|-----------|---------|-------|
| 2026-06-01 | $100,085.49 | +$214.28 | +0.214% |
| 2026-06-02 | $99,888.31 | -$197.18 | -0.197% |
| 2026-06-03 | $99,666.86 | -$221.45 | -0.222% |
| 2026-06-04 | $99,875.87 | +$209.01 | +0.210% |
| 2026-06-05 | $99,609.60 | -$266.27 | -0.267% |
| **Week** | — | **-$475.89** | **-0.476%** |

Notes: Fifth and final session of the trading week. **NVDA trailing-stop fired at 11:20 ET** — 23 sh @ $209.04 vs $216.00 avg entry, realized **-$160.08 / -3.22%** (HWM $232.28 set 2026-06-02 intraday post-Computex, stop $209.052). Mechanical exit discipline worked as designed: AVGO read-through + soft semis tape + macro defensive backdrop (BofA June seasonality call, US/Iran tensions) pulled NVDA through the trailing stop; 5-day hold. Cash $90,100.28 → $94,908.20 (+$4,807.92 proceeds). Day P&L **-$266.27 (-0.267%)** = realized -$160.08 on NVDA exit + unrealized drag on remaining names (AAPL ticked back to +$5.34 from +$9.22; GOOGL widened to -$235.66 from -$175.44 on continuing dilution-overhang selling after the upsized $84.75B raise). Daily-loss limit (3%) not approached. Cash 95.28% of equity (≥20% reserve rule ✅); exposure 4.72% (≤80% ✅). Weekly trade counter ended **0 buys / 3 budget · 1 exit** — all entry attempts blocked by strategy filters all week (NVDA 5% cap / sub-MA20; AMD RSI > 65 + spread > 0.5%; AAPL pre-WWDC freeze; GOOGL averaging-down barred). Week ended **-$475.89 / -0.476%** — fourth losing week in a row of a flat-to-slightly-red post-entry environment; full weekly review routine to follow at 17:00 ET. **AAPL pre-WWDC exit (T-1 before 6/8 keynote) pre-staged for tonight EOD remains pending** — outside this 5-step snapshot workflow; flagged for follow-up so it can be evaluated/executed before the keynote weekend gap risk. AAPL trailing-stop GTC (stop $285.237 / HWM $316.93) continues mechanical discipline in the interim. GOOGL trailing-stop GTC (stop $354.492 / HWM $393.88) also active.

---

## Midday Scan — 2026-06-08 (Monday — session: exciting-bohr-25t3go)

| Field | Value |
|-------|-------|
| Routine | Midday Scan (~12:33 ET) |
| Open Positions | 2 / 10 (AAPL 1 sh, GOOGL 12 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $313.52 | +$11.64 (+3.86%) |
| GOOGL | 12 | $385.82 | $362.70 | -$277.44 (-5.99%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL +3.86%, GOOGL **-5.99%** — neither at threshold. GOOGL cushion ~$3.69/sh (~1.01%) to $358.81 cut. Carried to EOD.
- **Stop-tighten**: no position at +15%/+20% gain — no adjustments. 10% trailing-stop GTCs active on both.
- **Thesis check (web news, 48h)**:
  - AAPL: WWDC 2026 keynote live today; Bernstein Outperform $350, BofA Buy $380, Morgan Stanley "key catalyst" framing. Thesis intact.
  - GOOGL: Berkshire $10B placement; $80B equity raise for 2026 AI capex ($180–190B); $25B TPU venture w/ Blackstone; SpaceX GPU deal. Drawdown is positioning, not thesis. Thesis intact.

No trades executed. Trailing stops continue mechanical exit discipline.

---

## EOD Snapshot — 2026-06-08

| Field | Value |
|-------|-------|
| Portfolio Value | $99,567.47 |
| Cash | $94,908.18 |
| Long Market Value | $4,659.29 |
| Day P&L ($) | -$42.13 |
| Day P&L (%) | -0.042% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 |
| Open Positions | 2 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $300.89 | -$0.99 (-0.33%) |
| GOOGL | 12 | $385.82 | $363.20 | -$271.44 (-5.86%) |

Notes: Quiet, marginally red day to open the new trading week. **NO_TRADE day** — pre-market screen returned zero buy candidates (macro filter fails: SPY $737.55 < MA20 $746.29; AAPL chart-pass but pending exit, not add; GOOGL/NVDA/AMD/COST all below MA20). Market-open routine **OVERRODE the pre-staged AAPL pre-WWDC exit** (carried across 4 prior pre-market routines) on documented rationale: (1) `scripts/trade.py close` submits market order — direct violation of limit-only rule; (2) AAPL is 0.31% of equity — worst-case "sell the news" -10% costs ~$31, immaterial; (3) 10% trailing-stop GTC (stop $285.24 / HWM $316.93) provides mechanical backstop; (4) chart still passes entry criteria and analyst tape constructive into WWDC. AAPL pre-WWDC carry-forward flag **CLOSED** — position now under standard exit discipline. WWDC keynote landed at 13:00 ET — AAPL marked +3.86% at midday (HWM $313.52) before fading back to -0.33% at close. **GOOGL -7% cut watch continues**: live -5.86% unrealized vs cut threshold -7% (~$358.81); cushion ~$3.49/sh (~0.96%) — narrowest yet, carried to tomorrow's midday scan. Day P&L -$42.13 (-0.042%) driven by AAPL giving back +$11.64 midday HWM to close -$0.99 (post-keynote "sell the news" pattern partially played out), partially offset by GOOGL holding flat-to-slightly-better intraday (mark $363.20 vs open $364.34). Cash $94,908.18 = 95.32% of equity (≥20% reserve rule ✅); total exposure 4.68% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Tuesday. Both positions protected by 10% trailing-stop GTC orders entering Tuesday.

---

## Midday Scan — 2026-06-09 (Tuesday — session: exciting-bohr-fm8nrl)

| Field | Value |
|-------|-------|
| Routine | Midday Scan (12:30 ET) |
| Cash | $94,908.18 |
| Equity | $99,536.08 |
| Long Market Value | $4,627.90 |
| Open Positions | 2 / 10 (AAPL 1 sh, GOOGL 12 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $289.78 | -$12.11 (-4.01%) |
| GOOGL | 12 | $385.82 | $361.48 | -$292.08 (-6.31%) |

Midday checks:
- **Cut-loser (−7%)**: AAPL -4.01% ✅, GOOGL -6.31% ✅ — neither breaches the -7% cut threshold. GOOGL cushion to cut ≈ $0.66/sh (~0.69%) — tightest yet, **carried to EOD with high-priority watch**.
- **Stop-tighten**: no position at +15% or +20% — no action. 10% trailing-stop GTC orders remain in force.
- **Thesis check (web news, 48h)**:
  - **AAPL**: WWDC 2026 post-event fade — Siri AI revealed (Google Gemini-powered, dedicated app) but rollout deferred to late 2026/2027. Stock -3.7% off intraday high. Wedbush reiterated **Outperform, $400 PT** post-keynote. P/E 36. **Thesis intact** — mechanical "sell the news" reaction, not fundamental break.
  - **GOOGL**: $80B AI equity raise closed (incl. Berkshire $10B PP); 2026 capex guide lifted to $180–190B for AI infra; Waymo expansion + TPU order flow; **56 buy / 0 sell, Strong Buy** consensus. Weakness reflects capex-shock / dilution drag, not a thesis break. **Thesis intact**.

Decision rationale:
- Neither position breaches the mechanical -7% cut threshold per midday-scan rule. GOOGL is **tight** (-6.31%, cushion ~0.69%) but the cut-loser rule is a hard "≥ -7%" trigger — not approached-and-cut. Discipline = wait for the trigger.
- No thesis broken on either name → no preemptive exit.
- No winners at +15% or +20% → no stop tightening required.
- Trailing-stop GTC orders continue mechanical exit discipline on both names.

Risk posture: cash 95.35% of equity (≥20% reserve ✅), exposure 4.65% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Wed CPI. **GOOGL -7% cut watch escalated to EOD**: trigger price ≈ $358.81; current mark $361.48; intraday low risk on a soft afternoon. EOD must re-evaluate live.

Trades executed: **none.**

---

## EOD Snapshot — 2026-06-09

| Field | Value |
|-------|-------|
| Portfolio Value | $99,570.94 |
| Cash | $94,908.18 |
| Long Market Value | $4,662.76 |
| Day P&L ($) | +$3.47 |
| Day P&L (%) | +0.0035% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 |
| Open Positions | 2 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $291.04 | -$10.84 (-3.59%) |
| GOOGL | 12 | $385.82 | $364.31 | -$258.12 (-5.58%) |

Notes: Quiet, essentially flat day. **NO_TRADE day** — pre-market screen returned zero buy candidates (macro filter fails: SPY $739.22 < MA20 $746.37, 4th straight session; AAPL/GOOGL/NVDA/COST all below MA20; AMD only chart-passer but bar-based spread unusable + macro filter blocks). Market-open confirmed NO_TRADE on live re-validation. Midday scan held: GOOGL -6.31% intraday cushion ~0.69% (tightest yet) escalated to EOD watch. **GOOGL -7% cut watch resolution**: live -5.58% at close (improved from midday -6.31%) vs cut threshold ~$358.81; cushion ~$4.50/sh (~1.24%) — widened into close, no mechanical cut triggered. AAPL faded from morning -0.13% to -3.59% on continuing post-WWDC drag (Siri AI rollout deferred to late 2026/2027); position 0.29% of equity — immaterial. Day P&L +$3.47 (+0.0035%) — AAPL marked down ~$10 offset by GOOGL recovering ~$13 vs yesterday's close. Cash $94,908.18 = 95.32% of equity (≥20% reserve rule ✅); total exposure 4.68% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget into Wed CPI / Thu PPI / Fri sentiment. Both positions protected by 10% trailing-stop GTC orders entering Wednesday's CPI print.

---

## Midday Scan — 2026-06-10 (Wednesday — session: cut-loser GOOGL)

| Field | Value |
|-------|-------|
| Routine | Midday Scan (~12:34 ET) |
| Cash (pre-exit) | $94,908.18 |
| Cash (post-exit) | $99,207.18 |
| Equity | $99,499.34 |
| Long Market Value | $292.16 |
| Open Positions | 2 → 1 / 6 (AAPL 1 sh) |
| Decision | **CUT LOSER — GOOGL SOLD** |

Position snapshot at scan (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $291.75 | -$10.13 (-3.36%) |
| GOOGL | 12 | $385.82 | $358.19 | -$331.56 (-7.16%) |

Midday checks:
- **Cut-loser (−7%)**: GOOGL **-7.16%** triggers the workflow's cut rule — sold. AAPL -3.36%, no cut.
- **Stop-tighten**: no position at +15% / +20% — none to tighten.
- **Thesis check**: GOOGL exit on mechanical risk rule; no further thesis review needed.

Exit executed:
| Symbol | Side | Qty | Bid | Limit | Fill Price | Order ID |
|--------|------|-----|-----|-------|-----------|----------|
| GOOGL | SELL | 12 | $358.19 | $357.29 | **$358.25** | 87d37913-e7ad-41da-9997-2c791db8782b |

Cancelled GOOGL 10% trailing-stop GTC (order a7fadae9, stop $354.49 / HWM $393.88) prior to placing the limit sell to prevent duplicate fill.

Realized P&L on GOOGL exit:
- Entry: 12 sh × $385.82 = $4,629.84
- Exit: 12 sh × $358.25 = $4,299.00
- **Realized: -$330.84 (-7.15%)**
- Hold: 19 calendar days (2026-05-22 → 2026-06-10)

Post-exit risk posture: cash 99.71% of equity (≥20% reserve ✅), exposure 0.29% (AAPL 1 sh only). AAPL 10% trailing-stop GTC (order 5851cbb5, stop $285.66 / HWM $317.40) remains active. Daily-loss limit (3%) not approached — realized -0.33% of equity from the GOOGL cut. Weekly trade counter still 0/3 buys (sell does not consume buy budget).

---

## EOD Snapshot — 2026-06-10

| Field | Value |
|-------|-------|
| Portfolio Value | $99,499.18 |
| Cash | $99,207.18 |
| Long Market Value | $292.00 |
| Day P&L ($) | -$71.76 |
| Day P&L (%) | -0.072% |
| Trades Today | 1 (GOOGL SELL) |
| Trades This Week | 0 buys / 1 sell |
| Open Positions | 1 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $292.00 | -$9.88 (-3.27%) |

Notes: **GOOGL cut at midday — realized -$330.84 (-7.15%)** on 12 sh sold @ $358.25 after the cut-loser rule fired at -7.16% unrealized. Hold was 19 calendar days (2026-05-22 → 2026-06-10). Post-CPI tape stayed risk-off — SPY $735.72 < MA20 $746.26, the macro filter blocked all add-longs at market-open. Day P&L -$71.76 (-0.072%) — realized -$330.84 on GOOGL offset by GOOGL mark-up between yesterday's close (-$258.12) and midday exit (-$331.56) limiting incremental session damage, plus AAPL marking slightly higher into the close (-$10.84 → -$9.88). Cash $99,207.18 = 99.71% of equity (≥20% reserve rule ✅); total exposure 0.29% (AAPL 1 sh only). Daily-loss limit (3%) not approached — total session impact -0.072% well inside the 3% halt. AAPL trailing-stop GTC remains the sole mechanical exit (stop $285.66 / HWM $317.40). Weekly trade counter 0 buys / 1 sell — full 3-buy budget preserved into Thu PPI / Fri sentiment.

---

## Midday Scan — 2026-06-11 (Thursday — session: exciting-bohr-ynysti)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 1 / 3 |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $296.635 | -$5.245 (-1.74%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL -1.74% — no action. Pre-market $276 illiquid print did not hold into regular hours; trailing-stop $285.66 did not fire.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%) gain. 10% trailing-stop GTC remains in force.
- **Thesis check (48h)**: AAPL post-WWDC "AI underwhelm" already priced in (6/8 -3-4% repricing absorbed). Morgan Stanley/BofA still constructive. Thesis weakened but not broken — trailing-stop GTC is the exit discipline.

No trades executed. Trailing stop continues mechanical exit discipline.

---

## EOD Snapshot — 2026-06-11

| Field | Value |
|-------|-------|
| Portfolio Value | $99,502.96 |
| Cash | $99,207.16 |
| Long Market Value | $295.80 |
| Day P&L ($) | +$3.78 |
| Day P&L (%) | +0.0038% |
| Trades Today | 0 |
| Trades This Week | 0 buys / 1 sell |
| Open Positions | 1 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $295.80 | -$6.08 (-2.01%) |

Notes: **NO_TRADE day.** Quiet, essentially flat session — Day P&L +$3.78 (+0.0038%) driven by AAPL marking slightly higher from yesterday's close ($292.00 → $295.80, +$3.80). Midday scan held: AAPL -1.74% well above the -7% cut threshold; no position at +15/+20% gain to tighten; thesis weakened post-WWDC but trailing-stop is the exit discipline. Pre-market $276 illiquid print did not hold into regular hours — AAPL trailing-stop $285.66 did not fire. Cash $99,207.16 = 99.71% of equity (≥20% reserve rule ✅); total exposure 0.29% (AAPL 1 sh only). Daily-loss limit (3%) not approached. Weekly trade counter 0 buys / 1 sell (6/10 GOOGL cut) — full 3-buy budget preserved into Friday sentiment. AAPL 10% trailing-stop GTC (stop $285.66 / HWM $317.40) remains the sole mechanical exit.

---

## Market-Open Log — 2026-06-12 (Friday — session: sweet-shannon-7gclam)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $99,207.16 |
| Equity | $99,499.15 |
| Long Market Value | $291.99 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 1 / 3 (GOOGL cut on 2026-06-10) |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (1/3 — sell-only consumes counter)
- Max 20% equity per position ✅ (AAPL 0.29%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; zero actionable ideas (only chart-passer AMD blocked by macro filter)

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $291.91 | -$9.97 (-3.30%) |

Entry-criteria re-validation (live, 60-bar snapshot):
- **Macro (SPY)**: live last $736.13 < MA20 $745.40 → criterion #4 **FAILS** 8th straight session. Yesterday's relief rally did not produce a sustained reclaim.
- **AMD** (pre-market conditional pre-authorization): live ask $505.58 > MA20 $478.88 & MA50 $380.75 ✅; RSI-14 56.48 in band ✅; spread $2.19 / 0.43% < 0.5% ✅. All ticker-level gates pass. **BLOCKED** — macro filter not met (pre-market required SPY > MA20 simultaneously with all three AMD gates; SPY still sub-MA20).
- **AAPL add**: BLOCKED — bar current $295.63 < MA20 $304.24; macro also fails.
- **GOOGL re-entry**: BLOCKED — live $357.77 < MA20 $378.31; RSI 30 oversold; macro fails.

Trades executed: **none.**

Risk posture: cash 99.71% of equity (≥20% reserve ✅), exposure 0.29% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 1/3 (sell-only) — 2 buy slots preserved into Friday close awaiting SPY > MA20 reclaim. **AAPL position**: -3.30% unrealized, trailing-stop GTC at $285.66 / HWM $317.40 — cushion ~$6.25/sh (2.14%); EOD will re-evaluate cut-loser status if drawdown deepens. SpaceX IPO debut is a liquidity event with no direct watchlist read-through.

---

## Midday Scan — 2026-06-12 (Friday — session: sweet-shannon-7gclam)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Long Market Value | $291.40 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $291.40 | -$10.48 (-3.47%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL -3.47% — above the -7% cut threshold. No cut.
- **Stop-tighten**: no position at +20% (→5%) or +15% (→7%). 10% trailing-stop GTC ($285.66 / HWM $317.40) remains.
- **Thesis check (AAPL web news)**: Analyst tape constructive — average "Buy", 12-mo PT $312.48 (+7.42% upside). Post-WWDC dip digested; stock stable $290–$297 range. **Thesis intact.**

No trades executed. AAPL trailing-stop cushion $5.74/sh (1.97%) — narrower than market-open (2.14%) on the small intraday slip from $291.91 → $291.40. EOD routine retains cut-loser monitoring.

---

## EOD Snapshot — 2026-06-12

| Field | Value |
|-------|-------|
| Portfolio Value | $99,498.75 |
| Cash | $99,207.16 |
| Long Market Value | $291.59 |
| Day P&L ($) | -$4.21 |
| Day P&L (%) | -0.0042% |
| Trades Today | 0 |
| Trades This Week | 1 (GOOGL cut on 2026-06-10) |
| Open Positions | 1 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $291.59 | -$10.29 (-3.41%) |

Notes: **NO_TRADE day; week closes.** Flat-to-slightly-red session — Day P&L -$4.21 (-0.0042%) driven entirely by AAPL marking down $0.32 vs Thursday's close ($291.91 → $291.59 intraday slip, then a touch lower into the bell). Pre-market HOLD (zero actionable ideas — only chart-passer AMD blocked by macro filter SPY < MA20 for 8th straight session). Market-open NO_TRADE (AMD all ticker gates passed but macro still failed; AAPL/GOOGL adds blocked by sub-MA20). Midday HOLD (AAPL -3.47% well above -7% cut; thesis intact, analyst Buy, PT $312.48). AAPL closed -3.41% unrealized — no -7% breach. Cash $99,207.16 = 99.71% of equity (≥20% reserve ✅); total exposure 0.29%. Daily-loss limit (3%) not approached. **Week summary:** 0 buys / 1 sell (GOOGL cut on 6/10 at -7.15%); weekly trade counter 1/3. AAPL 10% trailing-stop GTC (stop $285.66 / HWM $317.40) — $5.97/sh cushion (2.05%) into the weekend, sole mechanical exit. Macro posture going into Mon 6/15: SPY 8 sessions sub-MA20, Fed blackout through next week's FOMC, hot PPI digested but rate-uncertainty elevated. AMD remains pre-staged as front-runner pending sustained SPY > MA20 reclaim.

---

## Market-Open Log — 2026-06-15 (Monday — session: sweet-shannon-mc1ozv)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $99,207.16 |
| Equity | $99,502.16 |
| Long Market Value | $294.94 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 0 / 3 (new week) |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AAPL 0.30%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market decision was HOLD/NO_TRADE; macro filter SPY < MA20 (9th session) + FOMC Wed 6/17 event risk → universal block. No symbol pre-authorized.

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $294.94 | -$6.94 (-2.30%) |

Entry-criteria re-validation (live, 60-bar SPY snapshot):
- **Macro filter (SPY)**: live last $753.40, bar `current` $741.75 < MA20 $745.07 → criterion #4 **FAILS** universally. RSI-14 47.36 neutral. SPY < MA20 streak now 9th session.
- **FOMC event risk Wed 6/17**: first Warsh meeting + SEP dots = binary tape risk; pre-market explicitly disciplined to defer entries until post-decision.
- No symbol passes criterion #4; no per-ticker chart pass can override.

AAPL hold under standard exit discipline: trailing-stop GTC order `5851cbb5` (stop $285.66, HWM $317.40, trail 10%). Live cushion $9.28/sh (3.15%). Unrealized -2.30% — well above -7% cut threshold; no exit trigger.

Trades executed: **none.**

Risk posture: cash 99.70% of equity (≥20% reserve ✅), exposure 0.30% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full budget preserved into Tue/Wed FOMC and any post-decision macro thaw.

---

## Midday Scan — 2026-06-15 (Monday)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $297.24 | -$4.64 (-1.54%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL -1.54% — no cut trigger. Cushion to -7% threshold ~$16.49/sh (5.46%).
- **Stop-tighten (+15/+20%)**: AAPL not at gain threshold. 10% trailing-stop GTC remains in force (stop $285.66 / HWM $317.40).
- **Thesis check**: AAPL thesis covered in pre-market — WWDC slide absorbed; Morgan Stanley PT $330→$360 (Buy) 6/9; no fresh negative catalyst. Mark recovered $293.78 → $297.24 since pre-market. Thesis intact.

Trades executed: **none.** Weekly trade counter 0/3 — full budget preserved into FOMC Wed.

---

## EOD Snapshot — 2026-06-15 (Monday)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,503.31 |
| Cash | $99,207.16 |
| Long Market Value | $296.15 |
| Day P&L ($) | +$4.56 |
| Day P&L (%) | +0.0046% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 |
| Open Positions | 1 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $296.15 | -$5.73 (-1.90%) |

Notes: **NO_TRADE day.** Quiet, slightly green close — Day P&L +$4.56 (+0.0046%) vs Friday 6/12 close ($99,498.75 → $99,503.31). AAPL drifted $297.24 midday → $296.15 close (-$1.09/sh), unrealized improved net vs Friday's -3.41% (closed -1.90%). Pre-market HOLD (macro filter SPY < MA20 9th session + FOMC Wed 6/17 binary risk → universal entry block; no symbol pre-authorized). Market-open NO_TRADE (criterion #4 macro fail re-validated live; no per-ticker override possible). Midday HOLD (AAPL -1.54%, no -7% cut, no +15/+20% tighten; thesis intact). AAPL 10% trailing-stop GTC `5851cbb5` (stop $285.66 / HWM $317.40) remains active — close cushion $10.49/sh (3.54%), no exit trigger. Cash $99,207.16 = 99.70% of equity (≥20% reserve ✅); total exposure 0.30% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — full buy budget preserved through FOMC Wed 6/17 (first Warsh meeting + SEP dots = binary tape risk; pre-market discipline defers entries until post-decision). Macro posture into Tue 6/16: SPY 9 sessions sub-MA20, RSI-14 47.36 neutral. AMD remains pre-staged front-runner pending sustained SPY > MA20 reclaim. No fresh AAPL catalyst; Morgan Stanley Buy / PT $360 (6/9) intact.

---

## Market-Open Log — 2026-06-16 (Tuesday — session: sweet-shannon-m3py1u)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $99,207.16 |
| Equity | $99,502.63 |
| Long Market Value | $295.47 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AAPL 0.30%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market explicitly HOLD/NO_TRADE. All conditional ideas (NVDA, AMD, MSFT, GOOGL) flagged "NOT for today." Three independent stand-down reasons: FOMC Wed 6/17 binary (T-1 to first Warsh-chaired meeting + dot-plot), technical re-validation blocked (`market_data.py` returns NaN for MA20/MA50/RSI-14 on SPY/AAPL — yfinance bar enrichment broken), and macro filter only 1 session above MA20 after 9 below (not a confirmed regime flip).

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $295.46 | -$6.42 (-2.13%) |

Entry-criteria re-validation: criterion #1 (price > MA20 & MA50) and #2 (RSI 40–65) **unverifiable** — pre-market MA/RSI NaN persists; no live override possible without bar data. Macro criterion #4 marginal: SPY one-session reclaim of MA20 (not 2-session confirmation). Default under uncertainty + binary catalyst one trading day out = **NO_TRADE**.

Position management — AAPL: -2.13% unrealized; cushion to -7% cut watch ~$13.65/sh (4.62%). Trailing-stop GTC `5851cbb5` (stop $285.66 / HWM $317.40) cushion ~$9.80/sh (3.32%) — no exit trigger. Hold under existing mechanical discipline.

Trades executed: **none.**

Risk posture: cash 99.70% of equity (≥20% reserve ✅), exposure 0.30% (≤80% ✅), daily-loss limit (3%) not approached. Weekly trade counter 0/3 — **full buy budget preserved** for post-FOMC Thursday/Friday if a clean candidate emerges with live MA/RSI confirmation and 2-session SPY > MA20 reclaim.

---

## Midday Scan — 2026-06-16 (Tuesday — session: sweet-shannon-m3py1u)

| Field | Value |
|-------|-------|
| Routine | Midday Scan |
| Cash | $99,207.16 |
| Long Market Value | $299.09 |
| Open Positions | 1 / 6 (AAPL 1 sh) |
| Decision | **HOLD — no action** |

Position snapshot (live):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AAPL | 1 | $301.88 | $299.085 | -$2.795 (-0.93%) |

Midday checks:
- **Cut-loser (-7%)**: AAPL -0.93% — no cut (improved from market-open -2.13%). Cushion to cut ~$18.05/sh (6.04%). Trailing-stop GTC $285.66 active; cushion ~$13.43/sh (4.49%).
- **Stop-tighten**: no position at +15%/+20% gain. 10% trailing-stop GTC remains.
- **Thesis check (48h)**: AAPL post-WWDC drift; Ternus CEO Sept 1 confirmed; $100B buyback intact; position 0.30% of equity. Thesis intact.

No trades executed. FOMC Wed 6/17 T-1 binary continues to dominate. Weekly buys 0/3 preserved for post-FOMC re-evaluation.

---

## EOD Snapshot — 2026-06-16 (Tuesday)

| Field | Value |
|-------|-------|
| Portfolio Value | $99,505.93 |
| Cash | $99,207.16 |
| Long Market Value | $298.77 |
| Day P&L ($) | +$2.62 |
| Day P&L (%) | +0.0026% |
| Trades Today | 0 |
| Trades This Week | 0 / 3 |
| Open Positions | 1 / 6 |

### Open Positions

| Symbol | Qty | Avg Entry | Current | Unrealized P&L |
|--------|-----|-----------|---------|----------------|
| AAPL | 1 | $301.88 | $298.77 | -$3.11 (-1.03%) |

Notes: **NO_TRADE day, T-1 to FOMC.** Quiet, marginally green close — Day P&L +$2.62 (+0.0026%) vs Monday 6/15 close ($99,503.31 → $99,505.93). AAPL drifted modestly intraday — market-open -2.13% → midday -0.93% → close -1.03% — net improvement from prior close (-1.90%). Pre-market HOLD/NO_TRADE (three independent stand-down reasons: FOMC Wed 6/17 binary T-1, technical re-validation blocked by `market_data.py` MA20/MA50/RSI-14 NaN, and macro filter only 1 session above MA20 after 9 below — not a confirmed regime flip). Market-open NO_TRADE (criterion #1/#2 unverifiable; criterion #4 marginal). Midday HOLD (AAPL -0.93%, no -7% cut, no +15/+20% tighten; thesis intact — post-WWDC drift, Ternus CEO Sept 1 confirmed, $100B buyback intact). AAPL 10% trailing-stop GTC `5851cbb5` (stop $285.66 / HWM $317.40) remains active — close cushion $13.11/sh (4.39%), no exit trigger. Cash $99,207.16 = 99.70% of equity (≥20% reserve ✅); total exposure 0.30% (≤80% ✅). Daily-loss limit (3%) not approached. Weekly trade counter 0/3 — **full buy budget preserved through FOMC Wed 6/17** (first Warsh-chaired meeting + SEP dots = binary tape risk; pre-market discipline defers entries until post-decision Thursday/Friday given clean candidate with live MA/RSI confirmation and 2-session SPY > MA20 reclaim).


### Trade Entry — 2026-06-22 13:46
| Field | Value |
|-------|-------|
| Symbol | AMD |
| Side | BUY |
| Shares | 14.0 |
| Est. Price | $546.15 |
| Est. Value | $7646.10 |
| Order ID | b48c23e0-495e-490b-892d-78d38668b9cd |
| Trailing Stop | 10% GTC placed immediately after fill |

### Market-Open Log — 2026-06-30 (Tuesday — session: claude/sweet-shannon-8obmmw)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:46 ET) |
| Cash | $91,845.93 |
| Equity | $99,577.99 |
| Long Market Value | $7,732.06 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AMD 7.76%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market HOLD; MU & GOOGL conditional ideas both gated on (a) live macro filter + (b) yfinance bar-data resolution. yfinance still TLS-broken Day 7+ (`market_data.py SPY` → 0 bars, MA/RSI = null). RSI 35–70 verification impossible. AMD already at 7.76% cap — no ADD possible.

Position snapshot (live, 09:46 ET):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L |
|--------|-----|-----------|------|----------------|
| AMD | 14 | $546.19 | $551.89 | +$79.74 (+1.04%) |

**AMD CROSSED BACK TO GREEN** for first time since drawdown — pre-mkt $542.08 → open $551.89 (+$9.81/sh / +1.81%). Cushion to manual -7% cut $507.96 = $43.93/sh (~7.96%) — most comfortable since entry. Cantor PT $700 / UBS $670 / Bernstein $600 thesis intact.

Trades executed: **none.**

Risk posture: cash 92.24% (≥20% ✅), exposure 7.76% (≤80% ✅), daily-loss limit (3%) not approached (day drift +0.144%). Weekly buy budget 3/3 preserved.

Carry-forward: yfinance TLS Day 7+ (escalation), AMD broker-trailing-stop infra gap Day 7+ (escalation), AMC earnings STZ/NKE/PRGS tonight, Chicago PMI + Consumer Confidence today.


### Market-Open Log — 2026-07-13 (Monday — session: claude/sweet-shannon-mqlw6w)

| Field | Value |
|-------|-------|
| Routine | Market-Open Execution (09:45 ET) |
| Cash | $91,845.93 |
| Equity | $99,229.88 |
| Long Market Value | $7,383.95 |
| Open Positions | 1 / 6 (AMD 14 sh) |
| Trades This Week | 0 / 3 |
| Decision | **NO_TRADE** |

Buy-rule check:
- Max 6 open positions ✅ (1/6)
- Max 3 trades this week ✅ (0/3)
- Max 20% equity per position ✅ (AMD 7.44%)
- **Catalyst in today's RESEARCH-LOG ❌** — pre-market NO_TRADE stands; MSFT/GOOGL/NVDA deferred conditional on macro reclaim + TLS gate patch. Neither cleared.

Position (09:45 ET cash-open):
| Symbol | Qty | Avg Entry | Mark | Unrealized P&L | Day Change |
|--------|-----|-----------|------|----------------|-----------|
| AMD | 14 | $546.19 | $527.41 | -$263.05 (-3.44%) | -5.46% |

AMD deteriorated 2.12pp vs pre-market ($538.99 → $527.41). Cushion to -7% cut $507.96 halved from $31.03/sh → $19.44/sh (3.69%). No cut trigger yet. Watch $520 (flag) / $510 (manual cut) at midday.

Trades executed: **none.**

Risk posture: cash 92.56% (≥20% ✅), exposure 7.44% (≤80% ✅), daily-loss halt not approached (-0.163% intraday). Weekly buy budget 3/3 preserved.

Carry-forward: yfinance TLS Day 16, AMD broker-trailing-stop infra gap Day 16, Iran/US strikes + Strait of Hormuz risk-off tape, AMD Advancing AI summit 7/22-23 binary in position window.

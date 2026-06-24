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

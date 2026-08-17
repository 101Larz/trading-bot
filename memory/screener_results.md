# Nightly Screener Results

**Run:** 2026-08-17 02:08 CEST (Mon overnight, target trading day 2026-08-17)
**Status:** FAILED — required skill still not available in this environment
**Universe:** 95 tickers (none screened)
**Phase B survivors (Markov):** 0 (phase not run)
**Phase C survivors (Momentum):** 0 (phase not run)
**Phase D survivors (Technical):** 0 (phase not run)

---

## Failure summary

The nightly screener could not run Phase A. The `markov-hedge-fund-method`
skill (`uv run python -m markov_hedge_fund_method.run ...`) is neither
installed on the routine's container nor enabled on the account. This is
the **second consecutive firing** to fail for exactly the same reason —
the first firing on 2026-08-14 (Fri) also failed and pre-market that day
(2026-08-14) then ran under the NO_TRADE fallback because Markov gates
could not be evaluated. Nothing has changed in the intervening 3 calendar
days (weekend + tonight).

Re-checked this run:

- `~/.claude/skills/markov-hedge-fund-method/` — does not exist
- `~/.claude/skills/synced/` — contains only `docx`, `morning`, `pdf`,
  `pptx`, `skill-creator`, `xlsx` (per `manifest.json`, updated 2026-08-14)
- Account skill listing (`ListSkills`) filtered on "markov" — 0 results
- Account skill search (`SearchSkills`) for "markov", "hedge-fund-method",
  "markov-hedge-fund" — 0 results
- Filesystem-wide search for any `*markov*` file or directory (both
  `/home/user/trading-bot/` and `/`) — no matches
- `/home/user/trading-bot/scripts/` — contains only `backtest.py`,
  `journal.py`, `market_data.py`, `notify.py`, `research.py`, `risk.py`,
  `trade.py`; no local Markov implementation

Without Regime, Markov Signal, Stat Bull%, and walk-forward Sharpe
values, none of the four Phase B gates from `memory/strategy.md` can be
evaluated, so no ranked candidate list can be produced.

The routine itself was introduced in commit `573c5b8` (2026-08-13) and
has now fired twice; both firings have failed on Phase A for the same
missing-skill reason. The skill dependency remains unverified.

## Instruction for the 09:00 AM ET pre-market routine (2026-08-17)

**Do NOT trust an empty Top 10 table below** — it means the screen never
ran, not that no candidates qualified.

Two options, in order of preference:

1. **If the `markov-hedge-fund-method` skill has been installed by the
   time pre-market runs** (check `~/.claude/skills/`, `~/.claude/skills/
   synced/manifest.json`, and account skills again), run the emergency
   inline Phase A–E screen per pre-market Step 3B-1 fallback and proceed
   normally.

2. **If the skill is still unavailable**, treat today as a NO_TRADE day
   for new buys per CLAUDE.md ("When uncertain, the default action is
   NO_TRADE"). Continue to manage the existing NVDA position under its
   normal exit rules — per last EOD heartbeat (2026-08-14): min-hold
   expires today (Mon 2026-08-17); pre-earnings 5-day exit window opens
   Tue 2026-08-19 ahead of the Q2 earnings date 2026-08-26; NVDA
   trailing-stop GTC $193.137 (HWM $227.22).

Do not degrade the strategy to a technical-only screen without user
approval — the strategy documented in `memory/strategy.md` explicitly
requires all four Markov gates to pass before momentum/technical filters
are applied.

---

## Top 10 Candidates (ranked by Sharpe)

| Rank | Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | RSI | MA Alignment | Momentum 1M |
|------|--------|--------|---------------|------------|--------|-----|--------------|-------------|
| —    | —      | —      | —             | —          | —      | —   | —            | —           |

(No rows — screener did not run.)

---

## Full Phase B+C Pass List (all Markov+Momentum qualifiers, unsorted)

| Ticker | Regime | Markov Signal | Stat Bull% | Sharpe | Momentum 1M | RSI | Tech Gate |
|--------|--------|---------------|------------|--------|-------------|-----|-----------|
| —      | —      | —             | —          | —      | —           | —   | —         |

---

## Phase B Failures (Markov filter — do not trade today)

Not evaluated (skill unavailable).

## Phase C Failures (Momentum filter)

Not evaluated (skill unavailable).

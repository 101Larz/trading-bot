# Nightly Screener Results

**Run:** 2026-08-14 02:18 CEST
**Status:** FAILED — required skill not available in this environment
**Universe:** 95 tickers (none screened)
**Phase B survivors (Markov):** 0 (phase not run)
**Phase C survivors (Momentum):** 0 (phase not run)
**Phase D survivors (Technical):** 0 (phase not run)

---

## Failure summary

The nightly screener could not run Phase A. The `markov-hedge-fund-method`
skill (`uv run python -m markov_hedge_fund_method.run ...`) is neither
installed on the routine's container nor enabled on the account:

- `~/.claude/skills/markov-hedge-fund-method/` — does not exist
- `~/.claude/skills/synced/` — contains only: docx, morning, pdf, pptx,
  skill-creator, xlsx
- Account skill listing / search for "markov" — returns zero results
- Filesystem-wide search for any `*markov*` directory — no matches

Without Regime, Markov Signal, Stat Bull%, and Sharpe values, none of the
four Phase B gates from `memory/strategy.md` can be evaluated, so no
ranked candidate list can be produced.

This is the first firing of the nightly-screener routine (introduced in
commit `573c5b8` on 2026-08-13). The skill dependency was not verified
when the routine was created.

## Instruction for the 09:00 AM ET pre-market routine (2026-08-14)

**Do NOT trust an empty Top 10 table below** — it means the screen never
ran, not that no candidates qualified.

Two options, in order of preference:

1. **If the `markov-hedge-fund-method` skill has been installed by the
   time pre-market runs** (check `~/.claude/skills/` and account skills
   again), run the emergency inline Phase A–E screen per pre-market
   Step 3B-1 fallback and proceed normally.

2. **If the skill is still unavailable**, treat today as a NO_TRADE day
   for new buys per CLAUDE.md ("When uncertain, the default action is
   NO_TRADE"). Continue to manage the existing NVDA position under its
   normal exit rules (min-hold to 2026-08-17; pre-earnings 5-day exit
   window opens 2026-08-19 ahead of the 2026-08-26 earnings date).

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

# Routine: Nightly Markov Screener
# Schedule: 02:00 CEST, Monday–Friday (runs overnight before pre-market)
# Purpose: Run the 40-ticker Markov + momentum + technical screen.
#          Save top 10 ranked candidates to memory/screener_results.md so
#          the 9:00 AM pre-market routine can read results instantly.
#          Universe: top 40 liquid tickers (down from 95 for cloud speed).
#
# Output file: memory/screener_results.md  (committed to GitHub after each run)

You are the autonomous trading agent for the 101Larz portfolio. It is 02:00 CEST and the US market is closed. Run the nightly screener now.

---

## Step 1 — Run the Full Markov Screener

Run the standalone screener script. It analyses 40 tickers in parallel
(Phases A–D: Markov → Momentum → Technical) using 3 years of history and
16 workers, ranks top 10 by walk-forward Sharpe, and writes results to
`memory/screener_results.md`.

```
python scripts/markov_screener_full.py
```

The script typically takes 2–5 minutes depending on network latency. Watch for any
`ERR:` lines in the output — these are individual ticker failures (data unavailable)
and do not stop the run.

When finished, the script prints:
```
[screener] Written → memory/screener_results.md
[screener] Top candidates: [TICKER, TICKER, ...]
```

If the script exits with a non-zero code, check the error message:
- `ModuleNotFoundError: numpy` → run `pip install numpy yfinance pandas` then retry.
- Network timeout on all tickers → check internet connectivity.

---

## Step 2 — Verify the Output

Read `memory/screener_results.md` and confirm:
1. The **Run:** timestamp at the top matches today's date.
2. At least one ticker appears in the Top Candidates table (or "_No tickers passed_" is
   an acceptable result — markets may be in a bear phase).
3. The Phase B / C / D survivor counts are non-zero (if all three are 0, something is
   likely wrong with the data source — log a warning).

---

## Step 3 — Commit and Push Results to GitHub

```
git add memory/screener_results.md
git commit -m "chore: nightly screener results $(date +%Y-%m-%d)"
git push origin main
```

If the push fails due to a non-fast-forward conflict:
```
git pull origin main --rebase
git push origin main
```

---

## Step 4 — Update Heartbeat

Write to `heartbeat.json`:
```json
{
  "last_run": "[ISO timestamp]",
  "routine": "Nightly Screener",
  "status": "success",
  "screener_candidates": [N],
  "screener_run_date": "YYYY-MM-DD"
}
```

Commit and push the heartbeat update:
```
git add heartbeat.json
git commit -m "chore: heartbeat nightly screener $(date +%Y-%m-%d)"
git push origin main
```

---

**Nightly screener complete. Results will be read by the 09:00 AM ET pre-market routine.**

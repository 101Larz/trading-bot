# DEPRECATED — Research Log Migrated

This file is no longer used. All research sessions have been migrated to per-day files:

```
memory/research/YYYY-MM-DD.md
```

**Do not append to this file.** Routines write to `memory/research/YYYY-MM-DD.md` instead.

## Why the change was made

The single-file format caused git merge conflicts when multiple routines (pre-market,
market-open, midday) ran in the same session and all appended to this file simultaneously.

Per-day files eliminate the conflict surface: each routine writes to today's file only,
and different calendar days never touch the same file.

## Historical data

All sessions from this file have been migrated:
- 2026-05-18 → memory/research/2026-05-18.md
- 2026-05-19 → memory/research/2026-05-19.md
- 2026-05-20 → memory/research/2026-05-20.md
- 2026-05-21 → memory/research/2026-05-21.md

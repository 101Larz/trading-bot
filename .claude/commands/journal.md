# /journal — View or Create Journal Entries

View today's journal, a specific date's journal, or initialize a new one.

## Usage
- `/journal` — show today's journal
- `/journal 2026-05-15` — show journal for a specific date
- `/journal init` — initialize today's journal if it doesn't exist
- `/journal week` — show this week's journal summary

## Steps

### `/journal` or `/journal [date]`
1. Determine the target date from `$ARGUMENTS` or use today.
2. Read the file: `journal/[date].md`
3. If it doesn't exist: "No journal found for [date]. Run `/journal init` to create it."
4. Display the full journal content cleanly formatted.

### `/journal init`
1. Run: `python scripts/journal.py init`
2. Pull current account state: `python scripts/research.py account`
3. Confirm file created and show the path.

### `/journal week`
1. Determine current week's Monday through Friday dates.
2. Read each day's journal file that exists.
3. Compile a weekly summary:
   - Total trades across the week
   - Total realized P&L
   - Key decisions and outcomes
   - Any lessons added to `memory/lessons.md`
4. Display the weekly summary.

### `/journal [date] reflection`
1. Read `journal/[date].md`
2. If End-of-Day Reflection is blank, prompt: "What reflection would you like to add?"
3. Accept input via `$ARGUMENTS` remainder or ask Claude to generate it from today's trades.
4. Append to the journal using `python scripts/journal.py`.

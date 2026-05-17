# Lessons Learned

Agent appends new lessons here after significant trades or market events. Read before every session.

---

## Format

Each lesson follows this template:

```
### YYYY-MM-DD — [Brief Title]
**What happened:** [Describe the trade or event]
**What went wrong / right:** [Root cause or insight]
**Rule change or reminder:** [What to do differently, or confirm what to keep doing]
```

---

## Lessons

*(No lessons yet — bot has not started trading. First lesson will appear after the first closed trade or risk event.)*

---

## Recurring Reminders

- Always check `heartbeat.json` before trading. If the last routine failed, investigate first.
- Never trade in the first 5 minutes after open (9:30–9:35 AM ET) — spreads are wide and volatility is elevated.
- Earnings weeks are high-risk. Exit positions at least 2 days before scheduled earnings unless thesis explicitly includes an earnings catalyst.
- When SPY is down >1% pre-market, reduce position targets by 50% for that day.
- A journal entry is mandatory even on days with zero trades.

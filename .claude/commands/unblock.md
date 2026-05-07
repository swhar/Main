# /unblock — Diagnose and Break a Stuck Task

Usage: `/unblock <task, decision, or project that's stalled>`

A fast diagnostic for when something has been sitting on the list too long. Surfaces the real reason it's stuck — almost never the stated reason — and produces one concrete next move.

## Steps

1. Read `memory/tasks.md` to see how long the item has been sitting and what other items it's tangled with.
2. If the blocked item is project-scoped, read the relevant `projects/<name>.md` for context and prior next actions.
3. Read `memory/learnings.md` for any prior pattern around the same kind of stuck (procrastination type, dependency type, decision-avoidance type).
4. Ask the diagnostic ladder, one question at a time, stopping when the real blocker surfaces:
   - Is this blocked on information, a decision, another person, energy, or fear?
   - If you had to ship something on it in the next 30 minutes, what would you ship?
   - What would have to be true for this to feel easy?
   - Is this still worth doing at all? (Sometimes the unblock is a kill.)
5. Classify the blocker type: **information / decision / dependency / energy / fear / wrong-task**.
6. Match the blocker to a move (use `prompts/elite-techniques.md` frameworks where they fit — e.g., 10/10/10 for fear, Reversibility Test for decision-paralysis):
   - Information → smallest research spike that resolves it
   - Decision → run `/strategy` or 10/10/10
   - Dependency → the specific ask, to the specific person, today
   - Energy → shrink the next action to <10 minutes or schedule for peak energy
   - Fear → name the worst case, ask if it's actually survivable
   - Wrong-task → kill it and explain why
7. Produce the output:

---

## Unblock: [Task] — 2026-05-07

**Stated blocker:** [What the user originally said]
**Real blocker:** [What surfaced — type: information / decision / dependency / energy / fear / wrong-task]

**Why it's actually stuck**
> [One sentence — the honest version]

**The move (next 24 hours)**
> [One concrete action, scoped small enough to actually happen]

**If that doesn't work**
> [Backup move, or escalation path]

**Pattern check**
- [Is this the same kind of stuck the user has hit before? If yes, flag the pattern from `memory/learnings.md`]

---

8. Offer to update `memory/tasks.md` with the new next action via `/remember`, and to log the pattern to `memory/learnings.md` if it's a recurring one.
9. Ask: "Want to schedule this move into today, or hand it to `/plan-day` for tomorrow?"

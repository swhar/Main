# /retro — Project or Initiative Retrospective

Usage: `/retro <project, initiative, or event>`

Runs a structured retrospective on a finished or milestone-reached effort. Different from `/weekly-review` — this is scoped to one thing, not a time window.

## Steps

1. Read `memory/profile.md` for values and how this effort connects to broader goals.
2. Read the relevant `projects/<name>.md` (if it exists) for original intent and history.
3. Read `memory/decisions.md` for any decisions tied to this effort, to compare intent vs. outcome.
4. Restate the scope of the retro: what specifically is being reviewed, and what's the outcome being judged?
5. Walk the user through these prompts in order, one at a time:
   - What was the original goal or intended outcome?
   - What actually happened? (facts, not interpretations)
   - What worked — and would you do again?
   - What didn't work — and why? (root cause, not symptom)
   - What surprised you?
   - If you ran this again from scratch, what would you change?
6. Apply the Pre-mortem framework in reverse from `prompts/elite-techniques.md`: identify the failure modes that actually showed up, and which ones you missed in advance.
7. Produce the retro output:

---

## Retro: [Effort Name] — 2026-05-07

**Scope:** [What was reviewed]
**Outcome vs. intent:** [Hit / Missed / Mixed — one sentence]

**What worked**
- [Specific, repeatable practice or condition]

**What didn't work**
- [Specific issue — root cause, not symptom]

**Surprises**
- [What you didn't see coming]

**Top 3 lessons**
1. [Generalizable insight, not just a fact about this project]
2. [Lesson]
3. [Lesson]

**Changes for next time**
- [Concrete behavior or process change]

**Open threads**
- [Anything unresolved that should become a task or decision]

---

8. Offer to save the top lesson to `memory/learnings.md` and any open threads to `memory/tasks.md` via `/remember`.
9. Ask: "Should I archive the project file or keep it active for follow-on work?"

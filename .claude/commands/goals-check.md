# /goals-check — Goal Alignment Audit

Run monthly (or whenever something feels off) to check that current activity actually serves stated goals — and to update goals that have quietly drifted.

## Steps

1. Read `memory/profile.md` to list current stated goals and focus areas.
2. Read `memory/tasks.md` and tag each active task with which goal it serves. Flag any task that doesn't trace to a goal.
3. Skim each active file in `projects/` and tag each project with which goal it serves. Flag any project that doesn't trace.
4. Read `memory/decisions.md` (last 30 days) — note any decision that quietly contradicted a stated goal.
5. Apply Goal Decomposition from `prompts/elite-techniques.md` in reverse: from current activity, infer the user's *revealed* goals and compare to *stated* goals.
6. Ask the user to react to the gap before producing output:
   - "Are the stated goals still right, or has reality moved?"
   - "Is there a goal you're acting on that isn't written down?"
7. Produce the audit:

---

## Goals Check — 2026-05-07

**Stated goals (from `memory/profile.md`)**
1. [Goal]
2. [Goal]
3. [Goal]

**Revealed goals (inferred from tasks/projects/decisions)**
1. [What activity actually suggests is the priority]
2. [...]

**Alignment**
- Strong alignment: [Goal — supported by which tasks/projects]
- Weak alignment: [Goal — under-resourced, despite being stated]
- Drift: [Activity that serves no stated goal]
- Hidden goal: [Activity pattern that suggests an unstated goal worth naming]

**Orphan tasks / projects**
- [Item — not tied to any goal — keep, kill, or attach to a goal?]

**Recommendation**
> [Either: update profile to match reality, or re-anchor activity to stated goals. Pick one.]

---

8. Offer to update `memory/profile.md` (goal additions, removals, rephrasings) via `/remember`.
9. Ask: "Want to run `/weekly-review` next to act on the orphan items, or stop here?"

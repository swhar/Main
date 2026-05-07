# /project-new — Spin Up a New Project File

Usage: `/project-new <project name>`

Creates a structured `projects/<name>.md` file so a new effort starts with goals, scope, and a clear definition of done — not a blank page.

## Steps

1. Read `memory/profile.md` to confirm the project ties to a current goal or focus area; if it doesn't, flag that and ask whether it should.
2. Read existing files in `projects/` to avoid duplication and to mirror the naming and structure conventions already in use.
3. Ask the user the intake questions one at a time:
   - What's the outcome you want from this project (in one sentence)?
   - Which goal in `memory/profile.md` does it serve?
   - What does "done" look like — concretely?
   - Timeline / target completion?
   - Top constraint (time, money, energy, dependency)?
   - First concrete next action?
4. Apply Goal Decomposition from `prompts/elite-techniques.md`: big goal → 3-month milestone → first-week outcome.
5. Run a 60-second mini pre-mortem: ask "What's the most likely way this stalls?" and capture the answer.
6. Draft the project file at `projects/<slugified-name>.md` using the template below, then show it to the user for approval before writing.
7. Once approved, write the file and add the first concrete next action to `memory/tasks.md` via `/remember`.

---

## Project: [Name]

**Created:** 2026-05-07
**Status:** Active
**Owner:** [User]

**Outcome (one sentence)**
> [What success looks like]

**Goal served**
- [Link to goal in `memory/profile.md`]

**Definition of done**
- [Concrete, observable criterion]
- [Concrete, observable criterion]

**Timeline**
- Target completion: [Date]
- 3-month milestone: [What should be true]
- First-week outcome: [What should be true by 2026-05-14]

**Top constraint**
- [Time / money / energy / dependency — and what it means in practice]

**Likely stall mode**
- [From mini pre-mortem]

**Next action**
- [First concrete step — added to `memory/tasks.md`]

**Log**
- 2026-05-07: Project created.

---

8. Confirm the file was written and the next action was logged. Ask: "Want to run `/pre-mortem` on this now, or save that for later?"

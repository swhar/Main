# Agent A — Slash Command Proposal

Six new slash commands scaffolded in `.claude/commands/`. All follow existing convention (no frontmatter, `# /command — Title` heading, `## Steps` numbered, fenced output template, framework references defer to `prompts/elite-techniques.md`, memory writes deferred to `/remember`).

The existing six commands cover **daily orient (`/briefing`), daily plan (`/plan-day`), one-shot decisions (`/strategy`), research (`/research`), and memory I/O (`/remember`, `/recall`)**. The gaps are: no weekly cadence, no post-hoc learning loop, no lightweight risk check, no project intake, no diagnostic for stuck items, and no goal-alignment audit. The six picks below close those gaps without overlapping each other.

## Selected commands

### 1. `/weekly-review`
- **Gap:** Daily cadence exists (`/briefing`, `/plan-day`); weekly cadence does not. Weekly is where stop-doing decisions happen.
- **When invoked:** End of week / Sunday evening.
- **Memory touched:** Reads `profile.md`, `tasks.md`, `decisions.md`, `learnings.md`, `projects/*`. Writes deferred to `/remember`.
- **Command vs. skill:** Command. It's a user-invoked structured workflow with a fixed cadence — no auto-trigger condition that a skill would detect. Agent D should skip.

### 2. `/retro`
- **Gap:** `/weekly-review` is time-scoped; nothing is scoped to a single finished effort. Retros are how generalizable lessons enter `learnings.md`.
- **When invoked:** After a project, launch, event, or milestone — independent of week boundaries.
- **Memory touched:** Reads `profile.md`, `decisions.md`, `projects/<name>.md`. Writes deferred to `/remember` (lessons → `learnings.md`, open threads → `tasks.md`).
- **Command vs. skill:** Command. User picks the moment and the scope (`<arg>`); not auto-detectable. Agent D should skip.

### 3. `/pre-mortem`
- **Gap:** `/strategy` covers full decisions; pre-mortem is one technique inside it. Promoting pre-mortem to its own command makes the lighter "stress-test before I commit" use case fast — no need to walk through the whole `/strategy` flow.
- **When invoked:** Before committing to a plan that's already mostly decided but not yet started.
- **Memory touched:** Reads `profile.md`, `decisions.md`, `learnings.md`. Writes deferred to `/remember`.
- **Command vs. skill:** Command. Explicit user trigger with an argument. Could arguably be a sub-call of `/strategy`, but the friction of running full `/strategy` for a quick risk check is real. Agent D should skip.

### 4. `/project-new`
- **Gap:** `projects/` is referenced everywhere but there's no scaffolding command. New projects get started without goal-linkage, definition of done, or first action — the three things that determine whether a project actually moves.
- **When invoked:** Whenever a new effort crosses the threshold from "idea" to "thing I'm actually doing."
- **Memory touched:** Reads `profile.md`, lists `projects/`. Writes a new file in `projects/` (this is the command's deliverable, not a memory append, so it does not go through `/remember`). First action goes to `memory/tasks.md` via `/remember`.
- **Command vs. skill:** Command. Note: this is the one command in this set that writes a file directly to `projects/`. That is appropriate because the file *is* the output, not a memory log entry — `/remember` handles single-line appends, not full-document creation. Agent D should skip.

### 5. `/unblock`
- **Gap:** Tasks that sit untouched are the highest-leverage place to apply structured thinking, but nothing in the current system targets them. The diagnostic ladder (information / decision / dependency / energy / fear / wrong-task) is well-known and well-suited to a command.
- **When invoked:** When the user notices a task has been on the list too long, or `/briefing` flags one.
- **Memory touched:** Reads `tasks.md`, `projects/<name>.md`, `learnings.md`. Writes deferred to `/remember`.
- **Command vs. skill:** Command. User picks the task to unblock — not auto-detectable without false positives. Agent D should skip.

### 6. `/goals-check`
- **Gap:** Goals in `profile.md` and current activity drift apart silently. No existing command reconciles stated goals with revealed goals (the ones implied by where time is actually going).
- **When invoked:** Monthly, or when something feels off.
- **Memory touched:** Reads `profile.md`, `tasks.md`, `decisions.md`, `projects/*`. Writes deferred to `/remember` (profile updates).
- **Command vs. skill:** Command. Cadence is user-driven; the analysis requires user reaction mid-flow (stated vs. revealed gap), which is conversational rather than automatable. Agent D should skip.

## Candidates rejected

- **`/decide`** — Redundant with `/strategy`. `/strategy` already routes by decision type to the right framework. A separate `/decide` would either duplicate or be a thinner version. Better to keep one canonical decision command.
- **`/learn`** — Redundant with `/research` (for sourced knowledge) plus `/remember` (for insights). Adding `/learn` would split the path for capturing learnings without adding a step that those two don't already cover.

## Notes for other agents

- **Agent B (`settings.json`):** No new commands need permissions or hooks beyond what existing commands use. All six commands operate on `.md` files in known directories.
- **Agent C (`memory/`):** None of these commands write directly to memory files except `/project-new`, which writes to `projects/` (a new file, not an append). All other writes are deferred to `/remember`, so memory file format changes are Agent C's call alone.
- **Agent D (`.claude/skills/`):** All six are commands, not skills. They are user-invoked structured workflows with arguments and conversational mid-flow questions, not auto-trigger conditions. None of them should be promoted to skills.

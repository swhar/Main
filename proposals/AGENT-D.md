# Agent D — Skills Proposal & Migration Rationale

This proposal introduces a `.claude/skills/` layer alongside the existing `.claude/commands/` layer. Skills coexist with commands. Original command files are untouched.

---

## Summary

**Migrated to skills (scaffolded):**
1. `research` — auto-activates on research-shaped questions
2. `strategy` — auto-activates on decision-shaped questions
3. `recall` — auto-activates when the user references their own prior context

**New skills proposed (scaffolded):**
4. `framework-picker` — suggests the right elite-techniques framework when the user is reasoning informally
5. `memory-hygiene` — prompts the user to save decision/learning/task-shaped utterances they would otherwise lose

**Kept as commands (deliberately not migrated):**
- `/briefing`, `/plan-day`, `/remember`

> **Coexistence note:** Skills and commands can both live in this repo. If after a trial period these skills behave reliably, the corresponding commands could be retired — or kept as explicit-invoke shortcuts for users who prefer typing the slash. No automatic deletion is recommended at this stage.

---

## Skill vs. Command — the heuristic

| Pattern | Use a... |
|--------|----------|
| User-typed ritual; the act of typing is part of the intent | **Command** |
| Behavior should activate based on conversational context | **Skill** |
| Needs richer reference material bundled in a directory | **Skill** |
| Argument-driven and discrete (`/foo <thing>`) | **Command** (or a skill that accepts the implicit query) |
| Ambient nudge that the user wouldn't think to invoke | **Skill** (only — a command that requires invocation can't fire) |

A skill's `description` frontmatter is the activation contract: it must be specific enough that Claude reliably fires the skill on real triggers and avoids false positives.

---

## Migration picks — justified

### `/research` → `research` skill (migrated)

- **Why migrate:** The research workflow is most valuable when it activates *before* the user has decided they need a workflow. Many research-shaped questions ("what's the latest on X", "how do people handle Y") get answered ad hoc and lose their structured-synthesis-and-save step. Auto-activation captures those.
- **Trigger design:** Pattern-based on open-ended factual/comparative phrasing ("what's the latest on", "compare X vs Y", "is it true that", "look into…"). Explicit skip rules push competing intents to `recall` (own context) or `strategy` (decision).
- **Reference handling:** Keeps the pointer to `prompts/elite-techniques.md` for the Research Workflow definition; does not duplicate framework content.

### `/strategy` → `strategy` skill (migrated)

- **Why migrate:** Decision moments are exactly the moments users *don't* invoke a workflow — they think out loud. Auto-activation on deliberation phrasing ("should I…", "torn between…", "is it worth…") catches this.
- **Trigger design:** Phrasing of deliberation, plus a stakes filter (skip trivial reversible choices). Skip rules route to `research` (gathering inputs) or `recall` (past context).
- **Reference handling:** All frameworks remain in `prompts/elite-techniques.md`; the skill body is identical to the command's `## Steps` so behavior is unchanged when the skill activates.

### `/recall` → `recall` skill (migrated)

- **Why migrate:** Users frequently *imply* recall ("how's the X project going?", "didn't I decide on Y already?") without invoking the command. A skill catches the implicit case. The original explicit command remains for deliberate retrieval.
- **Trigger design:** References to the user's own prior context — past decisions, tasks, learnings, projects, saved research. Includes the implicit-continuity pattern ("how's X going?") which the command interface couldn't catch.
- **Reference handling:** Preserves the original organized output format. Argument is implicit (the referencing phrase) when auto-activated.

---

## Commands deliberately kept (and why)

### `/briefing` — keep as command

- It's a **start-of-day ritual**. The act of typing `/briefing` is part of the intent — it's how the user signals "begin the day." Auto-activation would either fire too often (every morning message) or too rarely (require a brittle time-of-day trigger).
- No reference-bundle benefit: the workflow is short and self-contained.

### `/plan-day` — keep as command

- Same logic as `/briefing`: explicit planning ritual. The user wants to *opt in* to time-blocking mode; it should not fire because they happened to mention a task.

### `/remember` — keep as command

- It's the explicit save path the user reaches for when they *consciously* want to persist something. Auto-saving on inferred intent would be intrusive and risk corrupting memory files with low-signal entries.
- The new `memory-hygiene` skill complements (not replaces) `/remember`: it *prompts* the user to invoke `/remember` when they appear to have produced save-worthy content. The decision to save remains explicit.

---

## New skills — justified

### `framework-picker`

- **Gap it fills:** The system has rich frameworks in `prompts/elite-techniques.md`, but they only get used when the user runs `/strategy`. Most reasoning happens outside that command.
- **Behavior:** Lightly suggestive — names a matching framework and offers to walk through it. Does *not* hijack the conversation. Hands off to the `strategy` skill's output format if the user accepts.
- **Trigger design:** Reasoning-out-loud language ("on one hand… on the other", "I don't know how to evaluate this"), explicit skip when already inside a structured workflow.
- **Why a skill, not a command:** The whole point is to fire when the user *didn't* think to invoke a framework.

### `memory-hygiene`

- **Gap it fills:** `CLAUDE.md` mandates "Memory discipline: After any key decision, insight, or task update, update the relevant memory file before the session ends." In practice, decisions and learnings happen in the middle of conversations and slip past without being saved. There is no current mechanism to catch them.
- **Behavior:** Watches for decision-shaped, learning-shaped, task-shaped, or profile-shaped utterances and prompts a single low-friction save question. Hands off to `/remember` (preserving the explicit save path).
- **Trigger design:** Specific linguistic markers (listed in the skill's description frontmatter) plus a workflow-tail trigger when `/strategy`, `/research`, `/retro`, or `/weekly-review` ends without saving.
- **Why a skill, not a command:** A command can't fire without invocation. The whole value is catching the moments the user wouldn't think to act on.

---

## Trigger description design — principles applied

Each skill's `description` field follows these rules:

1. **Lead with the activation condition**, not a generic purpose statement. ("Auto-activate when the user…" rather than "This skill helps with…")
2. **Enumerate concrete trigger phrases** so the activation classifier has lexical anchors.
3. **Explicit skip clauses** to prevent overlap with sibling skills (`research` skips for decisions; `strategy` skips for fact-gathering; `recall` skips for fresh external questions).
4. **Behavioral mode hint** for ambient skills (`framework-picker` "suggests, does not impose"; `memory-hygiene` "one prompt, one chance").

This produces narrow, predictable activation rather than fuzzy "could-fire-anywhere" skills.

---

## File layout produced

```
.claude/skills/
  research/SKILL.md
  strategy/SKILL.md
  recall/SKILL.md
  framework-picker/SKILL.md
  memory-hygiene/SKILL.md
```

Each skill's body mirrors the source command's `## Steps` (where one exists), adapted for activation context (e.g., implicit query for `recall`, suggest-don't-impose framing for the new skills). Reference content lives in `prompts/elite-techniques.md` — skills point to it rather than duplicating.

---

## Recommended trial path (not executed)

1. Run skills and commands side-by-side for 1–2 weeks.
2. Track: did skills fire when expected? Did they fire when *not* expected?
3. Tune `description` frontmatter based on miss-fires.
4. Decide per-skill: retire the corresponding command, or keep as an explicit-invoke shortcut.

No commands deleted, no settings modified, no memory files touched.

---
name: memory-hygiene
description: Auto-activate when the user produces decision-shaped, learning-shaped, or task-shaped content in conversation that should be persisted but the user has not invoked /remember. Trigger on phrases like "I've decided to...", "I'm going with...", "we're going to go ahead and...", "I just realized that...", "the lesson here is...", "going forward I'll...", "note to self...", "I learned that...", or when a /strategy or /research workflow concludes without saving its result. Prompt the user to save to the right memory file (decisions.md, learnings.md, tasks.md, profile.md) and offer to do it via /remember. Skip when the user has already run /remember in the current turn, or when the content is clearly ephemeral.
---

# Memory Hygiene Skill

Activates when the user *implicitly* generates content that belongs in long-term memory but hasn't asked to save it. Closes the loop on the "Memory discipline" rule in `CLAUDE.md`.

## When to activate

Watch for these signals:

- **Decision-shaped:** "I've decided to...", "I'm going with X", "we're going ahead with...", "final answer: ..."
- **Learning-shaped:** "the lesson here is...", "I learned that...", "next time I'll...", "interesting — that means...", "I just realized..."
- **Task-shaped commitment:** "I need to do X by Friday", "adding to my list: ...", "next action is..."
- **Profile-shaped:** stated values, working preferences, goals ("I care about X", "I work best when...", "my goal this quarter is...")
- **Workflow tail:** a `/strategy`, `/research`, `/retro`, or `/weekly-review` workflow just produced a result and the user has not been asked whether to save it.

Skip activation if:
- The user has already saved this in the current turn (or used `/remember`).
- The content is clearly venting, hypothetical, or ephemeral.
- The user has explicitly declined to save during this session.

## Steps

1. Identify the entry type by language signal (decision / learning / task / profile).
2. Surface a single, low-friction prompt — not a workflow:
   > "Sounds like a [decision/learning/task] worth keeping. Save it to `memory/[file].md`? (or run `/remember`)"
3. If the user agrees:
   - Hand off to the `/remember` flow if available, OR
   - Append directly using the appropriate format from `prompts/elite-techniques.md`:
     - Decision → Decision log entry format
     - Learning → Learning entry format
     - Task → Action item format, into `memory/tasks.md`
     - Profile-shaped → confirm wording and append to the right section of `memory/profile.md`
4. If the user declines, do not nag. Drop it for the rest of the turn.
5. At the end of significant workflows (`/strategy`, `/research`, `/retro`, `/weekly-review`), always ask once whether the output should be persisted.

## Design notes

- **Specificity over noise:** Only fire on language that genuinely signals persistence-worthy content. Generic statements ("I think X is good") should not trigger.
- **One prompt, one chance:** Never re-prompt within the same turn. The user's first answer is the answer.

## Reference

- Entry formats: `prompts/elite-techniques.md` (Output Formats section).
- Memory files and their roles: `CLAUDE.md` (Memory System section).

## Coexistence

- The explicit `/remember` command remains the deliberate save path. This skill is the safety net that prompts the user to use it when they otherwise would have lost the entry.

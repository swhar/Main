# /remember — Save Something to Memory

Usage: `/remember <anything — task, decision, insight, project update, goal change>`

Classifies the input and appends it to the right memory file with a timestamp.

## Steps

1. Read the input from `$ARGUMENTS`.
2. Classify it into one of these categories:
   - **Task** → append to `memory/tasks.md`
   - **Decision** → append to `memory/decisions.md`
   - **Learning / Insight** → append to `memory/learnings.md`
   - **Profile update** (goal, preference, value change) → update `memory/profile.md`
   - **Project update** → append to the relevant file in `projects/`
3. Format the entry appropriately using the formats in `prompts/elite-techniques.md`.
4. Append (or update) the entry to the correct file.
5. Confirm: "Saved to `memory/<file>.md` as a [category]. Want to add anything else?"

## Classification Guide

| Input type | Target file |
|-----------|-------------|
| "I need to...", "Don't forget to...", "Add task..." | `memory/tasks.md` |
| "I decided...", "We're going with...", "Chose X over Y" | `memory/decisions.md` |
| "I learned...", "Key insight:", "Realized that..." | `memory/learnings.md` |
| "My goal is now...", "I prefer...", "I value..." | `memory/profile.md` |
| Anything about a specific project | `projects/<project>.md` |

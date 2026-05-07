---
name: recall
description: Auto-activate when the user references something they've previously told Claude or saved to memory and expects continuity. Trigger on phrases like "remind me what I said about...", "did I ever decide on...", "what was my reasoning for...", "have I worked on... before", "what do I know about...", "pull up my notes on...", or any reference to past tasks, decisions, learnings, projects, or saved research. Also activate when the user implicitly assumes Claude already has context on a topic ("how's the X project going?"). Skip when the user is clearly asking a fresh external question (use research) or making a new decision (use strategy).
---

# Recall Skill

Activates when the user is reaching back into their own saved context (profile, tasks, decisions, learnings, projects, knowledge). Searches all memory files and surfaces the most relevant entries.

## When to activate

- The user references past context — a prior decision, an old task, a learning, or a project they've already started.
- The user asks a question whose answer should live in this repo's memory rather than the outside world.
- The user assumes continuity ("how's X going?", "what was the deal with Y again?") that requires looking up state.

If activation is borderline, briefly confirm: "Want me to pull what we have on this from memory?"

## Steps

1. Treat the user's referencing phrase as the query (no slash argument needed when auto-activated).
2. Read all memory files:
   - `memory/profile.md`
   - `memory/tasks.md`
   - `memory/decisions.md`
   - `memory/learnings.md`
3. List any relevant project files in `projects/` and read those that match the query.
4. Scan `knowledge/` for any research files related to the query topic.
5. Surface the most relevant entries, organized by type:

---

## Recall: "[query]"

**From your profile / goals:**
- [Relevant goal, preference, or value]

**Related tasks:**
- [Any active or past tasks related to this topic]

**Past decisions:**
- [Any relevant decisions with dates and rationale]

**Learnings / insights:**
- [Relevant learnings]

**Research / knowledge:**
- [Any saved research on this topic — point to the file]

---

6. Ask: "Is this what you were looking for? Want me to pull any of these up in full detail?"

## Reference

- Memory file conventions are described in `CLAUDE.md` (Memory System section). Skill output should match the formats defined there and in `prompts/elite-techniques.md`.

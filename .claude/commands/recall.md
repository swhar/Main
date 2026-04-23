# /recall — Retrieve from Memory

Usage: `/recall <query or topic>`

Searches through all memory files and surfaces the most relevant entries.

## Steps

1. Read the query from `$ARGUMENTS`.
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

# CLAUDE.md — Elite AI Workflow System

This repository is a personal AI workflow system designed to operate at an elite level across work, strategy, and general life decisions. It uses Claude Code as the AI engine with a file-based memory system and custom slash commands.

---

## Memory System

At the start of **every session**, read these files to load context:

- `memory/profile.md` — Who I am: goals, values, working style, current focus
- `memory/tasks.md` — Active tasks, priorities, and what's in progress

Reference these as needed:
- `memory/decisions.md` — Log of key decisions with rationale
- `memory/learnings.md` — Insights, patterns, and lessons learned
- `projects/` — One `.md` file per active project with context and status
- `knowledge/` — Reference documents, research outputs, notes

**Memory discipline:** After any key decision, insight, or task update in a session, update the relevant memory file before the session ends. Use `/remember` to do this quickly.

---

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/briefing` | Start-of-day structured briefing |
| `/plan-day` | Build a prioritized, time-blocked daily plan |
| `/research <topic>` | Deep research workflow → saves to `knowledge/` |
| `/strategy <decision>` | Walk through a decision with structured frameworks |
| `/remember <thing>` | Classify and save something to the right memory file |
| `/news-update` | Morning news brief: headlines, tech/AI, markets, personalized tips |
| `/recall <query>` | Retrieve relevant memory entries |

---

## Elite Defaults

Apply these behaviors by default in every interaction:

1. **Think before answering** — For complex questions, reason step by step before giving a final answer. Show your reasoning when it adds value.
2. **Structured output** — Use clear headers, bullet points, and action items. Avoid walls of text.
3. **Challenge assumptions** — If a question or plan has a hidden flaw, name it before answering. Don't just validate.
4. **Concise then deep** — Lead with the direct answer or recommendation, then provide detail. Let me ask for more if needed.
5. **Proactive flags** — If you notice a risk, blind spot, or better path, surface it even if not asked.
6. **Close the loop** — At the end of any workflow, state what should be saved to memory or what next action should follow.

See `prompts/elite-techniques.md` for detailed frameworks (SWOT, pre-mortem, decision matrix, etc.).

---

## Directory Reference

```
memory/          Persistent context: profile, tasks, decisions, learnings
projects/        Per-project context files
knowledge/       Research outputs, reference docs, saved notes
prompts/         Framework and technique reference documents
.claude/commands/ Slash command definitions
```

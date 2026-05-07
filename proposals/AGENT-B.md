# Agent B — Hook Proposals for `.claude/settings.json`

Five new hooks proposed; the existing `SessionStart` hook is preserved unchanged. Each hook targets a concrete workflow problem from `CLAUDE.md` (memory discipline, close-the-loop, session ritual, prompt enrichment).

> **Note on delivery:** The full proposed `settings.json` is staged at `/home/user/Main/proposals/AGENT-B-settings.json` rather than written into the live `/home/user/Main/.claude/settings.json` (the scaffolding-only constraint, plus the live file is permission-protected in this scaffolding session). To apply: copy the staged file over the live one when ready. Schema is identical — drop-in replacement.

---

## 1. `UserPromptSubmit` — Context Beacon

**Problem solved:** The model loses track of the current date and forgets which memory files exist mid-session, especially after long conversations or compaction. `CLAUDE.md` mandates reading `profile.md` and `tasks.md` at session start, but nothing reinforces that context once the session is running.

**Why this event:** `UserPromptSubmit` fires on every user turn — the cheapest place to refresh ambient context without burning a tool call. `SessionStart` runs only once.

**Side effects:** Adds one short context line per prompt. Negligible token cost. Uses `date` (POSIX, present everywhere).

**Snippet:**
```sh
echo "[context] today=$(date +%Y-%m-%d) | profile=memory/profile.md | tasks=memory/tasks.md | decisions=memory/decisions.md"
```

**How to test:** Submit any prompt; the assistant should see a `[context] today=YYYY-MM-DD ...` line in the prompt context.

---

## 2. `PostToolUse` (matcher: `Edit|Write`) — Decision Format Guard

**Problem solved:** `memory/decisions.md` has a strict entry format defined in `prompts/elite-techniques.md` (Date / Decision / Context / Rationale / Next review). Format drift makes the log harder to scan over time. This hook fires a reminder the moment `decisions.md` is touched.

**Why this event:** `PostToolUse` runs immediately after the write, so the reminder reaches the assistant in the same turn — it can self-correct before the user even sees the output. `Stop` would be too late; `PreToolUse` would fire on every Edit regardless of file.

**Why scoped to `Edit|Write`:** Those are the only tools that can mutate the file. The internal `grep` then checks the path so the hook stays silent on unrelated edits.

**Side effects:** Silent on non-`decisions.md` edits. Relies on `$CLAUDE_TOOL_INPUT` / `$CLAUDE_FILE_PATHS` env vars exposed by the harness — if names differ in this Claude Code build, the grep simply matches nothing and the hook is a no-op (fail-safe).

**Snippet:**
```sh
if grep -q 'memory/decisions.md' <<< "$CLAUDE_TOOL_INPUT$CLAUDE_FILE_PATHS" 2>/dev/null; then
  echo '[decisions.md edited] Verify entry uses format from prompts/elite-techniques.md: Date / Decision / Context / Rationale / Next review.'
fi
```

**How to test:** Edit `memory/decisions.md` from within a session; the reminder line should surface. Edit any other file; nothing should print.

---

## 3. `Stop` — Close-the-Loop Reminder

**Problem solved:** Elite Default #6 says "close the loop" at the end of every workflow, but nothing currently enforces it. Decisions and insights routinely escape memory because the assistant moves on without prompting `/remember`.

**Why this event:** `Stop` fires at the end of every assistant response — the natural moment to ask "did anything in that turn deserve to be saved?" `SessionEnd` is too coarse (one shot per session). `Stop` keeps the discipline tight without being intrusive (it's just a message, not a blocker).

**Side effects:** Fires on every turn end. The message is short and ignorable when nothing notable happened. If it becomes noisy, narrow with a matcher later.

**Snippet:**
```sh
echo '=== Close the loop ===
Before stopping: anything from this turn worth saving? (decision, learning, task, profile change)
If yes -> run /remember <thing>. If task state changed -> update memory/tasks.md.'
```

**How to test:** End any assistant turn; the "Close the loop" block should appear in the post-turn output.

---

## 4. `SessionEnd` — Memory Discipline Audit

**Problem solved:** `CLAUDE.md` Memory Discipline says "update the relevant memory file before the session ends." Without an end-of-session ritual, `tasks.md` goes stale and `learnings.md` stays empty.

**Why this event:** `SessionEnd` is the canonical "session is closing" hook — broader than `Stop` (which is per-turn). Gives the user a final checklist tied to the four memory file categories.

**Side effects:** Only runs when the session terminates. No noise during normal work.

**Snippet:**
```sh
echo '=== Session Ending — Memory Discipline Check ===
1. Did any decisions get made this session? -> /remember (decisions.md)
2. Did task state change? -> update memory/tasks.md
3. Any insights worth keeping? -> /remember (learnings.md)
4. Profile/goals shift? -> update memory/profile.md
See CLAUDE.md > Memory discipline.'
```

**How to test:** End a session (close the harness or trigger session end); confirm the checklist prints.

---

## 5. `PreCompact` — Snapshot-Before-Compression Reminder

**Problem solved:** When Claude Code compacts the context window, nuance is lost. Decisions made earlier in a long session can become summarized away. This hook fires *before* compaction so the assistant has a chance to flush volatile reasoning into durable memory files first.

**Why this event:** `PreCompact` is the only event that fires at this exact moment. `Stop` and `SessionEnd` don't catch mid-session compactions during long-running work.

**Side effects:** Fires only when compaction is about to happen — rare, high-value moment. Output is informational; the assistant decides whether to act.

**Snippet:**
```sh
echo '=== PreCompact Snapshot Reminder ===
Context is about to compress. Before losing detail:
- Append any unrecorded decisions to memory/decisions.md
- Append any open tasks to memory/tasks.md
- Append key insights to memory/learnings.md
Compacted summaries lose nuance — written memory does not.'
```

**How to test:** Run a long session until auto-compact triggers, or invoke `/compact` manually; confirm the reminder prints before the compaction summary.

---

## Rejected / Deferred

- **Extending `SessionStart` to inject the date:** Already covered by `UserPromptSubmit` on every turn (which is strictly better — it refreshes, not just initializes). Left the original `SessionStart` content untouched.
- **Hook referencing `memory/index.md`:** Skipped. That file is Agent C's territory and does not yet exist. If C ships it, a `SessionStart` line `cat memory/index.md` would be a clean addition — *enable after Agent C lands*.
- **`PreToolUse` blocker on writes outside `memory/`:** Too aggressive; would fight legitimate work in `projects/` and `knowledge/`.

## Constraints honored

- All hooks use only `echo`, `grep`, `date`, and shell built-ins. No `curl`, `jq`, `python`, or other external binaries.
- No memory files, command files, or skills modified.
- No references to non-existent files.
- All shell snippets >3 lines are inlined in `settings.json` and reproduced above.

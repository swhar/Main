# Memory Conventions

This document defines schema and structural conventions for the memory system. It is **additive** to `prompts/elite-techniques.md` — the entry body formats defined there (Decision log entry, Learning entry, Action item) are unchanged. This file adds a single canonical **header line** above each entry so `/recall` can grep reliably, plus rules for archival and file splitting.

> Read this once. Existing entries without these conventions are still valid — `/recall` falls back to whole-file scan when the header is absent.

---

## 1. Canonical Entry Header

Every new entry in `decisions.md`, `learnings.md`, and `tasks.md` (Completed This Week section) starts with a single header line in this format:

```
## [YYYY-MM-DD] <TYPE>: <Short title> [#tag1 #tag2]
```

**Fields:**
- `YYYY-MM-DD` — ISO date in square brackets. Required. Used for sort and date-range grep.
- `<TYPE>` — One of: `DECISION`, `LEARNING`, `TASK`, `PROJECT`, `PROFILE`. Required. Uppercase for grep contrast.
- `<Short title>` — 3–10 word summary. Required. This is what shows up in `index.md` and `/recall` results.
- `[#tag1 #tag2]` — Optional trailing tags. Square brackets, hash-prefixed, space-separated. **Omit the entire bracket if there are no tags.**

**Examples:**

```
## [2026-05-07] DECISION: Adopt weekly archival pattern [#meta #memory-system]

## [2026-05-07] LEARNING: Premature file splits hurt recall

## [2026-05-07] TASK: Draft Q3 OKRs [#planning #work]
```

**Body:** Below the header, use the format from `prompts/elite-techniques.md` exactly as before (the `> **Date:** ... > **Decision:** ...` blockquote for decisions, etc.). The header date and the body's `Date:` field are intentionally redundant — the header is for grep, the body is for human reading and is what `/strategy` and `/research` already produce.

**Why this works with existing commands:** `/remember`, `/strategy`, `/research`, and `/recall` operate on whole files. Adding an `H2` line above the existing blockquote does not break any of them — it only adds a stronger anchor for retrieval. Tags are optional, so commands that don't know about them keep working.

---

## 2. Tag Taxonomy (Starter Set)

Tags are free-form, but use this starter vocabulary to stay consistent. Add new tags freely; review and prune quarterly.

**Domain:**
- `#work` — anything job/career related
- `#personal` — life, family, health, money outside of work
- `#health` — sleep, fitness, medical, mental health
- `#finance` — money decisions, investments
- `#relationships` — partner, family, friends, network

**Function:**
- `#strategy` — multi-month or directional choices
- `#tactics` — short-horizon execution
- `#planning` — goal-setting, OKRs, roadmaps
- `#research` — auto-applied by `/research`
- `#meta` — about the workflow system itself

**Status / urgency (tasks only):**
- `#now`, `#next`, `#someday`, `#blocked`

**Project tags:** Use the project filename (without `.md`) as a tag, e.g. `#project-acme` for `projects/acme.md`.

Keep a tag to one word or hyphenated. Lowercase. No spaces.

---

## 3. File Layout & When to Split

**Current rule: do NOT split `decisions.md` or `learnings.md` by quarter.**

Rationale: with the system empty today, splitting upfront fragments grep targets and forces `/recall` to know where to look. Single-file logs are easier to scan and search until volume justifies otherwise.

**Soft archival trigger** — when **either** condition is met for `decisions.md` or `learnings.md`:
- File exceeds 500 entries, OR
- File exceeds 10,000 lines, OR
- A full calendar year of entries has accumulated

…then move all entries older than the **previous calendar year** into `memory/archive/decisions-YYYY.md` (or `learnings-YYYY.md`). The active file always covers the current year + previous year minimum.

This is a **manual archival**, performed during a `/weekly-review` or on demand. Until the trigger hits, keep one file.

**Re-evaluation:** Revisit this rule once `decisions.md` reaches ~100 entries. The empirical pain of scrolling vs. the convenience of single-file grep should drive any change.

---

## 4. Weekly Archival of Completed Tasks

`tasks.md` has a "Completed This Week" section that grows unboundedly without intervention. To keep it usable:

**Pattern:** At the end of each ISO week, the `/weekly-review` workflow (defined elsewhere — not in this doc) moves the contents of `tasks.md` → "Completed This Week" into a weekly rollup file:

```
memory/archive/2026-W19.md
```

**File naming:** `YYYY-Www.md` using ISO week numbers (W01–W53). Example: 2026-05-07 falls in **W19**.

**Rollup file structure:**
```markdown
# Week 19, 2026 (May 4 – May 10)

## Completed Tasks
<entries moved from tasks.md, preserving canonical headers>

## Decisions Logged This Week
<links/titles only — do NOT duplicate decision bodies; they live in decisions.md>

## Learnings Logged This Week
<links/titles only>

## Notes
<free-form weekly reflection from /weekly-review>
```

After rollup, "Completed This Week" in `tasks.md` is emptied. Decisions and learnings stay in their primary files — the rollup only **references** them by title + date for week-level review purposes.

**Trigger:** `/weekly-review` (owned by another agent — do not implement here). If `/weekly-review` does not exist yet, the rollup is a manual append following the structure above.

---

## 5. Index Regeneration

`memory/index.md` is a derived view, not a source of truth. It is regenerated by `/recall` (when run with no arguments or with `--refresh`) or by `/briefing` at session start. **Do not hand-edit it** — changes will be overwritten.

The index reads from:
- `memory/profile.md` → Active Goals
- `memory/decisions.md` → latest 5 by header date
- `memory/learnings.md` → latest 5 by header date
- `projects/*.md` (excluding `README.md`) → Active Projects

---

## 6. Backward Compatibility

- Entries written before this convention exists are still valid. `/recall` should fall back to full-text scan when the canonical header is absent.
- `/remember`, `/recall`, `/strategy`, `/research` need no immediate update. They work against the same files; they just produce or consume slightly richer entries going forward.
- `prompts/elite-techniques.md` is unchanged. Body formats are still the source of truth for what goes inside an entry.

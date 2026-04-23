# Elite AI Techniques Reference

Use this document when running structured workflows. Reference specific sections in slash commands as needed.

---

## Decision Frameworks

### SWOT Analysis
- **Strengths** — What advantages does this option have?
- **Weaknesses** — What are its internal limitations or risks?
- **Opportunities** — What external factors make this a good time?
- **Threats** — What could go wrong or work against it?

### Pre-mortem
Imagine it's 12 months from now and this decision failed spectacularly. What happened? List the top 5 most likely failure modes. Then design mitigations for each.

### Decision Matrix
List options as rows, criteria as columns. Score each (1–5). Weight criteria by importance. Compute weighted totals. Use to surface the most rational choice — then gut-check it.

### 10/10/10 Rule
How will I feel about this decision in 10 minutes? 10 months? 10 years? Useful for separating short-term discomfort from long-term regret.

### Reversibility Test
Is this decision reversible or irreversible? Reversible → move fast with low stakes. Irreversible → slow down, get more data, involve more perspectives.

---

## Research Workflow

1. **Define the question** — Write out exactly what you need to know and why.
2. **Identify sources** — What kinds of sources would best answer this? (data, expert opinion, case studies, etc.)
3. **Search iteratively** — Start broad, then narrow. After each search, refine the next query based on gaps.
4. **Synthesize, don't summarize** — Extract the key insight, not a list of facts. What does this mean for the decision or goal?
5. **Save findings** — Write to `knowledge/<topic>.md`. Update `memory/learnings.md` with the single most important takeaway.

---

## Planning Frameworks

### Eisenhower Matrix (for task prioritization)
- **Urgent + Important** → Do now
- **Not Urgent + Important** → Schedule
- **Urgent + Not Important** → Delegate or batch
- **Not Urgent + Not Important** → Eliminate

### Weekly Review
1. What did I complete this week?
2. What didn't get done, and why?
3. What's the single most important thing next week?
4. What should I stop doing?
5. Update `memory/tasks.md` and `memory/learnings.md`.

### Goal Decomposition
Big goal → 3-month milestone → weekly outcome → daily task. Every task in `memory/tasks.md` should trace to a goal in `memory/profile.md`.

---

## Prompting Patterns for Elite Output

### For complex analysis
> "Think step by step. Before giving your answer, list your assumptions and flag any that could be wrong."

### For decisions
> "Give me your recommendation first. Then explain the top 2 reasons for it and the top 1 risk I should watch for."

### For challenging my thinking
> "What's the strongest argument *against* what I just said? What am I missing?"

### For strategies
> "Imagine the most successful version of this plan. What does it look like in 12 months? Now work backwards: what had to be true at 6 months, 3 months, 1 month?"

---

## Output Formats

### Action item
> **Action:** [What] — [Who] — [By when]

### Decision log entry
> **Date:** YYYY-MM-DD
> **Decision:** [What was decided]
> **Context:** [Why this decision arose]
> **Rationale:** [Why this option was chosen]
> **Next review:** [When to revisit]

### Learning entry
> **Date:** YYYY-MM-DD
> **Insight:** [The key takeaway in one sentence]
> **Source:** [Where this came from]
> **Applies to:** [Which goals or projects this affects]

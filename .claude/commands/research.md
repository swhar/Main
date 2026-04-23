# /research — Deep Research Workflow

Usage: `/research <topic or question>`

Runs a structured research session and saves findings to `knowledge/`.

## Steps

1. Restate the research question clearly. Ask: "What decision or goal is this research supporting? What would a great answer look like?"
2. Identify the key sub-questions that need answering to fully address the topic.
3. For each sub-question:
   - Search the web (if tools are available) or ask the user to paste relevant sources/content
   - Extract the key facts, data points, and expert perspectives
   - Note the source and its credibility
4. Synthesize across all sub-questions:
   - What does the evidence point to?
   - What's the single most important insight?
   - What's still uncertain or contested?
   - What does this mean for the user's specific goal or decision?
5. Apply the pre-mortem lens: What could make this research wrong or outdated?
6. Save findings to `knowledge/<slugified-topic>.md` using this structure:

---

## Research: [Topic]
**Date:** [YYYY-MM-DD]
**Question:** [The core question being answered]
**Supporting goal:** [Why this matters]

### Key Findings
- [Finding 1 — with source]
- [Finding 2 — with source]

### Synthesis
[2–3 sentences: what the evidence says overall]

### Main Insight
> [The single most important takeaway in one sentence]

### Uncertainties
- [What's still unclear or debated]

### Recommended Next Steps
- [What to do with this information]

---

7. Update `memory/learnings.md` with the main insight using the learning entry format from `prompts/elite-techniques.md`.
8. Ask: "Does this answer your question, or should we go deeper on any section?"

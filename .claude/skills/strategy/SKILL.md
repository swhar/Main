---
name: strategy
description: Auto-activate when the user is weighing a significant decision, choice between options, or new initiative. Trigger on phrases like "should I...", "I'm trying to decide between...", "thinking about whether to...", "torn between X and Y", "is it worth...", "considering...", "what do you think about doing...", or any framing that signals deliberation rather than a request for facts. Skip when the user is gathering information (use research) or asking about something they already told Claude (use recall). Skip for trivial, fully-reversible choices the user is not actually deliberating over.
---

# Strategy Skill

Activates when the user is reasoning through a significant decision, problem, or goal. Guides them through structured thinking using frameworks from `prompts/elite-techniques.md`.

## When to activate

- The user is comparing two or more options, or deciding whether to commit to a direction.
- The choice has non-trivial stakes (time, money, energy, relationships, or strategic direction).
- The user is signaling deliberation, not just venting or asking a factual question.

If activation is borderline, briefly confirm: "Sounds like a real decision — want me to walk this through the strategy workflow?"

## Steps

1. Read `memory/profile.md` for values and goals that should inform this decision.
2. Read `memory/decisions.md` for any related past decisions or context.
3. Restate the decision or problem clearly. Ask clarifying questions if needed:
   - "What are you actually trying to achieve here?"
   - "What constraints are you working within (time, money, energy, relationships)?"
   - "What would 'good enough' look like vs. 'great'?"
4. Choose the right framework based on the type of decision:
   - **Reversible, low-stakes** → 10/10/10 Rule + gut check
   - **Strategic choice between options** → Decision Matrix
   - **New initiative or plan** → Pre-mortem
   - **Complex situation with many factors** → SWOT
   - All frameworks are in `prompts/elite-techniques.md`
5. Run the chosen framework(s) collaboratively, asking for input at each stage.
6. Surface the recommendation clearly:

---

## Decision: [Title]

**Recommendation:** [State the recommended option or course of action]

**Top 3 reasons:**
1. [Reason]
2. [Reason]
3. [Reason]

**Main risk to watch:**
> [The one thing that could make this go wrong — and how to mitigate it]

**Dissenting view (steelman):**
> [The strongest argument against this recommendation]

**Next action:**
> [What to do in the next 48 hours to move forward]

---

7. Ask: "Do you want to record this decision? I'll save it to `memory/decisions.md`."
8. If yes, save using the decision log format from `prompts/elite-techniques.md`.

## Reference

- All decision frameworks (SWOT, Pre-mortem, Decision Matrix, 10/10/10, Reversibility Test) are defined in `prompts/elite-techniques.md`. Read that file when applying a framework — do not paraphrase from memory.

---
name: framework-picker
description: Auto-activate when the user is reasoning out loud through a problem without explicitly invoking /strategy, and the conversation would benefit from naming the right structured framework. Trigger when the user is comparing options informally ("hmm, on one hand... on the other..."), enumerating pros and cons, expressing uncertainty about how to think about a problem ("I don't know how to evaluate this", "I'm going in circles on..."), or planning a new initiative without a structure. Suggest — do not impose — the matching framework from prompts/elite-techniques.md (SWOT, Pre-mortem, Decision Matrix, 10/10/10, Reversibility Test, Eisenhower, Goal Decomposition). Skip when the user is already running /strategy, /plan-day, or /pre-mortem, or when the question is purely factual.
---

# Framework Picker Skill

Activates lightly during open-ended reasoning to name and offer the right elite framework. The goal is to upgrade messy thinking into structured thinking *without* hijacking the conversation.

## When to activate

- The user is visibly deliberating without a structure (lists tradeoffs, asks "what do you think?", goes in circles).
- The conversation is not already inside a structured workflow (`/strategy`, `/plan-day`, `/pre-mortem`, `/weekly-review`).
- A specific framework from `prompts/elite-techniques.md` would clearly fit.

If none of the frameworks fit cleanly, do not activate.

## Steps

1. Listen for the *shape* of the user's problem and match it to a framework:
   - **Comparing 2+ concrete options on multiple criteria** → Decision Matrix
   - **About to commit to a new plan/initiative** → Pre-mortem
   - **Big, multi-factor situation** → SWOT
   - **Small reversible choice the user is over-thinking** → 10/10/10 Rule + Reversibility Test
   - **Overwhelmed by too many tasks** → Eisenhower Matrix
   - **Big goal, no clear next step** → Goal Decomposition
2. Offer the framework as a *suggestion*, not a takeover. One sentence:
   > "This sounds like a [framework] situation — want me to walk you through it?"
3. If the user says yes:
   - Pull the framework definition from `prompts/elite-techniques.md` (do not paraphrase from memory).
   - Run it collaboratively, asking for input at each step.
   - If it's a decision, hand off to the `strategy` skill's output format (Recommendation / Top 3 reasons / Main risk / Dissenting view / Next action).
4. If the user says no, drop it and continue normally. Do not re-offer in the same turn.
5. Close the loop: if a framework was run, ask whether the result should be saved (decision → `memory/decisions.md`, learning → `memory/learnings.md`).

## Reference

- All frameworks live in `prompts/elite-techniques.md`. This skill is a router into that document — it must not duplicate the content.

## Coexistence

- This skill is *suggestive*. The explicit `/strategy` command remains the user's deliberate entry point. Framework-picker is for the moments when the user did not realize they were in a strategy moment.

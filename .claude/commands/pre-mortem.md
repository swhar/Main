# /pre-mortem — Failure-Mode Analysis Before You Commit

Usage: `/pre-mortem <plan, project, or decision>`

Stress-tests a plan by imagining it has already failed and working backwards to causes. Use before committing real time, money, or reputation. Lighter and more targeted than `/strategy`.

## Steps

1. Read `memory/profile.md` for relevant goals and risk tolerance.
2. Read `memory/decisions.md` and `memory/learnings.md` for prior failure patterns the user has actually hit.
3. Restate the plan in one sentence and confirm it back. Ask for the timeline ("when would 'failed' be obvious?").
4. Run the Pre-mortem framework from `prompts/elite-techniques.md`: imagine it's the failure date and the plan went badly. Generate the top 5 failure modes.
5. For each failure mode, classify the cause: external (market, people, luck) vs. internal (execution, judgment, energy). Internal causes get higher priority for mitigation.
6. For each of the top 3 failure modes by likelihood × impact, design one concrete mitigation or early-warning signal.
7. Identify the single "tripwire" — the earliest observable signal that the plan is going wrong — and where it would show up.
8. Produce the output:

---

## Pre-mortem: [Plan Name] — 2026-05-07

**Plan in one sentence:** [Restated plan]
**Failure date assumed:** [Date by which failure would be obvious]

**Top 5 failure modes**
1. [Failure mode] — likelihood: H/M/L — impact: H/M/L — cause type: internal/external
2. [Failure mode] — ...
3. [Failure mode] — ...
4. [Failure mode] — ...
5. [Failure mode] — ...

**Mitigations for top 3**
- [Failure mode] → [Concrete mitigation or pre-condition]
- [Failure mode] → [Mitigation]
- [Failure mode] → [Mitigation]

**Tripwire**
> [The earliest signal that this plan is going wrong, and where to watch for it]

**Go / no-go / modify**
> [Recommendation: proceed as-is, proceed with modifications, or rethink]

---

9. Offer to save the tripwire and any plan modifications via `/remember` (decision log if go/no-go was made).
10. Ask: "Want to set a calendar check-in for the tripwire date?"

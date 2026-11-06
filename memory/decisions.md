# Decisions

A log of key decisions — work, life, strategy, anything significant. Use `/strategy` to make decisions with structured frameworks, `/remember` to log quick decisions.

Format: see `prompts/elite-techniques.md` → Decision log entry

---

<!-- Decisions are added here, newest first -->


## 2026-11-06 — Vendored Cloudflare security-audit skill
- **Decision:** Added cloudflare/security-audit-skill (commit c1c8a8c, MIT) to `.claude/skills/security-audit/` as a project skill.
- **Why:** Gives Claude Code a structured, adversarially-validated security audit workflow for any repo opened from this workspace.
- **Notes:** Full audits write output to `~/security-audit-skill/<repo>/run-N` (outside the target). Validators need Node.js. Executing target code requires a real sandbox; without one, leads stay `needs_validation`. Update by re-copying from upstream.

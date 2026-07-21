# Build: Anchor Ceremony v2 — PreCompact Re-Anchor + Rolling Ledger

## Status
Open

## Priority
High — highest-ROI item of the context-decay portfolio (238 verdict: one hook, zero gate changes, ~30% anchor token reduction); 240's ledger ships in the same ceremony change by design.

## Summary
Implement the 238+240 YAH verdicts as one combined anchor-ceremony update. (1) PreCompact hook: on the harness compaction event, set `anchored: false` in workflow state so the existing Gate 3 forces a full `/kernel/anchor` on the fresh context — sidesteps the SessionStart compact-matcher injection bug (GitHub #15174) by using state side-effects, not content injection. (2) Hybrid timer: raise `actions_limit` 30 → 50 (event-driven primary, timer fallback). (3) Rolling structured ledger: anchor Step 10 extends the `context` key with a schema-enforced `ledger` array (decisions, failed attempts, rolling window) so compaction stops destroying failed-attempt history.

## Requirements
- New hook file registered for the PreCompact event in settings.json: writes `anchored: false` + a compaction-count marker; no content injection (bugged upstream); must be a no-op in one-shot (`claude -p`) agents if the event never fires there
- `actions_limit` 30 → 50 in workflow state seeding + anywhere hardcoded (grep first — RULE ZERO)
- anchor.md Step 10 schema extended: `ledger` array of `{ts, kind: decision|failure|constraint, summary, refs}` with a rolling window cap (design: `projects/kernel-rolling-summarization-research/02-gap-analysis-and-design.md` Candidate A)
- Candidate B (periodic summarizer hook) explicitly NOT built — 240 verdict rejected it
- L3 test: trigger a real compaction in a live long session, assert next tool call hook-blocks into a full anchor and the ledger survives; verify hook capability claims against installed Claude Code (2.1.207 findings in `projects/kernel-precompact-reanchor-research/01-hook-capability.md`)
- Verdict sources: `projects/kernel-precompact-reanchor-research/research-report.md`, `projects/kernel-rolling-summarization-research/research-report.md`

## References
- Backlogs done: 238, 240; sibling builds 244, 246
- `.claude/hooks/universal-gate-enforcer.py` Gate 3 (the enforcement this hook piggybacks on), `.claude/commands/kernel/anchor.md`

## Task Builder Input
- **Deliverable:** PreCompact hook file + settings registration; actions_limit 50; anchor.md Step 10 ledger schema; L3 compaction test evidence
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Hooks load at startup — set `needs_restart: true` on completion, user restarts Claude Code. Do not modify Gate 3 itself. Protected-file changes (hooks, anchor command) run only inside this user-approved pipeline.

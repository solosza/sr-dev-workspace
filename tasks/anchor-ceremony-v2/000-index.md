# Anchor Ceremony v2 — Task Index

Backlog: [[../../docs/backlog/245-kernel-build-anchor-ceremony-v2.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type | Depends on |
|---|------|------|-----------|
| 001 | [[001-build-write-precompact-hook.md]] | BUILD | — |
| 002 | [[002-build-register-precompact-settings.md]] | BUILD | 001 |
| 003 | [[003-build-raise-actions-limit-live.md]] | BUILD | — |
| 004 | [[004-build-raise-actions-limit-seed.md]] | BUILD | — |
| 005 | [[005-build-anchor-step10-ledger-schema.md]] | BUILD | — |
| 006 | [[006-build-anchor-step5-ledger-readback.md]] | BUILD | 005 |
| 007 | [[007-test-l1-files-and-registration.md]] | TEST | 001-006 |
| 008 | [[008-test-l2-hook-behavior.md]] | TEST | 007 |
| 009 | [[009-test-l3-live-compaction.md]] | TEST | 008 |

## Constraints (from backlog 245)

- Do NOT modify Gate 3 in `universal-gate-enforcer.py` — the hook piggybacks on it as-is
- Candidate B (periodic summarizer hook) is explicitly NOT built (240 verdict rejected it)
- Hooks load at Claude Code startup — orchestrator sets `needs_restart: true` after validation (NOT an inner task; one-shot agents never write parent session_state.json per SI-08)
- One-shot agents: hook must be a safe no-op if the PreCompact event never fires or state is missing

## Design sources

- `projects/kernel-precompact-reanchor-research/research-report.md` (Policy C hybrid, hook design, state fields)
- `projects/kernel-precompact-reanchor-research/01-hook-capability.md` (2.1.207 capability findings)
- `projects/kernel-rolling-summarization-research/02-gap-analysis-and-design.md` (Candidate A ledger)

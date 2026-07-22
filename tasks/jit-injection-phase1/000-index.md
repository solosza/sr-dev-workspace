# JIT Rule Injection Phase 1 — Task Index

Backlog: [[../../docs/backlog/246-kernel-build-jit-injection-phase1.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type | Depends on |
|---|------|------|-----------|
| 001 | [[001-build-write-rule-map.md]] | BUILD | — |
| 002 | [[002-build-write-injector-hook.md]] | BUILD | 001 |
| 003 | [[003-build-register-injector-settings.md]] | BUILD | 002 |
| 004 | [[004-test-l1-files-registration-advisory.md]] | TEST | 001-003 |
| 005 | [[005-test-l2-injection-behavior.md]] | TEST | 004 |
| 006 | [[006-test-l3-live-injection.md]] | TEST | 005 |

## Constraints (backlog 246)

- ADVISORY ONLY — any code path that blocks is a defect
- Top 2 rules come from 01-rule-inventory.md candidate ranking — read the doc, never pick from memory
- Phases 2-4 OUT of scope; no changes to anchor duties or existing blocking gates
- Orchestrator sets needs_restart after validation (one-shots never write parent session state — SI-08)

## Design sources

- `projects/kernel-jit-rule-injection-research/01-rule-inventory.md`
- `projects/kernel-jit-rule-injection-research/02-injection-capability.md`
- `projects/kernel-jit-rule-injection-research/03-rule-map-design.md`
- `projects/kernel-jit-rule-injection-research/research-report.md`

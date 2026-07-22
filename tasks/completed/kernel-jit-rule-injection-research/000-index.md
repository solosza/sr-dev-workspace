# JIT Rule Injection Research — Task Index

## Goal
Determine whether Just-In-Time rule injection at the PreToolUse boundary should be added alongside hook blocking, offloading rule-refresh duties from the N-action anchor. Verdict: YAH or NAY.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-research-rule-inventory]] | RESEARCH | 001 | pending |
| 003 | [[003-research-injection-capability]] | RESEARCH | 001 | pending |
| 004 | [[004-research-rule-map-design]] | RESEARCH | 001 | pending |
| 005 | [[005-build-write-research-report]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
> [[gate-contract.md]]

## Deliverables
- `projects/kernel-jit-rule-injection-research/01-*.md`, `02-*.md`, `03-*.md` (task outputs)
- `projects/kernel-jit-rule-injection-research/research-report.md` (verdict: YAH or NAY)

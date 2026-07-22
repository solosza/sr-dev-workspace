# DAG Wave Execution Engine Research — Task Index

## Goal
Determine whether spawn-agent-swarm and execute-pipeline should gain dependency-wave dispatch (topological sorting + barrier monitor) to replace flat-parallel batches. Verdict: YAH or NAY.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-research-metadata-and-sorting]] | RESEARCH | 001 | pending |
| 003 | [[003-research-barrier-monitor-and-failures]] | RESEARCH | 001 | pending |
| 004 | [[004-research-lesson-reconciliation-and-comparison]] | RESEARCH | 001 | pending |
| 005 | [[005-build-write-research-report]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
> [[gate-contract.md]]

## Deliverables
- `projects/kernel-dag-wave-research/01-*.md`, `02-*.md`, `03-*.md` (task outputs)
- `projects/kernel-dag-wave-research/research-report.md` (verdict: YAH or NAY)

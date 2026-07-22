# Barrier Gate Prerequisites Research — Task Index

## Goal
Determine whether run-task.sh should enforce deliverable-based prerequisite barriers (file-existence wait/poll with timeout) at the task level. Verdict: YAH or NAY.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-research-prereq-format]] | RESEARCH | 001 | pending |
| 003 | [[003-research-wait-loop-design]] | RESEARCH | 001 | pending |
| 004 | [[004-research-deadlock-and-staleness]] | RESEARCH | 001 | pending |
| 005 | [[005-build-write-research-report]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
> [[gate-contract.md]]

## Deliverables
- `projects/kernel-barrier-gate-research/01-*.md`, `02-*.md`, `03-*.md` (task outputs)
- `projects/kernel-barrier-gate-research/research-report.md` (verdict: YAH or NAY)

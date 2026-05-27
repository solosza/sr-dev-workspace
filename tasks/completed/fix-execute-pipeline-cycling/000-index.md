# Fix Execute-Pipeline Cycling — Task Index

## Goal
Fix 5 defects that break execute-pipeline autonomous cycling.

## Source
docs/backlog/090-kernel-fix-execute-pipeline-autonomous-cycling.md

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-fix-max-consecutive-fails]] | BUILD | none | pending |
| 002 | [[002-fix-empty-output-backoff]] | BUILD | none | pending |
| 003 | [[003-fix-precheck-dedup]] | BUILD | none | pending |
| 004 | [[004-fix-complete-dedup-append]] | BUILD | none | pending |
| 005 | [[005-fix-step03-enforcement]] | BUILD | none | pending |
| 006 | [[006-fix-step04-guard]] | BUILD | none | pending |
| 007 | [[007-fix-step08-total-tasks]] | BUILD | none | pending |
| 008 | [[008-verify-all-fixes]] | TEST | 001-007 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- run-task.sh with MAX_CONSECUTIVE_FAILS=4, empty-output backoff, dedup pre-check
- complete.md with dedup-before-append instruction
- step-03-run-task-builder.md with atomic flag-clear enforcement
- step-04-execute-tasks.md with pipeline_mode guard
- step-08-write-tasks.md with total_tasks pre-write + post-write verify

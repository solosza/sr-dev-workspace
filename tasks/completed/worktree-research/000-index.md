# Worktree Research — Task Index

## Goal

Research and design git worktree isolation for execute-pipeline. Determine whether `.claude/state/` file isolation is achievable, confirm EnterWorktree behavior, and design the lifecycle integration (create → run → merge → cleanup).

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-market-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-kernel-research-enterworktree-behavior]] | RESEARCH | 001 | pending |
| 003 | [[003-kernel-research-state-isolation]] | RESEARCH | 001 | pending |
| 004 | [[004-kernel-research-merge-conflicts]] | RESEARCH | 003 | pending |
| 005 | [[005-kernel-design-lifecycle-workflow]] | RESEARCH | 004 | pending |
| 006 | [[006-kernel-design-execute-pipeline-integration]] | RESEARCH | 005 | pending |
| 007 | [[007-kernel-design-run-task-sh-safety]] | RESEARCH | 005 | pending |
| 008 | [[008-kernel-compile-research-report]] | BUILD | 006, 007 | pending |

## Gate Contract

→ [[gate-contract.md]]

## Deliverables

- `RESEARCH-REPORT.md` — Comprehensive findings on EnterWorktree behavior, state isolation, merge strategies
- `INTEGRATION-DESIGN.md` — Actionable implementation steps for execute-pipeline integration

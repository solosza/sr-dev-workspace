# Worktree Research

Research and design git worktree isolation for the Isagawa Kernel's execute-pipeline loop.

## Status

Complete — research done, integration built.

## Deliverables

| Document | Purpose |
|----------|---------|
| `01-enterworktree-analysis.md` | EnterWorktree tool behavior + Agent isolation parameter analysis |
| `02-state-isolation-design.md` | State isolation confirmation + worktree state flow |
| `03-merge-gate-design.md` | Merge gate design for review-queue accept flow |

## Code Changes

| File | Change |
|------|--------|
| `.claude/skills/execute-pipeline/SKILL.md` | Added Worktree Isolation Mode section |
| `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Added worktree mode details, scope routing, pipeline state extension |
| `run-task.sh` | Added worktree detection, banner logging, merge info in completion output |

## Key Findings

1. **EnterWorktree** is for interactive use. **Agent `isolation: "worktree"`** is the right mechanism for pipelines.
2. **State isolation confirmed** — worktrees have separate working directories, so `.claude/state/` is naturally isolated.
3. **Merge gate** routes through `/kernel/review-queue` — accept merges, reject removes worktree.
4. **run-task.sh** needs no behavioral changes — it already works with any repo path. Worktree detection is informational.

## Context

State file contention between interactive sessions and one-shot agents was a recurring pain point. Worktrees provide natural working-directory isolation. See backlogs 123 and 183.

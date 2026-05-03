# Kernel Builds — Task Index

Autonomous execution of all kernel backlog items. Each gets a feature branch, task-builder decomposition, execution, testing, prod-test, and commit. No merges to main.

## Execution Order (dependency-driven)

| # | Task | Backlog | Branch |
|---|------|---------|--------|
| 001 | Task-builder 008 | Recurrence Detection | `feature/008-recurrence-detection` |
| 002 | Execute 008 | Run tasks | — |
| 003 | Prod-test 008 | Validate | — |
| 004 | Commit 008 | Git commit to feature branch | — |
| 005 | Task-builder 006 | Tiered Memory Decay | `feature/006-tiered-memory-decay` |
| 006 | Execute 006 | Run tasks | — |
| 007 | Prod-test 006 | Validate | — |
| 008 | Commit 006 | Git commit to feature branch | — |
| 009 | Task-builder 007 | Skill Extraction | `feature/007-skill-extraction` |
| 010 | Execute 007 | Run tasks | — |
| 011 | Prod-test 007 | Validate | — |
| 012 | Commit 007 | Git commit to feature branch | — |
| 013 | Task-builder 023 | Cross-Repo Delegation | `feature/023-cross-repo-delegation` |
| 014 | Execute 023 | Run tasks | — |
| 015 | Prod-test 023 | Validate | — |
| 016 | Commit 023 | Git commit to feature branch | — |
| 017 | Task-builder 001 | Zep Cloud Research | `feature/001-zep-cloud-research` |
| 018 | Execute 001 | Run tasks | — |
| 019 | Commit 001 | Git commit (research, no prod-test) | — |
| 020 | Task-builder 019 | X Bookmark Scanner | `feature/019-x-bookmark-scanner` |
| 021 | Execute 019 | Run tasks | — |
| 022 | Prod-test 019 | Validate | — |
| 023 | Commit 019 | Git commit to feature branch | — |

## Rules

- Feature branch per backlog item, created from main
- Task-builder stops at step 8 (write only, no execute)
- Execute via sequential task cycling
- Prod-test after execution (skip for RESEARCH-only items)
- Commit only after successful tests pass
- Never merge to main — leave on feature branch
- Target repo: D:\my_ai_projects\isagawa-kernel

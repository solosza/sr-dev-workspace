# Worktree Research

Research and design git worktree isolation for the Isagawa Kernel's execute-pipeline loop.

## Goal

Determine whether Claude Code's native `EnterWorktree` tool can provide isolated execution for pipeline runs, and whether `.claude/state/` file contention can be solved with worktree isolation.

## Deliverables

- `RESEARCH-REPORT.md` — comprehensive findings
- `INTEGRATION-DESIGN.md` — implementation roadmap
- Supporting analysis documents (01-09)

## Context

State file contention between interactive sessions and one-shot agents is a recurring pain point in the kernel. Worktrees could provide working-directory isolation, but don't solve state file isolation unless `.claude/state/` is moved outside the git repo.

See backlog 123 for requirements.

# Design Run-Task.sh Compatibility

## Context

Evaluate whether run-task.sh one-shot mode is compatible with worktree isolation. Confirm that the one-shot agent model (spawned claude -p) works correctly inside a worktree without interfering with the parent session.

## Type

RESEARCH

## Execution

inline

## Dependencies

- Task 005 complete

## Phase Gate

- [ ] Lifecycle design exists

## Requirements

- Review run-task.sh implementation and one-shot mode
- Analyze whether one-shot agents need worktree-aware logic
- Determine if CLAUDECODE env var handling is sufficient
- Document any changes needed
- Confirm compatibility with existing agent spawning

## Acceptance Criteria

- [ ] Created `projects/worktree-research/09-run-task-sh-compatibility.md`
- [ ] One-shot mode analyzed
- [ ] Compatibility assessment documented
- [ ] Any required changes identified
- [ ] Edge cases (nested worktrees) addressed

## Gates Satisfied

BUILD-11

## Completion Signal

When acceptance criteria are met, invoke `/kernel/complete`.

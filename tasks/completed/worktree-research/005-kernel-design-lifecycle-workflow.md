# Design Worktree Lifecycle Workflow

## Context

Document the complete lifecycle for worktree-based pipeline isolation: create worktree at pipeline start, run tasks inside it, merge back to main, cleanup. Include branch strategy and cleanup discipline.

## Type

RESEARCH

## Execution

inline

## Dependencies

- Task 004 complete

## Phase Gate

- [ ] Merge conflict results exist

## Requirements

- Design complete lifecycle workflow
- Document each phase: create, run, merge, cleanup
- Define branch naming and cleanup strategy
- Identify rollback procedures
- Address edge cases (pipeline fails mid-run, worktree already exists)

## Acceptance Criteria

- [ ] Created `projects/worktree-research/07-lifecycle-design.md`
- [ ] Lifecycle phases documented with sequence
- [ ] Branch strategy defined
- [ ] Cleanup discipline specified
- [ ] Edge cases addressed

## Gates Satisfied

BUILD-09

## Completion Signal

When acceptance criteria are met, invoke `/kernel/complete`.

# Research .claude/state/ File Isolation

## Context

Empirically test whether .claude/state/ files are isolated between a parent session and a worktree branch. This is critical for pipeline isolation — if state files are shared, worktree isolation doesn't fully solve the contention problem.

## Type

RESEARCH

## Execution

inline

## Dependencies

- Task 002 complete

## Phase Gate

- [ ] EnterWorktree analysis exists

## Requirements

- Design test scenario: create worktree, modify state file, check parent session
- Execute test and record findings
- Determine if state files are isolated per worktree
- Document assumptions and methodology
- Identify any edge cases or limitations

## Acceptance Criteria

- [ ] Created `projects/worktree-research/03-state-isolation-experiment.md`
- [ ] Created `projects/worktree-research/04-state-isolation-results.md`
- [ ] Test hypothesis and methodology documented
- [ ] Results clearly state whether isolation is confirmed
- [ ] Any gotchas documented (e.g., shared git directory but separate working trees)

## Gates Satisfied

BUILD-05, BUILD-06

## Completion Signal

When acceptance criteria are met, invoke `/kernel/complete`.

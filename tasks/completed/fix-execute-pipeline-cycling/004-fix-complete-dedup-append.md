# Fix complete.md — Check for Duplicate Before Append

## Context
complete.md Mode A and Mode B both say "Add current_task to completed_tasks" but don't check if it's already there. Background agents or retried tasks can cause the same task to be appended twice, inflating the count and causing premature completion detection.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- In `.claude/commands/kernel/complete.md`, in both Mode A (step 1) and Mode B (step 1):
  - Add instruction: "Check that `current_task` is not already in `completed_tasks` before appending. If it is already present, skip the append (do not create duplicates)."

## Acceptance Criteria
- [ ] `grep -qi 'not already\|duplicate\|already in.*completed_tasks\|already present' .claude/commands/kernel/complete.md` exits 0

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

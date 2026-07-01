# Create /kernel/rollback extension command

## Context
The /kernel/rollback command manually reverts a learn event using the compensation pattern (forward-only, not destructive revert). Includes cascade detection.

## Type
BUILD

## Execution
inline

## Dependencies
- 004 (learn-events schema), 015 (learn event recording)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/learn-events.jsonl.schema.json` exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/commands/kernel/rollback.md`
- Command instructions:
  1. Take a learn_event_id as argument
  2. Read learn-events.jsonl, find the event
  3. Show what will be reverted: lesson topic, files modified, git commit hash
  4. Cascade detection: check if any later learn events modified the same files (if so, warn and list conflicts)
  5. If no cascades: create a compensating change (new forward change that undoes the effect)
  6. Record the rollback as a new learn event with status "rollback" and reference to original event
  7. Update original event status to "deprecated" with rollback_event_id
  8. Report what was rolled back
- Compensation pattern: never destructive revert (no git revert), always a forward change
- Installable: copied to workspace `.claude/commands/kernel/rollback.md`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/commands/kernel/rollback.md` exists
- [ ] Command takes learn_event_id as argument
- [ ] Command includes cascade detection logic
- [ ] Command uses compensation pattern (forward change, not revert)
- [ ] Command records rollback as new learn event

## Gates Satisfied
- BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

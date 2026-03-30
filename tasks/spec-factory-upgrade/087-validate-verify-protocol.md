# Verify Protocol Created

## Context
Protocol should reference SSH management layer after domain-setup.

## Type
TEST

## Dependencies
- 086

## Phase Gate
- [ ] run-task.sh completed (task 086)

## Requirements
- Glob for `$WORKSPACE/.claude/protocols/*-protocol.md`
- Read file
- Verify references ssh-management-layer

## Acceptance Criteria
- [ ] Protocol exists and refs SSH (verify: grep 'ssh-management-layer')

## Gates Satisfied
VAL-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

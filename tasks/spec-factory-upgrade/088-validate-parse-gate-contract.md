# Parse Gate Contract

## Context
Extract gates from SSH spec gate-contract.md.

## Type
TEST

## Dependencies
- 087

## Phase Gate
- [ ] Protocol verified (task 087)

## Requirements
- Read gate-contract.md
- Extract gate IDs, methods, pass criteria
- Count gates (expect 20+)

## Acceptance Criteria
- [ ] Gate count > 0 (verify: grep and count)

## Gates Satisfied
VAL-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

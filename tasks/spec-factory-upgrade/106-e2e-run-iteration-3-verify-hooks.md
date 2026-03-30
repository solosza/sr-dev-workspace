# E2E Iteration 3: Verify Hooks

## Context
Verify actions_since_anchor > 0 (hooks firing).

## Type
TEST

## Dependencies
- 105

## Phase Gate
- [ ] Task completed (task 105)

## Requirements
- Read workflow state
- Check actions_since_anchor > 0
- If 0: hooks broken

## Acceptance Criteria
- [ ] actions_since_anchor > 0 (verify: read JSON)

## Gates Satisfied
INT-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

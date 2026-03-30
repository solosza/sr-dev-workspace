# Verify factory hooks match latest

## Context
L2: test each hook.

## Type
TEST

## Execution
agent

## Dependencies
- 027, 028

## Phase Gate
- [ ] Factory resynced (027, 028)

## Requirements
- Pipe test JSON to each hook in C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/. Verify exits 0.

## Acceptance Criteria
- [ ] All hooks pass (verify: run_code)

## Gates Satisfied
FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

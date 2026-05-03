# Prod Test: Pytest Suite

## Context
Level 2: run pytest, all tests must pass.

## Type
TEST

## Dependencies
- 062, 063, 069

## Phase Gate
- [ ] test files (062, 063) and requirements (069) exist

## Requirements
- Install deps
- Run `pytest C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/framework/_reference/tests/ -v`

## Acceptance Criteria
- [ ] pytest exits 0 (verify: run_test)

## Gates Satisfied
PROD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

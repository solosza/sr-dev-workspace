# Write pytest conftest hook for coverage check

## Context
Integrates coverage check into the test pipeline so it runs automatically.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] cli.py exists (006)

## Requirements
- Edit `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/tests/conftest.py` or write a pytest plugin
- Add a session-scoped fixture or hook that runs coverage scan after tests
- Prints coverage summary at end of test run
- Does NOT fail tests — just reports

## Acceptance Criteria
- [ ] conftest.py or plugin has coverage hook (verify: grep 'coverage')

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

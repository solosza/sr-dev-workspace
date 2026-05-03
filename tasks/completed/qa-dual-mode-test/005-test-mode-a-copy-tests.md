# Copy Test Files to Testbed for Mode A

## Context
Copy the framework test files into the testbed so Mode A can run from the framework's own test directory.

## Type
BUILD
## Execution
inline

## Dependencies
- 002, 004

## Phase Gate
- [ ] Deps installed (002), conftest modified (004)

## Requirements
- Copy test subdirectories from `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/tests/` to `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/`
- Include test data: `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/tests/data/`
- Do NOT overwrite the modified conftest.py

## Acceptance Criteria
- [ ] Test files exist in testbed (verify: `test -d C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/automationex1/` or similar)

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

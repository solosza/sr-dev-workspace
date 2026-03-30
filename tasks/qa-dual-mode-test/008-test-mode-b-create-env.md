# Create .env with QA_FRAMEWORK_PATH

## Context
Set the env var so conftest.py resolves framework from the external py-selenium-framework-mcp location instead of the relative path.

## Type
BUILD
## Execution
inline

## Dependencies
- 004

## Phase Gate
- [ ] conftest.py supports env var (task 004)

## Requirements
- Create `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.env` with:
- `QA_FRAMEWORK_PATH=C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework`

## Acceptance Criteria
- [ ] .env exists with QA_FRAMEWORK_PATH pointing to framework (verify: `grep -q 'QA_FRAMEWORK_PATH' C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.env`)

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

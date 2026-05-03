# Run Pytest Mode A (from testbed, no env var)

## Context
Baseline: run tests with conftest.py resolving framework path via default relative path. QA_FRAMEWORK_PATH not set.

## Type
TEST
## Execution
agent

## Dependencies
- 005

## Phase Gate
- [ ] Test files copied (task 005)

## Requirements
- Run `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.venv/Scripts/python -m pytest C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/ -v --tb=short -x 2>&1`
- Do NOT set QA_FRAMEWORK_PATH
- Capture full output

## Acceptance Criteria
- [ ] pytest exits and produces output (verify: run_test)

## Gates Satisfied
TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

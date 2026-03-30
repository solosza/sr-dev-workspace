# Run Pytest Mode B (from testbed, with env var)

## Context
The key test: run the SAME tests from the SAME location but with QA_FRAMEWORK_PATH pointing to the external framework. conftest.py should resolve imports from there.

## Type
TEST
## Execution
agent

## Dependencies
- 005, 008

## Phase Gate
- [ ] Test files in testbed (005), .env created (008)

## Requirements
- Run `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.venv/Scripts/python -m pytest C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/ -v --tb=short -x 2>&1`
- QA_FRAMEWORK_PATH should be loaded from .env by conftest.py
- Capture full output

## Acceptance Criteria
- [ ] pytest exits and produces output (verify: run_test)

## Gates Satisfied
TEST-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

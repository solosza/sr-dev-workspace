# Install Framework Dependencies in Testbed

## Context
Install the QA framework deps so pytest can run.

## Type
BUILD
## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Testbed exists (task 001)

## Requirements
- Run `python -m venv C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.venv` then `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/.venv/Scripts/pip install -r C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/requirements.txt`

## Acceptance Criteria
- [ ] pip install exits 0 (verify: run_code)

## Gates Satisfied
BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

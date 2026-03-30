# Add QA_FRAMEWORK_PATH Override to conftest.py

## Context
The core change: if QA_FRAMEWORK_PATH env var is set, use it instead of the relative path. Modify the copy in the testbed so we do not touch the original.

## Type
BUILD
## Execution
inline

## Dependencies
- 003

## Phase Gate
- [ ] conftest.py logic understood (task 003)

## Requirements
- Copy `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/tests/conftest.py` to `C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/conftest.py` (create tests/ dir if needed)
- Edit the copy: change FRAMEWORK_PATH to `os.environ.get('QA_FRAMEWORK_PATH', str(Path(__file__).parent.parent / 'framework'))`
- Import os if not already imported

## Acceptance Criteria
- [ ] Testbed conftest.py has QA_FRAMEWORK_PATH check (verify: `grep -q 'QA_FRAMEWORK_PATH' C:/Users/solos/my_ai_projects/qa-dual-mode-testbed/tests/conftest.py`)

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

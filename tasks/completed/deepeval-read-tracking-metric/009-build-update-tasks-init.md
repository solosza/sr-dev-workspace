# Update Tasks __init__.py

## Context
Export run_read_compliance_eval from the tasks package so it can be imported as `from framework._reference.tasks import run_read_compliance_eval`.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-write-read-compliance-task

## Phase Gate
- [ ] `framework/_reference/tasks/run_read_compliance_eval.py` exists

## Requirements
- Edit: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/framework/_reference/tasks/__init__.py`
- Add import: `from .run_read_compliance_eval import run_read_compliance_eval, run_read_compliance_from_trace`

## Acceptance Criteria
- [ ] `grep -q "run_read_compliance_eval" framework/_reference/tasks/__init__.py` passes

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

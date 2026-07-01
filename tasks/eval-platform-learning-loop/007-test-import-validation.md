# Test: import validation for metrics modules

## Context
Verify that harness_metrics and architecture_notes are importable from the platform-deepeval framework directory.

## Type
TEST

## Execution
agent

## Dependencies
- 002 (harness_metrics.py), 003 (architecture_notes.py)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` exists
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` exists

## Requirements
- Run: `python -c "import sys; sys.path.insert(0,'D:/my_ai_projects/project_test_repos/platform-deepeval/framework'); from metrics.harness_metrics import make_geval_metric; print('harness_metrics OK')"` — must exit 0
- Run: `python -c "import sys; sys.path.insert(0,'D:/my_ai_projects/project_test_repos/platform-deepeval/framework'); from metrics.architecture_notes import get_notes; print('architecture_notes OK')"` — must exit 0

## Acceptance Criteria
- [ ] `make_geval_metric` imports successfully
- [ ] `get_notes` imports successfully

## Gates Satisfied
- FUNC-01, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

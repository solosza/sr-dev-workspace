# Write test_eval_kernel_minimal.py

## Context
The 17-test eval suite (12 GEval + 5 structural) wired with architecture notes via LLMTestCase.context. Imports from `metrics.harness_metrics` and `metrics.architecture_notes`.

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (harness_metrics.py), 003 (architecture_notes.py), 005 (conftest.py)

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` exists
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` exists
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/conftest.py` exists

## Requirements
- Copy from `D:/my_ai_projects/project_test_repos/eval-kernel-minimal-test/tests/test_eval_kernel_minimal.py`
- Write to `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py`
- Imports must work with the platform-deepeval directory structure (conftest adds framework/ to sys.path)
- Do NOT modify test logic — same 17 tests, same structure

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py` exists
- [ ] File imports `from metrics.harness_metrics import make_geval_metric`
- [ ] File imports `from metrics.architecture_notes import get_notes`

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

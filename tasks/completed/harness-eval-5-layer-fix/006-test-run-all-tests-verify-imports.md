# 006 — Run All Tests and Verify Import Direction

## Type
TEST

## What
Run all pytest tests and verify strict L5→L4→L3→L2→L1→SDK import direction.

## Where
`D:/my_ai_projects/project_test_repos/platform-deepeval`

## Acceptance Criteria
1. `pytest framework/tests/test_harness_eval.py --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -v` passes
2. `pytest framework/tests/test_ab_eval.py --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -v` still passes
3. No `from deepeval` imports exist in L2 (`harness_metrics.py`)
4. No `from deepeval` imports exist in L3 (`run_harness_eval.py`)
5. No `from deepeval` imports exist in L4 (`harness_evaluator.py`)
6. No `from deepeval` imports exist in L5 (`test_harness_eval.py`)
7. Import direction verified via grep: only L1 (`deepeval_interface.py`) imports from `deepeval` SDK

## Commands
```bash
# Verify no direct SDK imports in L2-L5
grep -n "from deepeval" D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py
grep -n "from deepeval" D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tasks/run_harness_eval.py
grep -n "from deepeval" D:/my_ai_projects/project_test_repos/platform-deepeval/framework/roles/harness_evaluator.py
grep -n "from deepeval" D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tests/test_harness_eval.py

# Run tests
PYTHONPATH=D:/my_ai_projects/project_test_repos/platform-deepeval/framework pytest D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tests/ --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -v
```

# Gate Contract — Harness Eval 5-Layer Fix

## Backlog
`docs/backlog/177-qa-fix-harness-eval-5-layer-compliance.md`

## Acceptance Criteria
1. No direct `deepeval` SDK imports in L2 (`harness_metrics.py`) — all access through DeepEvalInterface (L1)
2. L1 (`deepeval_interface.py`) exposes `create_geval_metric()` and test case param constants
3. L3 (`run_harness_eval.py`) imports only from L2
4. L4 (`harness_evaluator.py`) imports only from L3/L2
5. L5 (`test_harness_eval.py`) exists with AAA pattern, parametrized across dimensions
6. Import direction strictly L5→L4→L3→L2→L1→SDK
7. All existing tests (`test_ab_eval.py`) still pass
8. All new harness eval tests pass

## Deliverables
| Layer | File | Action |
|-------|------|--------|
| L1 | `framework/interfaces/deepeval_interface.py` | Add `create_geval_metric()`, expose `LLMTestCaseParams` |
| L2 | `framework/metrics/harness_metrics.py` | Remove direct SDK imports, use L1 |
| L3 | `framework/tasks/run_harness_eval.py` | Verify L2-only imports |
| L4 | `framework/roles/harness_evaluator.py` | Verify L3/L2-only imports |
| L5 | `framework/tests/test_harness_eval.py` | Create with AAA pattern |

## Target
`D:/my_ai_projects/project_test_repos/platform-deepeval` on branch `feature/harness-eval-5-layer`

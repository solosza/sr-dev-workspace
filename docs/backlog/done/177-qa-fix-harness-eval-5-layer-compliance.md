# Fix Harness Eval 5-Layer Compliance

## Status
Open

## Priority
High — harness eval (backlog 162) shipped with direct SDK imports and missing L3/L4/L5 layers, violating the 5-layer architecture it's supposed to enforce

## Summary
The harness eval system delivered by backlog 162 (harness_metrics.py, architecture_notes.py) has 5-layer compliance violations. L2 metrics import directly from `deepeval` SDK instead of going through L1 DeepEvalInterface, and the L3 (EvalTask), L4 (EvalRole), and L5 (test file) layers were never built. Code is isolated on `feature/harness-eval-5-layer` branch in platform-deepeval — must not merge to master until fully compliant.

## Requirements
- **Work on branch:** All changes on `feature/harness-eval-5-layer` in platform-deepeval, not master
- **L2 fix:** Remove direct `from deepeval.metrics import GEval` and `from deepeval.test_case import LLMTestCase, LLMTestCaseParams` from `harness_metrics.py`. Route all SDK access through `DeepEvalInterface` (L1)
- **L3 build:** Create `framework/tasks/harness_eval_task.py` — composes HarnessMetrics (L2) into an EvalTask that evaluates all 5 dimensions for a given harness
- **L4 build:** Create `framework/roles/harness_eval_role.py` — orchestrates the harness eval task(s), manages harness path resolution
- **L5 build:** Create `framework/tests/test_harness_eval.py` — pytest tests using AAA pattern, @pytest.mark.parametrize across dimensions, imports from L4/L3 only
- **Import direction:** Verify strict L5→L4→L3→L2→L1→SDK after all changes
- **Tests pass:** All existing tests (test_ab_eval.py on master) plus new harness eval tests must pass
- **Merge to master:** Only after all 5 layers are compliant and tests pass

## Violations Found

| File | Line | Violation | Required Pattern |
|------|------|-----------|-----------------|
| `framework/metrics/harness_metrics.py` | 13 | `from deepeval.metrics import GEval` — direct SDK import at L2 | Use DeepEvalInterface (L1) |
| `framework/metrics/harness_metrics.py` | 14 | `from deepeval.test_case import LLMTestCase, LLMTestCaseParams` — direct SDK import at L2 | Use DeepEvalInterface (L1) |
| `framework/tasks/` | — | No harness eval task exists (L3 missing) | Create harness_eval_task.py |
| `framework/roles/` | — | No harness eval role exists (L4 missing) | Create harness_eval_role.py |
| `framework/tests/` | — | No harness eval test file (L5 missing) | Create test_harness_eval.py |

## References
- Backlog 162 (source deliverable): `docs/backlog/done/162-kernel-build-eval-platform-learning-loop.md`
- Feature branch: `feature/harness-eval-5-layer` in platform-deepeval
- L1 interface: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/interfaces/deepeval_interface.py`
- 5-layer reference: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/`
- Backlog 175: SSH 5-layer audit (same class of violations)

## Task Builder Input
- **Deliverable:** Harness eval system fully compliant with 5-layer architecture (L1-L5), merged to master
- **Location:** `new-repo:D:/my_ai_projects/project_test_repos/platform-deepeval`
- **Scope:** REFACTOR
- **Constraints:** Work on feature/harness-eval-5-layer branch. Must not break existing test_ab_eval.py on master. Must preserve all 5 GEval dimensions and architecture_notes context system. Import direction must be strictly downward after refactor. Only merge to master when fully compliant.

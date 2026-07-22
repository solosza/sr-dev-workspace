# 001 — Add GEval Factory + LLMTestCaseParams to L1

## Type
BUILD

## What
Add `create_geval_metric()` method and expose `LLMTestCaseParams` via DeepEvalInterface so L2 metrics can access GEval and test case params without importing directly from the deepeval SDK.

## Where
`D:/my_ai_projects/project_test_repos/platform-deepeval/framework/interfaces/deepeval_interface.py`

## Acceptance Criteria
1. `DeepEvalInterface` has a `create_geval_metric(name, criteria, evaluation_params, threshold)` method that returns a `GEval` instance
2. `DeepEvalInterface` exposes `LLMTestCaseParams` as a class attribute or property (e.g., `DeepEvalInterface.TEST_CASE_PARAMS` or importable from the module)
3. `LLMTestCaseParams` is importable from `interfaces.deepeval_interface` (re-exported at module level)
4. Existing `create_custom_metric()` method still works

## Implementation Notes
- `GEval` is already imported in deepeval_interface.py (line 37)
- `LLMTestCaseParams` needs to be added to the import from `deepeval.test_case`
- Re-export `LLMTestCaseParams` at module level so L2 can do `from interfaces.deepeval_interface import LLMTestCaseParams`
- The `create_geval_metric` method wraps `GEval(name=..., criteria=..., evaluation_params=..., threshold=...)`

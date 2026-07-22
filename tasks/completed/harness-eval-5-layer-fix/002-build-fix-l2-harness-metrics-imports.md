# 002 — Fix L2 harness_metrics.py Imports

## Type
BUILD

## What
Remove direct `from deepeval.metrics import GEval` and `from deepeval.test_case import LLMTestCase, LLMTestCaseParams` imports. Replace with imports through DeepEvalInterface (L1).

## Where
`D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py`

## Acceptance Criteria
1. No `from deepeval` imports anywhere in harness_metrics.py
2. `GEval` access goes through `deepeval_interface.create_geval_metric()` or imported from `interfaces.deepeval_interface`
3. `LLMTestCaseParams` imported from `interfaces.deepeval_interface` (not from `deepeval.test_case`)
4. `LLMTestCase` type hint imported from `interfaces.deepeval_interface` (not from `deepeval.test_case`)
5. `make_geval_metric()` function uses the L1 interface to create GEval instances
6. `HarnessMetrics.evaluate()` method still works with the same API

## Implementation Notes
- Replace `from deepeval.metrics import GEval` with access through L1
- Replace `from deepeval.test_case import LLMTestCase, LLMTestCaseParams` with `from interfaces.deepeval_interface import LLMTestCaseParams` and import `LLMTestCase` from L1
- The `make_geval_metric()` function currently creates `GEval(...)` directly — route through `DeepEvalInterface.create_geval_metric()` or import GEval from L1
- Keep all DIMENSION_CRITERIA and DIMENSION_THRESHOLDS unchanged

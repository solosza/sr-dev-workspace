# Task 004: Refactor test_eval_harness.py to L2+L5 Pattern

## Action
Refactor the harness eval test file to use HarnessMetrics (L2) instead of inline GEval creation, and follow the L5 test pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/evals/eval-platform-selenium/tests/test_eval_harness.py` (current non-conforming code)
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tests/test_rag_pipeline.py` for the L5 pattern
3. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` for HarnessMetrics class (task 001 output)
4. Refactor `test_eval_harness.py`:
   - Remove all `from deepeval import assert_test` and `from deepeval.metrics import GEval`
   - Remove all inline criteria strings (they now live in HarnessMetrics via DIMENSION_CRITERIA)
   - Import `HarnessMetrics` from `framework.metrics.harness_metrics`
   - Each test function follows AAA pattern:
     - **Arrange:** create test case, instantiate HarnessMetrics
     - **Act:** call metrics.evaluate(test_case, dimension)
     - **Assert:** assert metrics.is_above_threshold(dimension)
   - Keep `@pytest.mark.parametrize` for command quality (already correct pattern)
   - Keep structural tests (test_skill_completeness, test_settings_wiring, test_reference_resolution) — those are L5 structural checks, not GEval
5. This file is the TEMPLATE — when `/kernel/eval` generates test_eval_harness.py for new harnesses, it should follow this pattern

## Acceptance Criteria
- No `from deepeval` imports in test_eval_harness.py
- No inline criteria strings
- All GEval tests use HarnessMetrics.evaluate() + is_above_threshold()
- AAA pattern in all test functions
- Structural tests (skill_completeness, settings_wiring, reference_resolution) unchanged
- Tests still runnable via `deepeval test run` or `pytest`

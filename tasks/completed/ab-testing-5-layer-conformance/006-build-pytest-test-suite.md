# Task 006: Build pytest Test Suite (L5)

## Action
Create real pytest tests for A/B evaluation following the `_reference/tests/test_rag_pipeline.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tests/test_rag_pipeline.py` for the L5 pattern
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tests/conftest.py` for fixture patterns
3. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tests/test_ab_eval.py` (create `tests/` dir if needed) with:

```python
import pytest
from framework.metrics.ab_metrics import ABMetrics

class TestABEvaluation:
    @pytest.mark.parametrize("metric_name", [
        "compliance", "adherence", "completeness", "following", "drift"
    ])
    def test_ab_metric_scores_REQ_L2(self, metric_name, deepeval_interface):
        """Each AB metric scores between 0 and 1."""
        # Arrange
        test_case = deepeval_interface.create_test_case(
            input="Evaluate this artifact output",
            actual_output="Sample agent output following instructions",
        )
        metrics = ABMetrics(deepeval_interface)

        # Act (mock LLM judge)
        metrics._scores[metric_name] = 0.85

        # Assert
        assert metrics.is_above_threshold(metric_name)

    def test_ab_metrics_evaluate_returns_self_REQ_L2(self, deepeval_interface):
        """ABMetrics.evaluate() returns self for fluent chaining."""
        # Arrange
        metrics = ABMetrics(deepeval_interface)

        # Act (mock)
        metrics._scores = {k: 0.8 for k in ABMetrics.METRIC_CRITERIA}
        result = metrics  # evaluate() should return self

        # Assert
        assert result is metrics
```

4. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tests/conftest.py` with fixtures for deepeval_interface (mocked) and experiment config
5. Tests must use AAA pattern, assert via `ABMetrics.is_above_threshold()` — not raw scores

## Acceptance Criteria
- File exists at `framework/tests/test_ab_eval.py`
- Tests use AAA pattern
- `@pytest.mark.parametrize` over metric names
- Assert via `is_above_threshold()` — not raw score comparison
- conftest.py provides deepeval_interface fixture (mocked for unit tests)
- Import direction: L5 imports L2 (ABMetrics) directly for assertions

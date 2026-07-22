# Task 001: Build ABMetrics Class (L2)

## Action
Create `ABMetrics` Metric Object class following the `_reference/metrics/custom_metrics.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/metrics/custom_metrics.py` for the L2 pattern
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/scorer.py` to extract the 5 criteria strings and understand current scoring
3. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/ab_metrics.py` with:

```python
class ABMetrics:
    # Constants — thresholds per metric
    COMPLIANCE_THRESHOLD = 0.7
    ADHERENCE_THRESHOLD = 0.7
    COMPLETENESS_THRESHOLD = 0.7
    FOLLOWING_THRESHOLD = 0.7
    DRIFT_THRESHOLD = 0.7

    # Criteria strings (moved from scorer.py DEFAULT_METRIC_CRITERIA)
    METRIC_CRITERIA = { ... }

    def __init__(self, thresholds=None): ...
    def evaluate(self, test_case) -> "ABMetrics": ...  # returns self
    def is_above_threshold(self, metric_name) -> bool: ...
    def get_score(self, metric_name) -> float: ...
    def get_detail(self, metric_name) -> dict: ...
```

4. `evaluate()` must use `DeepEvalInterface.measure_metric()` — not raw `metric.measure()`. Accept `deepeval_interface` as constructor arg or method param.
5. Store scores in `self._scores` dict, details in `self._details` dict — same pattern as CustomMetrics

## Acceptance Criteria
- File exists at `framework/metrics/ab_metrics.py`
- Class has 5 threshold constants matching the 5 AB metrics
- `evaluate()` returns `self`
- `is_above_threshold()` returns bool
- No direct `from deepeval` imports — uses DeepEvalInterface
- Criteria strings are the same 5 from scorer.py `DEFAULT_METRIC_CRITERIA`

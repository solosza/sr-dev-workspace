# Task 001: Build HarnessMetrics Class (L2)

## Action
Create a proper L2 Metric Object class that wraps the existing `harness_metrics.py` factory function, following the `_reference/metrics/custom_metrics.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/metrics/custom_metrics.py` for the L2 pattern
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` — this has `make_geval_metric()`, `DIMENSION_CRITERIA`, `DIMENSION_THRESHOLDS` already
3. Add a `HarnessMetrics` class to `harness_metrics.py` (same file, below existing code):

```python
class HarnessMetrics:
    """L2 Metric Object for harness evaluation dimensions."""

    # Use existing DIMENSION_THRESHOLDS as constants
    COMMAND_QUALITY_THRESHOLD = DIMENSION_THRESHOLDS["command_quality"]
    SKILL_COMPLETENESS_THRESHOLD = DIMENSION_THRESHOLDS["skill_completeness"]
    CLAUDEMD_COHERENCE_THRESHOLD = DIMENSION_THRESHOLDS["claudemd_coherence"]
    LOOP_INTEGRITY_THRESHOLD = DIMENSION_THRESHOLDS["loop_integrity"]
    HOOK_COVERAGE_THRESHOLD = DIMENSION_THRESHOLDS["hook_coverage"]

    def __init__(self, deepeval_interface=None, thresholds=None, use_context=False): ...
    def evaluate(self, test_case, dimension) -> "HarnessMetrics": ...  # returns self
    def evaluate_all(self, test_cases_by_dimension) -> "HarnessMetrics": ...
    def is_above_threshold(self, dimension) -> bool: ...
    def get_score(self, dimension) -> float: ...
    def get_detail(self, dimension) -> dict: ...
```

4. `evaluate()` must use `make_geval_metric()` (already exists in same file) to create metrics
5. Uses DeepEvalInterface.measure_metric() for retry logic — not raw metric.measure()

## Acceptance Criteria
- `HarnessMetrics` class added to `framework/metrics/harness_metrics.py`
- Uses existing `DIMENSION_CRITERIA` and `DIMENSION_THRESHOLDS` — no duplication
- Uses `make_geval_metric()` factory — no inline GEval creation
- `evaluate()` returns `self`
- `is_above_threshold()` returns bool

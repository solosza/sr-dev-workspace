# Task 002: Build run_harness_eval Task (L3)

## Action
Create `run_harness_eval()` EvalTask function following the `_reference/tasks/run_rag_eval.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tasks/run_rag_eval.py` for the L3 pattern
2. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tasks/run_harness_eval.py` with:

```python
from framework.metrics.harness_metrics import HarnessMetrics

def run_harness_eval(deepeval_interface, test_case, dimension, thresholds=None, use_context=False):
    """Run harness evaluation for one dimension. Returns None."""
    metrics = HarnessMetrics(deepeval_interface, thresholds, use_context).evaluate(test_case, dimension)
    test_case._eval_results = {dimension: metrics}
    return None
```

3. Ensure `framework/tasks/__init__.py` exists (may have been created by pipeline 172)

## Acceptance Criteria
- File exists at `framework/tasks/run_harness_eval.py`
- Function composes HarnessMetrics (L2), returns None
- Import direction: L3 imports L2 only

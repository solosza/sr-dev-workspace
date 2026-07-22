# Task 002: Build run_ab_eval Task (L3)

## Action
Create `run_ab_eval()` EvalTask function following the `_reference/tasks/run_rag_eval.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/tasks/run_rag_eval.py` for the L3 pattern
2. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tasks/run_ab_eval.py` (create `tasks/` dir if needed) with:

```python
from framework.metrics.ab_metrics import ABMetrics

def run_ab_eval(deepeval_interface, test_case_a, test_case_b, thresholds=None):
    """Score both variants using ABMetrics. Returns None."""
    metrics_a = ABMetrics(deepeval_interface, thresholds).evaluate(test_case_a)
    metrics_b = ABMetrics(deepeval_interface, thresholds).evaluate(test_case_b)

    # Store on test cases for assertion
    test_case_a._eval_results = {"ab_metrics": metrics_a}
    test_case_b._eval_results = {"ab_metrics": metrics_b}
    return None
```

3. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/tasks/__init__.py` if it doesn't exist

## Acceptance Criteria
- File exists at `framework/tasks/run_ab_eval.py`
- Function composes ABMetrics (L2), returns None
- Import direction: L3 imports L2 only
- No direct DeepEval SDK imports

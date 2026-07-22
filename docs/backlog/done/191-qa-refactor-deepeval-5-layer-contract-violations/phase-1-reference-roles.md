# Phase 1: Fix _reference/ Roles

## Status
NEW

## Location
`platform-deepeval/framework/_reference/roles/`

## What To Fix

All 4 `_reference/` roles return dicts instead of `None`. Must match platform-selenium's canonical pattern.

### Canonical Pattern (platform-selenium)

```python
class EmployeeManager:
    """
    - NO return values
    """
    def __init__(self, browser_interface):
        self.employee_management_tasks = EmployeeManagementTasks(browser_interface)

    def create_employee(self, name, description="", capabilities="") -> None:
        self.employee_management_tasks.login(...)
        self.employee_management_tasks.create_employee(...)
```

### Files To Fix

| File | Current Violation | Fix |
|------|-------------------|-----|
| `rag_evaluator.py:15-44` | `evaluate_pipeline()` returns `{"test_cases": results, ...}` | Return `None`. Store state on `self.metrics` dict. Add `self.test_cases` list. |
| `agent_evaluator.py:~40` | `evaluate_pipeline()` returns dict | Same pattern |
| `security_evaluator.py:17-54` | `evaluate_pipeline()` returns dict | Same pattern |
| `compliance_evaluator.py:~44` | `evaluate_pipeline()` returns dict | Same pattern |

### Target Pattern (after fix)

```python
class RAGEvaluator:
    """
    - @autologger("Role") on workflow methods
    - NO return values
    """
    def __init__(self, deepeval_interface):
        self.deepeval_interface = deepeval_interface
        self.metrics = {}       # State holder: {dimension: MetricObject}
        self.test_cases = []    # Evaluated test cases

    def evaluate_pipeline(self, dataset, pipeline_fn, thresholds=None) -> None:
        """Run full RAG eval. NO return value. State on self.metrics."""
        for golden in dataset:
            actual_output = pipeline_fn(golden["input"])
            test_case = self.deepeval_interface.create_test_case(...)
            run_rag_eval(self.deepeval_interface, test_case, thresholds)
            self.test_cases.append(test_case)
        # NO return

    # State-check methods (analogous to page object boolean methods)
    def is_dimension_passing(self, dimension: str) -> bool:
        """Check if a metric dimension is above threshold."""
        metric = self.metrics.get(dimension)
        return metric.is_above_threshold(dimension) if metric else False

    def get_score(self, dimension: str) -> float:
        """Get raw score for a dimension."""
        metric = self.metrics.get(dimension)
        return metric.get_score(dimension) if metric else 0.0

    def get_count(self) -> int:
        """Number of test cases evaluated."""
        return len(self.test_cases)
```

### Acceptance Criteria
- [ ] All 4 roles return `None` with `-> None` type hint
- [ ] All 4 roles have `"""NO return values"""` in docstring
- [ ] All 4 roles have `self.metrics` dict and `self.test_cases` list
- [ ] All 4 roles expose `is_dimension_passing()`, `get_score()`, `get_count()`
- [ ] No `return {...}` statements remain

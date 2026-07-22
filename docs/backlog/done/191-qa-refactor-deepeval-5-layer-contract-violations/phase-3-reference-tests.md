# Phase 3: Fix _reference/ Tests

## Status
NEW

## Location
`platform-deepeval/framework/_reference/tests/`

## What To Fix

Tests mock scores by directly setting `metrics._scores["..."] = 0.95` instead of calling `evaluate()` against mock test cases. This bypasses the metric's own evaluation logic.

### Current Violation Pattern

```python
# WRONG — directly sets _scores, bypasses evaluate()
metrics = SecurityMetrics()
metrics._scores["PromptInjectionResistance"] = 0.95  # VIOLATION
metrics._details["PromptInjectionResistance"] = {...}
assert metrics.is_above_threshold("PromptInjectionResistance")
```

### Canonical Pattern (platform-selenium tests)

```python
# Tests assert on page object state-check methods
# AAA: Arrange (create role), Act (call role workflow), Assert (query state)
employee_manager.create_employee(name=employee_name, ...)
assert self.employees_page.is_employee_displayed_in_list(employee_name)
```

### Target Pattern (after fix)

```python
# Option A: Mock GEval.measure at the metric boundary, call evaluate()
from unittest.mock import patch, MagicMock

def test_injection_resistance(self, scenario, deepeval_interface):
    # Arrange
    test_case = deepeval_interface.create_test_case(
        input=scenario["input"],
        actual_output=scenario["expected_output"],
        expected_output=scenario["expected_output"],
    )
    metrics = SecurityMetrics()

    # Act — mock at GEval boundary, but call evaluate()
    with patch.object(GEval, 'measure') as mock_measure:
        mock_measure.return_value = None
        # Simulate GEval setting score/reason on the metric object
        def side_effect(tc):
            # GEval sets .score and .reason on itself
            pass
        mock_measure.side_effect = side_effect
        metrics.evaluate(test_case)  # CORRECT: call evaluate(), not set _scores

    # Assert via state-check methods
    assert metrics.is_above_threshold("PromptInjectionResistance")
```

### Files To Fix

| File | Violation | Fix |
|------|-----------|-----|
| `test_prompt_injection.py:27-29` | `metrics._scores["..."] = 0.95` | Mock `GEval.measure`, call `metrics.evaluate()` |
| `test_prompt_injection.py:61-63` | Same `_scores` direct set | Same fix |
| `test_rag_pipeline.py` | Check for `_scores` direct access | Same fix |
| `test_hook_bypass.py` | Check for `_scores` direct access | Same fix |

### Acceptance Criteria
- [ ] No test directly sets `metrics._scores` or `metrics._details`
- [ ] All tests call `metrics.evaluate(test_case)` (with mocked GEval.measure)
- [ ] All assertions use state-check methods (`is_above_threshold`, `get_score`)
- [ ] AAA pattern preserved: Arrange (create metric + test case), Act (evaluate), Assert (state check)

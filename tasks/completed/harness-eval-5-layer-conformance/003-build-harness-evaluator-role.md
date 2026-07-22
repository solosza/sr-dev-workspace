# Task 003: Build HarnessEvaluator Role (L4)

## Action
Create `HarnessEvaluator` role class following the `_reference/roles/rag_evaluator.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/roles/rag_evaluator.py` for the L4 pattern
2. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/roles/harness_evaluator.py` with:

```python
from framework.tasks.run_harness_eval import run_harness_eval

class HarnessEvaluator:
    def __init__(self, deepeval_interface): ...

    def evaluate_harness(self, harness_root, dimensions=None, thresholds=None):
        """Orchestrate harness eval across all dimensions.

        Discovers commands, skills, hooks, CLAUDE.md from harness_root.
        Creates test cases per dimension.
        Calls run_harness_eval for each.

        Returns:
            dict with test_cases, dimension_scores, count, eval_type
        """
```

3. Ensure `framework/roles/__init__.py` exists (may have been created by pipeline 172)

## Acceptance Criteria
- File exists at `framework/roles/harness_evaluator.py`
- Class composes run_harness_eval (L3), not HarnessMetrics (L2) directly
- Handles harness discovery (reads commands, skills, hooks, CLAUDE.md)
- Import direction: L4 imports L3 only

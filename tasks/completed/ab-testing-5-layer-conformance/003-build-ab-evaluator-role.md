# Task 003: Build ABEvaluator Role (L4)

## Action
Create `ABEvaluator` role class following the `_reference/roles/rag_evaluator.py` pattern.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/roles/rag_evaluator.py` for the L4 pattern
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/runner.py` and `reporter.py` to understand the current orchestration
3. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/roles/ab_evaluator.py` (create `roles/` dir if needed) with:

```python
from framework.tasks.run_ab_eval import run_ab_eval

class ABEvaluator:
    def __init__(self, deepeval_interface): ...

    def evaluate_experiment(self, config, variant_a_outputs, variant_b_outputs, artifact_content):
        """Orchestrate: score all runs via run_ab_eval, collect results.

        Args:
            config: ExperimentConfig
            variant_a_outputs: list of output strings from flat variant
            variant_b_outputs: list of output strings from tiered variant
            artifact_content: the artifact text used as input context

        Returns:
            dict with test_cases_a, test_cases_b, count, eval_type
        """
```

4. Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/roles/__init__.py` if it doesn't exist
5. ABEvaluator composes L3 run_ab_eval — does NOT import L2 directly

## Acceptance Criteria
- File exists at `framework/roles/ab_evaluator.py`
- Class composes run_ab_eval (L3), not ABMetrics (L2) directly
- Import direction: L4 imports L3 only
- Does NOT replace ABRunner or ABReporter — those handle execution and reporting, not evaluation
- Returns structured results dict

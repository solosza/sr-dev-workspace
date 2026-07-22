# Task 005: Update ab_testing __init__.py Exports

## Action
Update the ab_testing package __init__.py to export new L2/L3/L4 components and ensure import paths work.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/__init__.py`
2. Update exports to include ABMetrics, run_ab_eval, ABEvaluator alongside existing exports
3. Verify import paths work by checking that:
   - `from framework.metrics.ab_metrics import ABMetrics` resolves
   - `from framework.tasks.run_ab_eval import run_ab_eval` resolves
   - `from framework.roles.ab_evaluator import ABEvaluator` resolves
   - Existing imports still work: `from framework.ab_testing import VariantGenerator, ABRunner, ABScorer, ABReporter, ExperimentConfig`

## Acceptance Criteria
- `__init__.py` updated with new imports
- All existing exports preserved
- No circular imports

# Task 001: Create ab_testing Package

## Action
Create the `ab_testing/` package directory inside `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/`.

## Steps
1. Create directory: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/`
2. Create `__init__.py` with imports for the public API:
   ```python
   from .variant_generator import VariantGenerator
   from .runner import ABRunner
   from .scorer import ABScorer
   from .reporter import ABReporter
   from .experiment_config import ExperimentConfig
   ```

## Acceptance Criteria
- `framework/ab_testing/__init__.py` exists
- Imports are present (they will fail until modules are created — that's expected)

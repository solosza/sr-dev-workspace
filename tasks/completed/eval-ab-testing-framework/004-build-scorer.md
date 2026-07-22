# Task 004: Build scorer.py

## Action
Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/scorer.py`.

## Requirements

Implements the `ABScorer` class:

1. `__init__(self, config: ExperimentConfig)` — takes config with metric list and judge model
2. `score_pair(self, output_a: str, output_b: str, artifact_content: str, run_id: int) -> dict` — scores both outputs against the artifact using GEval metrics, returns per-metric scores
3. `score_all_runs(self, results_dir: Path, artifact_content: str) -> list[dict]` — iterates all run directories, scores each pair

### Metrics (dynamically created from config)
Each metric is a GEval instance with:
- `name`: metric name (e.g., "Pattern Compliance")
- `criteria`: metric-specific evaluation criteria
- `evaluation_params`: `[LLMTestCaseParams.ACTUAL_OUTPUT]`
- `threshold`: 0.0 (no pass/fail — we're comparing, not gating)
- `model`: from config (default `gpt-4o-mini`)

### Default Metrics
| Metric | Criteria |
|--------|----------|
| Pattern Compliance | Did the output follow naming conventions and architecture rules stated in the artifact? |
| Reference Adherence | Did the agent use patterns from reference files vs. hallucinating its own approach? |
| Completeness | Did the agent cover all required elements specified in the artifact? |
| Instruction Following | Did the agent follow steps in order, skip none, and improvise nothing? |
| Drift Rate | How far did the output deviate from the artifact's prescribed approach? |

### Output Format
```python
{
    "run_id": 1,
    "scores": {
        "compliance": {"variant_a": 0.72, "variant_b": 0.88, "delta": 0.16},
        "adherence": {"variant_a": 0.65, "variant_b": 0.81, "delta": 0.16},
        ...
    }
}
```

## Acceptance Criteria
- File exists at the specified path
- `ABScorer` class with `score_all_runs()` method
- Uses DeepEval GEval (import from deepeval.metrics)
- Metrics are dynamically created from config, not hardcoded

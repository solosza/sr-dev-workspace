# Task 006: Build experiment_config.py

## Action
Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/experiment_config.py`.

## Requirements

Implements the `ExperimentConfig` dataclass:

```python
@dataclass
class ExperimentConfig:
    artifact: str                    # artifact name (e.g., "check-data-engine")
    source: Path                     # source repo path
    mode: str = "ab"                 # always "ab" for A/B experiments
    runs: int = 5                    # number of iterations
    model: str = "claude-sonnet-4-6" # model for claude -p runs
    judge_model: str = "gpt-4o-mini" # model for GEval scoring
    metrics: list[str] = field(default_factory=lambda: [
        "compliance", "adherence", "completeness", "following", "drift"
    ])
    thresholds: dict = field(default_factory=lambda: {
        "significant_delta": 0.05,
        "win_rate_threshold": 0.67
    })
    task_prompt: str | None = None   # if None, auto-generate
    output_dir: Path | None = None   # if None, use evals/eval-ab-<artifact>/
```

### Methods
1. `from_json(cls, path: Path) -> ExperimentConfig` — load from experiment-config.json
2. `to_json(self, path: Path)` — save to experiment-config.json
3. `resolve_output_dir(self) -> Path` — returns `D:/my_ai_projects/project_test_repos/evals/eval-ab-<artifact>/`
4. `get_metric_criteria(self) -> dict[str, str]` — returns criteria text for each metric name

## Acceptance Criteria
- File exists at the specified path
- `ExperimentConfig` dataclass with all fields
- JSON serialization/deserialization works
- Default values are sensible

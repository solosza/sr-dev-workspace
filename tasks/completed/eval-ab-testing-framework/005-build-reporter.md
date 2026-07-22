# Task 005: Build reporter.py

## Action
Create `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/reporter.py`.

## Requirements

Implements the `ABReporter` class:

1. `__init__(self, config: ExperimentConfig)` — takes config with thresholds
2. `compute_stats(self, scored_runs: list[dict]) -> dict` — computes per-metric statistics across N runs
3. `determine_verdict(self, stats: dict) -> str` — applies verdict logic
4. `generate_report(self, stats: dict, verdict: str, output_path: Path)` — writes `ab-report.md`
5. `write_scores_json(self, scored_runs: list[dict], output_path: Path)` — writes `scores.json`
6. `append_score_history(self, stats: dict, verdict: str, history_path: Path)` — appends to source repo score history

### Statistical Summary (per metric)
- Mean delta: `mean(score_b - score_a)` across runs
- Std delta: `std(score_b - score_a)`
- Effect size: Cohen's d = `mean_delta / pooled_std`
- Win rate: `count(delta > 0) / N`

### Verdict Logic
| Condition | Verdict |
|-----------|---------|
| Mean delta > `significant_delta` AND win rate ≥ `win_rate_threshold` | **Tiered is better** |
| Mean delta < `-significant_delta` AND win rate ≤ `1 - win_rate_threshold` | **Flat is better** |
| Otherwise | **No significant difference** |

Thresholds from `config.thresholds` (defaults: `significant_delta=0.05`, `win_rate_threshold=0.67`).

### Report Format (ab-report.md)
- Header with experiment metadata (artifact, source, date, N runs, model)
- Per-metric table: mean_a, mean_b, mean_delta, std_delta, effect_size, win_rate
- Overall verdict with reasoning
- Score distribution visualization (ASCII bar chart)
- Raw data reference (path to scores.json)

## Acceptance Criteria
- File exists at the specified path
- `ABReporter` class with `generate_report()` method
- Uses only stdlib math (no numpy dependency)
- Report is readable markdown

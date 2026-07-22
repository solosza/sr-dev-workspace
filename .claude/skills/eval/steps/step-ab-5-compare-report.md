# Step AB-5: Compare and Report

Compute statistics, determine verdict, and generate the A/B experiment report using `ABReporter` from `platform-deepeval/framework/ab_testing/reporter.py`.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `scored_runs` | Output of Step AB-4 | List of dicts with `run_id`, `scores`, `deltas` |
| `config.thresholds` | Experiment config | `{ "significant_delta": 0.05, "win_rate_threshold": 0.67 }` |
| `output_dir` | Eval working directory | `evals/eval-domain-setup/results/` |
| `source_path` | Original source repo | Path to source repo for score history |

## Procedure

1. **Instantiate ABReporter:**
   ```python
   from framework.ab_testing.reporter import ABReporter

   reporter = ABReporter(config=experiment_config)
   ```

2. **Compute statistics:**
   ```python
   stats = reporter.compute_stats(scored_runs)
   ```
   Per-metric: mean delta, std delta, Cohen's d effect size, win rate.

3. **Determine verdict:**
   ```python
   verdict = reporter.determine_verdict(stats)
   ```
   Returns one of: `"tiered_better"`, `"flat_better"`, `"no_significant_difference"`.

4. **Generate report:**
   ```python
   reporter.generate_report(
       stats=stats,
       verdict=verdict,
       output_path=Path(output_dir) / "ab-report.md"
   )
   ```

5. **Write scores JSON:**
   ```python
   reporter.write_scores_json(
       scored_runs=scored_runs,
       output_path=Path(output_dir) / "scores.json"
   )
   ```

6. **Append score history:**
   ```python
   reporter.append_score_history(
       stats=stats,
       verdict=verdict,
       history_path=Path(source_path) / "ab-score-history.json"
   )
   ```

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| GAB5.1 | Report exists | `(output_dir / "ab-report.md").exists()` | True |
| GAB5.2 | Scores JSON exists | `(output_dir / "scores.json").exists()` | True |
| GAB5.3 | Valid verdict | `verdict in {"tiered_better", "flat_better", "no_significant_difference"}` | True |
| GAB5.4 | History appended | `ab-score-history.json` in source repo updated | True |

All checks must pass before reporting results.

## Final Output

Print to user:
```
A/B Experiment Complete
Verdict: [verdict]
Mean delta: [mean_delta across metrics]
Win rate: [win_rate]
Report: [path to ab-report.md]
```

## Error Handling

| Failure | Action |
|---------|--------|
| Empty scored_runs | Report error — cannot compute stats with 0 runs |
| History file locked/missing | Create new history file, log warning |
| Stats computation error | Report raw scores without statistical summary |

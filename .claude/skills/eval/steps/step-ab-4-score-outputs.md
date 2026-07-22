# Step AB-4: Score Outputs

Score all variant outputs from Step AB-3 using `ABScorer` from `platform-deepeval/framework/ab_testing/scorer.py`.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `results_dir` | Output of Step AB-3 | `evals/eval-domain-setup/results/` |
| `artifact_content` | Output of Step AB-1 | Flattened/tiered skill content |
| `config.metrics` | Experiment config | `["completeness", "structure", "correctness"]` |
| `config.judge_model` | Experiment config | `"gpt-4o"` |

## Pre-Scoring: API Key Validation

Before scoring, verify the OpenAI API key is valid (lesson from 2026-06-25 — GEval requires working key):

```python
import os
from openai import OpenAI

def validate_api_key():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set. Cannot run GEval scoring.")
    try:
        OpenAI().models.list()
    except Exception as e:
        raise RuntimeError(f"OPENAI_API_KEY invalid: {e}. Fix key before scoring.")
```

If validation fails: report error, skip GEval scoring, return empty scores with `error` field populated.

## Procedure

1. **Validate API key:**
   ```python
   validate_api_key()  # Raises if key missing/invalid
   ```

2. **Instantiate ABScorer:**
   ```python
   from framework.ab_testing.scorer import ABScorer

   scorer = ABScorer(
       metrics=config.metrics,
       judge_model=config.judge_model
   )
   ```

3. **Score all runs:**
   ```python
   scored_results = scorer.score_all_runs(
       results_dir=results_dir,
       artifact_content=artifact_content
   )
   ```

4. **Per-run scoring:**
   For each run `i` in `results_dir/run-{i}/`:
   - Read `variant-a-output.md` and `variant-b-output.md`
   - Score each variant against each metric using GEval (LLM-as-judge)
   - Compute per-metric delta: `delta = score_b - score_a`
   - Write `results/run-{i}/scores.json`

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| GAB4.1 | All runs scored | `len(scored_results) == total_runs` | True |
| GAB4.2 | No null scores | Every metric score is numeric, not None | True |
| GAB4.3 | Deltas computed | Every scored run has `deltas` dict | True |
| GAB4.4 | Scores file written | `results/run-{i}/scores.json` exists per run | True |

All checks must pass before transitioning to Step AB-5.

## Error Handling

| Failure | Action |
|---------|--------|
| API key invalid | Skip GEval scoring. Return results with `error: "api_key_invalid"`. |
| GEval timeout (> 60s per metric) | Record timeout for that metric. Score remaining metrics. |
| Partial scoring (some metrics fail) | Keep successful scores. Record failed metrics in `errors` list. |
| Output file missing/empty | Score as 0 for all metrics. Record `warning: "empty_output"`. |

## Output

- `scored_results`: list of dicts with `run_id`, `variant`, `scores`, `deltas`, `errors`
- Per-run `scores.json` written to `results_dir/run-{i}/`
- State transition: `iterations_complete` -> `scoring_complete` -> ready for Step AB-5

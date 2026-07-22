# Scoring and Metrics

## Status
NEW

## Location
`platform-deepeval/framework/ab_testing/scorer.py`

## What It Does

Scores both variant outputs using DeepEval GEval metrics, produces paired comparisons, and computes statistical summaries.

## Metrics

| Metric | What It Measures | Criteria |
|--------|-----------------|----------|
| **Pattern Compliance** | Did the output follow naming conventions, architecture rules from the artifact? | Check output against artifact's stated rules, conventions, patterns |
| **Reference Adherence** | Did the agent use patterns from reference files vs. hallucinating its own? | Compare output structure/patterns to reference files in the artifact |
| **Completeness** | Did the agent cover all required elements specified in the artifact? | Check every step/requirement in artifact has corresponding output |
| **Instruction Following** | Did the agent follow steps in order, skip none, improvise nothing? | Sequence alignment between artifact steps and output actions |
| **Drift Rate** | How far did the output deviate from the protocol? | Semantic distance between output and artifact's prescribed approach |

All metrics use GEval with `gpt-4o-mini` as judge (consistent with existing eval platform).

## Scoring Approach

```python
for run_id in range(1, N+1):
    output_a = read(f"results/run-{run_id}/variant-a-output.md")
    output_b = read(f"results/run-{run_id}/variant-b-output.md")

    for metric in [compliance, adherence, completeness, following, drift]:
        score_a = geval(output_a, metric, artifact_content)
        score_b = geval(output_b, metric, artifact_content)
        delta = score_b - score_a  # positive = tiered is better

        record(run_id, metric, score_a, score_b, delta)
```

## Statistical Summary

For each metric across N runs:

| Stat | Formula | Purpose |
|------|---------|---------|
| Mean delta | `mean(score_b - score_a)` | Average improvement from tiered |
| Std delta | `std(score_b - score_a)` | Consistency of improvement |
| Effect size | `mean_delta / pooled_std` | Cohen's d — practical significance |
| Win rate | `count(delta > 0) / N` | How often tiered beats flat |

## Verdict Logic

| Condition | Verdict |
|-----------|---------|
| Mean delta > 0.05 AND win rate ≥ 0.67 | **Tiered is better** |
| Mean delta < -0.05 AND win rate ≤ 0.33 | **Flat is better** |
| Otherwise | **No significant difference** |

Thresholds are configurable in experiment config.

## Dependencies
- DeepEval with GEval
- OPENAI_API_KEY for LLM-as-judge
- numpy or stdlib for stats (avoid heavy deps)

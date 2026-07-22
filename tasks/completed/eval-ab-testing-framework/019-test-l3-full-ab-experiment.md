# Task 019: L3 Test — Full A/B Experiment (1 Run)

## Action
Run a complete A/B experiment against check-data-engine with N=1 to verify the full pipeline works end-to-end.

## Steps

1. Create experiment config:
   ```python
   from framework.ab_testing import ExperimentConfig
   config = ExperimentConfig(
       artifact="check-data-engine",
       source=Path("D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa"),
       runs=1,  # single run for L3 test
       model="claude-sonnet-4-6",
       judge_model="gpt-4o-mini"
   )
   ```

2. Run full pipeline:
   - Generate variants (VariantGenerator)
   - Auto-generate task prompt (or use a simple provided prompt)
   - Run 1 iteration of both variants (ABRunner)
   - Score outputs (ABScorer)
   - Generate report (ABReporter)

3. Verify outputs:
   - `evals/eval-ab-check-data-engine/variants/flat/` exists
   - `evals/eval-ab-check-data-engine/variants/tiered/` exists
   - `evals/eval-ab-check-data-engine/results/run-1/variant-a-output.md` exists and non-empty
   - `evals/eval-ab-check-data-engine/results/run-1/variant-b-output.md` exists and non-empty
   - `evals/eval-ab-check-data-engine/results/scores.json` exists with per-metric scores
   - `evals/eval-ab-check-data-engine/results/ab-report.md` exists with verdict
   - Verdict is one of: "Tiered is better", "Flat is better", "No significant difference"

## Acceptance Criteria
- Full pipeline completes without error
- All output files exist and are non-empty
- Scores are between 0.0 and 1.0
- Report contains a verdict
- This proves the A/B testing framework works end-to-end

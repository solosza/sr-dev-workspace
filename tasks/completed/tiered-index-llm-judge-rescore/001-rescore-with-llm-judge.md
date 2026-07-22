# Task 001: Rescore with LLM Judge

## Objective
Re-score the 30 existing model outputs from the 60K tiered index experiment using gpt-4o-mini as LLM judge, then regenerate statistical reports.

## Context
- The 60K experiment ran successfully (30 outputs in `60k/results/`)
- Task 019 was skipped because OpenAI API was unavailable
- OpenAI API is now working (sk-proj-... key confirmed)
- The 12K baseline used gpt-4o-mini as judge — we should match that for comparability

## Instructions

1. Read the experiment config: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/experiment-config.json`
2. Read the existing heuristic scorer: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/heuristic_scorer.py`
3. Read the 12K baseline's LLM judge implementation for reference: check `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/` for the original scoring approach
4. Read all 30 run output files in `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/`
5. For each output file, score with gpt-4o-mini using the same 5 metrics: compliance, adherence, completeness, following, drift
6. Write scores to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/scores-llm-judge.json`
7. Regenerate statistical report: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/statistical-report-llm-judge.md`
8. Regenerate baseline comparison against 12K: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/baseline-comparison-llm-judge.md`
9. Compare heuristic vs LLM-judge scores — note any divergence
10. Update final report if conclusions change: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/tiered-index-threshold-research/final-report.md`

## Key Constraint
- Use gpt-4o-mini as judge (matches 12K baseline)
- Do NOT re-run the model prompts — only re-score existing outputs
- Keep original heuristic scores intact (scores.json) — write new file (scores-llm-judge.json)

## Acceptance Criteria
- [ ] All 30 outputs scored by gpt-4o-mini
- [ ] scores-llm-judge.json written with per-run, per-metric scores
- [ ] Statistical report regenerated with LLM judge scores
- [ ] Baseline comparison regenerated
- [ ] Final report updated if conclusions differ

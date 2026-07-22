# Task 011: Create step-ab-4-score-outputs.md

## Action
Create `.claude/skills/eval/steps/step-ab-4-score-outputs.md`.

## Content
Step file for A/B mode — scores all variant outputs using ABScorer.

Include:
- Input table (results_dir, artifact_content, config.metrics, config.judge_model)
- Pre-scoring: verify OPENAI_API_KEY is valid (lesson from 2026-06-25)
- Procedure: instantiate ABScorer, call score_all_runs()
- Output: list of scored run dicts with per-metric scores and deltas
- Verification: all runs scored, no null scores, deltas computed
- Error handling: API key invalid, GEval timeout, partial scoring

## Acceptance Criteria
- File exists at `.claude/skills/eval/steps/step-ab-4-score-outputs.md`
- References `platform-deepeval/framework/ab_testing/scorer.py`
- Includes API key validation step
- Under 100 lines

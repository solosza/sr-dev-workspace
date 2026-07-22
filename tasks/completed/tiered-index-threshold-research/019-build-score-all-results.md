# Score All Results with ABScorer + GEval (gpt-4o)

## Context
Run the ABScorer from the refactored 5-layer framework against all 30 output files, using gpt-4o as the LLM judge. This produces per-run, per-metric scores for all 3 task types.

## Type
BUILD

## Execution
inline

## Dependencies
- 016-build-run-sequential-ab
- 017-build-run-precision-ab
- 018-build-run-crossref-ab

## Phase Gate
- [ ] At least 10 files in `results/sequential-*.txt`
- [ ] At least 10 files in `results/precision-*.txt`
- [ ] At least 10 files in `results/crossref-*.txt`

## Requirements
- Verify OPENAI_API_KEY is valid: `python -c "from openai import OpenAI; OpenAI().models.list()"`
- Use ABScorer from `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/ab_testing/scorer.py`
- Set PYTHONPATH to `D:/my_ai_projects/project_test_repos/platform-deepeval/framework`
- For each task type (sequential, precision, crossref):
  - Read flat outputs (run 1-5) and tiered outputs (run 1-5)
  - Read the corresponding corpus file as artifact_content
  - Score each pair with ABScorer using gpt-4o as model
  - Metrics: compliance, adherence, completeness, following, drift
- Aggregate all scores into `results/scores.json` with structure:
  ```json
  {
    "task_types": {
      "sequential": { "runs": [...] },
      "precision": { "runs": [...] },
      "crossref": { "runs": [...] }
    }
  }
  ```
- Config for DeepEvalInterface: `{"model": "gpt-4o", "threshold": 0.5}`
- Import pattern: `from ab_testing.scorer import ABScorer` (PYTHONPATH = framework/)

## Acceptance Criteria
- [ ] `results/scores.json` exists and contains scores for all 3 task types
- [ ] Each task type has 5 runs with both flat and tiered scores
- [ ] All 5 metrics present per run

## Gates Satisfied
- FUNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

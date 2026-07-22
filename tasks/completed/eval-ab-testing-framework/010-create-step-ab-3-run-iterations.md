# Task 010: Create step-ab-3-run-iterations.md

## Action
Create `.claude/skills/eval/steps/step-ab-3-run-iterations.md`.

## Content
Step file for A/B mode — runs N iterations of both variants via ABRunner.

Include:
- Input table (flat_path, tiered_path, prompt, config.runs, output_dir)
- Procedure: instantiate ABRunner, call run_experiment()
- Sequential execution (run A then B for each iteration)
- Output structure: results/run-N/variant-{a,b}-output.md + metadata.json
- Verification: all N*2 output files exist, no empty outputs
- Error handling: claude -p failures, timeouts, rate limits

## Acceptance Criteria
- File exists at `.claude/skills/eval/steps/step-ab-3-run-iterations.md`
- References `platform-deepeval/framework/ab_testing/runner.py`
- Under 100 lines

# Task 012: Create step-ab-5-compare-report.md

## Action
Create `.claude/skills/eval/steps/step-ab-5-compare-report.md`.

## Content
Step file for A/B mode — computes statistics, determines verdict, generates report.

Include:
- Input table (scored_runs, config.thresholds, output_dir, source_path)
- Procedure: instantiate ABReporter, call compute_stats(), determine_verdict(), generate_report()
- Outputs: ab-report.md, scores.json, append to ab-score-history.json in source repo
- Verification: report file exists, verdict is one of three valid values
- Final output to user: print verdict + key stats

## Acceptance Criteria
- File exists at `.claude/skills/eval/steps/step-ab-5-compare-report.md`
- References `platform-deepeval/framework/ab_testing/reporter.py`
- Under 100 lines

# Write Daily Scan Task Definitions

## Type
BUILD

## Description
Create task files that run-task.sh will execute for the daily fraud scan pipeline.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\tasks\daily-scan\` directory with:

`000-index.md`:
- Task index for daily scan pipeline

`001-run-pattern-discovery.md`:
- Execute Layer 0: scan sources for new fraud cases
- `python -m src.pipeline.layer0_pattern_discovery`

`002-run-awards-ingest.md`:
- Execute Layer 1: pull new awards from USASpending
- `python -m src.pipeline.layer1_awards_ingest`

`003-run-entity-verification.md`:
- Execute Layers 2-4: verify entities, analyze expenses, OSINT
- `python -m src.pipeline.pipeline_runner --layers 2,3,4`

`004-run-scoring-and-cases.md`:
- Execute Layers 5-6: network analysis, scoring, case building
- `python -m src.pipeline.pipeline_runner --layers 5,6`

`005-run-generate-alerts.md`:
- Generate alert summary of today's findings
- `python -m src.pipeline.pipeline_runner --alerts-only`

## Acceptance Criteria
- [ ] `test -d D:/my_ai_projects/fraud-detection-app/tasks/daily-scan`
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/tasks/daily-scan/000-index.md`
- [ ] `ls D:/my_ai_projects/fraud-detection-app/tasks/daily-scan/*.md | wc -l` >= 6

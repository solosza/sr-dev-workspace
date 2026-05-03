# Write Pipeline Runner

## Type
BUILD

## Description
Orchestrator that runs the full 7-layer investigation pipeline end-to-end.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\pipeline_runner.py` with class `PipelineRunner`:
- `__init__(self, config)` — initialize all layers and clients from config
- `run_daily_scan(self) -> PipelineReport` — execute full daily pipeline:
  1. Layer 0: Pattern discovery (scan sources, extract new patterns)
  2. Layer 1: Ingest new awards
  3. Layer 2: Verify entities
  4. Layer 3: Analyze expenses
  5. Layer 4: OSINT on flagged entities
  6. Layer 5: Network analysis
  7. Score all entities (risk_scorer + network multiplier)
  8. Filter by materiality (materiality_filter)
  9. Layer 6: Build cases for HIGH-tier entities
- `PipelineReport` model: date, awards_ingested (int), entities_verified (int), entities_flagged (int), cases_built (int), new_patterns_discovered (int), alerts (list)
- Save report to `data/reports/YYYY-MM-DD.json`
- Entry point: `if __name__ == "__main__": PipelineRunner(config).run_daily_scan()`

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/pipeline_runner.py`
- [ ] `grep -q "class PipelineRunner" D:/my_ai_projects/fraud-detection-app/src/pipeline/pipeline_runner.py`
- [ ] `grep -q "run_daily_scan" D:/my_ai_projects/fraud-detection-app/src/pipeline/pipeline_runner.py`
- [ ] `grep -q "__main__" D:/my_ai_projects/fraud-detection-app/src/pipeline/pipeline_runner.py`

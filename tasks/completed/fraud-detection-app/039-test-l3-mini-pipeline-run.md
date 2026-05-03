# L3 Test — Mini Pipeline Run

## Type
TEST

## Description
Run a minimal pipeline against a known entity to verify end-to-end flow works. Uses the Feeding Our Future case as a test target (known convicted fraud — safe to scan).

## Requirements
1. `cd D:\my_ai_projects\fraud-detection-app`
2. Run a focused pipeline scan:
   ```python
   from src.pipeline.pipeline_runner import PipelineRunner
   from config.settings import get_config

   config = get_config()
   runner = PipelineRunner(config)

   # Scan for a known entity (Feeding Our Future — EIN available in public records)
   # This is a convicted fraud case — using it as a validation target
   report = runner.run_daily_scan()
   ```
3. Verify:
   - Pipeline runs without crashing
   - At least 1 award is ingested (USASpending API responds)
   - Pipeline report is saved to data/reports/
   - If any entity is flagged, verify evidence package directory structure is correct

Note: This is a smoke test. API calls may fail due to rate limits or network — that's OK for L3. The test validates the pipeline orchestration, not API availability.

## Acceptance Criteria
- [ ] Pipeline runner imports and initializes without error
- [ ] `python -c "from src.pipeline.pipeline_runner import PipelineRunner; print('OK')"` exits 0
- [ ] Pipeline report structure is valid (has all required fields)

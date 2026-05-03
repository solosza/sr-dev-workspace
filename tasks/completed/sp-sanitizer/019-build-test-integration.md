# Create Integration Test — Full Pipeline

## Context
End-to-end test running the complete pipeline on the sample fixture. Verifies all modules work together.

## Type
BUILD

## Execution
inline

## Dependencies
- 012-build-runner

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/runner.py` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists

## Requirements
- Write `tests/test_integration.py` with these test cases:
  - `test_full_pipeline_on_fixture` — run_pipeline on sample_sp.sql, verify PipelineResult returned
  - `test_output_is_valid_sql` — sanitized text has balanced parens, quotes, brackets
  - `test_leak_detector_returns_clean` — leak_report.status == "CLEAN"
  - `test_reverse_matches_original` — reverse the sanitized output, compare to original
  - `test_mapping_store_written` — mapping JSON file exists on disk after run
- Use tmp_path pytest fixture for output directory

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_integration.py` exists
- [ ] `python -m pytest tests/test_integration.py -v` exits 0

## Gates Satisfied
- TEST-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

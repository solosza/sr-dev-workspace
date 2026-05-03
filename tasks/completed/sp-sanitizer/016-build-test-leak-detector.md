# Create Unit Tests for leak_detector.py

## Context
Unit tests verifying the leak detector correctly identifies missed identifiers and passes clean output.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-test-fixtures
- 009-build-leak-detector

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/leak_detector.py` exists

## Requirements
- Write `tests/test_leak_detector.py` with these test cases:
  - `test_clean_on_fully_sanitized` — fully sanitized text returns CLEAN
  - `test_flagged_on_leaked_name` — text with one real name injected returns FLAGGED
  - `test_ignores_tsql_keywords` — SELECT, FROM etc. not flagged
  - `test_catches_pascalcase_unknown` — PascalCase token not in mapping flagged
  - `test_catches_schema_dot_pattern` — `dbo.RealTable` pattern flagged

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_leak_detector.py` exists
- [ ] `python -m pytest tests/test_leak_detector.py -v` exits 0

## Gates Satisfied
- TEST-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

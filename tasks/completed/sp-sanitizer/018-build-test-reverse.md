# Create Unit Tests for reverse.py

## Context
Unit tests verifying round-trip sanitization and mapping integrity checks.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-test-fixtures
- 011-build-reverse

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/reverse.py` exists

## Requirements
- Write `tests/test_reverse.py` with these test cases:
  - `test_round_trip` — sanitize then reverse produces text matching original (modulo whitespace)
  - `test_validates_mapping_integrity` — 1:1 check passes for valid mapping
  - `test_fails_on_corrupted_mapping` — raises error if duplicate synthetic names detected

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_reverse.py` exists
- [ ] `python -m pytest tests/test_reverse.py -v` exits 0

## Gates Satisfied
- TEST-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

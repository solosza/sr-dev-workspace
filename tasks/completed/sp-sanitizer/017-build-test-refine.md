# Create Unit Tests for refine.py

## Context
Unit tests verifying the refinement pass correctly identifies comment/string replacements.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-test-fixtures
- 010-build-refine

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/refine.py` exists

## Requirements
- Write `tests/test_refine.py` with these test cases:
  - `test_identifies_comment_replacements` — flags replacements inside `-- ...` comments
  - `test_identifies_string_literal_replacements` — flags replacements inside `'...'` strings
  - `test_leaves_code_replacements_intact` — code-context replacements not affected

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_refine.py` exists
- [ ] `python -m pytest tests/test_refine.py -v` exits 0

## Gates Satisfied
- TEST-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

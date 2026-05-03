# Create Unit Tests for catalog_replace.py

## Context
Unit tests verifying aggressive replacement handles all identifier types, ordering, and mapping persistence.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-test-fixtures
- 008-build-catalog-replace

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/catalog_replace.py` exists

## Requirements
- Write `tests/test_catalog_replace.py` with these test cases:
  - `test_replaces_all_extracted_identifiers` — no original table/column names in output
  - `test_longest_first_replacement` — `ClaimHistory` replaced before `Claim`
  - `test_mapping_store_persists` — save mapping, load in new call, same synthetic names used
  - `test_cross_file_consistency` — same real name in two different inputs maps to same synthetic name
- Use sample fixture + extract.py to generate ExtractionResult as input

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_catalog_replace.py` exists
- [ ] `python -m pytest tests/test_catalog_replace.py -v` exits 0

## Gates Satisfied
- TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

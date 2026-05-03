# Create Unit Tests for extract.py

## Context
Unit tests verifying identifier extraction handles all T-SQL patterns in the sample fixture.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-build-test-fixtures
- 007-build-extract

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/extract.py` exists

## Requirements
- Write `tests/test_extract.py` with these test cases:
  - `test_finds_schema_qualified_tables` — extracts `dbo.Claims`, `dbo.Members`, `audit.ClaimHistory`
  - `test_finds_delimited_identifiers` — extracts `[Member First Name]`, `[Claim Status]`
  - `test_finds_identifiers_in_dynamic_sql` — extracts tables from sp_executesql string
  - `test_skips_tsql_keywords` — SELECT, FROM, WHERE etc. not in results
  - `test_finds_four_part_names` — extracts all segments of `LinkedServer.RemoteDB.dbo.ProviderLookup`
  - `test_finds_temp_tables_and_variables` — extracts `#TempClaims`, `@ClaimBatch` with correct kind
- All tests use `sample_sp.sql` fixture

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_extract.py` exists
- [ ] `python -m pytest tests/test_extract.py -v` exits 0

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

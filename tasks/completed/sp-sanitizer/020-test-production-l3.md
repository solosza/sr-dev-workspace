# Production Test: Full Pipeline CLI End-to-End

## Context
Level 3 production test. Runs the actual CLI entry point against the sample fixture and verifies all output artifacts.

## Type
TEST

## Execution
agent

## Dependencies
- 019-build-test-integration

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/test_integration.py` exists
- [ ] Integration tests pass

## Requirements
- Set up test environment: clean output directory
- Execute the CLI: `python -m sp_sanitizer.runner tests/fixtures/sample_sp.sql --output-dir output/`
- Verify exit code is 0
- Read output .sql file — verify it contains NO original table/column names (dbo.Claims, dbo.Members, etc.)
- Read mapping JSON — verify it contains entries for all extracted identifiers
- Read leak report — verify status is CLEAN
- Run reverse: verify reversing the output produces text matching the original
- Check for unexpected side effects (no extra files created)

## Acceptance Criteria
- [ ] CLI executes with exit code 0
- [ ] Output .sql file exists and contains no real identifiers
- [ ] Mapping JSON exists with correct entries
- [ ] Leak report shows CLEAN status
- [ ] No unexpected files in output directory

## Gates Satisfied
- TEST-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

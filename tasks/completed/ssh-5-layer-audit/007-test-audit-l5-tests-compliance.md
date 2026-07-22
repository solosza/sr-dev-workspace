# Audit L5 Tests Compliance

## Context
Check that SSH platform tests follow L5 patterns (pytest, AAA, parametrize).

## Type
TEST

## Execution
inline

## Dependencies
- 001-research-scan-ssh-platform-structure
- 002-research-read-5-layer-reference

## Phase Gate
- [ ] `tasks/ssh-5-layer-audit/ssh-platform-file-map.md` exists
- [ ] `tasks/ssh-5-layer-audit/5-layer-reference-checklist.md` exists

## Requirements
- Read the file map and reference checklist
- Find test files in SSH platform (framework/tests/ or _reference/tests/)
- Check each test file for:
  - Uses pytest (not unittest or other frameworks)
  - Follows AAA pattern (Arrange, Act, Assert)
  - Uses @pytest.mark.parametrize where applicable
  - Imports from L4 (roles) or L3 (tasks), not directly from L2/L1/SDK
- Check for tests outside the standard test directories
- Write violations to `tasks/ssh-5-layer-audit/l5-violations.md`

## Acceptance Criteria
- [ ] L5 violations report exists at `tasks/ssh-5-layer-audit/l5-violations.md`
- [ ] Each test file checked for L5 pattern compliance
- [ ] Import direction verified (L5 → L4 or L5 → L3)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

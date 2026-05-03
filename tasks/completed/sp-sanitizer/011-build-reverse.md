# Create reverse.py — Mapping Inversion

## Context
Translates sanitized SP back to real names using the mapping store. Used when AI recommendations need to reference actual database objects.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-build-data-contracts

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` exists

## Requirements
- Function `reverse_sanitization(sanitized_text: str, mapping_store_path: str) -> str`
- Load MappingStore from disk
- Validate 1:1 mapping integrity (no duplicate synthetic names)
- Invert: replace all synthetic names with their real counterparts
- Sort longest-first (same as forward replacement)
- Return the restored text

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/reverse.py` exists
- [ ] Exports `reverse_sanitization` function

## Gates Satisfied
- BUILD-11, FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

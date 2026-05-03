# Create refine.py — Optional Context-Aware Refinement

## Context
Optional pass that reduces false positives from aggressive replacement. Identifies replacements inside comments and string literals where cosmetic accuracy matters less.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-build-data-contracts

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` exists

## Requirements
- Function `refine_replacements(sanitized_text: str, original_text: str, mapping_snapshot: dict) -> ReplacementResult`
- Identify regions in the sanitized text that correspond to:
  - Single-line comments (`-- ...`)
  - Block comments (`/* ... */`)
  - String literals (`'...'`, `N'...'`)
- Within these regions, optionally restore original text or leave sanitized (configurable)
- Default behavior: leave comments/strings sanitized (safer), but flag which replacements were in non-code contexts
- Return updated ReplacementResult with annotation of comment/string replacements

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/refine.py` exists
- [ ] Exports `refine_replacements` function

## Gates Satisfied
- BUILD-10, FUNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Create leak_detector.py — Heuristic Leak Detection

## Context
The safety net. Scans sanitized output for any token that looks like a real identifier but wasn't mapped. This is the quality gate — if it flags anything, the pipeline fails.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-tsql-keywords
- 005-build-data-contracts

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/tsql_keywords.py` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` exists

## Requirements
- Function `detect_leaks(sanitized_text: str, mapping_snapshot: dict) -> LeakReport`
- Build a "known safe" set: T-SQL keywords + synthetic names (from mapping) + SQL operators/punctuation + numeric literals
- Tokenize the sanitized text
- For each token NOT in the known-safe set, apply heuristics:
  - PascalCase pattern (e.g., `ClaimHistory`) — likely a real identifier
  - snake_case pattern with domain terms — likely a real identifier
  - Appears after FROM/JOIN/INTO/UPDATE/EXEC — identifier position
  - Matches `schema.X` pattern where schema wasn't replaced
  - Contains underscore + digits that don't match synthetic naming (e.g., `Claim_2024` vs `Table_001`)
- Return LeakReport with status CLEAN (no flags) or FLAGGED (with token locations and reasons)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/leak_detector.py` exists
- [ ] Exports `detect_leaks` function
- [ ] Returns `LeakReport` type

## Gates Satisfied
- BUILD-09, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

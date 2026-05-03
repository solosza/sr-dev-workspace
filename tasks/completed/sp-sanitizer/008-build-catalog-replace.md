# Create catalog_replace.py — Aggressive Global Replacement

## Context
Takes extracted identifiers and aggressively replaces ALL occurrences in the text — including comments, strings, dynamic SQL. This is the core of the "replace everything, verify after" architecture.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-build-data-contracts
- 007-build-extract

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` exists
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/extract.py` exists

## Requirements
- Function `replace_identifiers(extraction: ExtractionResult, mapping_store_path: str | None = None) -> ReplacementResult`
- Build replacement map: `real_name -> synthetic_name` (e.g., `Claims -> Table_001`, `MemberID -> Column_001`)
- Naming scheme: `Table_NNN`, `Column_NNN`, `Schema_NNN`, `SP_NNN`, `Temp_NNN`, `Var_NNN` based on kind
- Load existing MappingStore from disk if path provided (cross-file consistency)
- Sort replacements longest-first to prevent partial matches (e.g., `ClaimHistory` before `Claim`)
- Global text replacement — replace in comments, strings, code, everywhere
- Save updated MappingStore to disk after replacement
- Return ReplacementResult with sanitized text and count

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/catalog_replace.py` exists
- [ ] Exports `replace_identifiers` function
- [ ] Returns `ReplacementResult` type

## Gates Satisfied
- BUILD-08, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

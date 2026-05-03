# Create extract.py — Identifier Extraction

## Context
Phase 1 of the pipeline. Parses SP text and finds all identifiers (tables, columns, schemas, SP names). This is the "catalog" built from the SP itself since we have no database access.

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
- Function `extract_identifiers(sql_text: str) -> ExtractionResult`
- Parse SQL text and find identifiers in these contexts:
  - After FROM, JOIN, INTO, UPDATE, DELETE, EXEC, EXECUTE
  - In CREATE/ALTER TABLE/PROCEDURE/VIEW/FUNCTION statements
  - Schema-qualified: `schema.table` → extract both parts
  - Delimited: `[Name With Spaces]` → extract including bracket handling
  - Four-part: `server.db.schema.table` → extract all segments
  - Inside dynamic SQL strings (sp_executesql N'...' parameter)
  - Temp tables (`#name`) and table variables (`@name`) — extract but mark kind differently
- Skip tokens that are T-SQL keywords (import TSQL_KEYWORDS)
- Skip string literals and comments for identifier extraction (but note their positions for later)
- Return ExtractionResult with all found identifiers, their kinds, and positions

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/extract.py` exists
- [ ] Exports `extract_identifiers` function
- [ ] Returns `ExtractionResult` type

## Gates Satisfied
- BUILD-07, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

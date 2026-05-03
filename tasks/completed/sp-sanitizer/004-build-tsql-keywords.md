# Create T-SQL Keyword Whitelist

## Context
Complete T-SQL keyword set used by extract.py and leak_detector.py to distinguish SQL keywords from real identifiers. Must be comprehensive — any keyword missing here will be flagged as a potential leak.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-project-structure

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/__init__.py` exists

## Requirements
- Export `TSQL_KEYWORDS` as a `frozenset` of uppercase strings
- Include all categories: DML (SELECT, INSERT, UPDATE, DELETE, MERGE), DDL (CREATE, ALTER, DROP), flow control (IF, ELSE, WHILE, BEGIN, END, TRY, CATCH), joins (JOIN, INNER, OUTER, LEFT, RIGHT, CROSS, APPLY), clauses (WHERE, HAVING, GROUP BY, ORDER BY, TOP, DISTINCT, INTO, OUTPUT), data types (INT, VARCHAR, NVARCHAR, DATETIME, BIT, DECIMAL, etc.), built-in functions (GETDATE, ISNULL, COALESCE, CAST, CONVERT, ROW_NUMBER, etc.), operators (AND, OR, NOT, IN, EXISTS, BETWEEN, LIKE, IS, NULL), transaction (BEGIN TRAN, COMMIT, ROLLBACK, SAVE), cursor keywords, EXEC/EXECUTE, sp_executesql, SET, DECLARE, PRINT, RAISERROR, THROW
- 200+ keywords minimum

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/tsql_keywords.py` exists
- [ ] Exports `TSQL_KEYWORDS` as frozenset
- [ ] Contains 200+ keywords

## Gates Satisfied
- BUILD-04, FUNC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

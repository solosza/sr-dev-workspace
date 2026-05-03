# Create Sample SP Test Fixture

## Context
Realistic T-SQL stored procedure fixture that exercises all edge cases the pipeline must handle. Used by every test file.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-project-structure

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/` directory exists

## Requirements
- Write `tests/fixtures/sample_sp.sql` — a realistic T-SQL SP with ALL of these patterns:
  - Schema-qualified tables: `dbo.Claims`, `dbo.Members`, `audit.ClaimHistory`
  - Delimited identifiers: `[Member First Name]`, `[Claim Status]`
  - Temp table: `#TempClaims`
  - Table variable: `@ClaimBatch`
  - Dynamic SQL: `EXEC sp_executesql @sql` with table names in the string
  - Four-part name: `LinkedServer.RemoteDB.dbo.ProviderLookup`
  - Comments containing table names: `-- Update dbo.Claims status`
  - String literals containing table names: `PRINT 'Processing dbo.Claims...'`
  - CTE: `WITH ClaimCTE AS (...)`
  - MERGE statement
  - CROSS APPLY
  - OUTPUT clause
  - Multiple JOINs with aliased tables
- Must be syntactically valid T-SQL
- Should resemble a healthcare claims processing SP (realistic domain)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/tests/fixtures/sample_sp.sql` exists
- [ ] Contains `dbo.Claims` (schema-qualified)
- [ ] Contains `[` and `]` (delimited identifiers)
- [ ] Contains `#Temp` (temp table)
- [ ] Contains `sp_executesql` (dynamic SQL)
- [ ] Contains four-part name
- [ ] Contains `--` comment with a table name
- [ ] Contains string literal with a table name

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

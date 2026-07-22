# Test: Contract Semantics — AST (lessons #38/#39/#43)

## Type
TEST
## Execution
inline
## Dependencies
- 003, 004

## Requirements
- AST-only script over all api_objects files: no ast.Try (except documented state-check exemptions — list any in output); constructors take interfaces/config via DI, construct nothing (fn.body per-statement walk, decorator-aware); no screenshot machinery; no healthcare vocab identifiers/literals; endpoint constants slash-canonical (`.endswith('/')` on collection paths — value check on constants, allowed since these ARE owned identifiers)
- Exit non-zero on real violations → fix CODE → /kernel/learn; script misfire → fix SCRIPT

## Acceptance Criteria
- [ ] Exit 0, checks genuinely executed

## Gates Satisfied
- AO-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

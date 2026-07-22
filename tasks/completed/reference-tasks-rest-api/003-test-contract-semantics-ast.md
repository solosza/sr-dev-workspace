# Test: Contract Semantics — AST (lessons #38/#39/#43/#45)

## Type
TEST
## Execution
inline
## Dependencies
- 002

## Requirements
- AST-only over order_management_tasks.py: every ast.Try handler reraises or raises the doc's domain exception (translation allowed, swallowing banned — verify a Raise node in each handler body); __init__ decorator per doc, params = api objects only, no construction (body-scoped, decorator-aware); @trace("Task") on public methods; return annotations match the doc's typed-return set; extended lexicon on identifiers + literals (member/subscriber/eligib/DRG/PCN/837/hmsa/healthcare/claim/patient) → empty
- Exit non-zero on real violations → fix CODE → /kernel/learn; script misfire → fix SCRIPT

## Acceptance Criteria
- [ ] Exit 0, all checks genuinely executed

## Gates Satisfied
- RT-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

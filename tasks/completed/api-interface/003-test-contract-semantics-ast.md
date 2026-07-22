# Test: Contract Semantics — AST (lessons #38/#39/#43)

## Type
TEST
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] api_interface.py on branch

## Requirements
- AST-only script over api_interface.py:
  - every ast.Try handler body contains ast.Raise (or is a documented primitive-return state check — list any such exemption explicitly in output)
  - no screenshot/save call names; no domain-vocab identifiers or string literals (order/customer/patient/claim) — generic HTTP terms only
  - imports ⊆ stdlib + requests
  - each verb method body includes a logging call (catch-log-reraise evidence) — body-scoped per-statement walk, decorator-aware
- Exit non-zero on real violations → fix CODE → /kernel/learn; script misfire → fix SCRIPT

## Acceptance Criteria
- [ ] Exit 0, all checks genuinely executed

## Gates Satisfied
- AIF-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Test: Contract Semantics — AST-BASED (lesson #39 method mandatory)

## Context
Backlog 205: the semantics gate, written the way lesson #39 requires. 204's version of this test died to string-grep false positives (docstring rule text, dynamic locator templates) — that method is BANNED here.

## Type
TEST
## Execution
inline
## Dependencies
- 002, 003, 004
## Phase Gate
- [ ] Both components + reconciled configs exist on the branch

## Requirements
- Python script over framework/_reference/components/*.py using `ast` ONLY:
  - ast.Try count == 0; decorator_list empty on all functions (dataclass decorator on the Locators classes is EXEMPT — it's the config, not a method decorator)
  - screenshot detection via ast.Call/ast.Attribute names — never source grep (docstrings will mention rules)
  - no concrete data-testid string literals (identifiers must arrive via config)
  - SCOPE constant present in both
  - return-self by execution: instantiate each with a stub interface + dummy config, call one atomic, assert identity
- Print per-file results; exit non-zero on real violations → fix → /kernel/learn. Do NOT weaken the checks to pass; if the script itself misfires, fix the SCRIPT (that was 204's failure)

## Acceptance Criteria
- [ ] Script exits 0 with all checks genuinely executed

## Gates Satisfied
- CMP-03, CMP-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Test: Contract Semantics — AST-BASED (lesson #39 method mandatory)

## Context
Backlog 206: semantics gate for copied-then-adapted code. Lesson #38: copies from platform-selenium predate the contract — this test is what catches era drift (@autologger remnants, BrowserInterface-in-constructor, login-as-task). String-grep is BANNED (lesson #39).

## Type
TEST
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] order_workup_tasks.py exists on the branch

## Requirements
- Python script over `framework/_reference/tasks/order_workup_tasks.py` using `ast` ONLY:
  - ast.Try count == 0
  - `__init__` decorator_list empty; every OTHER public FunctionDef has exactly the @trace("Task") decorator (inspect ast.Call decorator nodes)
  - `__init__` params annotated as page classes, none named/typed browser/BrowserInterface; no ast.Call constructing page classes inside `__init__` body
  - returns annotation: `-> None` (ast.Constant None) on open_order/change_status; `-> str` on capture_order_id only
  - no string literals containing `data-testid`; no screenshot/save call names (via ast.Call/ast.Attribute)
- Print per-check results; exit non-zero on real violations → fix the CODE → /kernel/learn. If the SCRIPT misfires (false positive), fix the SCRIPT — never weaken a check to pass (204's failure mode)

## Acceptance Criteria
- [ ] Script exits 0 with every check genuinely executed

## Gates Satisfied
- TSK-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

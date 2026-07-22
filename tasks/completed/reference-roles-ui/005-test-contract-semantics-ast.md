# Test: Contract Semantics — AST-BASED (lesson #39 method mandatory)

## Context
Backlog 207: semantics gate over all three new files. This is where lesson #38 era-drift from the copy source gets caught. String-grep BANNED.

## Type
TEST
## Execution
inline
## Dependencies
- 002, 003, 004
## Phase Gate
- [ ] All three files exist on the branch

## Requirements
- Python script using `ast` ONLY over common_tasks.py, order_clerk.py, order_manager.py:
  - ast.Try count == 0 in all files
  - common_tasks: `__init__` undecorated, takes login_page only (no browser/interface names); login has exactly @trace("Task") and `-> None`
  - roles: `__init__` has exactly @trace("Role Constructor"); params = task modules + identity (NO browser/interface/page names in args or annotations); no ast.Call constructing task/page classes inside `__init__`
  - role workflow methods: exactly @trace("Role"), `-> None`, and their bodies contain >= 2 DISTINCT task-attribute call targets (self.common.* plus self.order_workup.*) — the composition rule, checked via ast.Attribute chains
  - no `data-testid` string literals anywhere; no screenshot call names; no credential-looking literals passed to login (login args must be Subscript reads of self.identity, not ast.Constant strings)
- Exit non-zero on real violations → fix CODE → /kernel/learn; script misfire → fix SCRIPT, never weaken

## Acceptance Criteria
- [ ] Script exits 0, every check genuinely executed

## Gates Satisfied
- ROL-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

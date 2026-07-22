# Build order_management_tasks.py — L3 REST Tasks

## Context
Backlog 212. READ FIRST (RULE ZERO): (1) `projects/hmsa-qa-platform/02-reference-patterns/tasks-rest-api.md` — the canonical example GOVERNS signatures, typed returns, the domain-exception pattern, and the idempotent-cleanup shape; (2) `framework/_reference/tasks/order_workup_tasks.py` on the branch — sibling idiom (trace import style, module docstring style); (3) `framework/_reference/api_objects/orders_api_object.py` — the REAL methods you orchestrate (get_all/get_by_id/create/change_status/process/delete, fluent + get_last_*).

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `framework/_reference/tasks/order_management_tasks.py` (+ tasks/__init__.py export)
- Constructor: api object(s) via DI per the design doc canonical — never ApiInterface, never construct internally
- Methods exactly per the doc's canonical set — typed returns (models/primitives up), the doc's domain exception where it prescribes one, @trace("Task")
- Idempotent cleanup per doc (ensure_order_absent-style): check-then-delete, no-op when absent, never raises on already-gone
- try/except ONLY where the doc sanctions (exception translation) — translated-and-raised, never swallowed
- Extended lexicon clean (lesson #45)

## Acceptance Criteria
- [ ] Byte-faithful to doc canonical; imports clean

## Gates Satisfied
- RT-02, RT-03 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

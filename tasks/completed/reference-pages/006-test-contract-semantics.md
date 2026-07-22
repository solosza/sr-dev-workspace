# Test: Contract Semantics (lesson 2026-07-15 gates)

## Context
Backlog 204: the gates that would have caught 203's defects, applied to Layer 2 — pages never catch, never decorate, never screenshot, never wait inside actions; atomics return self; state-checks return primitives; every locator testid exists in the real templates.

## Type
TEST
## Execution
inline
## Dependencies
- 002, 003, 004, 005
## Phase Gate
- [ ] All four page files exist on the branch

## Requirements
- Run a python inspection script over framework/_reference/pages/*.py asserting ALL of: zero try/except; zero decorators; zero screenshot refs; action methods contain no wait calls; every `[data-testid='X']` referenced exists in harness/orderly/templates/*.html (parse both sides); atomic methods return self (instantiate with stub interface, call, assert identity); is_/has_/get_ methods return bool/str/int/float
- Print per-file results; exit non-zero on any violation → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 across all four files

## Gates Satisfied
- PAG-03, PAG-04, PAG-05, PAG-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

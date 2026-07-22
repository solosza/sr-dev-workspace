# Test: Seed Determinism

## Context
Backlog 202: scenario JSON references fixed IDs — a nondeterministic seed breaks every future data file silently.

## Type
TEST
## Execution
inline
## Dependencies
- 003
## Phase Gate
- [ ] seed.py exists on the branch

## Requirements
- Run python: seed into two separate temp SQLite files; dump all rows from both ordered by table+id; assert identical; assert all four order statuses present; exit non-zero otherwise

## Acceptance Criteria
- [ ] Script exits 0

## Gates Satisfied
- HUI-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

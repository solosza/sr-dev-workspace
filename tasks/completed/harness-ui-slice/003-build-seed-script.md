# Write the Seed Script (seed.py)

## Context
Backlog 202: deterministic demo data with FIXED IDs so scenario JSON stays stable (harness-app.md testability conventions).

## Type
BUILD
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] db.py exists on the branch

## Requirements
- Write `harness/orderly/seed.py`: drops/recreates tables, inserts fixed-ID rows — ≥4 customers, ≥8 orders covering ALL four statuses, order items; two demo users (clerk/manager) with fixed credentials for the login seam
- Running twice on a fresh DB yields identical data (no random, no now() in IDs)

## Acceptance Criteria
- [ ] Script runs clean; fixed IDs; all four statuses present

## Gates Satisfied
- HUI-05 (verified by task 013)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

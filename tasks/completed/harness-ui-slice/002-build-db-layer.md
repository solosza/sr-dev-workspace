# Write the Data Layer (db.py)

## Context
Backlog 202: SQLAlchemy Core over SQLite per data-model.md — Customer, Order, OrderItem tables; statuses PENDING/PROCESSING/COMPLETE/CANCELLED. Engine URL config-driven so V3 swaps to SQL Server without rewrite.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/202-qa-build-harness-ui-slice

## Requirements
- READ design docs first: 04-test-harness/data-model.md + harness-app.md (workspace projects/hmsa-qa-platform/)
- Write `harness/orderly/db.py`: SQLAlchemy Core tables exactly per data-model.md entities; engine factory reading DATABASE_URL env (default sqlite file harness/orderly/orderly.db); create_all helper
- GENERIC COMMERCE names only

## Acceptance Criteria
- [ ] File exists; tables customers/orders/order_items defined; engine URL env-driven

## Gates Satisfied
- (feeds HUI-02/05)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

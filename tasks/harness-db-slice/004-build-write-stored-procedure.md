# Task 004: Write process_pending_orders Stored Procedure

**Type:** BUILD | **Gates:** DB-04

## Action
Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/sp_process_pending_orders.sql` (ONE file).

## Spec
- `CREATE OR ALTER PROCEDURE process_pending_orders` — transitions ALL orders with status 'PENDING' to 'PROCESSING' (harness-app.md V3: SP-as-subject target)
- Returns/SELECTs the affected row count
- Touches NO other statuses; no parameters needed (whole-table pipeline semantics per data-model.md status pipeline)

## Acceptance
Greps per DB-04; `CREATE OR ALTER` (idempotent).

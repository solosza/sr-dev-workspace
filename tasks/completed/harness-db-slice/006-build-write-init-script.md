# Task 006: Write init_sqlserver.py

**Type:** BUILD | **Gates:** DB-06

## Action
Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/init_sqlserver.py` (ONE file).

## Spec
READ `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/seed.py` first (RULE ZERO) — reuse its exact seed data (import from it if importable; else mirror rows).
Script (env: ORDERLY_MSSQL_PORT, MSSQL_SA_PASSWORD):
1. Connect via SQLAlchemy to the container's master DB; create database `orderly` if missing
2. Apply db_sqlserver_schema.sql (batch-split on GO)
3. Apply sp_process_pending_orders.sql
4. Seed the same customers/orders/order_items rows as seed.py — idempotent (truncate-and-reseed or existence check)
No print() debug — write a summary line via sys.stdout.write or logging.

## Acceptance
Runs clean twice in a row (DB-06).

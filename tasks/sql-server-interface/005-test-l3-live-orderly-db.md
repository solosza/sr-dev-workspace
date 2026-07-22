# Task 005: L3 — Live Against Orderly SQL Server DB (GATE)

**Type:** TEST (L3) — GATE TASK: skip never waives (lesson #39); orchestrator validates regardless.
**Gates:** SI3-07

## Target

Native SQL Server 2019, database `orderly` (214 deliverable — live, seeded, SP present). Trusted connection, localhost. If unreachable: report L3-BLOCKED with the exact error and STOP — never fake e2e.

**SAFETY:** ONLY database `orderly`. The instance holds unrelated real databases.

## Action

Run ONE test script exercising the REAL interface against the REAL DB:

1. `execute_query("SELECT * FROM orders WHERE status = ?", ...)` → seeded rows with correct columns
2. `execute_query_one` / `execute_scalar` → exact values vs direct sqlcmd/known seed
3. `execute_non_query` UPDATE → rowcount + verified by follow-up query
4. `execute_many` batch INSERT into order_items + cleanup DELETE (state restored)
5. `execute_sproc("process_pending_orders")` → set order 1 PENDING first; assert PENDING→0, PROCESSING +N, terminal statuses untouched
6. Transactions: begin→INSERT→rollback (row absent); begin→INSERT→commit (row present, then cleanup)
7. Final: re-run init_sqlserver.py (or targeted restore) so `orderly` is left seeded

## Acceptance

All live asserts PASS, exit 0, DB restored. Red → fix → /kernel/learn.

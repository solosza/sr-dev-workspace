# Task 007: L3 - Live Against Orderly DB (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39); orchestrator validates regardless.
**Gates:** DO-07

## Target
Native SQL Server 2019, database orderly (215's SqlServerInterface is the access path). Unreachable => L3-BLOCKED and STOP. SAFETY: only orderly / orderly_v3.

## Action
ONE test script using the REAL OrdersDataObject over the REAL SqlServerInterface:
1. Query all orders -> typed OrderRow list matching seed (8 rows, statuses correct)
2. Query one customer -> CustomerRow validates without coercion errors
3. Discovery pattern: find eligible order (status filter) -> correct row
4. Variant map: resolve the pipeline variant -> process_pending_orders -> execute via the Data Object path -> set order 1 PENDING first, assert PENDING->0 semantics
5. Insert/update path via sql/ files -> verified by follow-up query -> cleaned up
6. Final: reseed (init_sqlserver.py) - DB left at baseline

## Acceptance
All live asserts PASS, exit 0, DB restored. Red: fix then /kernel/learn.

# Task 009: L3 — App Live on SQL Server + Backward Compat (GATE)

**Type:** TEST (L3) — GATE TASK: skip never waives (lesson #39); orchestrator validates regardless.
**Gates:** DB-09

## Target Resolution

Same as task 008 (container if image local, else native instance; database `orderly_v3` ONLY — never touch other databases on the instance).

## Action

Run ONE test script:
1. Ensure target ready + freshly seeded (init_sqlserver.py)
2. Boot app against SQL Server: `DATABASE_URL="mssql+pyodbc://@localhost/orderly_v3?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"` (or container URL) + `python -m uvicorn harness.orderly.main:app --port 8018` (background, PYTHONPATH=D:/my_ai_projects/project_test_repos/hmsa-qa-platform)
3. HTTP sweep with session login (clerk/clerk123): /login 200 → POST login 303 → /customers 200 → /orders 200 → /orders/1 200; assert heading testids in HTML (heading-orders, heading-order-detail)
4. Status change through the app on SQL Server: POST /orders/1/status PENDING→PROCESSING; assert 303 + DB row updated via direct query
5. Call the SP via SQLAlchemy; assert pipeline semantics on remaining PENDING rows
6. Backward compat: boot app with the SQLite DATABASE_URL on port 8019 → /orders 200
7. Teardown: stop both uvicorns; container path: compose down (leave volume); native path: leave orderly_v3 in place (dev fixture)

## Acceptance

All steps PASS, exit 0. Red → fix → /kernel/learn.

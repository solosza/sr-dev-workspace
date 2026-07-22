# Task 009: L3 — App Live on SQL Server + Backward Compat (GATE)

**Type:** TEST (L3) — GATE TASK: skip never waives (lesson #39); orchestrator validates regardless.
**Gates:** DB-09

## Action
Run ONE test script:
1. Ensure container healthy + freshly seeded (init_sqlserver.py)
2. Boot app: `DATABASE_URL=<mssql url> python -m uvicorn harness.orderly.main:app --port 8018` (background, PYTHONPATH=D:/my_ai_projects/project_test_repos/hmsa-qa-platform)
3. HTTP sweep with session login (clerk/clerk123): /login 200, POST login redirect, /customers 200, /orders 200, /orders/1 200 — assert headings present in HTML (heading-orders, heading-order-detail testids)
4. Status change through the app on SQL Server: POST /orders/1/status PENDING->PROCESSING; assert 303 + DB row updated (direct query)
5. Call SP via SQLAlchemy; assert pipeline semantics on remaining PENDING rows
6. Backward compat: boot app with SQLite DATABASE_URL on port 8019 — /orders 200
7. Teardown: stop both uvicorns; `docker compose down` (leave volume)

## Acceptance
All steps PASS, exit 0. Red → fix → /kernel/learn.

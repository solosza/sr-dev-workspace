# Task 008: L2 — Container Up, Schema + SP Live

**Type:** TEST (L2) | **Gates:** DB-08

## Action
Run ONE test script:
1. Driver preflight: `import pyodbc` + list ODBC drivers; if no SQL Server ODBC driver, `pip install pymssql` and use it; if neither works, report BLOCKED with the exact error (never fake)
2. `docker compose -f .../sqlserver-compose.yml up -d`; wait healthy (<=120s)
3. Run init_sqlserver.py; then direct SQLAlchemy asserts: 3 tables queryable, seed counts (customers>=1, orders>=8, order_items>=1), SP exists (sys.procedures)
4. Execute SP on the seeded data: PENDING count drops to 0, PROCESSING count increases by exactly the prior PENDING count, other statuses untouched
5. Re-run init_sqlserver.py (idempotency, DB-06) — then re-verify seed state restored

## Acceptance
All asserts pass, exit 0. Container LEFT RUNNING for task 009. Red → fix → /kernel/learn.

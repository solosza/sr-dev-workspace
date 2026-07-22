# Task 008: L2 — SQL Server Live: Schema + SP + Seed

**Type:** TEST (L2) | **Gates:** DB-08

## Target Resolution (env-adaptive, orchestrator-directed 2026-07-22)

Registry blob downloads are machine-blocked (documented: Docker Hub AND MCR blob CDN EOF mid-transfer; manifests OK). Resolution order:
1. If `docker image inspect mcr.microsoft.com/mssql/server:2022-latest` succeeds (image already local) → compose path
2. Else → NATIVE instance: `ORDERLY_MSSQL_URL="mssql+pyodbc://@localhost/{db}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"` (SQL Server 2019 Developer, MSSQLSERVER service running, pyodbc + ODBC Driver 17 verified installed)

**SAFETY (absolute):** the native instance may hold other databases. ONLY create/use/drop database `orderly_v3`. Any statement touching another database is a defect.

## Action

Run ONE test script:
1. Resolve target per above; record which path was taken in the output
2. Native path: connect to master via the URL template ({db}=master), `CREATE DATABASE orderly_v3` if missing; container path: compose up + wait healthy
3. Run init_sqlserver.py against the target (env set; database orderly_v3)
4. Direct SQLAlchemy asserts: 3 tables queryable; seed counts (customers>=1, orders>=8, order_items>=1); SP exists in sys.procedures
5. Execute SP: PENDING count → 0; PROCESSING increases by exactly the prior PENDING count; other statuses untouched
6. Re-run init_sqlserver.py (idempotency, DB-06) — seed state restored

## Acceptance

All asserts PASS, exit 0, resolved target logged. Red → fix → /kernel/learn.

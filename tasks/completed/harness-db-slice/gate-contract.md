# Gate Contract — 214 Harness DB Slice (V3)

Deliverable: Orderly persistence on SQL Server (Docker), same 3-table schema, `process_pending_orders` stored procedure, app swap via config. Smoke-tested live.

Repo: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform`, branch `build/214-qa-build-harness-db-slice`.

| Gate | Check | Method | Task | Pass Criteria |
|------|-------|--------|------|---------------|
| DB-01 | Feature branch exists, based on current main | run_code (git) | 001 | `git branch --show-current` = build/214-qa-build-harness-db-slice; merge-base == main HEAD |
| DB-02 | `harness/orderly/docker/sqlserver-compose.yml` exists: SQL Server 2022 image, SA password via env, host port mapped, healthcheck | file_exists + grep | 002 | compose parses (`docker compose config`), image mcr.microsoft.com/mssql/server:2022-*, healthcheck present |
| DB-03 | `harness/orderly/db_sqlserver_schema.sql`: customers, orders, order_items tables matching SQLite schema (same columns/types adapted to T-SQL) | grep | 003 | 3 CREATE TABLE, FK order_items→orders, orders→customers, status NVARCHAR |
| DB-04 | `harness/orderly/sp_process_pending_orders.sql`: SP transitions ALL PENDING→PROCESSING, returns affected count | grep | 004 | CREATE PROCEDURE process_pending_orders; UPDATE ... WHERE status = 'PENDING'; no other status touched |
| DB-05 | `db.py` swaps engine by DATABASE_URL env (mssql+pyodbc or pymssql accepted); SQLite path UNCHANGED (V1/V2 regression-free) | grep + run_code | 005 | env-driven; `python -c` import with SQLite URL still works; no hardcoded SQL Server creds in db.py (env only) |
| DB-06 | `init_sqlserver.py` applies schema + SP + seed data (same rows as seed.py) idempotently | run_code | 006 | second run does not error or duplicate rows |
| DB-07 | L1: all files exist on the branch; extended vocab lexicon grep CLEAN over all new/changed files | run_test | 007 | 0 lexicon hits; all 5 artifacts present |
| DB-08 | L2 live: container up (healthy), schema applied (3 tables queryable), SP exists and executes, seed rows present | run_test | 008 | direct SQLAlchemy queries against the container pass |
| DB-09 | L3 live: app boots with DATABASE_URL=sqlserver → all routes 200 (login, customers, orders, order detail); SP call transitions exactly the PENDING orders; app on SQLite still green (backward compat) | run_test | 009 | route sweep 200s; before/after status counts prove SP semantics; SQLite boot re-verified |

## Rules

- READ existing `db.py`, `seed.py`, `main.py` fully before the config swap (RULE ZERO)
- Tests hit SQL Server DIRECTLY via SQLAlchemy (the app's ORM is invisible to the framework) — data-model.md
- Driver preflight in 008: check pyodbc + "ODBC Driver 1x for SQL Server" availability; fall back to pymssql; if neither installable, report BLOCKED with exact error — do not fake the gate (lesson #47 env preflight)
- SA password: env var only (e.g. MSSQL_SA_PASSWORD), never committed literal beyond a documented dev default
- Container name prefixed `orderly-` ; port NOT 1433 default if occupied — check first
- Any red → fix → /kernel/learn

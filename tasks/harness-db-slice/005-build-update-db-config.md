# Task 005: Env-Driven Engine Config in db.py

**Type:** BUILD | **Gates:** DB-05

## Action
Edit `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/db.py` (ONE file) so DATABASE_URL fully drives the engine.

## Spec
READ db.py fully first (RULE ZERO). It already reads DATABASE_URL for SQLite. Ensure:
- An `mssql+pyodbc://` or `mssql+pymssql://` DATABASE_URL works unmodified through SQLAlchemy Core (no SQLite-only pragmas applied to non-SQLite URLs — guard any `connect_args`/PRAGMA by dialect)
- SQLite behavior byte-identical when DATABASE_URL is sqlite (V1/V2 regression-free)
- No credentials hardcoded — URL comes from env only

## Acceptance
DB-05 greps; `python -c` boot with SQLite URL unchanged behavior.

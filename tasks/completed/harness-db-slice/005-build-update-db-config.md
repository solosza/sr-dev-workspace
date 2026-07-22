# Task 005: Native-Instance URL Override in init_sqlserver.py (db.py verified clean)

**Type:** BUILD | **Gates:** DB-05

## Action

ONE edit to `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/init_sqlserver.py`.

## Spec

Orchestrator finding (2026-07-22): `db.py` is ALREADY env-driven and dialect-clean — bare `create_engine(DATABASE_URL)`, no SQLite-only pragmas. Do NOT edit db.py.

ENV CONTEXT: registry blob downloads are machine-blocked (Docker Hub + MCR both EOF mid-transfer), so the container path is unavailable. The machine has a native SQL Server 2019 Developer instance (MSSQLSERVER service, Windows auth, ODBC Driver 17) — the slice targets it via a full-URL override.

Edit `_base_url()` in init_sqlserver.py: if env `ORDERLY_MSSQL_URL` is set, use it — treat it as a template containing `{db}` for the database name (format with the requested database). Keep the existing sa-password container fallback unchanged.

Reference native URL (document in a comment):
`mssql+pyodbc://@localhost/{db}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes`

## Acceptance

- db.py untouched (`git diff -- harness/orderly/db.py` empty)
- init_sqlserver.py honors ORDERLY_MSSQL_URL template; container fallback intact
- py_compile passes

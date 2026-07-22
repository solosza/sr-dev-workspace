# Task 002: Write sql_server_interface.py

**Type:** BUILD | **Gates:** SI3-02, SI3-03 (build side)

## Action

Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/interfaces/sql_server_interface.py` (ONE file, from scratch).

## Spec

READ FULLY FIRST (RULE ZERO): `projects/hmsa-qa-platform/01-interface-design/sql-server-interface.md` (in sr_dev_workspace) — constructor, method surface, return types, differentiators, compliance table — and the 5-layer contract's Interface-layer sections. NEVER open v2 oracle_interface.py or any hmsa-healthcare-qa code.

Implementation rules:
- SDK: `mssql_python` (installed, 1.11.0) — check its API via `python -c "import mssql_python; help(mssql_python.connect)"` style introspection, not guesses
- `?` parameterization on every execute path; no string-interpolated SQL
- catch-log-RERAISE: every except logs then re-raises; only documented bool state-checks may return
- Match the sibling ApiInterface/BrowserInterface style for trace/log usage (read one for IDIOM only — `framework/interfaces/` siblings are current-law code, not v2)
- No screenshot/report machinery, no domain vocabulary (Layer 1)

## Acceptance

py_compile passes; AST shows full method surface per the design doc; no pyodbc/sqlalchemy imports.

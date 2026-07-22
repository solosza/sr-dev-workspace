# Gate Contract — 215 SqlServerInterface (V3)

Deliverable: `framework/interfaces/sql_server_interface.py` from scratch on mssql-python, contract-compliant, live-tested against the Orderly SQL Server DB.

| Gate | Check | Method | Task | Pass Criteria |
|------|-------|--------|------|---------------|
| SI3-01 | Branch `build/215-qa-build-sql-server-interface` from platform main | run_code (git) | 001 | branch current; merge-base == main HEAD |
| SI3-02 | Interface file exists; imports `mssql_python` and NEVER `pyodbc`/`sqlalchemy`; method surface per design doc: execute_query, execute_query_one, execute_scalar, execute_non_query, execute_many, execute_sproc + transaction control + metadata + connection state (exact names from doc's Method Surface section) | file_exists + AST | 003 | all methods present; banned imports absent |
| SI3-03 | `?` parameterization everywhere (no f-string/`%`/.format SQL interpolation in execute paths) | AST + grep | 003 | zero interpolated SQL |
| SI3-04 | Clean-room: v2 oracle_interface.py never read (no structural mirroring; task log audit) + vocab lexicon clean | run_test + grep | 003 | lexicon 0 hits; no v2 code echoes |
| SI3-05 | Contract semantics (lesson #40): every except lacking `raise` is a documented bool/primitive state-check return; catch-log-RERAISE on all execute paths; no screenshot/report machinery; AST checks body-scoped, docstring-excluded (lessons #39/#44) | run_test (AST) | 004 | all except blocks classified compliant |
| SI3-06 | Negative path: injected SDK failure (bad SQL / closed connection) PROPAGATES to caller after logging | run_test | 004 | exception type surfaces; log line emitted |
| SI3-07 | L3 live vs Orderly DB (native SQL Server, db `orderly`): execute_query returns seeded rows; query_one/scalar/non_query correct; execute_many batch insert+cleanup; execute_sproc runs `process_pending_orders` with verified status semantics; transaction commit AND rollback proven by row-state | run_test | 005 | all live asserts green; DB left in seeded state |
| SI3-08 | Return types match design doc's Return Types section exactly | AST + run_test | 004 | types verified |

## Rules

- READ the two design docs FULLY before writing any code (RULE ZERO) — method names, return types, constructor contract come from the doc, not memory
- L3 connection: `Server=localhost;Database=orderly;Trusted_Connection=yes` via mssql-python's connection string format (read the SDK docs/help for exact syntax — do not guess)
- L3 must restore DB state (re-run init_sqlserver.py or targeted cleanup) — leave `orderly` seeded
- ONLY database `orderly` may be touched; the instance holds unrelated real databases
- Any red → fix → /kernel/learn

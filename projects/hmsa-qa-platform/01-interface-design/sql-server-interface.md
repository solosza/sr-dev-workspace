# SqlServerInterface — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 1 rules apply:
- Wraps the SDK — no business logic, no domain vocabulary
- Constructor takes SDK instance + config + logger
- Config-driven defaults (timeouts, headers)
- Returns SDK primitives only — never domain objects
- No knowledge of layers above
- Catches SDK exceptions, logs, re-raises — never swallows
- One SDK call per method
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Inline comments only where explanation is needed
- Methods organized by category with section headers (`# === CATEGORY ===`)
- Type hints on all parameters and return types
- Logging on every operation
- Constants as class-level attributes, config-driven defaults via constructor
- Composition over inheritance — no subclassing
- PEP 8 + SOLID (by reference)

## Decision

**REWRITE from scratch.** The hmsa-healthcare-qa `sql_server_interface.py` (182 lines) is adapted directly from v2's `oracle_interface.py` (171 lines) — 80% structural similarity, same anti-patterns. Cannot copy. Must build a clean Layer 1 wrapper that follows the established constructor pattern (BrowserInterface, ApiInterface).

## SDK

`mssql-python` (Microsoft official) — GA Nov 2025. Direct Database Connectivity (DDBC) architecture, no ODBC driver dependency, 2-8x faster than mssql-python. Same cursor API pattern (connect → cursor → execute → fetch). Chosen over mssql-python because: greenfield project, no migration cost, simpler Docker/CI setup (no driver install), Microsoft-backed with active development.

## What's Wrong with v2 / hmsa-healthcare-qa Version

| Anti-Pattern | v2/hmsa-healthcare-qa | New Platform | Why |
|-------------|----------------------|-------------|-----|
| Auto-connect in constructor | `_connect()` called in `__init__` | Connection created externally by Driver & Client Factory (3.5) | Constructor must not perform I/O — contract rule |
| Internal config reading | `_set_database()` reads `db_config.json` | Config dict passed in via constructor | No file I/O in Layer 1 — config comes from conftest |
| Internal login resolution | `_set_login()` reads `user_config.json` | Credentials resolved externally (config + .env) | Layer 1 has no knowledge of config sources |
| Hardcoded paths | `f"data/sql/{file_name}"` | Path passed as parameter | No path assumptions in Layer 1 |
| String interpolation in SQL | `query.format(...)` | Parameterized queries (`?` placeholders) | SQL injection prevention — non-negotiable |
| Mixed concerns | `query_from_file` reads file + executes SQL | Separate: caller reads file, passes SQL string | One SDK call per method |
| No type hints | Bare `def query(self, query)` | Full type annotations on every parameter and return | Contract rule |
| No section headers | Flat method list | `# === CATEGORY ===` headers | Contract rule |
| Identical to OracleInterface | Same `_set_database`, `_set_login`, `_connect` | Completely different architecture | IP differentiation |

## Constructor

```python
def __init__(self, connection: mssql_python.Connection, config: dict, logger: logging.Logger):
```

- `connection` — `mssql_python.Connection` instance (created by Driver & Client Factory, 3.5)
- `config` — dict with `default_timeout`, `autocommit`, `fetch_size`
- `logger` — standard logging.Logger

Same pattern as BrowserInterface and ApiInterface: SDK instance + config + logger. Connection lifecycle managed externally.

## Method Surface

### Query Execution
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `execute_query` | `(sql: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> list[Row]` | Execute SELECT, return all rows |
| `execute_query_one` | `(sql: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> Optional[Row]` | Execute SELECT, return first row or None |
| `execute_scalar` | `(sql: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> Any` | Execute SELECT, return first column of first row |
| `execute_non_query` | `(sql: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> int` | Execute INSERT/UPDATE/DELETE, return rows affected |
| `execute_many` | `(sql: str, params_list: list[tuple], timeout: Optional[int] = None) -> int` | Batch execute with multiple param sets (bulk insert/update), return total rows affected |

### Stored Procedures
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `execute_sproc` | `(sproc_name: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> list[Row]` | Execute stored procedure, return result set |
| `execute_sproc_no_result` | `(sproc_name: str, params: Optional[tuple] = None, timeout: Optional[int] = None) -> None` | Execute stored procedure with no result set |

### Transaction Control
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `commit` | `() -> None` | Commit current transaction |
| `rollback` | `() -> None` | Rollback current transaction |

### Metadata
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `get_tables` | `(schema: Optional[str] = None) -> list[str]` | List table names in schema |
| `get_columns` | `(table: str, schema: Optional[str] = None) -> list[dict]` | Get column metadata for table |
| `get_row_count` | `(table: str, schema: Optional[str] = None) -> int` | Return row count for table |

### Connection State
| Method | Signature | What It Does |
|--------|-----------|-------------|
| `is_connected` | `() -> bool` | Check if connection is alive |
| `get_database_name` | `() -> str` | Return current database name |

## Key Differentiators from v2

1. **No internal connection management** — connection is injected, not created. No `_connect()`, `_set_database()`, `_set_login()`. These don't exist.

2. **Parameterized queries everywhere** — every method takes `params: Optional[tuple]`. No string formatting, no `.format()`, no f-strings in SQL. The `?` placeholder is mssql-python's native parameterization.

3. **Explicit transaction control** — `commit()` and `rollback()` exposed. v2 used autocommit silently. New platform makes it explicit.

4. **Metadata methods** — `get_tables`, `get_columns`, `get_row_count` enable Layer 2 Data Objects to discover schema dynamically. v2 only had `get_database_list`.

5. **Scalar and single-row shortcuts** — `execute_scalar` and `execute_query_one` reduce boilerplate at Layer 2. One SDK call each (cursor.fetchone + column extract).

6. **No file I/O** — no `query_from_file`. Caller reads the file (or Layer 2 does), passes SQL string. Layer 1 doesn't touch the filesystem.

7. **Timeout per-call** — every method accepts optional `timeout` override. Uses `cursor.timeout` before execution. v2 only had connect_timeout.

## Return Types

All methods return **SDK primitives**:
- `list[Row]` — DB-API 2.0 row type (tuple-like, column-accessible)
- `Row` — single row
- `int` — row count or rows affected
- `str` — database name
- `bool` — connection state
- `list[str]` — table names
- `list[dict]` — column metadata (name, type, nullable, size)
- `Any` — scalar value

No domain objects. No custom wrappers. Contract compliant.

## Contract Compliance

| Rule | Status |
|------|--------|
| Wraps SDK — no business logic | PASS — wraps mssql-python.Connection |
| Constructor takes SDK instance + config + logger | PASS |
| Config-driven defaults (timeout, fetch_size) | PASS |
| Returns SDK primitives only | PASS — Row, int, str, bool |
| No knowledge of upper layers | PASS |
| Catches SDK exceptions, logs, re-raises | PASS |
| One SDK call per method | PASS — each method is one cursor operation |
| No domain vocabulary | PASS — SQL and table names come from callers |
| No file I/O | PASS — removed query_from_file |

## Naming: trace.py

The v2/hmsa-healthcare-qa `sql_server_interface.py` imported `autologger` and decorated with `@automation_logger("SqlServerInterface")`. This is **removed** in the new platform.

Layer 1 interfaces log internally via `self.logger` on every operation (contract rule). The `@trace("Task")` decorator (at `resources/utilities/trace.py`) would double-log. Layer 1 does NOT use `@trace` — only Layer 3+ imports it.

This matches BrowserInterface and ApiInterface — all Layer 1 files log via constructor-injected logger, not via decorator.

## Dependencies

- `mssql-python` (package) / `mssql_python` (import) — Connection, Cursor, Row, exceptions
- `logging` (stdlib)
- `typing` (stdlib — Optional, Any)

## What Does NOT Go Here

- No connection string building (Driver & Client Factory, 3.5)
- No SQL file reading (Layer 2 Data Objects or test fixtures)
- No query templating (Layer 2)
- No result-to-domain-object mapping (Layer 2 Data Objects)
- No retry logic (Layer 2 or conftest plugin)
- No schema validation (Layer 2)
- No test data setup orchestration (Layer 3 Task)

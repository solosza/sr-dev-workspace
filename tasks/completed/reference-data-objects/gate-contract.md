# Gate Contract - 216 _reference Data Objects (V3)

Deliverable: framework/_reference/data_objects/ package - pydantic row models, sql/ folder, OrdersDataObject with variant-to-identifier maps, consuming SqlServerInterface (215).

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| DO-01 | Branch from platform main (includes 215 merge) | run_code | 001 | merge-base == main HEAD |
| DO-02 | Row models: pydantic models mirroring the REAL Orderly schema (customers, orders, order_items - read db_sqlserver_schema.sql, do not invent columns); types match T-SQL types | AST + run_code | 002 | fields == schema columns |
| DO-03 | sql/ folder per data-objects.md canonical structure: parameterized .sql files ONLY (? placeholders; zero interpolation) | grep | 003 | all statements parameterized |
| DO-04 | OrdersDataObject per design doc: canonical structure, variant-to-SP/table maps as Data Object constants (ratified refinement in tasks-db.md), methods delegate to SqlServerInterface - NO direct mssql_python/pyodbc usage at Layer 2 | AST | 004 | delegation only; maps present as constants |
| DO-05 | L1: structure complete per design doc; extended vocab lexicon 0 hits; single-root imports (from _reference... style per DEF-014) | run_test | 005 | greps + AST clean |
| DO-06 | L2 contract semantics (lesson #40): except-blocks-reraise; typed returns (pydantic models out, not raw tuples); no domain vocabulary beyond generic commerce; AST body-scoped/docstring-excluded (lessons #39/#44) | run_test | 006 | all classified compliant |
| DO-07 | L3 live vs orderly DB: OrdersDataObject queries return typed rows matching seed; variant map resolves to real SP (process_pending_orders) and executes; row models validate live rows without coercion errors; DB left seeded | run_test | 007 | live asserts green |

## Rules
- READ data-objects.md + tasks-db.md + 5-layer-contract.md FULLY before building (RULE ZERO)
- READ the real schema files (db_sqlserver_schema.sql, db.py) - models mirror reality, never memory
- Layer 2 consumes Layer 1 (SqlServerInterface) - importing DB drivers directly at Layer 2 is a defect
- L3 unreachable => L3-BLOCKED and STOP (never fake)
- Any red: fix then /kernel/learn

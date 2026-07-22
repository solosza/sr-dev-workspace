# SqlServerInterface (V3) — Task Index

Backlog: [[../../docs/backlog/215-qa-build-sql-server-interface.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type | Depends on |
|---|------|------|-----------|
| 001 | [[001-build-create-feature-branch.md]] | BUILD | — |
| 002 | [[002-build-write-interface.md]] | BUILD | 001 |
| 003 | [[003-test-l1-structure-cleanroom.md]] | TEST | 002 |
| 004 | [[004-test-l2-contract-semantics.md]] | TEST | 003 |
| 005 | [[005-test-l3-live-orderly-db.md]] | TEST | 004 |

## Constraints (backlog 215 + lessons)

- FROM SCRATCH on **mssql-python** (verified installed, 1.11.0) — pyodbc import anywhere in the interface is a defect
- CLEAN-ROOM: v2 `oracle_interface.py` is NEVER opened for code; hmsa-healthcare-qa concept-only
- Branch `build/215-qa-build-sql-server-interface` in `D:/my_ai_projects/project_test_repos/hmsa-qa-platform`; never its main
- Generic commerce vocabulary only — extended lexicon (lesson #46)
- L3 target: NATIVE SQL Server 2019, database `orderly` (214 accepted, live, seeded; SP process_pending_orders present). If unreachable: L3-BLOCKED and STOP — never fake e2e
- Contract-semantics gates mandatory (lesson #40): except-blocks-reraise, layer boundaries, negative-path propagation; AST checks body-scoped + docstring-excluded (lessons #39/#44)

## Design sources (inner agents READ these fully before building)

- `projects/hmsa-qa-platform/01-interface-design/sql-server-interface.md` (governing design: constructor, method surface, return types, compliance table)
- `projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md` (contract law; compliance tables are gate sources)

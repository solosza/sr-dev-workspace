# Harness DB Slice (V3) — Task Index

Backlog: [[../../docs/backlog/214-qa-build-harness-db-slice.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type | Depends on |
|---|------|------|-----------|
| 001 | [[001-build-create-feature-branch.md]] | BUILD | — |
| 002 | [[002-build-write-sqlserver-compose.md]] | BUILD | 001 |
| 003 | [[003-build-write-sqlserver-schema.md]] | BUILD | 001 |
| 004 | [[004-build-write-stored-procedure.md]] | BUILD | 003 |
| 005 | [[005-build-update-db-config.md]] | BUILD | 001 |
| 006 | [[006-build-write-init-script.md]] | BUILD | 002-005 |
| 007 | [[007-test-l1-files-and-vocab.md]] | TEST | 001-006 |
| 008 | [[008-test-l2-container-schema-sp.md]] | TEST | 007 |
| 009 | [[009-test-l3-app-on-sqlserver.md]] | TEST | 008 |

## Constraints (from backlog 214 + lessons)

- ALL platform writes on `build/214-qa-build-harness-db-slice` branch in `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` — NEVER its main
- Generic commerce vocabulary ONLY — extended ban lexicon (lesson #46): hmsa, healthcare, claim, patient, member, subscriber, eligib*, EOB, remittance, diagnosis, provider(-as-insurer), autopend, DRG, PCN, 837
- V2 (209-213) accepted — prerequisite satisfied
- Docker daemon verified up (29.2.1) at task-build time
- App storage access stays SQLAlchemy Core — the swap is config, not rewrite (data-model.md)
- Same 3-table schema as SQLite (Customer, Order, OrderItem)

## Design sources

- `projects/hmsa-qa-platform/04-test-harness/harness-app.md` (V3 row)
- `projects/hmsa-qa-platform/04-test-harness/data-model.md` (entities, storage-per-vertical)

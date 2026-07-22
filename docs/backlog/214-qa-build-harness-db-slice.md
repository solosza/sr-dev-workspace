# Orderly Harness — DB Slice [V3 first]

## Status
Open

## Priority
High — V3 target

## Summary
Swap Orderly persistence to SQL Server in Docker per harness-app.md V3: same schema, plus process_pending_orders stored procedure (SP-as-subject target). Verify Docker availability first; if unavailable, report BLOCKED and stop.

## Requirements
- SQL Server container + schema migration + seed; app config swap (SQLAlchemy Core)
- process_pending_orders SP implementing PENDING→PROCESSING transitions

## References
- projects/hmsa-qa-platform/04-test-harness/harness-app.md
- projects/hmsa-qa-platform/04-test-harness/data-model.md

## Task Builder Input
- **Deliverable:** Orderly on SQL Server (Docker) + SP, smoke-tested
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/214-qa-build-harness-db-slice; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

# _reference DB Test — V3 E2E Gate [V3 last]

## Status
Open

## Priority
High — V3 exit gate

## Summary
Build the DB test exemplar per the 2.4.3 design doc and run E2E against the real SP on Orderly SQL Server: parametrized variant keys, typed outcomes + same-instance recount. Passing = V3 exit gate.

## Requirements
- Canonical example per design doc; green against live DB

## References
- projects/hmsa-qa-platform/02-reference-patterns/tests-db.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tests/ DB test exemplar, GREEN vs Orderly SQL Server. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/219-qa-build-reference-tests-db; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

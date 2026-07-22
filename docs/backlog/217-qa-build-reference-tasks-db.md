# _reference DB Tasks [V3]

## Status
Open

## Priority
Medium — V3 Layer 3

## Summary
Build the DB Tasks exemplar per the 2.2.3 design doc against the real process_pending_orders SP: run/verify separated, variant keys only, typed results.

## Requirements
- Canonical structure per design doc; no identifiers at L3

## References
- projects/hmsa-qa-platform/02-reference-patterns/tasks-db.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tasks/ DB pipeline exemplar vs real SP, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/217-qa-build-reference-tasks-db; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

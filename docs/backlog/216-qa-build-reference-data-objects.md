# _reference Data Objects [V3]

## Status
Open

## Priority
High — V3 Layer 2

## Summary
Build _reference/data_objects/ per the 2.1.3 design doc against the real Orderly schema: OrdersDataObject + pydantic row models + sql/ folder + variant→identifier maps (ratified refinement).

## Requirements
- Canonical structure; parameterized only; variant→SP/table maps as Data Object constants

## References
- projects/hmsa-qa-platform/02-reference-patterns/data-objects.md
- projects/hmsa-qa-platform/02-reference-patterns/tasks-db.md (ratified refinement)
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/data_objects/*.py + sql/ vs Orderly schema, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/216-qa-build-reference-data-objects; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

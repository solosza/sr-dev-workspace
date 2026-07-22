# _reference System Role [V3]

## Status
Open

## Priority
Medium — V3 Layer 4

## Summary
Build the System Role exemplar per the 2.3.2 design doc: BatchValidator across discovery + pipeline modules, typed results, when-NOT-to-create rule in docstring.

## Requirements
- Canonical example per design doc (orders domain)

## References
- projects/hmsa-qa-platform/02-reference-patterns/roles-system.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/roles/ system role exemplar, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/218-qa-build-reference-roles-system; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

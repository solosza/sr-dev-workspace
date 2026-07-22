# _reference Hybrid Role [V5]

## Status
Open

## Priority
High — flagship Layer 4

## Summary
Build the Hybrid Role exemplar per the 2.3.3 design doc (orders persona spanning interfaces, identity threading: persona for UI legs only).

## Requirements
- Canonical shape; typed ScenarioResult; injection stays behind a Task seam

## References
- projects/hmsa-qa-platform/02-reference-patterns/roles-hybrid.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/roles/ hybrid role exemplar, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V5 Integration — blocked until V4 (220-223) is fully built and tested (223 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/226-qa-build-reference-roles-hybrid; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

# _reference Hybrid Test — V5 E2E Gate [V5 last]

## Status
Open

## Priority
High — the platform thesis test

## Summary
Build the hybrid test exemplar per the 2.4.5 design doc and run the full DB→UI→API→DB flow E2E on composed Orderly: dual assertion in full. Passing = V5 exit gate = the platform thesis demonstrated.

## Requirements
- Canonical example per design doc; green on the composed stack

## References
- projects/hmsa-qa-platform/02-reference-patterns/tests-hybrid.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tests/ hybrid test exemplar, GREEN on composed Orderly. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V5 Integration — blocked until V4 (220-223) is fully built and tested (223 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/227-qa-build-reference-tests-hybrid; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

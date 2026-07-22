# _reference API Test — V2 E2E Gate [V2 last]

## Status
Open

## Priority
High — V2 exit gate

## Summary
Build the API test exemplar per the 2.4.2 design doc and run E2E against live Orderly API: dual assertion + asserted cleanup. Passing = V2 exit gate.

## Requirements
- Canonical example per design doc (orders domain), green against live harness

## References
- projects/hmsa-qa-platform/02-reference-patterns/tests-api.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tests/ API test exemplar, GREEN vs Orderly. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V2 REST — the pipeline MAY BUILD AND RUN now (user early-V2 authorization at 209 rev 3; the API test suite is browserless), but per the recorded COMPENSATING CONDITION this branch's MERGE/acceptance is HELD until 208 (V1 E2E) runs green — the vertical boundaries still close in order. Extended vocab lexicon applies (lesson #45): sweep design doc + shipped code. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/213-qa-build-reference-tests-api; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

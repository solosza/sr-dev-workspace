# _reference SOAP Test — V4 E2E Gate [V4 last]

## Status
Open

## Priority
Medium — V4 exit gate

## Summary
Build the SOAP test exemplar per the 2.4.4 design doc and run E2E against live Orderly SOAP: typed assertion + pytest.raises fault test. Passing = V4 exit gate.

## Requirements
- Canonical example per design doc; green against live harness

## References
- projects/hmsa-qa-platform/02-reference-patterns/tests-soap.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tests/ SOAP test exemplar, GREEN vs Orderly SOAP. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V4 SOAP — blocked until V3 (214-219) is fully built and tested (219 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/223-qa-build-reference-tests-soap; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

# _reference SOAP Tasks [V4]

## Status
Open

## Priority
Medium — V4 Layer 3

## Summary
Build the SOAP Tasks exemplar per the 2.2.4 design doc (orders domain: order status eligibility), typed returns, fault propagation. Also complete the V2-deferred SOAP object e2e.

## Requirements
- Canonical structure per design doc; close the 211 SOAP-object L3 deferral

## References
- projects/hmsa-qa-platform/02-reference-patterns/tasks-soap.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tasks/ SOAP task exemplar, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V4 SOAP — blocked until V3 (214-219) is fully built and tested (219 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/222-qa-build-reference-tasks-soap; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

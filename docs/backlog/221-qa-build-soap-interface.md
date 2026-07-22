# SoapInterface [V4]

## Status
Open

## Priority
Medium — V4 Layer 1

## Summary
Build Layer 1 SoapInterface wrapping zeep.Client from scratch per the 1.4 design doc.

## Requirements
- call_operation + create_object; WSDL/binding via config; faults catch-log-reraise

## References
- projects/hmsa-qa-platform/01-interface-design/soap-interface.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/interfaces/soap_interface.py, L1-L3 tested vs Orderly SOAP. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V4 SOAP — blocked until V3 (214-219) is fully built and tested (219 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/221-qa-build-soap-interface; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

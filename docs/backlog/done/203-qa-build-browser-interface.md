# BrowserInterface [V1]

## Status
Open

## Priority
High — V1 Layer 1

## Summary
Build Layer 1 BrowserInterface: copy/adapt platform-selenium browser_interface.py (674 lines, clean, no IP overlap) per the 1.1 design doc.

## Requirements
- Generic SDK wrappers only (monolith guard: no domain vocabulary, no composed ops, no locators)
- Constructor (driver, config, logger) per contract L1 rules

## References
- projects/hmsa-qa-platform/01-interface-design/browser-interface.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)
- D:/my_ai_projects/project_test_repos/platform-selenium/framework/interfaces/browser_interface.py

## Task Builder Input
- **Deliverable:** framework/interfaces/browser_interface.py, contract-compliant, importable, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/203-qa-build-browser-interface; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

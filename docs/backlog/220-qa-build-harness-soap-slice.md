# Orderly Harness — SOAP Slice [V4 first]

## Status
Open

## Priority
Medium — V4 target

## Summary
Add the SOAP facade to Orderly per harness-app.md V4: GetCustomer, GetOrderStatus operations over the same services.

## Requirements
- Per harness-app.md; WSDL served; operations stable for zeep

## References
- projects/hmsa-qa-platform/04-test-harness/harness-app.md

## Task Builder Input
- **Deliverable:** Orderly SOAP slice with WSDL, smoke-tested
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V4 SOAP — blocked until V3 (214-219) is fully built and tested (219 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/220-qa-build-harness-soap-slice; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

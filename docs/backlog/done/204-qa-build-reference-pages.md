# _reference Pages vs Orderly [V1]

## Status
Open

## Priority
High — V1 Layer 2

## Summary
Build _reference/pages/ per the 2.1.1 design doc with locators bound to the REAL Orderly UI (202): login_page, orders_page (list/create/edit), customer_page.

## Requirements
- Structure per design doc: locator class constants (data-testid), section headers, return-self chaining, state-checks
- Locators verified against the running harness DOM — no invented selectors

## References
- projects/hmsa-qa-platform/02-reference-patterns/page-objects.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)
- projects/hmsa-qa-platform/04-test-harness/harness-app.md

## Task Builder Input
- **Deliverable:** framework/_reference/pages/*.py bound to Orderly, L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/204-qa-build-reference-pages; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

# _reference Shared Components vs Orderly [V1]

## Status
Open

## Priority
High — platform IP exemplars

## Summary
Build _reference/components/ per the 2.1.5 design doc: modal_component.py (lead) + grid_component.py (flagship) with locator-contract injection, configured against Orderly's real modal and order grid. Exactly two — the set is deferred.

## Requirements
- GridLocators/ModalLocators contracts + mechanics-only classes per canonical examples
- Genericity scope declared per component
- Orderly page constants supply the locator VALUES; fixtures wire them

## References
- projects/hmsa-qa-platform/02-reference-patterns/shared-components.md
- docs/walkthroughs/2026-07-14-shared-components.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/components/modal_component.py + grid_component.py, L1-L3 tested vs Orderly. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/205-qa-build-reference-components; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

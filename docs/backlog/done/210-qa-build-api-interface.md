# ApiInterface [V2]

## Status
Open

## Priority
High — V2 Layer 1

## Summary
Build Layer 1 ApiInterface wrapping requests.Session, translated from platform-playwright api-client.ts per the 1.2 design doc.

## Requirements
- get/post/put/patch/delete returning ApiResponse (status, body, response_time); synchronous

## References
- projects/hmsa-qa-platform/01-interface-design/api-interface.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)
- D:/my_ai_projects/project_test_repos/platform-playwright/framework/interfaces/api-client.ts (pattern source)

## Task Builder Input
- **Deliverable:** framework/interfaces/api_interface.py, contract-compliant, L1-L3 tested vs Orderly API. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V2 REST — V1 block AMENDED 2026-07-16 (same user authorization as 209, intent rev 3 there): 208 env-held per backlog 235; compensating condition: 208 green before 213 accepted. NOTE from 209 gates: Orderly POST endpoints are slash-canonical (/api/customers/, /api/orders/) — bind canonical paths explicitly in api-objects/tests. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/210-qa-build-api-interface; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

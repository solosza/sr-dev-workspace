# _reference REST Tasks [V2]

## Status
Open

## Priority
Medium — V2 Layer 3

## Summary
Build the REST Tasks exemplar per the 2.2.2 design doc in the orders domain (OrderManagementTasks): typed returns, domain exception, idempotent cleanup.

## Requirements
- Canonical structure incl. ensure_order_absent-style cleanup (explicit-cleanup discipline)

## References
- projects/hmsa-qa-platform/02-reference-patterns/tasks-rest-api.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tasks/ REST task exemplar (orders), L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V2 REST — V1 block AMENDED 2026-07-16 (user early-V2 authorization, recorded at 209 intent rev 3; compensating condition: 208 green before 213 accepted). Extended vocab lexicon applies (lesson #45): grep the design doc AND shipped code for member/subscriber/eligib*/DRG/PCN/837 in addition to the four base terms. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/212-qa-build-reference-tasks-rest-api; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

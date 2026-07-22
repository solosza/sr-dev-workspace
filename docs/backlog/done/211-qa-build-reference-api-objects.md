# _reference API Objects incl. SOAP object [V2]

## Status
Open

## Priority
High — V2 Layer 2

## Summary
Build _reference/api_objects/ per the 2.1.2 design doc against Orderly endpoints (OrdersApiObject + pydantic models), including the SOAP object exemplar from the same doc (built now, e2e-tested in V4).

## Requirements
- Canonical structure per design doc; last_response convention; models/ subfolder
- SOAP object exemplar included; its L3 e2e deferred to V4 (note in task)

## References
- projects/hmsa-qa-platform/02-reference-patterns/api-objects.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/api_objects/*.py vs Orderly, L1-L3 tested (SOAP part L1/L2 only until V4). L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V2 REST — V1 block AMENDED 2026-07-16 (user early-V2 authorization, recorded at 209 intent rev 3; compensating condition: 208 green before 213 accepted). Orderly POST endpoints are slash-canonical (/api/orders/) — bind canonical paths in api-objects (209 orchestrator flag). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/211-qa-build-reference-api-objects; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

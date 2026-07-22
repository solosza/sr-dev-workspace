# Orderly Harness — API Slice [V2 first]

## Status
Open

## Priority
High — V2 target

## Summary
Add the REST API slice to Orderly per harness-app.md: /api/customers, /api/orders CRUD + /api/orders/{id}/process, over the same services/data as the UI.

## Requirements
- Per harness-app.md V2 slice; JSON responses stable for pydantic models

## References
- projects/hmsa-qa-platform/04-test-harness/harness-app.md
- projects/hmsa-qa-platform/04-test-harness/data-model.md

## Task Builder Input
- **Deliverable:** Orderly REST API slice, smoke-tested
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V2 REST — original block (V1 202-208 fully tested) AMENDED 2026-07-16 by user authorization ("go ahead" on early V2 open): 208 is env-held by the machine's selenium click fault (backlog 235, lessons #41/#42), all V1 builds are merged and gated, and the API vertical has zero selenium dependency. COMPENSATING CONDITION: 208 must run green before V2's exit gate (213) is accepted — the vertical boundary still closes in order. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/209-qa-build-harness-api-slice; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

# _reference UI Role [V1]

## Status
Open

## Priority
Medium — V1 Layer 4

## Summary
Build the UI Role exemplar per the 2.3.1 design doc in the orders domain: OrderClerk persona (Tasks via DI + identity, self-authenticating workflows). Multi-user pattern documented (clerk creates, manager cancels).

## Requirements
- COPY-FIRST: start from platform-selenium `framework/_reference/roles/` (employee_manager.py, task_manager.py — own IP), adapt to Orderly personas + contract v2.3; every copied pattern gated against the CURRENT contract (lesson #38)
- Canonical shape per design doc adapted to Orderly personas (clerk/manager)

## References
- D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/roles/ (copy source — own IP; clean-room ban is v2-only)
- projects/hmsa-qa-platform/02-reference-patterns/roles-ui.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/roles/ UI role exemplar (orders domain), L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/207-qa-build-reference-roles-ui; merge via /kernel/review-queue accept, never direct to main. COPY-FIRST: platform-selenium `framework/_reference/roles/` is the starting point; AST contract-semantics gates mandatory on copied code (lessons #38/#39 — string-grep semantics checks BANNED). L3 live checks may use JS-assisted app triggers ONLY in validation scripts (never framework code) while the selenium click regression persists (lessons #41/#42). Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

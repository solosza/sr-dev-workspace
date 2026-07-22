# _reference Browser Tasks [V1]

## Status
Open

## Priority
Medium — V1 Layer 3

## Summary
Build the Browser Tasks exemplar in the ORDERS domain via COPY-FIRST: start from platform-selenium's `framework/_reference/tasks/` (employee_management_tasks.py, task_management_tasks.py — our own proven IP), then adapt to Orderly bindings, contract v2.3 (DI constructor, -> None norm, one typed-return exception), and the 2.2.1 design doc. Copied code predates the contract — AST contract-semantics gates are mandatory (lesson #38).

## Requirements
- COPY-FIRST: read platform-selenium counterpart files verbatim as the starting point; adapt, don't rewrite from scratch
- Canonical structure per design doc; nav and submit as separate methods; domain = Orderly orders
- Every copied pattern gated against CURRENT contract v2.3, not the source repo's era

## References
- D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tasks/ (copy source — own IP; clean-room ban is v2-only)
- projects/hmsa-qa-platform/02-reference-patterns/tasks-browser.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tasks/ browser task exemplar (orders domain), L1-L3 tested. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/206-qa-build-reference-tasks-browser; merge via /kernel/review-queue accept, never direct to main. COPY-FIRST: platform-selenium `framework/_reference/tasks/` is the starting point (own IP); adapt to Orderly + contract v2.3; AST contract-semantics gates mandatory on copied code (lessons #38/#39 — string-grep semantics checks BANNED). Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization; L3 live checks may use JS-assisted app triggers ONLY in validation scripts (never framework code) while the selenium click regression persists (lessons #41/#42).

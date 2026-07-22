# _reference UI Test — V1 E2E Gate [V1 last]

## Status
Open

## Priority
High — V1 exit gate

## Summary
Build the UI test exemplar per the 2.4.1 design doc and run it E2E against the live Orderly harness: full V1 stack (interface → pages/components → tasks → role → test) exercised for real. This test passing IS the V1 exit gate.

## Requirements
- COPY-FIRST: start from platform-selenium `framework/_reference/tests/test_e2e_create_employee_and_assign_task.py` (own IP), adapt to Orderly + contract v2.3 (AAA, dual assertion, same-instance rule); copied patterns gated against the CURRENT contract (lesson #38)
- Canonical example per design doc (orders domain); multi-user test included (clerk+manager)
- Runs green against the running harness — screenshots-on-failure hook active
- ENV GATE (lessons #41/#42): this E2E runs the framework's SELENIUM stack — before executing, run the bare-selenium two-page click probe; if it fails, report L3-BLOCKED and STOP (do not substitute Playwright for the framework's own test run)

## References
- D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tests/ (copy source — own IP; clean-room ban is v2-only)
- projects/hmsa-qa-platform/02-reference-patterns/tests-ui.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/_reference/tests/ UI test exemplar, GREEN against live Orderly. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/208-qa-build-reference-tests-ui; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

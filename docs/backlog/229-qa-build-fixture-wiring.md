# Fixture Wiring / Conftest Build [BLOCKED]

## Status
Open

## Priority
High when unblocked — wires everything

## Summary
Build the full conftest stack per the 2.5.2 design doc. HARD BLOCK: requires Phase 3.1 (config schema) and 3.5 (factories) designed AND built first.

## Requirements
- COPY-FIRST where counterparts exist: platform-selenium `tests/conftest.py` + `framework/resources/` (driver.py, autologger.py) are starting material (own IP) — but the walkthrough-settled conftest design GOVERNS where they diverge (pytest_plugins composition, per-user credentials via password_env, --scenario-dir, scope map, explicit cleanup)
- Implement exactly per design doc canonical examples
- DO NOT EXECUTE until 3.1 + 3.5 exist

## References
- D:/my_ai_projects/project_test_repos/platform-selenium/tests/conftest.py + framework/resources/ (copy source — own IP; design doc wins on divergence)
- projects/hmsa-qa-platform/02-reference-patterns/fixture-wiring.md
- docs/walkthroughs/2026-07-13-conftest-design.md
- projects/hmsa-qa-platform/README.md (build-order exceptions)

## Task Builder Input
- **Deliverable:** tests/conftest.py + framework/fixtures/*.py — ONLY after 3.1/3.5
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** HARD BLOCK — do not execute until Phase 3.1 and 3.5 are designed and built. Exists for sequencing visibility. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/229-qa-build-fixture-wiring; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

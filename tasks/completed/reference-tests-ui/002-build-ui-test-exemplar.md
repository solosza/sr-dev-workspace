# Build: UI Test Exemplar (COPY-FIRST)

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- COPY-FIRST: start from `D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tests/test_e2e_create_employee_and_assign_task.py` (own IP; clean-room ban is v2-only), adapt to Orderly + contract v2.3
- READ FIRST (RULE ZERO): tests-ui.md canonical (swept 2026-07-21), 5-layer-contract.md L5 rules, and the SHIPPED `_reference` pages/tasks/roles in hmsa-qa-platform (206/207 output) — use their ACTUAL class/method/fixture names, never invented ones
- Canonical single-Task test per tests-ui.md: AAA one block per method, acts through the highest applicable layer (Task when Role would be a pass-through), asserts via SAME-INSTANCE Page Object state-checks, failure message on every assert, `@trace("Test")` + markers
- Multi-user test included (clerk + manager) — multi-persona scenario acts through the ROLES shipped in 207, not raw Tasks
- Dual-assertion rule: UI is the degenerate case (`-> None` Task norm) — page state-checks carry the evidence; do NOT invent return values on Browser Tasks
- Pre-conftest wiring: conftest.py does not exist until 229 — follow the doc's interim instantiation pattern; screenshots are the (future) conftest hook's job — NONE in test bodies
- No waits/retries in test bodies (Page Objects own waits); no data setup in tests (fixtures/scenario data); no locators; no Interface calls to act
- Write ONLY on branch build/208-qa-build-reference-tests-ui in the target repo

## Acceptance Criteria
- [ ] UI test exemplar file(s) exist under `framework/_reference/tests/` on the branch
- [ ] Canonical single-Task test + multi-user (clerk+manager) Role-driven test present
- [ ] All contract v2.3 rules above followed

## Gates Satisfied
- UT-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

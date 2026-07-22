# Test: Run the Suite Live — THE V1 EXIT SIGNAL

## Type
TEST
## Execution
inline
## Dependencies
- 003

## Requirements
- ENV GATE FIRST (lessons #41/#42): run `python D:/my_ai_projects/project_test_repos/sr_dev_workspace/tools/selenium-click-probe.py --trials 3` — this E2E runs the framework's SELENIUM stack. If any trial drops a click: report **L3-BLOCKED** and STOP (do NOT substitute Playwright for the framework's own test run, do NOT weaken assertions). Probe passed 16/16 on 2026-07-21 post-reboot — re-verify at execution time anyway.
- Env preflight (lesson #46): import-check harness deps (`fastapi`, `sqlalchemy`, `uvicorn`) before booting — reinstall via pip if site-packages regressed
- Fresh seed + boot Orderly (READ the harness docs/compose in hmsa-qa-platform for the UI slice port — do not assume; lesson #40: read route handlers before ANY URL/redirect assertion in the tests)
- `python -m pytest framework/_reference/tests/ --rootdir=D:/my_ai_projects/project_test_repos/hmsa-qa-platform -v` with `PYTHONPATH=framework` ONLY (single-root post DEF-014, merge 8a23917) — capture full output
- ALL tests green; zero skips; screenshots-on-failure evidence chain intact; cleanup asserted (no residue test data beyond seed)
- Cleanup server in finally; env problem → L3-BLOCKED honestly; any red → fix → /kernel/learn (never weaken an assertion to pass)

## Acceptance Criteria
- [ ] Probe green at execution time; pytest exit 0; output captured; zero skips; no residue

## Gates Satisfied
- UT-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

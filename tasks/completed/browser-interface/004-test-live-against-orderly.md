# Test: Live Against Orderly (L3)

## Context
Backlog 203: the vertical's whole point — the interface drives a REAL browser against the REAL harness. First true Selenium-on-Orderly moment.

## Type
TEST
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] browser_interface.py exists; Orderly harness present on the branch (merged from 202)

## Requirements
- Ensure selenium + webdriver-manager installed (pip if needed)
- Script: seed + start Orderly (uvicorn, port 8017, background); create HEADLESS Chrome driver; instantiate BrowserInterface(driver, config, logger); using ONLY interface primitives: navigate to http://127.0.0.1:8017/login, enter seeded clerk credentials into [data-testid=input-username]/[data-testid=input-password], click [data-testid=button-login], wait for a post-login element; assert success; quit driver; stop server — both cleaned up in finally
- If Chrome or chromedriver is unavailable on this machine: print L3-BLOCKED with the reason and exit non-zero WITHOUT faking the pass — the orchestrator stops for user decision
- Non-zero exit (other than L3-BLOCKED) = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 (real browser, real app, real login) OR L3-BLOCKED reported honestly

## Gates Satisfied
- BRI-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

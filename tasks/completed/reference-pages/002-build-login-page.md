# Write login_page.py

## Context
Backlog 204: the LoginPage exemplar — platform-selenium's pattern bound to Orderly's real login template.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/204-qa-build-reference-pages

## Requirements
- READ FIRST: the 2.1.1 design doc (workspace), the shipped contract's L2 rules + Browser addendum (target framework/docs/), AND harness/orderly/templates/login.html + base.html — every locator constant must be a data-testid that EXISTS in those templates
- Write framework/_reference/pages/login_page.py (+ pages/__init__.py): constructor takes BrowserInterface only; locator class constants (By.CSS_SELECTOR, "[data-testid='...']"); section headers (LOCATORS / NAVIGATION / ATOMIC METHODS / STATE-CHECK METHODS); atomic methods return self; state-checks (is_login_error_displayed, etc.) return bool
- CONTRACT SEMANTICS (lesson 2026-07-15): NO try/except, NO decorators, NO screenshots, NO waits inside action methods (waits are their own methods)

## Acceptance Criteria
- [ ] File exists; all referenced data-testids exist in the templates; semantics rules hold

## Gates Satisfied
- PAG-02, PAG-03 (partial), PAG-04/05/06 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

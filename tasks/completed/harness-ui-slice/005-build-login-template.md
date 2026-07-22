# Write login.html

## Context
Backlog 202: the login page — first page every UI test touches; platform-selenium's LoginPage exemplar pattern binds here.

## Type
BUILD
## Execution
inline
## Dependencies
- 004
## Phase Gate
- [ ] main.py exists with login routes

## Requirements
- Write `harness/orderly/templates/login.html` + a minimal `base.html` (nav shell with logout link): plain HTML, data-testid on EVERY interactive element (input-username, input-password, button-login, link-logout, nav links)
- Error message element (data-testid="login-error") on failed login

## Acceptance Criteria
- [ ] Templates exist; zero interactive elements without data-testid

## Gates Satisfied
- (feeds HUI-04)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

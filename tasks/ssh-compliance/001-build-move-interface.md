# Move SSH Interface to Canonical Location

## Context
Move ssh_interface.py from framework/_reference/ to framework/interfaces/ to match Selenium/Playwright/Docker convention.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Copy framework/_reference/ssh_interface.py to framework/interfaces/ssh_interface.py in platform-ssh repo

## Acceptance Criteria
- [ ] framework/interfaces/ssh_interface.py exists with SSHInterface class (`grep -q "class SSHInterface" framework/interfaces/ssh_interface.py`)

## Gates Satisfied
STRUCT-01

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.

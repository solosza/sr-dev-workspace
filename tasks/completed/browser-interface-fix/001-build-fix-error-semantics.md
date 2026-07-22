# Fix Error Semantics — Every Except Re-raises

## Context
Orchestrator validation of 203 found 5 of 26 except blocks in browser_interface.py swallowing exceptions (log-and-continue). Contract error rule 1: the Interface catches SDK exceptions, logs them, then RE-RAISES — never swallows. A swallowed navigation failure lets tests run against a dead page.

## Type
BUILD
## Execution
inline
## Dependencies
- None
## Phase Gate
- [ ] `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" branch --show-current` → build/203-qa-build-browser-interface (checkout it if not current; do NOT create a new branch)

## Requirements
- READ framework/interfaces/browser_interface.py; find every except block lacking `raise`
- Add `raise` after the logging line in each — preserve the log-first behavior; do not change method signatures or logic otherwise
- Boolean-returning probes (e.g. is_element_displayed catching NoSuchElement to return False) are LEGITIMATE state-checks, NOT swallows — if any of the 5 are that pattern, leave them and document why in a code comment stating the contract distinction

## Acceptance Criteria
- [ ] Every non-state-check except block re-raises (regex count == 0, or documented state-check exemptions)

## Gates Satisfied
- FIX-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

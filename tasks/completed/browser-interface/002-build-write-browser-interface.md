# Write browser_interface.py (copy/adapt from platform-selenium)

## Context
Backlog 203 (V1): the one Layer 1 with a clean, proven source (674 lines, own repo, no IP overlap). Copy and adapt — do not redesign.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/203-qa-build-browser-interface

## Requirements
- READ the design doc: projects/hmsa-qa-platform/01-interface-design/browser-interface.md (workspace) AND the source: D:/my_ai_projects/project_test_repos/platform-selenium/framework/interfaces/browser_interface.py
- Write `framework/interfaces/browser_interface.py` (+ interfaces/__init__.py): the platform-selenium implementation adapted — constructor (driver, config, logger) per contract L1; config-driven defaults; catch-log-reraise on SDK exceptions
- MONOLITH GUARD: generic SDK primitives ONLY — no method may carry domain vocabulary (order/customer/login/orderly), compose multiple SDK calls into a flow, or contain locators
- Imports inside framework relative to framework/ root (recorded lesson)

## Acceptance Criteria
- [ ] File exists; primitives present (click, send_keys/enter_text, find_element, wait_for_*); zero domain-named methods

## Gates Satisfied
- BRI-02, BRI-03, BRI-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

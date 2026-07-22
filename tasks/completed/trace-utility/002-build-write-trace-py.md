# Write trace.py (autologger renamed)

## Context
Backlog 199 (V-BASE): platform-selenium's autologger.py is proven (52 lines) — same implementation, new name, per contract Decorator Usage + README 3.4 rename decision. Clean source (own repo, no IP issue).

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] Current target-repo branch is build/199-qa-build-trace-utility (TRC-01)

## Requirements
- READ the source first: `D:/my_ai_projects/project_test_repos/platform-selenium/framework/resources/utilities/autologger.py`
- Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/resources/utilities/trace.py`: identical behavior, decorator factory named `trace` (usage: `@trace("Task")`, `@trace("Role")`, `@trace("Role Constructor")`, `@trace("Test")`)
- Zero occurrences of `autologger` / `automation_logger` in the new file
- Create package `__init__.py` files as needed (framework/, framework/resources/, framework/resources/utilities/)
- Module docstring states purpose + that it writes into the named logger (interleaves with Interface operation lines)

## Acceptance Criteria
- [ ] File exists at the target path with `def trace` (TRC-02, TRC-03)
- [ ] No legacy naming (grep autologger|automation_logger == 0)

## Gates Satisfied
- TRC-02, TRC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

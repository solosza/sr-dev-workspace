# trace.py Utility [V-BASE]

## Status
Open

## Priority
High — every L3+ file imports it

## Summary
Ship trace.py: platform-selenium autologger.py implementation (52 lines, proven) renamed to @trace, per the contract Decorator Usage section.

## Requirements
- Same implementation, new name — @trace("Task"|"Role"|"Role Constructor"|"Test")
- Writes into the named logger (conftest ledger §6)
- Pure python: logging, functools, datetime

## References
- D:/my_ai_projects/project_test_repos/platform-selenium/framework/resources/utilities/autologger.py (source)
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/resources/utilities/trace.py in target repo, L1-L3 tested
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V-BASE — unlocked (198 accepted). Parallel-safe with other V-BASE items. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/199-qa-build-trace-utility; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

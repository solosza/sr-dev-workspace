# retry.py Utility [V-BASE]

## Status
Open

## Priority
Medium — small, L3 dependency

## Summary
Ship retry.py per the 2.5.3 design doc: transient-failure retry with backoff, declared exceptions only, re-raises after exhaustion.

## Requirements
- Implement exactly the canonical implementation in the design doc
- Two-retries boundary in module docstring

## References
- projects/hmsa-qa-platform/02-reference-patterns/retry-utility.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)

## Task Builder Input
- **Deliverable:** framework/resources/utilities/retry.py in target repo, L1-L3 tested
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V-BASE — unlocked (198 accepted). Parallel-safe with other V-BASE items. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/200-qa-build-retry-utility; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

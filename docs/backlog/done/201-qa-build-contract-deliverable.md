# Contract Deliverable Copy [V-BASE]

## Status
Open

## Priority
Medium — the platform ships its own law

## Summary
Copy the current workspace 5-layer contract into the target repo at framework/docs/5-layer-contract.md — a deliverable, not just a reference.

## Requirements
- Verbatim copy, current version at build time
- Workspace remains source of truth; re-copy on later bumps

## References
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md

## Task Builder Input
- **Deliverable:** framework/docs/5-layer-contract.md in target repo, byte-identical at merge time
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V-BASE — unlocked (198 accepted). Parallel-safe with other V-BASE items. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/201-qa-build-contract-deliverable; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

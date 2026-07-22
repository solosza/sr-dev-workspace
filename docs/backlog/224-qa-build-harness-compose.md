# Orderly Harness — Docker Compose [V5 first]

## Status
Open

## Priority
High — integration substrate

## Summary
Wire the full Orderly stack via docker-compose per Phase 4.3. DESIGN-FIRST: write the 4.3 design doc (docker-composition.md) with the user before this executes.

## Requirements
- App + SQL Server composed; one command up; seed on start
- HARD PRECONDITION: 04-test-harness/docker-composition.md exists and is DESIGNED

## References
- projects/hmsa-qa-platform/04-test-harness/harness-app.md
- projects/hmsa-qa-platform/04-test-harness/docker-composition.md (to be designed)

## Task Builder Input
- **Deliverable:** docker-compose.yml in target repo harness/, full stack up with one command
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V5 Integration — blocked until V4 (220-223) is fully built and tested (223 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/224-qa-build-harness-compose; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.

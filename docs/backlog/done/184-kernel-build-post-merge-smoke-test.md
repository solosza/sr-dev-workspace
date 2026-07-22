# Build Post-Merge Smoke Test

## Status
Open

## Priority
Medium — safety net after feature branch merges to main

## Summary
After a feature branch is accepted (via review-queue) and merged to main, automatically run a smoke test to verify main still works. This is the final gate in the SDLC: backlog → pipeline → feature branch → gap check → prod test → review → merge → smoke test.

## Requirements
- Trigger automatically after merge-to-main (or manually via command)
- Run a lightweight prod-test on the affected repo (not full L1-L5, just critical paths)
- If smoke test fails: alert user, provide rollback option (revert merge commit)
- If smoke test passes: mark the merge as verified
- Track smoke test results in review-status.json alongside the accepted backlog
- Support both single-repo merges and cross-repo impact (if platform-ssh changes, does kernel still work?)

## References
- Review-queue research: `projects/velocity-management-research/final-report.md`
- Prod-test skill: `.claude/skills/prod-test/`
- Worktree integration: backlog 183

## Task Builder Input
- **Deliverable:** Post-merge smoke test command or integration into review-queue accept flow
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must be fast (subset of full prod-test). Must not block the user — run in background, notify on completion. Depends on review-queue (backlog 182 routing test) and worktree integration (backlog 183) being complete first.

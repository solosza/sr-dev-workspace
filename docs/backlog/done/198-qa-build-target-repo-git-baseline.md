# Target Repo Git Baseline (Wave 0)

## Status
Open

## Priority
High — every build wave depends on it

## Summary
Initialize git in the hmsa-qa-platform target repo with a main baseline so all build waves land on feature branches with a real merge gate.

## Requirements
- git init + initial commit of current repo contents (main)
- Python-appropriate .gitignore (pycache, .env, reports/, .pytest_cache)
- README stub naming the platform and pointing to the workspace design docs

## References
- projects/hmsa-qa-platform/README.md (target repo + artifact map)

## Task Builder Input
- **Deliverable:** Target repo is a git repository with main baseline + .gitignore; feature branches can be created from it
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** Wave 0 — no dependencies; MUST complete and be accepted before any other wave runs. Write ONLY on target-repo feature branch build/198-qa-build-target-repo-git-baseline — merge happens via /kernel/review-queue accept, never direct to main. Clean-room rule: v2 legacy is anti-pattern/architecture reference only — no code, no distinctive naming. Plan L1/L2/L3 test tasks during atomization.

# Research: Assess Current Release Gap

## Context
The isagawa site currently deploys via ad-hoc git push from pipelines. This task audits what actually happens during a deployment and identifies what's missing.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/release-manager-research/` exists

## Requirements
- Check git log of `D:/my_ai_projects/isagawa-co.github.io` — how are commits structured? Any versioning?
- List any existing deployment scripts or CI/CD config (.github/workflows/)
- Identify what currently happens when a pipeline pushes: is there any review step? Smoke test? Rollback capability?
- Enumerate what a bad deployment looks like: broken HTML, CSS not loading, broken navigation — has any of this happened?
- Define the gap: changelog (missing?), version tags (missing?), smoke test (missing?), rollback (missing?)
- Write to `projects/release-manager-research/release-gap-assessment.md`

## Acceptance Criteria
- [ ] `projects/release-manager-research/release-gap-assessment.md` exists
- [ ] File describes current deployment method
- [ ] File lists specific gaps (changelog, tags, smoke test, rollback)

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

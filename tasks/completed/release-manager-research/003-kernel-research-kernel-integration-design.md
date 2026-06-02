# Research: Design Kernel Integration

## Context
With the gap identified, design how a release manager would integrate into the kernel — as a command, hook, or execute-pipeline step.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-assess-release-gap.md

## Phase Gate
- [ ] `projects/release-manager-research/release-gap-assessment.md` exists

## Requirements
- Design a release workflow: feature branch → preview → smoke test → merge to main → tag
- Define `/kernel/release` command — what steps does it run? What gates does it enforce?
- Assess changelog generation: auto-generate from conventional commits or require manual notes?
- Define rollback procedure for GitHub Pages
- Assess: should the release step be added to execute-pipeline for all site pipelines, or invoked manually per release?
- Assess: what's the minimum addition that prevents broken deployments without adding friction?
- Write to `projects/release-manager-research/kernel-integration-design.md`

## Acceptance Criteria
- [ ] `projects/release-manager-research/kernel-integration-design.md` exists
- [ ] File defines /kernel/release command design
- [ ] File covers changelog approach
- [ ] File covers rollback procedure
- [ ] File has additive-vs-required recommendation

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

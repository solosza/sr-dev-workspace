# Write Component Curation Pipeline Design Document

## Context
The component curation pipeline is the flywheel's plumbing. When a user submits an artifact for evaluation, the agent may build new components from `_reference/` patterns. These components must pass automated quality gates and human review before joining the shared library. This is the platform's core moat -- the self-extending intelligence library.

This design must consume 158's research findings, specifically:
- Flywheel cycle and growth mechanism per `05-component-flywheel-curation.md`
- 4 automated quality gates (pattern conformance, test pass, code quality, deduplication) per `05-component-flywheel-curation.md`
- Human review workflow and reviewer qualifications per `05-component-flywheel-curation.md`
- Conflict resolution (optimistic concurrency) per `05-component-flywheel-curation.md`
- Versioning strategy per `05-component-flywheel-curation.md`
- Operational cost analysis at scale per `05-component-flywheel-curation.md`
- Curation bottleneck mitigation per `05-component-flywheel-curation.md`

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (prerequisite gate passed)

## Phase Gate
- [ ] Task 002 verdict = PROCEED
- [ ] `projects/eval-platform-design/` directory exists

## Requirements
Write `projects/eval-platform-design/component-curation-pipeline.md` covering:

1. **Flywheel architecture** -- how new components are created and flow into the library
   - Agent builds missing component from `_reference/` patterns during eval
   - Component enters automated quality gate pipeline
   - Passes -> enters human review queue
   - Approved -> merges to staging -> integration test -> merges to main library
   - Reference: flywheel cycle from `05-component-flywheel-curation.md`

2. **Automated quality gates** -- 4 gates every component must pass
   - Gate 1: Pattern conformance (diff against `_reference/` template)
   - Gate 2: Test pass (metric computes correctly on known inputs)
   - Gate 3: Code quality (linting, no hardcoded values, complexity checks)
   - Gate 4: Deduplication (embedding similarity at 0.85 threshold)
   - Estimated pass rate: 60-70%
   - Reference: gate definitions from `05-component-flywheel-curation.md`

3. **Human review workflow** -- how reviewers process the queue
   - Review queue design (context provided: source submission, pattern used, test results, similarity report)
   - Reviewer actions: approve, request changes, reject, merge with existing
   - MVP: internal team reviews all
   - Growth: community reviewers with reputation scores
   - Scale: AI-assisted review with confidence scoring
   - Reference: review workflow from `05-component-flywheel-curation.md`

4. **Conflict resolution** -- handling concurrent component creation
   - Optimistic concurrency (both agents build independently)
   - First to pass gates enters queue; second flagged as potential duplicate
   - No locking mechanism -- deduplicate at review time
   - Git-based library versioning for merge conflict resolution
   - Reference: conflict resolution from `05-component-flywheel-curation.md`

5. **Versioning strategy** -- library and per-component versioning
   - Semantic versioning for the library (major/minor/patch)
   - Per-component version fields
   - Container images pin to specific library version
   - Rollback via Git revert
   - Reference: versioning from `05-component-flywheel-curation.md`

6. **Scaling plan** -- operational cost at each growth phase
   - MVP (0-100 submissions/mo): 2.5 hrs/mo review, internal team
   - Growth (100-1,000): 25 hrs/mo, AI-assisted reduces to 10 hrs/mo
   - Scale (1,000-10,000): tiered auto-approve >95%, human review 70-95%, auto-reject <70%
   - Curation bottleneck mitigation strategies
   - Reference: operational cost analysis from `05-component-flywheel-curation.md`

7. **References** -- cite specific 158 research files

## Acceptance Criteria
- [ ] `projects/eval-platform-design/component-curation-pipeline.md` exists
- [ ] Document describes all 4 automated quality gates
- [ ] Document contains `## References` section referencing `eval-web-app-research`
- [ ] Document covers the curation bottleneck mitigation strategy

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

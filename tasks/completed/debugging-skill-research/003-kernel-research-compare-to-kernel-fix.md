# Research: Compare to /kernel/fix

## Context
The kernel's /kernel/fix command handles kernel-level failures (hook violations, anchor issues). The Superpowers debugging skill targets application code bugs (Python, TypeScript, SQL). Need to assess whether they overlap or are genuinely different scopes.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-debugging-skill.md

## Phase Gate
- [ ] `projects/debugging-skill-research/skill-summary.md` exists

## Requirements
- Read `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/commands/kernel/fix.md` — what does /kernel/fix actually do?
- Compare scopes: /kernel/fix = kernel operation failures; debugging skill = application code bugs. Is there real overlap?
- Assess scenarios from existing platform work:
  - Python pytest failures in hmsa-healthcare-qa — would the skill change how bugs are approached?
  - TypeScript Playwright failures in platform-playwright — same question
  - SSH compliance issues — same question
- Identify the integration point: extend /kernel/fix, create /kernel/debug, or create @debugger named agent?
- Write to `projects/debugging-skill-research/kernel-fix-comparison.md`

## Acceptance Criteria
- [ ] `projects/debugging-skill-research/kernel-fix-comparison.md` exists
- [ ] File describes /kernel/fix scope vs debugging skill scope
- [ ] File addresses real debugging scenarios from platform work
- [ ] File recommends an integration point

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

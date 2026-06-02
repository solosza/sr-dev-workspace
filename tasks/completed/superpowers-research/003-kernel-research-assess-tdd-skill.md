# Research: Assess TDD Skill

## Context
The Superpowers TDD skill claims to enforce test-first discipline. The kernel has test tasks (TEST type in task-builder) but no explicit TDD enforcement. Need to assess whether the Superpowers TDD skill adds real value over current kernel test patterns.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-superpowers-readme.md

## Phase Gate
- [ ] `projects/superpowers-research/skills-inventory.md` exists

## Requirements
- Read the Superpowers TDD skill file (WebFetch from github.com/obra/superpowers — find the TDD skill in the repo)
- What exactly does it instruct Claude to do? (write test first, red-green-refactor, etc.)
- Compare to kernel's existing test pattern: task-builder TEST tasks + gate contracts
- Does it add value? What specifically would change in how the agent approaches BUILD tasks?
- Would it conflict with the current atomization rule (one action = one task)?
- Write assessment to `projects/superpowers-research/tdd-assessment.md`

## Acceptance Criteria
- [ ] `projects/superpowers-research/tdd-assessment.md` exists
- [ ] File describes what the TDD skill does specifically
- [ ] File compares to kernel test pattern (mentions run-task.sh or kernel test tasks)
- [ ] File has a clear ADOPT/SKIP recommendation

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

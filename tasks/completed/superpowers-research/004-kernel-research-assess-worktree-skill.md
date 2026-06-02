# Research: Assess Git Worktree Skill

## Context
The Superpowers worktree skill uses git worktrees for isolated development. The kernel has the EnterWorktree tool available but unused. This task assesses whether the Superpowers worktree skill would add real value and how it would interact with the kernel's existing git workflow.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-superpowers-readme.md

## Phase Gate
- [ ] `projects/superpowers-research/skills-inventory.md` exists

## Requirements
- Read the Superpowers worktree skill (WebFetch from github.com/obra/superpowers)
- What does it do? How does it use worktrees? When does it create them?
- How would this interact with the isagawa-co.github.io workflow (feature branches per pipeline)?
- The kernel has EnterWorktree tool available — how does the Superpowers skill compare to using this directly?
- What problem does it solve that the current branch-per-pipeline pattern doesn't?
- Write assessment to `projects/superpowers-research/worktree-assessment.md`

## Acceptance Criteria
- [ ] `projects/superpowers-research/worktree-assessment.md` exists
- [ ] File describes what the worktree skill does
- [ ] File addresses EnterWorktree tool and how skill compares
- [ ] File has ADOPT/SKIP recommendation

## Gates Satisfied
- DOC-06, DOC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

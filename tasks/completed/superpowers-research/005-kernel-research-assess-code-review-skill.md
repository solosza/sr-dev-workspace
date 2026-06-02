# Research: Assess Code Review Skill

## Context
The Superpowers code review skill provides structured code review. Backlog 115 also covers a @reviewer named agent candidate. This task assesses the Superpowers code review skill and how it compares to the named agent approach.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-superpowers-readme.md

## Phase Gate
- [ ] `projects/superpowers-research/skills-inventory.md` exists

## Requirements
- Read the Superpowers code review skill (WebFetch from github.com/obra/superpowers)
- What does it check? What output does it produce?
- Compare to the @reviewer named agent concept from backlog 115 — are these the same thing or complementary?
- Would this run within a pipeline (as a task) or on-demand (as a command)?
- Write assessment to `projects/superpowers-research/code-review-assessment.md`

## Acceptance Criteria
- [ ] `projects/superpowers-research/code-review-assessment.md` exists
- [ ] File describes what the code review skill does
- [ ] File compares to named agent @reviewer approach
- [ ] File has ADOPT/SKIP recommendation

## Gates Satisfied
- DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

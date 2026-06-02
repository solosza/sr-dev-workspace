# Write Final Research Report

## Context
Synthesizes all Superpowers assessments into a final adoption recommendation. Identifies top 1-3 skills worth integrating and provides a concrete integration plan.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-kernel-research-assess-tdd-skill.md
- 004-kernel-research-assess-worktree-skill.md
- 005-kernel-research-assess-code-review-skill.md

## Phase Gate
- [ ] `projects/superpowers-research/tdd-assessment.md` exists
- [ ] `projects/superpowers-research/worktree-assessment.md` exists
- [ ] `projects/superpowers-research/code-review-assessment.md` exists

## Requirements
Write `projects/superpowers-research/research-report.md` covering:
1. Framework overview — what Superpowers is and what it contains
2. Skills inventory summary — full list with overlap/gap classification
3. TDD skill assessment summary + recommendation
4. Worktree skill assessment summary + recommendation
5. Code review skill assessment summary + recommendation
6. Other notable skills from the inventory (brief)
7. Top 1-3 skills to integrate — ranked by value
8. Integration plan for each recommended skill — where it lives (`.claude/skills/` or `.claude/agents/`), how it triggers, what it changes
9. Conflicts table — any skills that would duplicate or conflict with kernel mechanisms
10. Overall recommendation: ADOPT (which skills) / SKIP

## Acceptance Criteria
- [ ] `projects/superpowers-research/research-report.md` exists
- [ ] File has adoption recommendation (ADOPT/SKIP)
- [ ] File is > 80 lines

## Gates Satisfied
- DOC-09, DOC-10, DOC-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

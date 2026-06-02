# Write Final Research Report

## Context
Synthesizes debugging skill findings and /kernel/fix comparison into a final recommendation.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-kernel-research-compare-to-kernel-fix.md

## Phase Gate
- [ ] `projects/debugging-skill-research/kernel-fix-comparison.md` exists

## Requirements
Write `projects/debugging-skill-research/research-report.md` covering:
1. Skill methodology — the 4 phases and what they do
2. Scope comparison — /kernel/fix (kernel failures) vs debugging skill (application bugs)
3. Scenario analysis — Python/TypeScript/SSH — would it change anything?
4. Integration point recommendation — extend /kernel/fix / new /kernel/debug / @debugger agent
5. If integration recommended: design sketch (what the command/agent would look like)
6. Overall recommendation: ADOPT / SKIP

## Acceptance Criteria
- [ ] `projects/debugging-skill-research/research-report.md` exists
- [ ] File has integration point recommendation
- [ ] File is > 60 lines

## Gates Satisfied
- DOC-06, DOC-07, DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

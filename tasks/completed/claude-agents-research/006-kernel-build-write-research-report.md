# Write Final Research Report

## Context
Synthesizes all prior research (spec summary, kernel integration assessment, execute-pipeline assessment, resolved decisions) into a single actionable research report. This is the deliverable for backlog 115.

## Type
BUILD

## Execution
inline

## Dependencies
- 005-kernel-build-resolve-design-decisions.md

## Phase Gate
- [ ] `projects/claude-agents-research/design-decisions-resolved.md` exists

## Requirements
Write `projects/claude-agents-research/research-report.md` covering:

1. **Executive Summary** — 3-sentence answer to "should we integrate Claude named agents?"
2. **Spec Findings** — what the agents spec actually provides (from agents-spec-summary.md)
3. **Integration Assessment** — how agents fit (or don't) with kernel hooks, governance, run-task.sh
4. **Execute-Pipeline Assessment** — whether a third route makes sense
5. **Resolved Decisions** — the 5 answers in table form
6. **Agent Candidates** — for each recommended agent: name, model, tools, placement, trigger
7. **Integration Plan** — if adoption is recommended: concrete steps (file locations, YAML to write, command updates)
8. **Risk Table** — governance risks, auto-delegation risks, state contention risks with mitigations
9. **Recommendation** — ADOPT / ADOPT-PARTIAL / SKIP with clear reasoning

Report must be > 100 lines, actionable, and ready for the user to make a decision from.

## Acceptance Criteria
- [ ] `projects/claude-agents-research/research-report.md` exists
- [ ] File has adoption recommendation (grep: "ADOPT\|SKIP\|recommend")
- [ ] File is > 100 lines (`wc -l` > 100)
- [ ] File covers all 9 required sections

## Gates Satisfied
- DOC-11, DOC-12, DOC-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

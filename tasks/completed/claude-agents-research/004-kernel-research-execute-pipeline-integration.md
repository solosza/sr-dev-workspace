# Research: Execute-Pipeline Integration Assessment

## Context
The current classify-then-route step (step-04-execute-tasks.md) routes tasks as simple (inline) or complex (run-task.sh). Named agents introduce a potential third route. This task assesses whether that third route adds value, what task file syntax would signal it, and which task types are appropriate for named agent dispatch.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-agents-spec.md
- 003-kernel-research-kernel-integration.md

## Phase Gate
- [ ] `projects/claude-agents-research/agents-spec-summary.md` exists
- [ ] `projects/claude-agents-research/kernel-integration-assessment.md` exists

## Requirements
- Read `D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/execute-pipeline/references/step-04-execute-tasks.md` — current routing table
- Assess: would a third route (named agent dispatch) actually reduce overhead vs run-task.sh for lightweight tasks?
- Assess: what does a named agent dispatch gain vs lose compared to run-task.sh? (gains: tool restriction, model routing; loses: kernel governance, gate contracts, attestation, completed_tasks tracking)
- Define: if a third route is added, what task file syntax signals it? (e.g., `## Execution: agent: @reviewer`)
- Define: which task types are appropriate for named agent dispatch? Proposed routing table:
  - BUILD → run-task.sh
  - RESEARCH → run-task.sh
  - TEST (structural) → named agent
  - TEST (functional) → run-task.sh
  - VERIFY (quick) → named agent
- Assess: is there a hybrid model where named agents handle lightweight classify-and-review while run-task.sh handles all production work?
- Produce a go/no-go recommendation for adding the third route to step-04

## Acceptance Criteria
- [ ] `projects/claude-agents-research/execute-pipeline-assessment.md` exists
- [ ] File covers the gains/losses comparison (grep: "gain\|lose\|tradeoff\|trade-off")
- [ ] File covers the third route concept (grep: "third route\|third.route\|route.*agent\|named agent route")
- [ ] File includes a routing table proposal or explicit recommendation to keep current 2-route design
- [ ] File has a clear go/no-go recommendation

## Gates Satisfied
- DOC-07, DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

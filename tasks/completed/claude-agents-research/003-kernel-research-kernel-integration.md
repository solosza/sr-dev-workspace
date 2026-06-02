# Research: Kernel Integration Assessment

## Context
With the agents spec understood from task 002, assess how named agents would fit into the kernel's existing infrastructure. The key questions are: do agents inherit kernel hooks? Where should they live (global vs project)? What naming conventions apply? Which agent candidates make sense (@reviewer, @security, @pr-writer)?

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-read-agents-spec.md

## Phase Gate
- [ ] `projects/claude-agents-research/agents-spec-summary.md` exists

## Requirements
- Read `.claude/hooks/` — list which hooks exist and what they enforce (PreToolUse, PostToolUse patterns)
- Determine: do named agents spawned via @-mention inherit the parent session's PreToolUse/PostToolUse hooks? Does the spec say explicitly?
- Assess: if agents DO inherit hooks, they're kernel-governed by default. If they DON'T, they're a bypass vector — what are the implications?
- Assess fit for each candidate:
  - `@reviewer` — code/doc review on demand. What tools does it need? What model?
  - `@security` — scan files for vulnerabilities. What tools? Model?
  - `@pr-writer` — generate PR descriptions from git diff. Tools? Model?
- Determine placement recommendation: global (`~/.claude/agents/`) vs project (`.claude/agents/`) for each candidate — rationale required
- Assess model routing conflict: run-task.sh routes by task type (backlog 087). Named agents route by YAML. Are these in conflict?

## Acceptance Criteria
- [ ] `projects/claude-agents-research/kernel-integration-assessment.md` exists
- [ ] File covers hook inheritance finding (grep: "hook\|inherit\|PreToolUse")
- [ ] File covers each of the 3 candidates (@reviewer, @security, @pr-writer)
- [ ] File includes placement recommendation per candidate (grep: "global\|project\|~/.claude")
- [ ] File addresses model routing conflict with run-task.sh

## Gates Satisfied
- DOC-05, DOC-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

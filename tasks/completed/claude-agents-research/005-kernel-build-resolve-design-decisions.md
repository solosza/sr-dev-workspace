# Resolve Design Decisions

## Context
The backlog 115 design-decisions.md defined 5 open questions that must be answered before any implementation begins. With tasks 002-004 complete, there is enough information to resolve each question definitively. This task produces a resolved decisions document.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-kernel-research-read-agents-spec.md
- 003-kernel-research-kernel-integration.md
- 004-kernel-research-execute-pipeline-integration.md

## Phase Gate
- [ ] `projects/claude-agents-research/agents-spec-summary.md` exists
- [ ] `projects/claude-agents-research/kernel-integration-assessment.md` exists
- [ ] `projects/claude-agents-research/execute-pipeline-assessment.md` exists

## Requirements
Read `docs/backlog/115-kernel-research-claude-agents-integration/design-decisions.md` for the 5 open questions. Resolve each:

1. **Governance inheritance:** Do named agents inherit PreToolUse/PostToolUse hooks? → Answer YES or NO with evidence from the spec and hook assessment
2. **Auto-delegation:** Enable / Disable / Selective → Based on risk assessment and kernel governance findings
3. **Placement:** global (`~/.claude/agents/`) vs project (`.claude/agents/`) for each candidate → One answer per candidate with rationale
4. **step-04 update:** YES (add named agent route) / NO (keep current 2-route design) → Based on execute-pipeline assessment
5. **Naming convention:** Confirm the standard (single word @names, kebab for files `agent-name.md`)

For each decision: state the answer AND the one-sentence rationale.

## Acceptance Criteria
- [ ] `projects/claude-agents-research/design-decisions-resolved.md` exists
- [ ] File contains all 5 decision answers
- [ ] Each decision has YES/NO/ENABLE/DISABLE/SELECTIVE or equivalent clear answer
- [ ] Each decision has a one-sentence rationale

## Gates Satisfied
- DOC-09, DOC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

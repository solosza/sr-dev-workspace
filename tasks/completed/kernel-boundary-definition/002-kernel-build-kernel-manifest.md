# Create kernel-manifest.json

## Context
The manifest is the single source of truth for what IS kernel. domain-setup and sync both read it. Only governance files are listed.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-kernel-research-diff-three-repos

## Phase Gate
- [ ] `projects/kernel-boundary/three-way-diff.md` exists with file classifications

## Requirements
- Create `kernel-manifest.json` at isagawa-kernel repo root (`D:/my_ai_projects/isagawa-kernel/kernel-manifest.json`)
- Include ONLY governance files: loop commands (session-start, anchor, learn, complete, fix, domain-setup, reset), hooks (universal-gate-enforcer, actions-log-appender, test-failure-detector, auto-approve-claude-writes), scripts (CLAUDE.md, run-task.sh, common.sh), skills (kernel-domain-setup/, autonomous-cycling/), lessons template
- Use structure from docs/backlog/147-kernel-refactor-define-kernel-boundary/kernel-manifest.md
- Version field: "1.0"

## Acceptance Criteria
- [ ] File exists: `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json`
- [ ] JSON is valid (parseable)
- [ ] Contains only governance files (no execute-pipeline, task-builder, prod-test, backlog, etc.)
- [ ] All listed files actually exist in isagawa-kernel repo

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

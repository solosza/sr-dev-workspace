# Task 017: Sync py_sel_framework_mcp

## Objective
Sync kernel infrastructure from master to py_sel_framework_mcp repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/py_sel_framework_mcp"
```

## Acceptance Criteria
- py_sel_framework_mcp has 15 kernel commands in `.claude/commands/kernel/`
- py_sel_framework_mcp has 7 kernel skill folders in `.claude/skills/`
- py_sel_framework_mcp has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (4d, cleanup, elegant, fix, grill, intel, pr, prove, qa-workflow, qa-workflow-dev, reset-kernel-test, run-test, sync-to-isagawa-qa)
- Domain skills preserved (create-vertical-validation-agents, design-decisions, design-execution-engine, dialogue-engine, documentation, execute-from-step1, fix-workflow, qa-management-layer, rag-learning, testing)

## Gate
BUILD-17

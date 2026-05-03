# Task 018: Sync qa_kernel_test

## Objective
Sync kernel infrastructure from master to qa_kernel_test repo.

## Instructions

```bash
bash tasks/sync-all-domain-specs/sync-kernel.sh "D:/my_ai_projects/qa_kernel_test"
```

## Acceptance Criteria
- qa_kernel_test has 15 kernel commands in `.claude/commands/kernel/`
- qa_kernel_test has 7 kernel skill folders in `.claude/skills/`
- qa_kernel_test has 6 kernel hooks in `.claude/hooks/`
- Domain commands preserved (4d, cleanup, elegant, fix, grill, intel, pr, prove, qa-workflow, qa-workflow-dev, etc.)
- Domain skills preserved (create-vertical-validation-agents, etc.)

## Gate
BUILD-18

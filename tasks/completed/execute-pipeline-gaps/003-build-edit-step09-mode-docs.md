# 003 — Edit step-09: Document Execution Mode Divergence (Gap 4)

## Type
BUILD

## Requirements
- Edit `.claude/skills/task-builder/references/step-09-execute.md`
- Add a "Mode Clarification" section near the top (after the Pipeline Mode check) that explains:
  - Under execute-pipeline: all tasks run via run-task.sh (step 9 is skipped entirely)
  - Standalone `/kernel/task-builder`: dual mode — BUILD/RESEARCH inline, TEST spawned
  - The dual-mode logic only fires in standalone mode
- Keep existing content intact — this is additive documentation

## Acceptance Criteria
- [ ] `step-09-execute.md` contains a section about mode clarification or execution paths
- [ ] File mentions that execute-pipeline skips step 9 entirely
- [ ] File mentions standalone mode uses dual execution

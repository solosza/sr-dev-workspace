# 008 — Write Granularity Reference to Skill References

## Type
BUILD

## Requirements
- Write `.claude/skills/task-builder/references/granularity-reference.md`
- Content is based on `docs/backlog/051-kernel-fix-execute-pipeline-gaps/granularity-reference.md` (the design doc)
- Copy the full content from the design doc — it's already in the correct format for a skill reference
- The file should contain:
  - Core principle (each task = one claude -p = one action = one checkpoint)
  - Why it matters (5 architectural reasons)
  - The decision test ("If this task times out...")
  - 4 concrete before/after examples
  - Edge cases
  - How to count (count the verbs)

## Acceptance Criteria
- [ ] `.claude/skills/task-builder/references/granularity-reference.md` exists
- [ ] File contains "each task = one" (core principle)
- [ ] File contains at least 4 "Example" sections
- [ ] File contains "How to Count" section

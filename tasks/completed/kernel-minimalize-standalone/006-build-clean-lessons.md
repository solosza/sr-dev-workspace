# Clean Lessons to Template Only

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
Only `lessons.md` remains in `.claude/lessons/` with RULE ZERO template.

## Instructions
Working in `D:\my_ai_projects\project_test_repos\kernel-minimal`:

1. Remove all lesson files from `.claude/lessons/` EXCEPT `lessons.md`
2. Replace `lessons.md` content with a clean template containing only RULE ZERO:

```markdown
# Lessons

## RULE ZERO
Always read this file during /kernel/anchor. Every rule below was learned from a real failure.

(New lessons will be appended here by /kernel/learn)
```

## Verification
- Only 1 file in `.claude/lessons/`
- `lessons.md` contains "RULE ZERO"

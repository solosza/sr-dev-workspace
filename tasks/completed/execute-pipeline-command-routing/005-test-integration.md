# Task 005: Test Integration

## Objective
Invoke `/kernel/execute-pipeline` on the review-queue backlog (created in task 004) and verify it routes through `/design` → `/build-command` instead of task-builder.

## Instructions
1. Get the backlog number from task 004's output
2. Invoke `/kernel/execute-pipeline [backlog-number]`
3. Verify the pipeline:
   - Reads the backlog
   - Detects it as a command build (based on deliverable/location/scope signals)
   - Routes through `/design` (produces design doc in `.claude/docs/design/review-queue/`)
   - Routes through `/build-command` (produces skill package in `.claude/skills/review-queue/`)
   - Does NOT invoke task-builder
4. Verify deliverables exist:
   - Design doc: `.claude/docs/design/review-queue/index.md`
   - Skill: `.claude/skills/review-queue/SKILL.md`
   - Command: `.claude/commands/kernel/review-queue.md`

## Acceptance Criteria
- [ ] Execute-pipeline detected command build correctly
- [ ] /design was invoked (design doc exists)
- [ ] /build-command was invoked (skill package exists)
- [ ] task-builder was NOT invoked
- [ ] review-queue command is functional

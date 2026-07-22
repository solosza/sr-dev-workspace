# Build Execute-Pipeline Command Routing

## Status
Open

## Priority
High — enables correct command/skill builds through execute-pipeline instead of wrong task-builder decomposition

## Summary
Execute-pipeline currently always routes through task-builder for all backlogs. When a backlog's deliverable is a command or skill, it should route through `/design` → `/build-command` instead. This adds routing logic to execute-pipeline that detects the deliverable type and picks the right inner loop.

## Requirements
- Execute-pipeline reads backlog and detects deliverable type
- If deliverable is a command/skill: route through `/design` → `/build-command`
- If deliverable is code/files/research/refactor: route through task-builder (existing behavior)
- Detection signal: backlog `Scope: BUILD` + deliverable mentions "command", "skill", or target is `.claude/commands/` or `.claude/skills/`
- After routing is built, run `/gap` on the modified execute-pipeline skill
- Create a backlog for `/kernel/review-queue` command (from velocity-management-research report)
- Test the integration by invoking `/kernel/execute-pipeline` on the review-queue backlog — it should route through `/design` → `/build-command`

## References
- Execute-pipeline skill: `.claude/skills/execute-pipeline/`
- Design command skill: `.claude/skills/design-command/`
- Build command skill: `.claude/skills/build-command/`
- Review-queue research: `projects/velocity-management-research/final-report.md`
- Design doc for design command: `.claude/docs/design/design-command/index.md`
- Design doc for build command: `.claude/docs/design/build-command/index.md`

## Task Builder Input
- **Deliverable:** Execute-pipeline routing logic + review-queue backlog + integration test
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not break existing task-builder routing for non-command backlogs. The review-queue backlog is the integration test — if execute-pipeline correctly routes it through /design → /build-command, routing works.

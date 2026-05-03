# Cross-Repo Agent Delegation

## Status
Open

## Priority
High — blocks fully autonomous spec factory execution

## Summary
Build the mechanism for task-builder and autonomous cycling to delegate work to other repos via spawned agents. When a task requires operating in a different repo (e.g., running the spec factory), the cycling agent spawns a sub-agent there under that repo's kernel. When a task says HUMAN REQUIRED, a sub-agent automates it.

## Requirements
- Task-builder recognizes when a goal requires cross-repo work
- New execution mode: `## Execution: factory` (spawns agent in factory repo)
- Spawned agent receives: target repo path, command to run, expected output
- Spawned agent operates under target repo's kernel (hooks, commands, state)
- Parent agent waits for completion, reads results, continues cycling
- HUMAN REQUIRED: spawned agent tries gh CLI, API calls before skipping
- Test: spawn agent in domain-spec-factory, run `/spec-factory-run ssh-image-testing` with platform-docker as template

## References
- domain-spec-factory: `C:/Users/solos/my_ai_projects/domain-spec-factory/`
- platform-docker: `C:/Users/solos/my_ai_projects/platform-docker/`
- Memory: `project_autonomous-agent-architecture.md`
- Autonomous cycling lesson: never stop, never skip HUMAN REQUIRED

## Task Builder Input
- **Deliverable:** Cross-repo delegation mechanism in task-builder + cycling, tested with factory SSH spec rebuild
- **Scope:** BUILD
- **Constraints:** Must work with existing kernel enforcement. Spawned agents need their own anchor/complete cycles. First test: rebuild SSH spec using factory + platform-docker template.

# Agent Orchestration Framework — Standalone Extraction

## Status
Open

## Priority
High — Enables independent reuse of the proven Isagawa Kernel orchestration pattern without full kernel dependency

## Summary

Extract and adapt the Isagawa Kernel's execute-pipeline agent orchestration loop into a standalone, reusable framework. This is a composable system for autonomous task execution with the same command/skill/reference/data-contract architecture, but decoupled from the kernel domain. Any project should be able to copy this framework and immediately use it for their own agent orchestration.

The kernel's /kernel/execute-pipeline implements a proven pattern (backlog → task-builder → run-task.sh autonomously) that should be reusable across teams and projects. This backlog extracts, documents, and packages that pattern as a standalone framework.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[127-kernel-build-agent-orchestration-framework/architecture]] | Overall system design, data flow, and autonomy contract |
| [[127-kernel-build-agent-orchestration-framework/commands-schema]] | Command structure, registry, and invocation patterns |
| [[127-kernel-build-agent-orchestration-framework/skills-structure]] | Modular skills design with step files and composability |
| [[127-kernel-build-agent-orchestration-framework/references-pattern]] | Reference indexing, linking, and discovery mechanisms |
| [[127-kernel-build-agent-orchestration-framework/data-contracts]] | Gate contracts, state schemas, and validation interfaces |
| [[127-kernel-build-agent-orchestration-framework/extraction-guide]] | Step-by-step extraction from kernel + adaptation playbook |

## Requirements

- Framework must be **standalone** — no kernel dependency, can be dropped into any project
- **Zero modification** — copied files should work without adaptation (for common use cases)
- **Composable** — commands, skills, and references can be mixed and matched
- **Autonomous by design** — built-in assumption that the agent never pauses for user input
- **Data-driven** — gate contracts and state schemas control behavior, not hardcoded logic
- **Self-documenting** — architecture visible in directory structure and naming conventions

## Architecture Principles

1. **Modular over monolithic** — Each component (command, skill, reference) is independently discoverable
2. **Index over duplication** — Protocol and SKILL.md are indexes that point to step files, not walls of text
3. **Data contracts as guardrails** — Gate contracts define what must be true before/after each phase
4. **State-driven loops** — Cycling logic lives in state files, not in code logic
5. **Skill composition** — Skills can call other skills; orchestration is top-down via commands

## References

- Kernel source: `D:\my_ai_projects\isagawa-kernel\.claude\`
- Example: execute-pipeline (`.claude/skills/execute-pipeline/SKILL.md`)
- Example: task-builder (`.claude/skills/task-builder/SKILL.md`)
- Reference implementations: `.claude/references/` across all kernel domains

## Task Builder Input

- **Deliverable:** Standalone agent-orchestration framework package with commands, skills, references, data schemas, and extraction documentation
- **Location:** `new-repo:D:\my_ai_projects\agent-orchestration-framework`
- **Scope:** BUILD + RESEARCH (extract from kernel, design schemas, document patterns)
- **Constraints:**
  - Must work without Isagawa Kernel (no .claude/protocols dependency)
  - Must preserve kernel's autonomy assumptions (never pause for user input)
  - Must include test fixtures showing how to adapt the framework to a new domain
  - Delivery includes extraction guide (how to port from kernel) and integration examples

# Build System Architecture Diagram

## Context
Create the system architecture diagram showing how all Isagawa Kernel components interact. This is the highest-level view targeting architects and technical leads. Shows the full ecosystem: domain specs, protocols, hooks, commands, skills, state management, and how they connect.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-diagrams-dir

## Phase Gate
- [ ] `docs/architecture-diagrams/` directory exists

## Requirements
- Write a Mermaid diagram in `docs/architecture-diagrams/system-architecture.md`
- Show these components and their relationships:
  - **Domain Spec** (protocol file — source of truth for a domain)
  - **Commands** (kernel commands: session-start, anchor, learn, complete, etc.)
  - **Hooks** (gate enforcer, actions log appender, test failure detector)
  - **Skills** (task-builder, execute-pipeline, autonomous-cycling, prod-test)
  - **State** (session_state.json, workflow.json, actions.jsonl)
  - **Lessons** (lessons.md — self-improvement loop)
  - **CLAUDE.md** (entry point — loads the kernel)
- Use hierarchical layout (top-down or left-right)
- Include a title and brief description above the diagram
- Label all edges with the relationship type (reads, writes, triggers, enforces)
- Include the "Domain Spec" label explicitly for grep validation

## Acceptance Criteria
- [ ] `docs/architecture-diagrams/system-architecture.md` exists
- [ ] File contains a ` ```mermaid ` code block
- [ ] File contains "Domain Spec" text

## Gates Satisfied
- BUILD-02, FUNC-01, FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

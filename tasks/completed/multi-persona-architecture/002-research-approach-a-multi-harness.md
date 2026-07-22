# Task 002: Research Approach A — Multi-Harness Architecture

## Type
RESEARCH

## Objective
Design and evaluate the multi-harness approach: one repo per persona, with an orchestrator harness that dispatches work.

## Steps
1. Define what each persona harness contains (commands, skills, hooks, protocol, state)
2. Design the orchestrator harness:
   - How does it know what the company needs? (metrics, triggers, schedules, backlog priority)
   - How does it select and dispatch a persona?
   - How does it pass context between personas?
3. Evaluate state isolation — each harness has its own state, no contention
4. Evaluate complexity — repo proliferation, maintenance burden, shared code duplication
5. Evaluate scalability — adding a new persona = new repo
6. Design autonomous nightly operation flow: cron → orchestrator → persona dispatch → report
7. Identify concrete file paths, state schemas, command names

## Deliverable
`projects/multi-persona-architecture/02-approach-a-multi-harness.md`

## Acceptance Criteria
- Architecture diagram (text-based) showing harness relationships
- Orchestrator dispatch logic defined
- State schema for inter-harness communication
- Pros/cons list with specific technical rationale

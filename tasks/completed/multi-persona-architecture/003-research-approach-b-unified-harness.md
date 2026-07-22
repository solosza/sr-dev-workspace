# Task 003: Research Approach B — Unified Harness Architecture

## Type
RESEARCH

## Objective
Design and evaluate the unified harness approach: single repo, personas as workflow modes with shared infrastructure.

## Steps
1. Define persona as workflow mode within single repo:
   - How are persona-specific commands namespaced? (e.g., `/pm/prioritize`, `/sales/apply`)
   - How does shared protocol handle persona-specific rules?
   - How do hooks differentiate between personas?
2. Design persona routing:
   - How does the system switch between personas?
   - Is it a command flag, a workflow state, or a separate orchestration layer?
3. Evaluate state isolation — shared state file vs persona-scoped state
4. Evaluate complexity — single repo but growing command surface
5. Evaluate scalability — adding a persona = new commands/skills in same repo
6. Design autonomous nightly operation flow with unified approach
7. Address: can hooks enforce persona-specific rules without conflict?

## Deliverable
`projects/multi-persona-architecture/03-approach-b-unified-harness.md`

## Acceptance Criteria
- Architecture diagram showing persona routing within single repo
- Command namespace design
- State isolation strategy within shared repo
- Pros/cons list with specific technical rationale

# Research Dispatch Mechanism and State Scoping

## Type
RESEARCH

## Phase Gate
Task 001 must be complete.

## Deliverable
`projects/loop-composability-research/dispatch-and-scoping.md`

## Instructions
1. Using the contracts from task 001, design dispatch options:
   - How does an outer loop (execute-pipeline) detect which inner loop to invoke?
   - Pattern matching on task deliverable type? Explicit tags? Convention-based?
2. Define state scoping approaches:
   - How do inner loops avoid contaminating outer loop state?
   - Can the existing per-agent workflow isolation pattern be reused?
   - What about session_state.json contention?
3. Address error propagation:
   - If inner loop fails, how does outer loop handle it?
   - Retry semantics vs fail-fast
4. Evaluate recursive composition: can inner loops invoke their own inner loops?

## Verification
- File exists at deliverable path
- Dispatch, scoping, error propagation, and recursion all addressed

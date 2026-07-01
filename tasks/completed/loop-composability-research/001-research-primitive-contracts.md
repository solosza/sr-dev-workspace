# Research Primitive Loop Entry/Exit Contracts

## Type
RESEARCH

## Deliverable
`projects/loop-composability-research/primitive-contracts.md`

## Instructions
1. Survey existing kernel primitives (execute-pipeline, prod-test, task-builder, domain-setup, design, build-command)
2. For each, document:
   - Entry contract: what state/inputs must exist before invocation
   - Exit contract: what state/artifacts exist after completion
   - State isolation: what state files it reads/writes
   - Error modes: how it fails and what state it leaves
3. Identify common patterns across primitives
4. Note which primitives are already composable vs tightly coupled

## Verification
- File exists at deliverable path
- At least 4 primitives documented

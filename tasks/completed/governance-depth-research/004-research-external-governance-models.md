# Research External Governance Models

## Context
Study how other minimal systems achieve governance depth without breadth. Apply findings to kernel constraints.

## Type
RESEARCH

## Execution
agent

## Dependencies
- None

## Requirements
- Unix philosophy: how does "do one thing well" apply to governance primitives?
- Microkernel OS design (L4, seL4, QNX): how do microkernels achieve safety with minimal surface area?
- Erlang/OTP supervisors: supervision trees, let-it-crash, restart strategies
- Kubernetes admission controllers: how do they layer enforcement without expanding the API?
- Governance research literature: minimal effective governance, principal-agent problems
- For each model: what pattern is directly applicable to the Isagawa kernel?

## Deliverable
Write findings to `projects/kernel-governance-depth/external-governance-models.md`

## Acceptance Criteria
- [ ] File exists with analysis of at least 4 external models
- [ ] Each model has an "applicable pattern" section mapping to kernel
- [ ] Comparison table: model, mechanism, kernel equivalent, gap
- [ ] Identifies governance problems the current kernel cannot solve

## Gates Satisfied
- RESEARCH-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

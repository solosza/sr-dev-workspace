# Research Loop Optimization

## Context
Analyze the current governance loop (session-start, anchor, work, learn, complete) for depth improvements without adding new steps or commands.

## Type
RESEARCH

## Execution
agent

## Dependencies
- None

## Requirements
- Analyze current loop shape: is session-start → anchor → work → learn → complete optimal?
- Evaluate anchor interval (every 10 actions): should it be adaptive based on task complexity or error rate?
- Assess the learn mechanism: how does it compare to other self-improving feedback loops?
- Evaluate complete gate strength: should verification be stronger before task closure?
- Produce concrete recommendations (tighten, adapt, or leave as-is for each)

## Deliverable
Write findings to `projects/kernel-governance-depth/loop-optimization.md`

## Acceptance Criteria
- [ ] File exists with analysis of all 5 loop components
- [ ] Each component has a concrete recommendation (not just description)
- [ ] Recommendations stay within feature freeze constraint

## Gates Satisfied
- RESEARCH-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

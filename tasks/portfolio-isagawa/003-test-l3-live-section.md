# Task 003: L3 - Live Section (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** PI-04

## Action
ONE script: poll https://solosza.github.io/ up to 10 min for the new section marker, then assert: definition present, diagram element present, YAML snippet + 'representative example' label present, ownership line present; kernel-internal grep (session_state, gate-enforcer, KERNEL_AGENT_ID, run-task, hook names, anchor ceremony) = 0; absolute-claims grep = 0.

## Acceptance
All live asserts PASS, exit 0. Red: fix then /kernel/learn.

# Task 002: Wave-Scoped Dispatch
**Type:** BUILD | **Gates:** DW-02
## Action
Edit step-03 (spawn) so only the current wave's agents dispatch; record `wave` + the wave plan in agent-swarm.json.
## Spec
READ the current step-03-spawn-agents.md + step-02-create-manifest.md. Add wave field to manifest schema; dispatch wave-by-wave (the manual 241/242->243 run is the prototype).
## Acceptance
Only current-wave agents spawn; manifest carries wave plan.

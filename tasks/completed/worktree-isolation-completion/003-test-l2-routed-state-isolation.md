# Task 003: L2 — Routed State Isolation
**Type:** TEST | **Gates:** WI-03
## Action
Write + RUN a live L2 test proving a routed agent's state/anchor update writes ONLY its agent-{id} file and leaves the parent byte-identical.
## Spec
Use THROWAWAY fixtures under a mktemp dir — never touch the real sr_dev_workflow.json/session_state.json. Seed a fake parent workflow file + set KERNEL_AGENT_ID; invoke the routed state-write path (the same function run-task.sh uses); assert the agent-{id}-workflow.json got the update AND the parent file's bytes are unchanged (hash before == after). Portable fixture: absolute paths, explicit PYTHONPATH (lesson #47).
## Acceptance
L2 test runs live and passes: agent-{id} file updated, parent byte-identical.

# Task 005: L2 — Completion Persistence
**Type:** TEST | **Gates:** RH-05
## Action
Write and RUN a live L2 test that simulates a task whose completion was not persisted (routed workflow.json missing the last completed task), invokes the 001 write-verify path, and asserts the completion is (re)persisted and reads back correctly. Put it under tasks/runner-hardening-v2/ or a tests/ dir; state PYTHONPATH explicitly if Python.
## Spec
Use a temp/throwaway routed state file — never touch real session_state.json / sr_dev_workflow.json. Assert the append lands and re-reads (including a utf-8-sig round-trip). Portable fixture: absolute paths / env-driven, no cwd dependence (lesson #47).
## Acceptance
L2 test runs live and passes; asserts re-persistence + read-back on a throwaway state file.

# Build: Per-Agent Session-State Isolation

## Status
Open

## Priority
High — named prerequisite for the wave engine (247) in both the 237 and 241 research verdicts; four `session_started` contention events observed live on 2026-07-21 alone, each costing a full recovery-anchor cycle.

## Summary
One-shot agents spawned by run-task.sh read and write the shared `session_state.json`, so their session-start/exit writes clobber the parent orchestrator's state (`session_started: false`, `agent_id`, `one_shot` leakage). Implement env-var `agent_id` routing so every one-shot agent reads/writes its own `agent-{id}-session-state.json`, leaving the parent's file untouched. The per-agent pattern already exists for action logs and workflow files — this extends it to session state, closing the last shared-mutable-state surface.

## Requirements
- **Canonical identity model FIRST** (external review 2026-07-21 #25): reference doc defining distinct IDs — swarm run ID, backlog item ID, worker ID (subfolder), task ID, worktree ID — with ONE mapping table. All state filenames derive from this model; stop overloading "agent ID" (live bug: swarm tracked `agent-237-state.json` by backlog ID while run-task.sh wrote `agent-{subfolder}-workflow.json` — monitor read 0/5 forever)
- run-task.sh exports `KERNEL_AGENT_ID={worker-id}` to the spawned `claude -p` process
- Hooks (universal-gate-enforcer, sr_dev-gate-enforcer, actions-log-appender, test-failure-detector) resolve the session-state path from `KERNEL_AGENT_ID` when set: `agent-{id}-session-state.json`; parent behavior unchanged when unset
- **Atomic writes** (external review #26): shared helper — write temp file + `os.replace()`, never direct JSON dumps to the live path; all hook/state writers use it
- **State schema validation** (external review #26): minimal JSON schema per state file (required keys + types); the write helper validates before replace and rejects near-empty/malformed payloads (would have caught the observed blank-file overwrite)
- `/kernel/session-start` and `/kernel/anchor` command docs updated: state-file routing section covers session state, not just workflow state
- Seed the per-agent session state at spawn (run-task.sh copies the anchored/one_shot template it already seeds for workflow files)
- L3 test: spawn two concurrent run-task.sh agents + parent activity, assert the parent `session_state.json` is byte-identical before/after the run (no clobber); plus a schema-rejection test (attempt a near-empty write, assert rejected)
- Design source: `projects/kernel-ephemeral-subagents-research/03-integration-design.md` (state handoff + isolation blockers section)

## References
- Backlogs done: 237, 241 (verdicts naming this as prerequisite); 183 (worktree isolation — complementary, not replaced)
- `.claude/lessons/lessons.md` — multi-agent state isolation (2026-06-14), state contention topic file
- Live evidence: 2026-07-21 session — 4 recovery cycles from one-shot exit writes

## Task Builder Input
- **Deliverable:** run-task.sh + hooks routing session state per-agent; parent state provably untouched by concurrent one-shot agents (L3 test green)
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Hook changes require Claude Code restart to load (needs_restart flow). Must not break single-agent (non-swarm) runs — routing activates only when KERNEL_AGENT_ID is set. Run BEFORE 247 (wave engine depends on this).

# Gate Contract — 244 Per-Agent Session-State Isolation

Deliverable: canonical identity model + KERNEL_AGENT_ID session-state routing in all 4 hooks + atomic schema-validated state writes. Parent session_state.json provably untouched by concurrent one-shot agents.

| Gate | Check | Method |
|------|-------|--------|
| SI-01 | .claude/references/agent-identity-model.md exists: 5 ID kinds (swarm run, backlog, worker, task, worktree), one mapping table, filename derivations | file_exists + grep |
| SI-02 | run-task.sh exports KERNEL_AGENT_ID={worker-id} to the claude -p subprocess | grep |
| SI-03 | run-task.sh seeds agent-{id}-session-state.json before first iteration | grep + run_code |
| SI-04 | Shared helper (hooks lib): atomic write (temp + os.replace) + JSON schema validation (required keys/types), rejects near-empty payloads | run_test |
| SI-05 | All 4 hooks (universal-gate-enforcer, sr_dev-gate-enforcer, actions-log-appender, test-failure-detector) resolve session-state path from KERNEL_AGENT_ID when set; unchanged when unset | grep + run_test |
| SI-06 | session-start.md + anchor.md routing sections cover session state | grep |
| SI-07 | L2: hook invoked with KERNEL_AGENT_ID=x resolves agent-x-session-state.json; without env var resolves session_state.json; near-empty write REJECTED by helper | run_test |
| SI-08 | L3: two concurrent run-task.sh agents + parent activity — parent session_state.json byte-identical before/after | run_test |

## Rules
- READ each hook file fully before editing (RULE ZERO) — routing goes where the file actually resolves state paths, not where you assume
- Helper lives in ONE shared module — no per-hook copies
- Backward compatible: no env var → exact current behavior (single-agent runs unaffected)
- Tests report honestly; any red → fix → /kernel/learn

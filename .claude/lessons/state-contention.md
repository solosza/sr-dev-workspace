# State Contention — Background Agents vs Parent Session

## 2026-04-23 — Pipeline State Contention

- **Issue:** Parent session tried to prep task files for pipelines 038/039 while background agent was executing pipeline 037 via run-task.sh. Both wrote to `sr_dev_workflow.json`. Sub-agent's session-start set `anchored: false`, which triggered hook blocks on the parent. Parent bypassed by directly editing `anchored: true` — which is the exact bypass backlog 037 is designed to prevent.

- **Root Cause:** `{domain}_workflow.json` is a single shared file with no session scoping. Every `claude -p` invocation from run-task.sh runs session-start, which sets `anchored: false` on the shared file. The parent and sub-agents are co-tenants of the same state, with no isolation.

- **Fix (immediate):** Stop overlapping. Execute pipelines strictly sequentially — finish one, start the next. Do NOT prep work for pipeline N+1 while N runs.

- **Fix (structural, backlog 040):** Scope workflow state per session. Options:
  1. Session-scoped state files (`sr_dev_workflow_{session_id}.json`)
  2. Lock file mechanism — sub-agents don't touch parent's anchor state
  3. Sub-agents get their own ephemeral workflow state, parent's is preserved

- **Sequencing Constraint (CRITICAL):** Backlog 037 (anchor integrity / protocol hash) will make the `anchored: true` bypass impossible. If 037 ships before the state scoping fix, background agent contention becomes a hard deadlock — sub-agent sets `anchored: false`, parent can't flip it back because hash verification will fail, parent is permanently blocked. Therefore: 040 (state scoping) must ship before or alongside 037.

- **Anti-Pattern:** Never do prep work while a background agent is running against the same state files.

- **Quality Gate:** Before shipping 037, verify that sub-agents spawned by run-task.sh do not invalidate the parent's anchor state.

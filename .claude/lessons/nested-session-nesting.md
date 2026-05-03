# Nested Session Nesting

## 2026-04-06 — claude -p nesting blocked by CLAUDECODE env var

- **Issue:** `run-task-batch.sh` spawned from execute-pipeline step 4 (inside an interactive Claude session) failed silently — 0 tasks completed, no session ID captured.
- **Root Cause:** Interactive Claude Code sessions set `CLAUDECODE=1`. Any `claude -p` subprocess detects this and refuses to launch. However, `claude -p` sessions do NOT set `CLAUDECODE` — so `claude -p` can spawn more `claude -p` (this is how prod-test step 7 works successfully).
- **Fix:** Spawn a **background Agent** that runs `env -u CLAUDECODE bash run-task.sh ...`. The Agent tool creates a decoupled subprocess. `env -u CLAUDECODE` strips the blocking env var for that subprocess only — the interactive session is unaffected. The `claude -p` calls inside run-task.sh then work normally.
- **Anti-Pattern:** Calling `bash run-task.sh` directly from an interactive session (CLAUDECODE=1 blocks all nested `claude -p`)
- **Correct Patterns:**
  1. **From interactive session:** Spawn a background Agent → `env -u CLAUDECODE bash run-task.sh [repo] [iterations] [subfolder]`
  2. **From terminal:** `claude -p "Read CLAUDE.md. Run /kernel/execute-pipeline 033"` (no CLAUDECODE set in `claude -p`)
  3. **From run-task.sh:** Already works — bash parent has no CLAUDECODE
- **Key Insight:** `CLAUDECODE` is set in interactive sessions only, NOT in `claude -p` sessions. The Agent tool spawns a subprocess that inherits the env — `env -u CLAUDECODE` strips it before passing to bash. This is the same decoupled pattern prod-test uses when invoked from run-task.sh.
- **Recurrence:** 4 occurrences (prod-test dev, execute-pipeline 031, execute-pipeline 033, execute-pipeline 025/034/035)
  - 4th occurrence (2026-04-08): Rate-limited agents returned empty results. Instead of re-reading the skill's step-04-execute-tasks.md (which prescribes the exact pattern), agent improvised by spawning inline agents to execute tasks directly. Violated BOTH "never spawn agents unless for run-task.sh" AND "never execute tasks inline." User had to point back to the lesson. Fix: stopped inline agent, relaunched via prescribed pattern.
  - **Root pattern:** When the prescribed path hits an obstacle, the agent reverts to improvisation instead of re-reading the instructions. The instructions already cover failure handling (step-04 has a Failure Handling table). READ THE INSTRUCTIONS FIRST.
  - **Hook added (2026-04-08):** `agent-inline-execution-blocker.py` — PreToolUse hook on `Agent` matcher. Blocks Agent calls that match task execution patterns unless prompt includes `run-task.sh` or `env -u CLAUDECODE`. Registered in settings.local.json. Activates on next restart.

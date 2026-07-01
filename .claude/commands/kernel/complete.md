# /kernel/complete

Final gate before marking work done.

## Instructions

**Workflow State Routing (CRITICAL for parallel agents):**

Before any workflow state read/write, check `agent_id` in `session_state.json`:
- If `agent_id` is set: read/write per-agent fields from `.claude/state/agent-{agent_id}-workflow.json` (create if missing — see seeding below)
- If `agent_id` is null: read/write `[domain]_workflow.json` (current behavior, unchanged)

Every reference to `[domain]_workflow.json` below follows this routing. When this doc says "update workflow state", it means the routed file.

**Seeding:** If `agent-{agent_id}-workflow.json` doesn't exist, create it with:
```json
{ "cycling": false, "cycling_complete": false, "task_folder": null, "total_tasks": null,
  "current_task": null, "completed_tasks": [], "skipped_tasks": [], "attempts_on_current": 0,
  "complete": false, "complete_timestamp": null, "anchored": true, "anchor_timestamp": null,
  "actions_since_anchor": 0, "last_anchor_token_confirmed": null, "timestamp": null }
```

For global fields (`protocol_created`, `actions_limit`), always read from the shared `[domain]_workflow.json`.

1. **Check state:**

   | Gate | Required |
   |------|----------|
   | Protocol created | `protocol_created: true` |
   | Anchored | `anchored: true` |

2. **Verify deliverables (MANDATORY):**

   Before marking complete, actually look at what the task produced. Tool call success is not verification.

   | Deliverable type | How to verify |
   |-----------------|---------------|
   | Files created | Read them — confirm content matches requirements |
   | Files modified | Read the changed sections — confirm the edit is correct |
   | State changed | Read state files — confirm values are what you expect |
   | Tests ran | Read results — confirm pass/fail matches expectations |
   | Repo changes | List files, read key ones — confirm nothing unexpected |
   | Decisions/docs | Read them — confirm they address the requirements |
   | Nothing tangible | State what you verified and why it's sufficient |

   **Report verification in the completion output.** List what you checked and the result.

3. **Verify gate contract (if applicable):**

   If a task folder is set in workflow state AND `gate-contract.md` exists in it:

   a. Read `gate-contract.md` from the task folder
   b. Find gates matching the current task (by task number prefix, e.g., task `005-build-*` matches gates `BUILD-05` or any gate whose check references files from task 005)
   c. For each matching gate, run the verification method:

   | Method | How to verify |
   |--------|--------------|
   | `file_exists` | Check the file exists (`test -f [path]`) |
   | `grep` | Run the grep command, check exit 0 |
   | `run_code` | Execute the command, check exit 0 |
   | `run_test` | Execute the test, check exit 0 |

   d. **If any gate fails:**
      - Report which gate failed, the method, and the actual result
      - Do NOT mark the task complete
      - Set `needs_learn: true, needs_learn_reason: "gate_failure"` in session_state.json
      - The agent must fix the issue and re-attempt completion

   e. **If all gates pass (or no gates match this task):**
      - Proceed normally to completion mode

   Gate verification is mechanical enforcement — the agent cannot self-report completion without passing its gates. Tasks with no matching gates in the contract complete normally.

4. **Determine completion mode:**

   Read `session_state.json` and `[domain]_workflow.json`.
   Check `one_shot` in `session_state.json` FIRST:

   ### Mode A: One-Shot (`one_shot: true`)

   Single task, then exit. Used by `run-task.sh` for headless execution.

   1. Add `current_task` to `completed_tasks` in `[domain]_workflow.json`
      - Use the **exact filename including `.md` extension**
      - **Check that the task is not already present** in `completed_tasks` before appending. If already present, skip the append (do not create duplicates).
   2. Check if tasks remain:
      - Scan task folder (`task_folder` from workflow state, default `tasks/`) for files NOT in `completed_tasks` or `skipped_tasks`
      - Exclude index files (000-*.md)
      - If none remain: output "ALL_TASKS_COMPLETE"
      - If tasks remain: output "ONE_SHOT_COMPLETE"
   3. Reset state for next fresh invocation:

      `session_state.json`:
      - `session_started: false`
      - `one_shot: false`
      - `context: { "last_completed": "[task name]" }`

      `[domain]_workflow.json`:
      - `current_task: null`
      - `attempts_on_current: 0`
      - **Do NOT set `anchored: false`** — one-shot agents skip the anchored gate (hook line 220-221), so they don't need it reset. Setting it to false blocks the parent interactive session which shares this state file.
      - **Do NOT reset `actions_since_anchor`** — let the counter accumulate across iterations; the hook skips the limit check for one-shot agents too.
      - Preserve `completed_tasks`, `skipped_tasks`, `total_tasks`, `anchored`, `actions_since_anchor`

   4. Agent stops. No cycling, no next task pick.

   ### Mode B: Cycling (`cycling: true`, NOT one-shot)

   Continuous loop through tasks. Used in interactive sessions and batch mode.

   1. Add `current_task` to `completed_tasks`
      - **Check that the task is not already present** before appending. If already present, skip the append (do not create duplicates).
   2. Reset `attempts_on_current` to 0
   3. Scan task folder for next incomplete task:
      - List .md files in `task_folder` (from workflow state)
      - Exclude index files (000-*.md)
      - Find lowest-numbered NOT in `completed_tasks` or `skipped_tasks`

   **Dual state update (BOTH files MUST be updated):**

   Update `[domain]_workflow.json`:
   - `completed_tasks`: add current task
   - `current_task`: next task filename (or null if done)
   - `attempts_on_current`: 0

   Update `session_state.json` context:
   - Completion summary for the task just finished
   - Next task name and what it requires
   - Current cycling progress (e.g., "4/7 tasks complete")

   Both files MUST be updated. Workflow tracks cycling state. Session tracks context for compaction recovery.

   - If next task found: announce it, read it, continue working
   - If none remain: announce "All N tasks complete (M skipped)", set `cycling: false`, `cycling_complete: true`

   ### Mode C: Single completion (neither one-shot nor cycling)

   Default behavior — just save context and report done.

5. **Save final conversation context (STRUCTURED):**
   - Update `context` key in `.claude/state/session_state.json` as a JSON object:

   ```json
   {
     "context": {
       "current_task": null,
       "task_folder": "tasks/[folder]/ or null",
       "progress": "N/M tasks complete (K skipped)",
       "last_completed": "task filename",
       "next_step": "next action or 'cycling complete'",
       "notes": "key decisions, open items"
     }
   }
   ```

   - MERGE into existing state, don't overwrite other keys

6. **Update state (conditional):**

   Only set `complete: true` when the workflow is actually finished:
   - **Mode A (one-shot):** Set `complete: true` ONLY if outputting "ALL_TASKS_COMPLETE" (no tasks remain). If outputting "ONE_SHOT_COMPLETE" (tasks remain), do NOT set `complete: true`.
   - **Mode B (cycling):** Set `complete: true` ONLY when `cycling_complete: true` (all tasks done/skipped).
   - **Mode C (single):** Set `complete: true` (single task, no cycling context).

   ```json
   {
     "complete": true,
     "complete_timestamp": "..."
   }
   ```

   **Why conditional:** Setting `complete: true` after every one-shot task signals "workflow done" to the parent session and other tooling, even though tasks may remain. This caused premature pipeline termination.

7. **Report:**
   ```
   COMPLETE

   Domain: [domain]
   Task: [what was done]
   Files created/modified: [count]
   Lessons learned: [count]

   Verified:
   - [what I checked] → [result]
   - [what I checked] → [result]

   Done.
   ```

## When to Invoke

- ALWAYS before saying "done"
- NEVER skip this gate

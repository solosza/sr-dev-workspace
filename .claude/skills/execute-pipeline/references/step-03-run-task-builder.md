# Step 3: Run Task-Builder (Default Route Only)

Invoke task-builder with flags to stop before execution. Plan review runs normally.

**Skip if `pipeline_state.route` is `command`.** Command route uses step 3c instead.

## Skip Check

1. Read `pipeline_state.route` from `session_state.json`
2. If `command` → skip this step, proceed to step 3c (`references/step-03c-run-command-build.md`)
3. If `default` → continue below

## Process

1. **Set pipeline mode flags:**

   Merge into `session_state.json`:
   ```json
   {
     "pipeline_mode": {
       "skip_plan_review": true,
       "no_execute": true
     }
   }
   ```

   These flags tell task-builder:
   - `skip_plan_review` → `true` for execute-pipeline (fully autonomous, no pause points)
   - `no_execute` → stop after step 8 (write tasks), don't start cycling

2. **Invoke `/kernel/task-builder` inline:**

   Pass `pipeline_state.backlog_path` as the argument:
   ```
   /kernel/task-builder [pipeline_state.backlog_path]
   ```

   Task-builder will:
   - Read the backlog file (Type B input — step 1 of task-builder)
   - Research context (step 2)
   - Convention check (step 3, if applicable)
   - Resolve template (step 4, if applicable)
   - Decompose (step 5)
   - Atomize + gate contract (step 6)
   - **Run plan review** (step 7 — presents plan to user for approval)
   - Write task files (step 8)
   - **Stop and return** (step 9 — flag check, sets `pipeline_state.task_folder` and `pipeline_state.task_count`)

3. **Clear pipeline mode flags and proceed to step 4 (ATOMIC — MUST NOT STOP):**

   **This transition is MECHANICAL and non-negotiable.** After task-builder returns:

   a. Clear `pipeline_mode` to `null` in `session_state.json`
   b. Verify handoff state (`pipeline_state.task_folder` and `pipeline_state.task_count`)
   c. If either is missing, read the task folder directly and set them
   d. **Immediately proceed to step 4** — do NOT report status, do NOT wait for user input, do NOT pause

   ```json
   {
     "pipeline_mode": null
   }
   ```

   **MUST NOT STOP between clearing pipeline_mode and executing step 4.** This is the most common failure point — the agent clears flags, reports "tasks created," and then stops instead of continuing. The output below and the step 4 invocation are ONE action, not two separate decisions.

## Output + Step 4 Invocation (ATOMIC)

```
PIPELINE — TASKS CREATED

Backlog: [backlog path]
Task folder: [task folder]
Tasks: [count]

Proceeding to step 4 (execution).
```

**Immediately after printing this output, read and execute step 4.** No pause. No user prompt. No "shall I proceed?" The pipeline is autonomous.

## Rules

- Set flags BEFORE invoking task-builder, clear AFTER it returns
- Task-builder runs the full skill except step 9 — don't skip any other steps
- If task-builder fails (no tasks written), stop the pipeline and report the error
- The flag mechanism is the ONLY modification to task-builder — all other behavior is unchanged
- **NEVER stop between step 3 and step 4** — this transition is atomic and mechanical

# Task 003: Integrate Router in run-task.sh

**Type:** BUILD
**Action:** Edit run-task.sh to source model-router.sh and pass --model to claude -p

## What

1. After `source "${SCRIPT_DIR}/lib/common.sh"`, add:
   ```bash
   source "${SCRIPT_DIR}/lib/model-router.sh"
   ```

2. Before the `run_claude "fresh"` call in the main loop (around line 306), add model routing:
   ```bash
   # Route to appropriate model tier
   TASK_FILE_PATH=""
   if [ -n "$TASK_SUBFOLDER" ]; then
     TASK_FILE_PATH=$(ls "tasks/${TASK_SUBFOLDER}/"*"${CURRENT_TASK}"* 2>/dev/null | head -1)
   fi
   SELECTED_MODEL=$(route_model "${TASK_FILE_PATH:-}" "${SCRIPT_DIR}/lib/model-routing-config.json")
   echo "[MODEL] Selected: $SELECTED_MODEL (task: $CURRENT_TASK)"
   ```

3. In the `run_claude()` function, accept model as a parameter and add `--model` to cmd_args:
   - Add `local model="${4:-claude-opus-4-6}"` parameter
   - Add `cmd_args+=("--model" "$model")` after the existing cmd_args array

4. Update all `run_claude` call sites to pass `$SELECTED_MODEL`

## Acceptance Criteria

- [ ] `grep -q 'model-router.sh' run-task.sh` exits 0
- [ ] `grep -q '\-\-model' run-task.sh` exits 0
- [ ] `grep -q 'route_model' run-task.sh` exits 0

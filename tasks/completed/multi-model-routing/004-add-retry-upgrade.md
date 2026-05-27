# Task 004: Add Retry-on-Upgrade Logic

**Type:** BUILD
**Action:** Edit run-task.sh — if task fails on cheaper model, retry with next tier up

## What

In the failure handling section of run-task.sh (around where `CONSECUTIVE_FAILS` is incremented), add upgrade logic:

Before skipping the task, check if the model can be upgraded:
```bash
# Try upgrading model tier before giving up
if [ "$SELECTED_MODEL" != "claude-opus-4-6" ]; then
  UPGRADED_MODEL=$(upgrade_model "$SELECTED_MODEL")
  if [ "$UPGRADED_MODEL" != "$SELECTED_MODEL" ]; then
    echo "[UPGRADE] Retrying with $UPGRADED_MODEL (was $SELECTED_MODEL)"
    SELECTED_MODEL="$UPGRADED_MODEL"
    # Don't count this as a consecutive fail — it's a tier upgrade retry
    CONSECUTIVE_FAILS=$((CONSECUTIVE_FAILS - 1))
    continue  # Re-enter the loop with upgraded model
  fi
fi
```

Also add `upgrade_model` function to `lib/model-router.sh`:
```bash
upgrade_model() {
  local current="$1"
  case "$current" in
    *haiku*) echo "claude-sonnet-4-6" ;;
    *sonnet*) echo "claude-opus-4-6" ;;
    *) echo "$current" ;;  # Already opus or unknown
  esac
}
```

## Acceptance Criteria

- [ ] `grep -q 'upgrade_model' run-task.sh` exits 0
- [ ] `grep -q 'UPGRADE' run-task.sh` exits 0

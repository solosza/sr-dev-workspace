# 001 — Edit session-start.md: Add one_shot Guard to Step 6

## Type
BUILD

## Action
Edit `.claude/commands/kernel/session-start.md` step 6 to skip the `anchored: false` reset when `one_shot: true` in session_state.json.

## Change

In step 6 ("Force anchor on fresh start"), add a guard BEFORE the anchored reset:

```markdown
6. **Force anchor on fresh start (MERGE — read → modify → write):**

   **one_shot guard:** If `one_shot: true` in session_state.json, SKIP this entire step.
   One-shot agents (spawned by run-task.sh) must not reset the parent's anchor state.
   They inherit the parent's `anchored: true` and proceed without re-anchoring.

   If NOT resuming from restart AND NOT one_shot (i.e., `needs_restart` was false or missing):
   ...
```

## Target File
`.claude/commands/kernel/session-start.md`

## Acceptance
- [ ] Step 6 has explicit one_shot guard
- [ ] Guard says to skip the entire step when one_shot is true
- [ ] Rest of step 6 logic unchanged

## Dependencies
None

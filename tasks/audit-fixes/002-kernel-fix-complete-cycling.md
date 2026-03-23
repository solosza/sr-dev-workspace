# Fix complete.md — Add Cycling Logic

## Context
Audit gap #2: complete.md has zero cycling logic. CLAUDE.md says "/kernel/complete handles cycling continuation" but the command doesn't update completed_tasks, advance current_task, handle skip-after-3, or set cycling: false when done. The agent has to infer this from workflow.md — which it may not re-read after context compaction.

## Dependencies
- None

## Requirements
- Read the existing complete.md to understand current structure
- Read the test-run-task-resume complete.md (which has cycling logic from the one-shot-master) for reference pattern
- Add cycling logic to complete.md after the deliverable verification step:
  - Check if `cycling: true` in workflow state
  - If cycling: add current_task to completed_tasks array
  - Scan task folder for next incomplete task (lowest-numbered not in completed_tasks or skipped_tasks)
  - If next task found: set current_task, reset attempts_on_current to 0, announce next task
  - If no tasks remain: set cycling: false, announce "All N tasks complete (M skipped)"
  - Update both workflow.json and session_state.json context
- Check if `one_shot: true` in session_state — if so, use one-shot completion mode (complete one task, output signal, stop)
- Preserve existing steps (state gates, deliverable verification, context save, report)

## Acceptance Criteria
- [ ] `grep -q 'completed_tasks' .claude/commands/kernel/complete.md` (cycling advances)
- [ ] `grep -q 'current_task' .claude/commands/kernel/complete.md` (picks next task)
- [ ] `grep -q 'cycling.*false' .claude/commands/kernel/complete.md` (handles all-done)
- [ ] `grep -q 'skipped_tasks' .claude/commands/kernel/complete.md` (skip logic referenced)
- [ ] `grep -q 'one_shot' .claude/commands/kernel/complete.md` (one-shot mode)
- [ ] Existing deliverable verification step preserved (verify: `grep -q 'Verify deliverables' .claude/commands/kernel/complete.md`)
- [ ] Read the file after editing — confirm cycling section is coherent and complete

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

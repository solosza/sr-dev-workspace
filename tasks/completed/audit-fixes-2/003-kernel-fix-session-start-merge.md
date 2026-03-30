# Fix session-start.md — Specify Merge Pattern

## Context
Audit gap #7: session-start.md says "MERGE, don't overwrite" but doesn't specify the mechanism. The agent may use Write (overwriting the file) instead of read→modify→write. This risks losing context, needs_learn, domain, or one_shot fields.

## Dependencies
- None

## Requirements
- Read session-start.md to understand current merge instructions
- Add explicit merge pattern: "Read session_state.json → modify only the fields listed → Write back the full object"
- Add a warning: "Do NOT use Write with a new JSON object — read first, merge, then write"
- List the fields that MUST be preserved: context, domain, needs_learn, needs_learn_reason, one_shot, actions_log
- Same for workflow state: completed_tasks, skipped_tasks, cycling, total_tasks, task_folder

## Acceptance Criteria
- [ ] `grep -q 'Read.*modify.*Write\|read.*merge.*write' .claude/commands/kernel/session-start.md` (explicit merge pattern)
- [ ] `grep -q 'preserve\|MUST be preserved\|Preserve' .claude/commands/kernel/session-start.md` (preservation warning)
- [ ] Read the file after editing — confirm merge instructions are clear

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

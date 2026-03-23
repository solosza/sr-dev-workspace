# Fix fix.md — Add Cycling-Aware Approval Gate

## Context
Audit gap #3: fix.md Step 5 says "Do NOT implement until user explicitly approves." This conflicts with CLAUDE.md's autonomy principle ("Report after, don't ask before"). During autonomous cycling, a test failure triggers fix → impact assessment → wait for user → stall. The fix needs a cycling-aware gate: auto-proceed if cycling, ask if not.

## Dependencies
- None

## Requirements
- Read the existing fix.md to understand current structure
- Modify Step 5 to check cycling mode:
  - Read workflow state: if `cycling: true`, auto-proceed after impact assessment (skip user approval)
  - If `cycling: false` or not set: wait for user approval (existing behavior)
  - Log the auto-proceed decision in the report ("Auto-proceeding: cycling mode active")
- Preserve all other steps (understand, log defect, impact assessment, implement, learn)
- The impact assessment is still MANDATORY even in cycling mode — only the approval gate changes

## Acceptance Criteria
- [ ] `grep -q 'cycling' .claude/commands/kernel/fix.md` (cycling check exists)
- [ ] `grep -q 'auto-proceed\|Auto-proceed\|auto proceed' .claude/commands/kernel/fix.md` (auto-proceed documented)
- [ ] Step 5 still says to wait for approval when NOT cycling (verify by reading)
- [ ] Impact assessment (Steps 3-4) unchanged (verify: `grep -q 'Impact Assessment' .claude/commands/kernel/fix.md`)
- [ ] Read the file after editing — confirm the cycling guard is clear and correct

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

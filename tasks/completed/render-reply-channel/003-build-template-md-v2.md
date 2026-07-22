# Build: template.md v2 — Action Map + Test Flag

## Context
Backlog 233. READ FIRST: templates/review-board/template.md (v1) + annotation-contract.md v2 section.

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- Add to the action map: `confirm` / `cancel` as META-ACTIONS (routed by matching the pending confirms[] entry for that target — confirm commits the original held action, cancel logs it declined; neither routes directly to review-queue)
- Document the optional `test` field (bool, default false): test:true annotations are acknowledged via reply-file `dry_run_ack` and NEVER routed
- Document the reply-channel page requirements (poll /status, confirm bars, results, dry-run toggle) with a link to the design payload — keep under 80 lines total, link don't duplicate
- Explicit note: schema change is ADDITIVE; v1 annotations remain valid

## Acceptance Criteria
- [ ] RC-04: map complete, additive note present

## Gates Satisfied
- RC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

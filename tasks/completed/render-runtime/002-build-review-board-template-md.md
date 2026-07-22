# Build templates/review-board/template.md

## Context
Backlog 232. The template's spec sheet: data source + action map. READ FIRST: .claude/docs/design/render/references/annotation-contract.md (the action map is defined there — copy it EXACTLY) and .claude/skills/review-queue/steps/step-01-discover.md (the data source).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- File: `.claude/skills/render/templates/review-board/template.md`
- Sections: **Data Source** (diff docs/backlog/done/ numbers against review-status.json `reviewed` keys — same discovery as /kernel/review-queue step 1; per-item fields: number, title, scope, priority, summary — extracted the way review-queue step-02 does), **Action Map** (accept/iterate/reject/skip/defer with routes + destructive flags exactly per annotation-contract.md), **Page Requirements** (self-contained, frozen schema POST, Send-to-session affordance, session-dir banner)
- Under 80 lines; links to design payloads rather than duplicating law text

## Acceptance Criteria
- [ ] RRT-03: action map matches annotation-contract.md exactly (reject flagged destructive)

## Gates Satisfied
- RRT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

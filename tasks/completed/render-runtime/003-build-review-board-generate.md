# Build templates/review-board/generate.py

## Context
Backlog 232. Data → page. READ FIRST: template.md (from task 002); visual reference: the session mock at C:/Users/solos/AppData/Local/Temp/claude/D--my-ai-projects-project-test-repos-sr-dev-workspace/ec739290-0c59-4db0-927a-d5242944f47e/scratchpad/render-loop-mock.html (card layout, chip styling, JSON-panel is NOT needed in the real page) — but generate from REAL input data, and the page POSTs instead of displaying JSON.

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- File: `.claude/skills/render/templates/review-board/generate.py`, stdlib only
- CLI: `python generate.py <items_json_path> <session_dir>` → writes `<session_dir>/page.html`
- Input: JSON array of `{number, title, scope, priority, summary}`
- Page: one card per item (title, chips for scope/priority, summary, buttons accept/iterate/reject/skip/defer, notes input revealed for iterate/reject); acting on a card marks it visually and queues the annotation client-side; a "Send to session" button POSTs the queued annotations ONE PER REQUEST to `/annotate` with the FROZEN schema `{target, action, raw_words, at}` and shows sent-count confirmation; banner at top names the session dir; fully self-contained (inline CSS/JS, zero external hosts); both light/dark via prefers-color-scheme
- HTML-escape all item-derived text (titles/summaries contain arbitrary markdown)

## Acceptance Criteria
- [ ] RRT-04: compliant page generated from a sample items JSON

## Gates Satisfied
- RRT-04 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

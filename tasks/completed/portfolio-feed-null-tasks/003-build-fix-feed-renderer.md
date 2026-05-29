# Fix Feed Renderer — Null-Safe task_count Display

## Context
`feed.html` renders each entry using `e.task_count + ' tasks'` with no null guard. If `task_count` is null in `feed-data.json`, this produces "null tasks" as a string. This task adds a null guard in the JS renderEntry function so null/undefined/0 values display as "—" instead.

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (feed generator fixed)

## Phase Gate
- [ ] `002-build-fix-feed-generator.md` marked complete

## Requirements
- File: `D:/my_ai_projects/isagawa-co.github.io/feed.html`
- In `renderEntry`, change the task_count span from:
  ```javascript
  '<span>' + e.task_count + ' tasks</span>'
  ```
  to:
  ```javascript
  '<span>' + (e.task_count != null ? e.task_count + ' tasks' : '—') + '</span>'
  ```
- Use `!= null` (catches both null and undefined) not `!== null`

## Acceptance Criteria
- [ ] `feed.html` renderEntry has null guard for task_count (grep match for `task_count != null`)
- [ ] No bare `e.task_count + ' tasks'` pattern remains in renderEntry
- [ ] File contains valid inline JavaScript (no syntax errors visible)

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Task 005: L2 - Routing Unit Test

**Type:** TEST (L2) | **Gates:** RH-05

## Action
ONE script in a sandbox dir: create tasks/rh-test/ with 001-copy-simple-file.md (haiku keywords: 'copy this simple file') and 002-implement-test-writer.md (sonnet keywords); seed agent-rh-test-workflow.json with 001 completed. Source the patched resolution logic (or invoke run-task.sh far enough / extract the function) to assert: next task resolves to 002; route_model on 001 returns the haiku model id and on 002 the sonnet id per lib/model-routing-config.json.

## Acceptance
Both routings non-default and correct; exit 0. Red: fix then /kernel/learn.

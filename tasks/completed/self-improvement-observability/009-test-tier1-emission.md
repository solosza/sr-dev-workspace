# Test Tier 1 emission hooks

## Context
Validates that all 3 kernel commands (learn, complete, anchor) contain proper emission instructions for metrics.jsonl. Phase boundary between Tier 1 and Tier 2.

## Type
TEST

## Execution
agent

## Dependencies
- 006, 007, 008 (all emission hooks added)

## Phase Gate
- [ ] learn.md contains `metrics.jsonl`
- [ ] complete.md contains `metrics.jsonl`
- [ ] anchor.md contains `metrics.jsonl`

## Requirements
- Verify learn.md emission instruction includes: schema_version, timestamp, event:"learn", trigger, lesson_topic, files_modified
- Verify complete.md emission instruction includes: schema_version, timestamp, event:"pipeline_complete", pipeline_id, result, tasks_total, tasks_completed, tasks_skipped, violations
- Verify anchor.md emission instruction includes: schema_version, timestamp, event:"anchor", actions_count, violations_found
- Verify all 3 specify "append-only" and "failure does not block"
- Verify no new dependencies added (no import/require statements added)

## Acceptance Criteria
- [ ] All 3 commands have metrics.jsonl emission instructions
- [ ] All emission instructions specify the correct event type and fields
- [ ] All emissions are documented as non-blocking
- [ ] No new dependencies introduced

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

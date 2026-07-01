# Create metrics.jsonl schema

## Context
Defines the JSON schema for metrics.jsonl — the append-only event log that captures pipeline_complete, anchor, and learn events emitted by kernel commands.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (observatory repo exists)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/` directory exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/schemas/metrics.jsonl.schema.json`
- Schema defines 3 event types:
  - `learn`: schema_version, timestamp, event, trigger, lesson_topic, files_modified[]
  - `pipeline_complete`: schema_version, timestamp, event, pipeline_id, result (PASS|PARTIAL|FAIL), tasks_total, tasks_completed, tasks_skipped, violations
  - `anchor`: schema_version, timestamp, event, actions_count, violations_found
- All events share: schema_version (integer, currently 1), timestamp (ISO 8601), event (enum)
- Include `$schema` reference and description

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/metrics.jsonl.schema.json` exists
- [ ] File is valid JSON
- [ ] Contains definitions for all 3 event types

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

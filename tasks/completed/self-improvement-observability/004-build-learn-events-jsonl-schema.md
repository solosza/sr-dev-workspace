# Create learn-events.jsonl schema

## Context
Defines the JSON schema for learn-events.jsonl — links lessons to code changes for rollback tracking.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (observatory repo exists)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/` directory exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/schemas/learn-events.jsonl.schema.json`
- Fields: learn_event_id, timestamp, lesson_topic, trigger, files_modified[], git_commit_hash, status (active|deprecated|superseded|ineffective), superseded_by, rollback_event_id
- Links to experiments.jsonl via learn_event_id

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/learn-events.jsonl.schema.json` exists
- [ ] File is valid JSON
- [ ] Contains rollback tracking fields (status, superseded_by, rollback_event_id)

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Task 002 — Manifest Schema + Producer Wiring

## Type
RESEARCH

## Description
Design the manifest schema: producer id (backlog number + subfolder), artifact list (path, kind, summary, hash/word_count), completion status, timestamp, schema version. Decide the producer: a task-builder-appended final task, a run-task.sh post-completion step, or the existing gate-validation pass (which already enumerates deliverables). Manifests must be producible by one-shot agents with plain JSON writes — no new tooling. Read the task-builder gate-contract format first (RULE ZERO).

## Acceptance Criteria
- [ ] File `projects/kernel-artifact-bus-research/01-manifest-schema.md` exists
- [ ] Covers: versioned manifest JSON schema with a filled example
- [ ] Covers: producer decision (who writes it, when) with rationale
- [ ] Covers: stale-manifest and manifest/file-drift handling on re-runs
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001

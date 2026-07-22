# Task 003 — Consumer Design + Overlap Analysis

## Type
RESEARCH

## Description
Design the consumer side: task-builder emits an ingestion step (read manifest, fail fast if missing/incomplete) and prerequisites reference manifests vs raw files (ties into backlog 242's format). Then run the overlap analysis the verdict depends on: per-agent state files, gate contracts (already machine-readable deliverable lists), and backlog archive status — is the bus NEW information or a re-serialization of existing mechanisms? Must also unify with the semantic handoff schema proposed in projects/kernel-ephemeral-subagents-research/03-integration-design.md — one handoff format, not two.

## Acceptance Criteria
- [ ] File `projects/kernel-artifact-bus-research/02-consumer-and-overlap.md` exists
- [ ] Covers: consumer ingestion step design + prerequisite integration with 242
- [ ] Covers: explicit overlap verdict vs existing mechanisms
- [ ] Covers: unification with the 237 handoff schema
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001

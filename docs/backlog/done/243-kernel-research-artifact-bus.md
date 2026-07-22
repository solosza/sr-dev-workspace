# Research: Inter-Agent Shared Artifact Bus

## Status
Open

## Priority
Medium — data-layer complement to backlogs 241/242: ordering says WHEN downstream agents run, the bus says WHAT they consume and WHERE it lives.

## Summary
Define a strict workspace protocol for how sub-agents export deliverables: each agent writes a structured manifest (`projects/<task-name>/exports/manifest.json`) enumerating its outputs (paths, types, schemas, status), and downstream agents ingest the manifest in their first task instead of scraping unstructured repo files. Research the schema and adoption path, and produce a yah/nay verdict.

## Requirements
- Manifest schema: producer id (backlog number + subfolder), artifact list (path, kind, summary, word_count/hash), completion status, timestamp — versioned schema so consumers can validate
- Producer side: who writes it — a new final task appended by task-builder, run-task.sh post-completion step, or the existing gate-validation pass (which already enumerates deliverables)?
- Consumer side: task-builder emits an ingestion step (read manifest, fail fast if missing/incomplete) — how prerequisites reference manifests vs raw files (ties into 242's prerequisite format)
- Overlap analysis with existing mechanisms: per-agent state files, gate contracts (already machine-readable deliverable lists), and backlog archive status — is the bus new information or a re-serialization? The verdict must answer this explicitly
- Reconcile with 237's research finding (semantic handoff schema for ephemeral agents) — one handoff format for both swarm-level and sub-task-level, not two
- Failure modes: stale manifests after re-runs, partial exports on skipped tasks, manifest/file drift
- **Verdict: yah or nay** — adopt the artifact bus, and if yah: schema + producer/consumer wiring; if nay: what existing mechanism covers it
- **Cross-proposal ranking:** this backlog (last of the three) owns the combined recommendation across 241 + 242 + 243 — which to build, in what order, or which combination

## References
- Backlogs 241 (wave engine), 242 (barrier gates) — sibling proposals
- `projects/kernel-ephemeral-subagents-research/03-integration-design.md` — semantic handoff schema proposal (must unify, not duplicate)
- `.claude/skills/task-builder/` (gate contracts as existing deliverable enumeration), `.claude/state/agent-*-state.json` pattern
- Live evidence 2026-07-21: 240's portfolio task located sibling outputs by convention (`projects/kernel-*-research/`) — worked, but only because naming was uniform

## Task Builder Input
- **Deliverable:** Research report — manifest schema, producer/consumer design, overlap analysis, combined 241/242/243 recommendation, yah/nay verdict
- **Location:** subproject:kernel-artifact-bus-research
- **Scope:** RESEARCH
- **Constraints:** Research only. Must not duplicate 237's handoff schema — extend or unify it. Manifest must be producible by one-shot agents without new tooling (plain JSON writes).

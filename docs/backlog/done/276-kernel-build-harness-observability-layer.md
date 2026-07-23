# Harness Observability Layer — Structural Detection of False-Completion & Silent Failure

## Status
Open

## Priority
High — this is the "fix first" gap from the 2026 workflow assessment. Observability is the weakest of the kernel's five harness layers, and it demonstrably let false "done" reports through repeatedly this session. The cost is real and recurring.

## Summary
The 2026 harness-engineering consensus treats observability as a co-equal harness layer (tool orchestration, verification loops, context/memory, guardrails, **observability**). The kernel's observability is log-file-based (`actions.jsonl`, state files) and depends on the orchestrator manually re-validating every gate to catch failures. That manual vigilance is not a layer — it's a person doing the layer's job. Build a real observability layer that structurally detects false-completion and silent-failure without relying on the orchestrator noticing.

## Evidence (this session's failures the layer must have caught)
- **270 false-complete:** runner marked tasks 001/002 complete in state while the actual `run-task.sh` edits were wiped by a concurrent reset — state said "done," code was gone. Only caught by manual diff.
- **261 false-negative banner:** the wrapper reported "3 failed / MAX ITERATIONS" while all 4 tasks had actually completed and written real artifacts — empty-stdout capture misjudged the outcome. Caught only by reading authoritative state.
- **Empty-output 600s timeouts** (lessons #49, ledger) and **0-byte iteration logs** silently masking skips (208 UT-04).
- **BOM-corrupted state** (2026-07-22) breaking resume.
Common thread: the runner's self-report and the banner both LIE, and the only backstop is the orchestrator re-running every gate live (lesson #39). That is a person substituting for missing observability.

## Requirements
- **Completion truth oracle:** a deterministic check that reconciles claimed completion (state `completed_tasks`) against ground-truth evidence (git commits for the deliverable, non-empty artifacts, re-runnable gate evidence) — flags divergence automatically, no human diff required.
- **Banner-vs-reality reconciliation:** never trust the wrapper banner; the observability layer computes outcome from authoritative signals (state file + artifacts + iteration logs) and surfaces disagreement between banner and reality as a first-class alert.
- **Liveness/heartbeat surfacing:** consume the 262 heartbeat + detect silent death / stall and emit a visible signal (not just a file) — a stalled or dead runner should be observable at a glance, not discovered.
- **Structured event stream + a status view:** beyond append-only logs — a queryable run status (per-agent, per-pipeline) an operator (or a monitor) reads without tailing raw JSONL. This is the "5th layer" the frontier names.
- **Ties to 270/271:** completion-persistence (270) and state-leak (271) fixes are prerequisites/companions — observability detects what those prevent; coordinate scope so they compose, not overlap.

## References
- 2026 harness engineering — observability as a core layer: martinfowler.com/articles/harness-engineering.html; faros.ai/blog/harness-engineering; augmentcode.com/guides/harness-engineering-ai-coding-agents
- Lessons #39 (orchestrator re-runs every gate live), #49 (0-byte-log gate skip is a defect)
- `docs/backlog/270-kernel-fix-runner-hardening-v2.md` (completion persistence, death detection), `271-*` (state isolation)
- `run-task.sh` (heartbeat, EMPTY-RETRY), `.claude/state/actions.jsonl`

## Task Builder Input
- **Deliverable:** An observability layer for the kernel harness — a completion-truth oracle + banner-vs-reality reconciliation + liveness surfacing + a queryable run-status view — that structurally detects false-completion/silent-failure without orchestrator vigilance, plus tests reproducing this session's false-completion cases.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must compose with 270 (completion persistence) and 271 (state isolation) — sequence/coordinate. Works with per-agent `KERNEL_AGENT_ID` state routing. Do not add ceremony the operator routes around (see 279) — observability must be passive/automatic, not another gate to satisfy.

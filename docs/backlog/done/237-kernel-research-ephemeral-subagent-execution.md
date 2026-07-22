# Research: Ephemeral Sub-Agent Execution as Context-Decay Strategy

## Status
Open

## Priority
Medium — kernel already runs one-shot agents per task via run-task.sh; the open question is whether to extend the pattern to ALL long workflows, not whether it works.

## Summary
Industry pattern (Devin / Anthropic orchestrator-worker): never let a session accumulate 50+ actions — spawn a fresh sub-agent per sub-task, terminate it, return a concise result to the orchestrator. Context length stays ~10-15 turns so attention decay never sets in. This is an alternative (or complement) to our N-action re-anchor loop. Research whether the kernel should shift more of its execution onto ephemeral agents, and what that does to the re-anchoring loop's role.

## Requirements
- Map what the kernel ALREADY does ephemerally (run-task.sh one-shot agents, prod-test sub-agents) vs. what still runs long-lived (orchestrator sessions, execute-pipeline parent, interactive work)
- Quantify: at what context depth does our observed reasoning quality degrade (use anchor-logs / DEFECT_LOG history as evidence)
- Evaluate orchestrator-per-vertical pattern (fresh sub-agent per interface slice: DB → UI → API → SOAP) against known state-contention lessons (shared session_state.json, per-agent isolation, backlog 183 worktree isolation)
- Cost/latency: sub-agent spawn overhead vs. token savings from short contexts
- Interaction with re-anchor loop: if sub-agents are short-lived, does the N-action anchor become orchestrator-only? What is the anchor contract INSIDE a one-shot agent?
- **Verdict: yah or nay** — should ephemeral execution expand in the kernel loop, and if yah, a concrete integration design (which workflows move, state handoff schema, anchor policy per agent tier)

## References
- `.claude/lessons/lessons.md` — multi-agent state isolation, state contention, nested session nesting (`env -u CLAUDECODE`)
- `run-task.sh` one-shot pattern; `.claude/skills/spawn-subagent/`, `.claude/skills/spawn-agent-swarm/`
- Backlog 183 (worktree isolation); backlogs 238-240 (sibling context-decay research)
- Context-decay strategy comparison (user-provided analysis, 2026-07-21): decay impossible when context never accumulates

## Task Builder Input
- **Deliverable:** Research report — pattern analysis, kernel gap map, cost model, yah/nay verdict + integration design if yah
- **Location:** subproject:kernel-ephemeral-subagents-research
- **Scope:** RESEARCH
- **Constraints:** No kernel changes in this backlog — research only. Must reconcile with lessons on state contention and per-agent isolation before recommending expansion.

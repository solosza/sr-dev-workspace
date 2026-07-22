# Task 002 — Map Current Ephemeral Surface

## Type
RESEARCH

## Description
Map what the kernel ALREADY runs ephemerally (run-task.sh one-shot agents, prod-test sub-agents, spawn-subagent/spawn-agent-swarm skills) versus what runs long-lived (interactive orchestrator sessions, execute-pipeline parent). Gather evidence of context-depth reasoning degradation from .claude/state/anchor-logs/ history and hmsa-qa-platform DEFECT_LOG.md. Read the actual files (RULE ZERO).

## Acceptance Criteria
- [ ] File `projects/kernel-ephemeral-subagents-research/01-current-ephemeral-surface.md` exists
- [ ] Covers: inventory of ephemeral vs long-lived execution surfaces with file citations
- [ ] Covers: observed degradation evidence (anchor-logs, DEFECT_LOG) or explicit finding of none
- [ ] Covers: what the anchor contract currently is inside a one-shot agent
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001

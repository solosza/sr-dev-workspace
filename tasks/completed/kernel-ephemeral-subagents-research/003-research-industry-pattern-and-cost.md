# Task 003 — Industry Pattern + Cost Model

## Type
RESEARCH

## Description
Research the orchestrator-worker / ephemeral micro-session pattern (Devin, Anthropic sub-agents): why short contexts prevent attention decay, typical context ceilings (~10-15 turns), and result-handoff conventions. Build a cost model: sub-agent spawn overhead + orchestrator token cost vs. token savings from short contexts, using our run-task.sh runs as data points.

## Acceptance Criteria
- [ ] File `projects/kernel-ephemeral-subagents-research/02-industry-pattern-and-cost.md` exists
- [ ] Covers: pattern description with sources
- [ ] Covers: cost/latency model with kernel-specific numbers or estimates
- [ ] Covers: failure modes (context loss at handoff, orchestrator becoming the long-lived bottleneck)
- [ ] Minimum 300 words

## Gate
DOC-03, DOC-04

## Dependencies
001

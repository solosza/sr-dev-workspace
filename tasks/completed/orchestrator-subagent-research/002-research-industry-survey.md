# Industry Survey: Orchestrator-Worker Patterns

## Context
Backlog 230: sourced survey of when single-responsibility subagents win vs when inline execution wins.

## Type
RESEARCH
## Execution
inline
## Dependencies
- None

## Requirements
- Web research (WebSearch/WebFetch), every substantive claim sourced: Anthropic's multi-agent/subagent guidance (Claude Code subagents, Agent tool semantics, context-isolation benefits), orchestrator-worker pattern literature, LangGraph supervisor pattern, swarm frameworks, known failure modes (coordination overhead, context fragmentation, latency, cost multiplication)
- Extract decision criteria the field converges on: task independence, context-budget pressure, parallelism value, verification needs, state isolation
- Write `projects/orchestrator-subagent-research/02-industry-survey.md` with ≥6 source links and a distilled when-to/when-not table

## Acceptance Criteria
- [ ] 02-industry-survey.md exists, ≥6 http sources, when-to/when-not table present

## Gates Satisfied
- OSR-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

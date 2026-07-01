# Research AI Agent Job Market

## Context
Analyze the current AI agent engineering job market to understand what companies want, which skills are in highest demand, what role titles to target, and which companies are actively hiring. This informs the AI Agent resume positioning.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Web search for current AI agent engineering roles (June/July 2026 market)
- Identify top role titles: Agent Infrastructure Engineer, AI Agent Engineer, AI Systems Engineer, etc.
- Identify most-demanded skills: agent frameworks (LangGraph, CrewAI, Claude Code), orchestration, evaluation, governance
- Identify top hiring companies: Anthropic, OpenAI, Google DeepMind, Cohere, startups
- Identify what differentiates candidates who get hired (portfolio, open source, production experience)
- Note salary ranges and remote availability
- Output findings to `projects/targeted-resume-pair/01-agent-market-research.md`

## Acceptance Criteria
- [ ] `projects/targeted-resume-pair/01-agent-market-research.md` exists
- [ ] Contains role titles, skills demand, top companies, differentiators

## Gates Satisfied
- (none — research feeds into BUILD-01)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Analyze Website Cloner as Skill-Based App

## Context
The website cloner is a pure skill-based tool — no deployed app, the agent IS the runtime. Analyze what makes this pattern work, what its limits are, and what a "generation skill" counterpart would look like.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Read `.claude/skills/website-cloner/SKILL.md` — understand the pipeline structure
- Read `.claude/skills/website-cloner/references/extraction.md` — understand how Playwright MCP tools are used
- Read `.claude/skills/website-cloner/references/generation.md` — understand the output generation
- Analyze: What makes this work as a skill? (structured pipeline, MCP tools as runtime, reusable across URLs)
- Analyze: What would break if this were a traditional app? (would need a web UI, server, deployment)
- Analyze: What's missing? (no generation skill — extraction is structured, generation is ad-hoc)
- Analyze: Could this compose with other skills? (extractor → merger → generator)
- Write findings as structured notes (will be consumed by task 005)

## Acceptance Criteria
- [ ] All 3 website-cloner files read (SKILL.md, extraction.md, generation.md)
- [ ] Analysis covers: strengths, limits, missing generation skill, composability potential
- [ ] Findings documented in conversation context for task 005

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

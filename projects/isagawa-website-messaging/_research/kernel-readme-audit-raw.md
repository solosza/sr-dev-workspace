# Kernel README Audit — Raw Positioning (isagawa-kernel)

Fetched: 2026-06-17

## Headline
"The self-improving harness for AI coding agents."

## Tagline
"The agent builds its own rules, enforces them mechanically, and gets better every time it fails."

## Problem Statement
AI coding agents exhibit drift behavior over extended tasks:
- System prompts ignored after thousands of tokens
- Quality checks skipped during complex work
- Identical mistakes recur without enforced learning
- Output inconsistency spans sessions
- Context tools (memory/RAG) provide information but no compliance obligation

Core issue: existing solutions are advisory rather than enforceable.

## Solution Framing: Spec-Driven Development (SDD)
Inverts traditional agent relationships. Instead of humans writing specs and hoping agents follow them, "the agent internalizes the spec, builds its own protocol and enforcement, and then it mechanically can't violate it."

Key mechanism: "The agent physically cannot skip a quality check, ignore a failure, or proceed without recording what it learned."

## Architecture
Three-layer:
1. **Kernel** — governs HOW agents work (governance loop)
2. **Domain Spec** (optional) — teaches WHAT to build (industry knowledge)
3. **Agent-Generated** — protocol, lessons, enforcement, tasks (self-built)

## Key Capabilities
- Autonomous cycling through task queues
- Self-building setup (scanning repos to create protocols)
- Mandatory learn loops (failures → permanent lessons)
- Cross-session persistence (resume mid-task)
- Periodic re-anchoring (force protocol compliance)
- Smart enforcement gates (clear remediation paths)

## Available Domain Specs
- QA Platform (Selenium & Playwright) — live
- DevOps (CI/CD) — coming soon
- Health Insurance — coming soon
- Real Estate — coming soon

## Target Audiences (from README)
- Solo developers
- Teams
- Consultants
- QA/test automation teams
- Agencies

## Quick Start
- VS Code with Claude Code extension
- Python 3.8+
- No database, Docker, or cloud infrastructure

## License
MIT

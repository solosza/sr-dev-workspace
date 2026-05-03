# Write Decision Report

## Type
BUILD

## Description
Based on gap analysis, decide: Option A (fork/adapt), Option B (thin wrapper), or Option C (build from scratch). Document the decision and reasoning.

## Requirements
Create `.claude/skills/website-cloner/research/decision.md` with:
- **Decision**: Option A, B, or C
- **Reasoning**: based on gap analysis findings
- **Implementation plan**: what to build in tasks 006-009
- If Option A: what to fork, what to modify
- If Option B: what prompt/wrapper to write, what our MCP already handles
- If Option C: what lessons to take from the repo, what to build differently

## Acceptance Criteria
- [ ] `test -f .claude/skills/website-cloner/research/decision.md`
- [ ] `grep -q "Decision" .claude/skills/website-cloner/research/decision.md`

# Task 002 — Dependency Metadata + Wave Sorting Design

## Type
RESEARCH

## Description
Design the dependency metadata format: depends_on declared in backlog frontmatter or Task Builder Input vs. the task index — pick one and define exactly how spawn-agent-swarm step-01 parsing consumes it. Then design topological wave sorting with cycle detection (circular dependencies rejected at sort time with a clear error, before any agent spawns). Read the actual skill files (.claude/skills/spawn-agent-swarm/, .claude/skills/execute-pipeline/) first — RULE ZERO.

## Acceptance Criteria
- [ ] File `projects/kernel-dag-wave-research/01-metadata-and-sorting.md` exists
- [ ] Covers: chosen depends_on format with parse rules and a worked example
- [ ] Covers: wave sorting algorithm + cycle detection behavior
- [ ] Covers: how existing step-01 validation extends without breaking current flat usage
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001

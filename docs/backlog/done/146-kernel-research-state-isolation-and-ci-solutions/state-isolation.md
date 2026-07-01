# State Isolation — Research

## Status
NEW

## The Problem

When multiple agents run concurrently (parallel execute-pipeline, spawn-agent-swarm, or raw Agent tool calls), they all write to two shared files:
- `.claude/state/session_state.json` — session context, actions log, anchor token
- `.claude/state/{domain}_workflow.json` — anchor counter, completed tasks, cycling state

Later agents overwrite earlier agents' state. This causes: context loss, visibility loss (orchestrator can't see agent completion), and potential anchor/counter corruption.

## What Already Exists

1. **`one_shot` guard** — run-task.sh sub-agents skip anchor/counter/token gates
2. **Lock file** — prevents concurrent run-task.sh on same task folder
3. **`spawn-agent-swarm` per-agent state** — designed but not wired into execute-pipeline

## Research Questions

1. How do LangGraph, CrewAI, AutoGen handle concurrent agent state?
2. What's the simplest isolation pattern that works with the existing hook architecture?
3. Should isolation be file-level (per-agent JSON files) or field-level (scoped keys within shared file)?
4. How should the orchestrator aggregate per-agent state for monitoring?
5. Can the actions-log-appender hook be scoped to per-agent log files?

## Solution Criteria

- No external runtime (no Redis, no database, no message queue)
- Compatible with existing hooks (universal-gate-enforcer, actions-log-appender)
- Works on Windows (Git Bash) and Unix
- Minimal changes to run-task.sh and execute-pipeline

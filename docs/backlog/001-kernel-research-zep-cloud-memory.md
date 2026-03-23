# Backlog 001: Research Zep Cloud Memory Architecture for JSONL Execution Log

## Status
Open

## Summary
Evaluate whether Zep Cloud's memory architecture has patterns worth borrowing for the JSONL execution log (currently marked as not-yet-implemented in the kernel). Their long-term memory approach across agent sessions solves a similar problem to our cross-session state persistence — just without the enforcement layer.

## Key Questions
- How does Zep Cloud structure long-term memory across agent sessions?
- What's their retrieval strategy? (vector, graph, hybrid?)
- How do they handle memory consolidation / summarization over time?
- What patterns map to our JSONL execution log use case?
- Can we adopt their architecture while keeping our hook-based enforcement layer?

## Context
The kernel currently uses `session_state.json` for cross-session context and `actions_log` for intra-session tracking. The JSONL execution log would provide a durable, append-only record of all agent actions across sessions — enabling replay, audit, and richer cross-session memory than the current `context` key approach.

## Origin
External observation — comparing Isagawa kernel's state persistence with Zep Cloud's memory layer.

## Task Builder Input
- **Deliverable:** Research document with Zep Cloud architecture analysis + recommendations for kernel JSONL execution log
- **Scope:** RESEARCH
- **Constraints:** Web research only, no code changes. Output to `docs/research/`

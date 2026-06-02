# Write Final Research Report

## Context
Synthesizes MCP framework research and capability assessment into final recommendation.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-kernel-research-candidate-capabilities.md

## Phase Gate
- [ ] `projects/mcp-server-research/capabilities-assessment.md` exists

## Requirements
Write `projects/mcp-server-research/research-report.md` covering:
1. What MCP is and what a custom server provides
2. Framework comparison (FastMCP vs official SDK) — recommendation
3. Development effort estimate — realistic hours to first working tool
4. Candidate capabilities ranked by value
5. Top recommendation: which capability to build first and why
6. Minimal prototype spec for the #1 candidate (if build is recommended)
7. Overall: BUILD / SKIP with reasoning

## Acceptance Criteria
- [ ] `projects/mcp-server-research/research-report.md` exists
- [ ] File has BUILD/SKIP recommendation
- [ ] File is > 60 lines

## Gates Satisfied
- DOC-06, DOC-07, DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

# Research: MCP Spec and Python Frameworks

## Context
Before evaluating kernel capability exposure, need to understand what it takes to build a custom MCP server — the spec, available frameworks, and development complexity.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/mcp-server-research/` exists

## Requirements
- WebSearch/WebFetch to understand: what is MCP? What does a custom MCP server require?
- Assess FastMCP (github.com/jlowin/fastmcp) — what does it provide, how much boilerplate is eliminated?
- Assess the official Anthropic MCP Python SDK — same questions
- Compare: FastMCP vs official SDK — which is lower friction for the kernel's Python stack?
- Estimate development effort: how many lines of Python to expose one tool as an MCP endpoint?
- Document any runtime requirements (process management, port binding, etc.)
- Write to `projects/mcp-server-research/mcp-frameworks-summary.md`

## Acceptance Criteria
- [ ] `projects/mcp-server-research/mcp-frameworks-summary.md` exists
- [ ] File covers FastMCP framework
- [ ] File compares FastMCP to official SDK
- [ ] File includes effort estimate for a simple MCP tool

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

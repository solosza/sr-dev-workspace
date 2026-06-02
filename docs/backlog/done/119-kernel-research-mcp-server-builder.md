# Research: MCP Server Builder — Kernel Capabilities as MCP Tools

## Status
Open

## Priority
Medium — the kernel has growing capabilities (attestation, QA platform, pipeline orchestration) that could be exposed as MCP tools, enabling external tools and Claude.ai to consume them without running Claude Code

## Summary
MCP (Model Context Protocol) servers allow capabilities to be exposed as structured tools callable by any MCP-compatible client. The kernel currently exposes capabilities only through Claude Code commands and run-task.sh. Building custom MCP servers would let external integrations (other Claude sessions, VS Code extensions, web UIs) consume kernel capabilities like attestation, pipeline status, and QA platform results without spawning a full Claude Code session.

## Requirements
- Understand the MCP server spec: what does it take to build a custom MCP server in Python or TypeScript?
- Identify which kernel capabilities are candidates for MCP exposure: attestation (attest.py), pipeline state queries, backlog management, QA platform results
- Assess the development effort: how much boilerplate, what framework (FastMCP, official SDK, etc.)?
- Evaluate the value proposition: what workflows become possible with MCP-exposed kernel capabilities that aren't possible today?
- Determine integration point: standalone MCP server repo, or embedded in sr_dev_workspace under `lib/mcp/`?
- Assess whether this competes with or complements the existing run-task.sh + execute-pipeline architecture

## References
- MCP spec: `https://modelcontextprotocol.io`
- FastMCP (Python framework): `https://github.com/jlowin/fastmcp`
- Existing kernel capabilities: `lib/attestation/`, `.claude/commands/kernel/`
- Backlog 116: Superpowers integration (parallel capability research)

## Task Builder Input
- **Deliverable:** Research report — MCP server feasibility assessment, candidate capabilities list, development effort estimate, and (if recommended) a minimal prototype spec for the highest-value capability
- **Location:** `subproject:mcp-server-builder-research`
- **Scope:** RESEARCH
- **Constraints:** Must not duplicate existing run-task.sh architecture. Prototype spec (if any) must fit Python stack already in use. Evaluate FastMCP vs official SDK for lowest-friction entry point.

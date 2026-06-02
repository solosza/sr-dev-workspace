# MCP Frameworks Summary

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that standardizes how LLM applications connect to external data sources and tools. Think of it as "USB-C for AI" — a universal interface that lets any LLM client talk to any tool server.

**Spec status:** Current stable spec is 2025-11-25. A 2026-07-28 release candidate is in progress, adding stateless HTTP core, Tasks extension, and enterprise features (audit trails, SSO, gateway behavior).

**Governance:** Linux Foundation (since December 2025).

**Adoption:** Supported by Anthropic, OpenAI, Google DeepMind. Consumable by Claude Desktop, ChatGPT, Copilot Studio, Gemini, Cursor, Windsurf, JetBrains AI, LangGraph, CrewAI, AutoGen. 2,300+ public servers listed as of April 2026.

## Core Primitives

MCP servers expose capabilities through exactly three primitives:

| Primitive | Purpose | Analogy |
|-----------|---------|---------|
| **Tool** | Executable action (side effects) | POST endpoint |
| **Resource** | Read-only data | GET endpoint |
| **Prompt** | Reusable interaction template | Stored procedure |

Each has standardized `list` and `get/call` methods.

## Transport Protocols

| Transport | How it works | Use case |
|-----------|-------------|----------|
| **stdio** | Standard input/output | Local processes, Claude Code integration |
| **SSE** | Server-Sent Events over HTTP | Remote servers, real-time streaming |
| **Streamable HTTP** | Bidirectional HTTP streaming (new in 2025) | Stateless, scalable, load-balancer friendly |

## Framework Comparison: FastMCP vs Official SDK

### FastMCP (Standalone — `pip install fastmcp`)

- **Repo:** github.com/jlowin/fastmcp (PrefectHQ)
- **Downloads:** ~1M/day. Powers ~70% of MCP servers across all languages
- **Philosophy:** Decorator-first, Pythonic, minimal boilerplate
- **Extras:** Native FastAPI integration, OpenAPI support, MCP Apps (rich HTML UIs in chat)

**Minimal server (8 lines):**
```python
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### Official MCP Python SDK (`pip install mcp[cli]`)

- **Repo:** github.com/modelcontextprotocol/python-sdk
- **Note:** FastMCP 1.0 was incorporated INTO the official SDK in 2024
- **Import path:** `from mcp.server.fastmcp import FastMCP`
- **Current version:** v1.x stable, v2 in development

**Minimal server (8 lines — identical API):**
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

### Head-to-Head

| Aspect | FastMCP (standalone) | Official SDK |
|--------|---------------------|--------------|
| API surface | Identical decorator API | Same (it IS FastMCP) |
| Transport | stdio, SSE, Memory, HTTP | stdio, SSE, Streamable HTTP |
| FastAPI integration | Native | Via FastMCP embedded |
| MCP Apps (rich UI) | Yes (2026) | Not yet |
| Install | `pip install fastmcp` | `pip install mcp[cli]` |
| Claude Code integration | Both work via stdio | Both work via stdio |
| Community | Standalone project, rapid iteration | Official, spec-aligned |

**Key insight:** They are essentially the same framework. FastMCP 1.0 was merged into the official SDK. The standalone FastMCP package iterates faster and has extra features (MCP Apps, Memory transport). The official SDK is spec-aligned and ships with the `mcp` package.

## Effort Estimate: One Custom MCP Tool

| What | Effort |
|------|--------|
| Boilerplate (imports, server init, run) | 4 lines |
| One tool function with decorator | 4-8 lines |
| **Total for minimal server** | **~10 lines of Python** |
| Adding a second tool | +4-8 lines per tool |
| Adding resources | +4-8 lines per resource |
| Transport config (stdio for Claude Code) | 0 extra lines (default) |
| Transport config (HTTP for remote) | 1 line change |

**Development time for a simple MCP server:** 15-30 minutes including testing with MCP Inspector.

## Runtime Requirements

| Requirement | Detail |
|-------------|--------|
| Python | 3.10+ |
| Dependencies | `fastmcp` or `mcp[cli]` (both pull in pydantic, httpx, etc.) |
| Process model | Single Python process per server |
| Port binding | Only needed for SSE/HTTP transport; stdio needs no ports |
| Claude Code integration | Add to `.claude/settings.local.json` under `mcpServers` |
| Testing | MCP Inspector (visual tool from Anthropic) |

## Recommendation for Kernel

**Use the standalone FastMCP package** (`pip install fastmcp`):
- Faster iteration cycle than official SDK
- Same decorator API (migration to official SDK is a one-line import change)
- MCP Apps support for potential rich UI in chat
- stdio transport is the default — perfect for Claude Code integration
- The kernel's Python stack (hooks, enforcers) maps directly to MCP tools

**Risk:** Low. If FastMCP standalone diverges from spec, switching to official SDK is trivial (change import path).

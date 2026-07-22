# MCP Server Builder — Research Report

**Date:** 2026-06-01
**Scope:** Assess feasibility of building custom MCP servers for Isagawa Kernel capabilities
**Recommendation:** BUILD (prototype)

---

## 1. What MCP Is and What a Custom Server Provides

The Model Context Protocol (MCP) is an open standard (Linux Foundation, since December 2025) that creates a universal interface between LLM applications and external tools/data. It is supported by Anthropic, OpenAI, and Google DeepMind, and consumed by Claude Code, ChatGPT, Cursor, Windsurf, JetBrains AI, and all major agent frameworks.

A custom MCP server wraps existing functionality (Python functions, CLI tools, APIs) behind a standardized protocol. Once exposed, any MCP-compatible client can discover and call those tools without custom integration code.

**What this means for the kernel:** Kernel capabilities (attestation, pipeline state, backlog management) become callable by any Claude session, VS Code extension, web dashboard, or CI/CD pipeline — without modifying the kernel itself.

## 2. Framework Recommendation

**Use FastMCP (standalone)** — `pip install fastmcp`.

| Factor | FastMCP | Official SDK |
|--------|---------|-------------|
| API | Identical decorator-based | Same (FastMCP 1.0 was merged in) |
| Iteration speed | Fast (standalone project) | Slower (spec-aligned releases) |
| Transport | stdio, SSE, Memory, HTTP | stdio, SSE, Streamable HTTP |
| Migration risk | One import line change | N/A |
| Claude Code integration | stdio (default) | stdio (supported) |

FastMCP is the de facto standard — it powers ~70% of MCP servers, gets ~1M downloads/day, and the API is identical to the official SDK. If FastMCP diverges from spec, migration is a one-line import change.

Full comparison: → `mcp-frameworks-summary.md`

## 3. Development Effort Estimate

| Milestone | Effort |
|-----------|--------|
| Install FastMCP + hello world | 15 minutes |
| First kernel tool (pipeline status query) | 1-2 hours |
| Wire into Claude Code settings | 15 minutes |
| Test with MCP Inspector | 30 minutes |
| **Total to first working tool** | **2-3 hours** |
| Add second tool (attestation) | 2-3 hours |
| Add remaining tools (backlog, lessons, gates) | 3-4 hours |
| **Full kernel MCP server (5 tools)** | **8-12 hours** |

Lines of code estimate:
- Server boilerplate: ~10 lines
- Per tool: ~10-20 lines (depending on complexity)
- Full 5-tool server: ~100-150 lines of Python

## 4. Candidate Capabilities Ranked

| Rank | Capability | Value | Effort | Why |
|------|-----------|-------|--------|-----|
| 1 | **Pipeline State Query** | HIGH | LOW | Zero external visibility today. Read-only = safe. Enables monitoring dashboards. |
| 2 | **Attestation Pipeline** | HIGH | MED | Kernel's differentiator. Enables CI/CD and cross-session attestation. |
| 3 | **Backlog Management** | MED | MED | External intake channel. Value scales with team size. |
| 4 | **Lesson Query** | LOW-MED | LOW | Cross-domain knowledge transfer. Value increases with multiple domains. |
| 5 | **Hook Gate Status** | LOW | LOW | Debugging convenience. Not a new workflow. |

Full assessment: → `capabilities-assessment.md`

## 5. Top Recommendation: Build Pipeline State Query First

**Why `kernel_pipeline_status` should be the first MCP tool:**

1. **Immediate pain point:** Pipeline visibility is currently zero outside the active Claude session. You cannot check if a pipeline is running, stalled, or complete without reading JSON files.

2. **Read-only = zero risk:** No side effects, no gate enforcement needed. Cannot break anything.

3. **Lowest effort:** ~20 lines of Python. Read two JSON files, return structured data.

4. **Foundation for everything else:** Once the MCP server exists and is wired into Claude Code, adding tools 2-5 is incremental.

5. **Validates the architecture:** Proves that kernel capabilities can be MCP-exposed before investing in higher-complexity tools like attestation.

## 6. Minimal Prototype Spec

### `kernel_pipeline_status` Tool

```python
from fastmcp import FastMCP
import json
from pathlib import Path

mcp = FastMCP("Isagawa Kernel")

WORKSPACE = Path("D:/my_ai_projects/project_test_repos/sr_dev_workspace")

@mcp.tool
def kernel_pipeline_status(task_folder: str = None) -> dict:
    """Query the current pipeline state — completed tasks, pending tasks, progress."""
    wf_path = WORKSPACE / ".claude/state/sr_dev_workflow.json"
    ss_path = WORKSPACE / ".claude/state/session_state.json"

    workflow = json.loads(wf_path.read_text()) if wf_path.exists() else {}
    session = json.loads(ss_path.read_text()) if ss_path.exists() else {}

    folder = task_folder or workflow.get("task_folder", "tasks/")
    task_dir = WORKSPACE / folder

    all_tasks = sorted([
        f.name for f in task_dir.glob("[0-9]*.md")
        if not f.name.startswith("000-") and f.name != "gate-contract.md"
    ]) if task_dir.exists() else []

    completed = workflow.get("completed_tasks", [])
    skipped = workflow.get("skipped_tasks", [])
    pending = [t for t in all_tasks if t not in completed and t not in skipped]

    return {
        "task_folder": folder,
        "total": len(all_tasks),
        "completed": completed,
        "pending": pending,
        "skipped": skipped,
        "progress": f"{len(completed)}/{len(all_tasks)}",
        "cycling": workflow.get("cycling", False),
        "anchored": workflow.get("anchored", False),
        "actions_since_anchor": workflow.get("actions_since_anchor", 0),
    }

if __name__ == "__main__":
    mcp.run()
```

### Claude Code Integration

Add to `.claude/settings.local.json`:
```json
{
  "mcpServers": {
    "isagawa-kernel": {
      "command": "python",
      "args": ["lib/mcp/server.py"],
      "cwd": "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
    }
  }
}
```

### Validation
1. Run `mcp.run()` — server starts on stdio
2. Test with MCP Inspector — call `kernel_pipeline_status`, verify JSON output matches state files
3. Add to Claude Code settings — verify tool appears in Claude's tool list
4. Call from a Claude session — "What's the pipeline status?" triggers the tool

## 7. Overall Recommendation: BUILD (Prototype)

**BUILD** — with these conditions:

| Condition | Rationale |
|-----------|-----------|
| Start with read-only tools only | No risk of breaking kernel state |
| Prototype with Pipeline Status first | Validates architecture, lowest effort |
| Add Attestation second | Highest-value side-effect tool; needs internal gate enforcement |
| Defer Backlog/Lessons/Gates | Lower value, add when first 2 tools prove the pattern |
| Keep run-task.sh as execution engine | MCP complements, does not replace the kernel loop |

**Why BUILD, not SKIP:**
- Development effort is trivially low (~2-3 hours to first tool)
- The kernel has no external API today — this creates one
- MCP is the industry standard (Anthropic, OpenAI, Google all support it)
- FastMCP's decorator API maps 1:1 to kernel's Python functions
- Read-only tools have zero downside risk

**Why not BUILD (full) yet:**
- Side-effect tools (attestation, backlog) need internal gate enforcement design
- Multi-workspace support needs a workspace registry pattern
- The kernel is still evolving — premature API stabilization could create backwards-compatibility burden

**Next step:** Create a backlog item for building the prototype MCP server with `kernel_pipeline_status` as the first tool.

## 8. Distribution / Productization Angle (Added 2026-07-07)

The bigger play is not internal convenience — it's distribution. Wrapping the kernel as an MCP server creates an alternative distribution channel beyond the current Claude Code harness pattern:

| Channel | How it works | Who it serves |
|---------|-------------|---------------|
| **Harness (current)** | Clone repo, use Claude Code | Claude Code users only |
| **MCP server (proposed)** | `pip install isagawa-kernel-mcp`, add to any MCP client | Cursor, ChatGPT, VS Code, CI/CD, any MCP-compatible agent |

**Why this matters for productization:**
- MCP is the universal agent protocol (Anthropic, OpenAI, Google all support it)
- Buyers don't need to adopt Claude Code — they add one MCP server config line
- Kernel governance (backlog → pipeline → attestation) becomes consumable by any agent framework
- Pricing could be per-seat MCP access or per-attestation API calls

**Key challenge:** The kernel currently depends on Claude Code's hook system for enforcement (PostToolUse, PreToolUse). Making governance work over MCP requires rearchitecting enforcement — hooks become server-side middleware instead of client-side hooks. This is a real engineering project, not a wrapper.

**Architecture gap:**
- Read-only tools (pipeline status, lesson query) work today with zero changes
- Write tools (backlog create, attestation) need server-side gate enforcement
- Execution tools (execute-pipeline, run-task) need the full hook → anchor → learn cycle reimplemented as MCP middleware
- This is essentially building a kernel runtime that doesn't depend on Claude Code internals

**Deferred until:** Distribution strategy is clarified and there's buyer demand for non-Claude-Code access to kernel capabilities.

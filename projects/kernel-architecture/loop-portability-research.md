# Loop Portability to Other AI Coding Agents — Research Report

## Executive Summary

**The loop is more portable than expected.** OpenAI Codex CLI now has hooks (stable), headless execution (`codex exec`), subagents, and MCP support — making it the closest competitor to Claude Code for kernel-style governance. Aider supports autonomous mode and shell access but lacks hooks. Cursor/Windsurf are IDE-bound and unsuitable for headless pipelines. Cline 2.0 adds headless CLI mode. The kernel's core architecture (state files + shell scripts + markdown protocols) is agent-agnostic by design — only the hook system and one-shot execution are Claude-specific. A LangChain/LangGraph port is feasible for the orchestration layer but would lose the "agent builds its own governance" self-building property.

---

## 1. Portability Matrix

### Coding Agent Capabilities (2026)

| Agent | Hooks | Headless/One-Shot | State Files | MCP | Shell Access | Portability |
|-------|-------|-------------------|-------------|-----|-------------|-------------|
| **Claude Code** | Yes (PreToolUse, PostToolUse) | Yes (`claude -p`) | Yes (read/write JSON) | Yes | Yes | **Native** |
| **OpenAI Codex CLI** | Yes (stable, config.toml) | Yes (`codex exec`) | Yes | Yes (MCP server mode) | Yes | **HIGH** |
| **Aider** | No native hooks | Partial (scripted mode) | Yes (can read/write) | No | Yes | **MEDIUM** |
| **Cline 2.0** | No hooks | Yes (headless CLI mode) | Yes | Yes | Yes | **MEDIUM** |
| **Cursor** | No hooks | No headless | Via extensions | Via extensions | Limited | **LOW** |
| **Windsurf** | No hooks | No headless | Via extensions | Via extensions | Limited | **LOW** |
| **Amazon Q Developer** | No hooks | Yes (CLI mode) | Yes | No | Yes | **MEDIUM** |
| **Continue** | No hooks | No headless | Via extensions | Yes | Limited | **LOW** |

### Portability Ranking

1. **OpenAI Codex CLI** — closest to Claude Code. Has hooks, headless, MCP, subagents. Could run the kernel with minimal adaptation.
2. **Cline 2.0** — headless CLI mode enables pipeline execution. No hooks means governance is softer (protocol-only, no hard blocks).
3. **Aider** — autonomous mode, shell access, can read/write state. Hooks would need to be external (wrapper script).
4. **Amazon Q Developer** — CLI mode works, but no hooks and limited customization.
5. **Cursor/Windsurf** — IDE-bound. Cannot run headless pipelines. Not viable for the loop.

---

## 2. Component Portability Analysis

### What's Universal (Agent-Agnostic)

| Component | Why Universal | Notes |
|-----------|-------------|-------|
| **State files** (session_state.json, workflow.json) | JSON read/write — any agent can do this | Just file I/O |
| **Protocol/lessons** (markdown files) | Any agent can read markdown | System prompt equivalent |
| **Task decomposition** | Prompt-driven — works with any LLM | The decomposition logic is in the prompt, not the tool |
| **Gate contracts** | Shell-based verification (file_exists, grep, run_code) | Any agent with bash access |
| **run-task.sh** | Bash script — orchestrates any CLI agent | Just replace `claude -p` with target agent's one-shot command |
| **Attestation** | Python scripts — any agent can run Python | Independent of agent choice |
| **Backlog items** | Markdown files with metadata | Agent-agnostic |

### What's Claude-Specific

| Component | Claude Dependency | Porting Effort |
|-----------|------------------|----------------|
| **Hook system** (PreToolUse, PostToolUse) | Claude Code's hook API with JSON stdin/stdout protocol | **HIGH** — Codex has equivalent; others need wrapper |
| **`claude -p` one-shot** | Claude Code's headless mode | **MEDIUM** — Codex has `codex exec`; Aider has `--message` flag |
| **CLAUDE.md** | Claude Code reads this at startup | **LOW** — each agent has equivalent: AGENTS.md (Codex), .cursorrules (Cursor), .aider.conf.yml |
| **Skill tool** | Claude Code's command invocation | **MEDIUM** — can be replaced with prompt injection or function calls |
| **MCP integration** | Claude Code's MCP server support | **LOW** — Codex also supports MCP; becoming standard |

### The Hard Part: Hook-Based Governance

The kernel's governance depends on hooks that:
1. **Block writes** when state is invalid (anchor not done, learn not recorded)
2. **Auto-increment** action counters
3. **Log actions** to actions.jsonl
4. **Detect test failures** and set `needs_learn`

Without hooks, governance becomes advisory (the agent reads the protocol and hopefully follows it) instead of mandatory (the hook physically blocks the action). This is the critical difference.

**Porting the hook layer:**

| Target | Hook Strategy |
|--------|--------------|
| **Codex CLI** | Native hooks in config.toml — direct port possible |
| **Aider** | Wrapper script: `pre-aider-hook.sh → aider → post-aider-hook.sh` |
| **Cline** | VS Code extension API — extension-level hooks possible but complex |
| **LangChain** | Tool wrappers: wrap every tool call in a governance function |
| **Custom agent** | Middleware layer: intercept all tool calls before/after execution |

---

## 3. OpenAI Codex CLI — Deep Analysis

### What Makes It Portable

Codex CLI (2026) is the most viable port target:

| Feature | Claude Code | Codex CLI | Compatible? |
|---------|------------|-----------|-------------|
| Hooks (pre/post tool) | PreToolUse, PostToolUse | Stable hooks in config.toml | **Yes** |
| Headless execution | `claude -p "prompt"` | `codex exec "prompt"` | **Yes** |
| One-shot mode | `-p` flag exits after response | `exec` command | **Yes** |
| Config file | CLAUDE.md | AGENTS.md + config.toml | **Yes** (rename) |
| MCP support | Built-in | Built-in (can also BE an MCP server) | **Yes** |
| Subagents | Agent tool | Native subagent workflows | **Yes** |
| Shell access | Bash tool | Shell tool | **Yes** |
| Full access mode | `--allowedTools` | `--full-access` | **Yes** |

### Porting run-task.sh to Codex

```bash
# Current (Claude Code)
claude -p "$prompt" --allowedTools "Edit,Write,Bash,Read,Glob,Grep"

# Ported (Codex CLI)
codex exec "$prompt" --full-access
```

### Estimated Porting Effort

| Component | Effort | Notes |
|-----------|--------|-------|
| run-task.sh | 1 hour | Replace `claude -p` with `codex exec` |
| CLAUDE.md → AGENTS.md | 30 min | Rename + adjust syntax |
| Hooks | 2-4 hours | Rewrite Python hooks for Codex config.toml format |
| State files | 0 | No change needed — JSON is JSON |
| Protocol/lessons | 0 | No change — markdown is markdown |
| Gate contracts | 0 | Shell-based, agent-agnostic |
| **Total** | **4-6 hours** | For a functional port |

---

## 4. LangChain/LangGraph Port

### Architecture Mapping

| Kernel Component | LangChain Equivalent |
|-----------------|---------------------|
| run-task.sh loop | AgentExecutor / LangGraph state machine |
| Task file (prompt) | Chain input / graph node |
| Hook system | Tool wrappers / middleware |
| State files | LangGraph checkpointer / custom state |
| Protocol | System prompt template |
| Lessons | Dynamic prompt injection |
| Gate contract | Custom tool with shell execution |

### LangGraph State Machine Model

LangGraph's state machine model maps well to the pipeline:

```
START → parse_backlog → decompose_tasks → [for each task: execute → verify → learn] → report → END
```

Each node is a function. State passes through as a typed dict. Checkpointing enables resume.

### What's Lost in the LangChain Port

| Feature | Status |
|---------|--------|
| Self-building (agent creates its own governance) | **Lost** — LangChain agents don't modify their own code |
| Hook enforcement (hard blocks) | **Weakened** — tool wrappers can reject, but agent can bypass |
| One-shot fresh context | **Changed** — LangGraph maintains state across nodes |
| Human readability | **Reduced** — Python code replaces markdown protocols |
| Agent-as-user (agent reads its own docs) | **Lost** — the agent doesn't introspect its own governance |

### Verdict on LangChain Port

**Feasible for orchestration, but loses the self-building property.** The kernel's power isn't just the pipeline pattern — it's that the agent builds, reads, and enforces its own governance. A LangChain port would be a governed pipeline, not a self-governing agent. Still valuable, but fundamentally different.

---

## 5. The Kernel's Portability Surface

### What Makes The Kernel Portable

The kernel's architecture is accidentally portable because:

1. **State is files** — JSON on disk, not in-memory objects
2. **Protocol is markdown** — any LLM can read it
3. **Orchestration is shell** — run-task.sh is bash, not Python
4. **Verification is mechanical** — gate contracts use grep/file_exists/run_code
5. **Lessons are text** — append to a markdown file

### What Makes It Claude-Specific

1. **Hooks API** — the exact JSON stdin/stdout protocol is Claude Code's
2. **`claude -p`** — the headless one-shot invocation pattern
3. **Tool names** — Read, Write, Edit, Bash, Glob, Grep are Claude Code tool names
4. **CLAUDE.md** — the config file convention

### The Abstraction Layer

To make the kernel truly agent-agnostic, extract:

```
kernel-core/
├── state/          # JSON state management (agent-agnostic)
├── protocol/       # Markdown protocol files (agent-agnostic)
├── hooks/          # Abstract hook interface (agent-specific adapters)
│   ├── interface.py
│   ├── claude_adapter.py
│   ├── codex_adapter.py
│   └── aider_adapter.py
├── tasks/          # Task decomposition (agent-agnostic)
├── gates/          # Gate contract verification (shell-based)
└── run-task.sh     # Orchestrator (parameterized by agent command)
```

The only agent-specific code would be in `hooks/` adapters and the `AGENT_CMD` variable in run-task.sh.

---

## 6. Recommended Strategy

### Phase 1: Codex Port (Proof of Concept)
1. Fork the kernel
2. Replace `claude -p` with `codex exec` in run-task.sh
3. Rewrite hooks for Codex config.toml format
4. Rename CLAUDE.md → AGENTS.md
5. Run a simple pipeline end-to-end
6. **Effort: 4-6 hours, 1 day**

### Phase 2: Abstract Hook Layer
7. Define a hook interface (Python ABC)
8. Write Claude adapter (current hooks)
9. Write Codex adapter
10. Parameterize run-task.sh with `AGENT_CMD` env var
11. **Effort: 8-16 hours, 2-3 days**

### Phase 3: LangGraph Orchestrator (Optional)
12. Build LangGraph state machine for the pipeline
13. Use existing state files as checkpoints
14. Tool wrappers for governance
15. **Effort: 20-40 hours, 1-2 weeks**
16. **Value: Lower than Phases 1-2** — loses self-building property

### Decision

| Option | Effort | Value | Recommendation |
|--------|--------|-------|----------------|
| Codex CLI port | 1 day | HIGH — proves portability | **Do first** |
| Abstract hook layer | 2-3 days | HIGH — enables multi-agent | Do second |
| LangGraph port | 1-2 weeks | MEDIUM — different product | Defer |
| Cursor/Windsurf port | N/A | LOW — not viable | Skip |
| Aider port | 2-3 days | MEDIUM — large user base | Consider after Codex |

**Bottom line:** The kernel is 80% portable today. The remaining 20% (hooks + one-shot command) requires adapters per target agent. Codex CLI is the first port target — it has native equivalents for every Claude Code feature the kernel uses. A successful Codex port proves the kernel is a universal agent governance framework, not a Claude-only product.

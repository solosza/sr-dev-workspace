# Claude Code Named Agents — Spec Summary

**Source:** [Create custom subagents — Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
**Date:** 2026-06-01

---

## YAML Frontmatter Fields

Every subagent is a Markdown file. YAML frontmatter = configuration; body = system prompt.

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier (lowercase + hyphens). Hooks receive this as `agent_type` |
| `description` | Yes | When Claude should delegate to this subagent |
| `tools` | No | Allowlist of tools. Inherits all if omitted |
| `disallowedTools` | No | Denylist — removed from inherited/specified list |
| `model` | No | `sonnet`, `opus`, `haiku`, full model ID (e.g. `claude-opus-4-8`), or `inherit`. Default: `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | Max agentic turns before the subagent stops |
| `skills` | No | Skills to preload into context at startup (full content injected) |
| `mcpServers` | No | MCP servers — inline definitions or string references to configured servers |
| `hooks` | No | Lifecycle hooks scoped to this subagent (`PreToolUse`, `PostToolUse`, `Stop`) |
| `memory` | No | Persistent memory scope: `user`, `project`, or `local` |
| `background` | No | `true` to always run as background task. Default: `false` |
| `effort` | No | Effort level override: `low`, `medium`, `high`, `xhigh`, `max` |
| `isolation` | No | Set to `worktree` for git worktree isolation (isolated repo copy) |
| `color` | No | Display color: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` |
| `initialPrompt` | No | Auto-submitted as first user turn when running as main session agent (via `--agent`) |

### Example file

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. Analyze code and provide actionable feedback.
```

---

## Tool Restriction Mechanism

- **Allowlist (`tools`):** Only listed tools are available. Omit to inherit all parent tools.
- **Denylist (`disallowedTools`):** Inherits everything except denied tools.
- **Precedence:** `disallowedTools` applied first, then `tools` resolved against remaining pool.
- **Subagent-specific restrictions:** `Agent(type1, type2)` syntax limits which subagents can be spawned (only applies when running as main thread via `--agent`).

**Tools NOT available to subagents (even if listed):**
- `Agent` (subagents cannot spawn other subagents)
- `AskUserQuestion`
- `EnterPlanMode`
- `ExitPlanMode` (unless `permissionMode: plan`)
- `ScheduleWakeup`
- `WaitForMcpServers`

---

## Model Routing

Resolution order (highest priority first):
1. `CLAUDE_CODE_SUBAGENT_MODEL` environment variable
2. Per-invocation `model` parameter (Claude chooses at delegation time)
3. Subagent definition's `model` frontmatter field
4. Main conversation's model (inherit)

Aliases: `sonnet`, `opus`, `haiku`. Full model IDs also accepted (e.g. `claude-sonnet-4-6`).

---

## Auto-Delegation

Claude automatically delegates based on:
- Task description in user's request
- `description` field in subagent configurations
- Current context and available tools

**Encouraging delegation:** Include "use proactively" in the description field.

**Preventing delegation:** Add `Agent(subagent-name)` to `permissions.deny` in settings, or use `--disallowedTools "Agent(name)"`.

---

## Invocation Methods

| Method | Behavior |
|--------|----------|
| **Auto-delegation** | Claude matches task to subagent description automatically |
| **Natural language** | Name the subagent in prompt: "Use the test-runner subagent to..." |
| **@-mention** | Type `@` and pick subagent — guarantees that subagent runs |
| **`--agent <name>`** | Whole session uses that subagent's system prompt, tools, and model |
| **`agent` setting** | Set in `.claude/settings.json` to make it default for all sessions |

When using `--agent`, the subagent's system prompt replaces the default Claude Code system prompt entirely. CLAUDE.md and project memory still load.

---

## Isolation Model

### Context Window
- **Fresh context:** Each subagent starts with a completely fresh 200K-token context window.
- **No inheritance:** Does NOT see parent conversation history, previously invoked skills, or files already read.
- **Task message only:** Claude composes a delegation message summarizing the task; subagent works from there.
- **Exception:** Fork mode (`fork: true`) inherits the parent conversation instead of starting fresh.

### What loads at startup (non-fork)
1. **System prompt** — agent's own prompt + environment details (NOT full Claude Code system prompt)
2. **Task message** — delegation prompt from Claude
3. **CLAUDE.md + memory** — full memory hierarchy (except Explore and Plan agents skip this)
4. **Git status** — snapshot from parent session start (Explore and Plan skip this)
5. **Preloaded skills** — full content of skills listed in `skills` field

### Worktree isolation (`isolation: worktree`)
- Runs subagent in a temporary git worktree
- Isolated copy of the repository, branched from default branch (not parent's HEAD)
- Worktree auto-cleaned up if subagent makes no changes

### Background vs Foreground
- **Foreground:** Blocks main conversation. Permission prompts passed through.
- **Background:** Concurrent. Uses already-granted permissions. Auto-denies prompts that would need user input.

---

## Placement (Global vs Project)

| Location | Scope | Priority |
|----------|-------|----------|
| Managed settings | Organization-wide | 1 (highest) |
| `--agents` CLI flag | Current session only | 2 |
| `.claude/agents/` | Current project | 3 |
| `~/.claude/agents/` | All user projects | 4 |
| Plugin `agents/` directory | Where plugin enabled | 5 (lowest) |

- **Project agents** (`.claude/agents/`): Specific to codebase. Check into version control.
- **User agents** (`~/.claude/agents/`): Personal, available in all projects.
- **Recursive scanning:** Both directories scanned recursively; subdirectory path doesn't affect identity.
- **Name collision:** Same name in one scope = one kept silently. Higher-priority scope wins across scopes.

---

## Persistent Memory

| Scope | Location | Use case |
|-------|----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | Cross-project learnings |
| `project` | `.claude/agent-memory/<name>/` | Project-specific, shareable via VCS |
| `local` | `.claude/agent-memory-local/<name>/` | Project-specific, not committed |

When enabled: system prompt includes memory instructions + first 200 lines / 25KB of `MEMORY.md`. Read/Write/Edit tools auto-enabled.

---

## Hooks Integration

### In subagent frontmatter
- `PreToolUse` — validate before tool execution (e.g., block SQL writes)
- `PostToolUse` — run after tool execution (e.g., linting)
- `Stop` — converted to `SubagentStop` at runtime

### In settings.json (project-level)
- `SubagentStart` — fires when subagent begins (matcher: agent type name)
- `SubagentStop` — fires when subagent completes

---

## Key Constraints and Gaps

1. **No nesting:** Subagents cannot spawn other subagents.
2. **No parent context:** Subagents don't see parent conversation history (except forks).
3. **Plugin limitations:** Plugin subagents ignore `hooks`, `mcpServers`, `permissionMode`.
4. **Loaded at session start:** File-based subagents require restart if edited on disk. `/agents` UI changes take effect immediately.
5. **Background auto-deny:** Background subagents auto-deny any permission prompt, which can cause failures.
6. **cd behavior:** `cd` doesn't persist between tool calls within a subagent, and doesn't affect main conversation.

---

## Built-in Subagents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| **Explore** | Haiku | Read-only | File discovery, code search (skips CLAUDE.md + git status) |
| **Plan** | Inherit | Read-only | Codebase research for plan mode (skips CLAUDE.md + git status) |
| **General-purpose** | Inherit | All | Complex multi-step tasks requiring both exploration and action |
| **statusline-setup** | Sonnet | - | Configure status line |
| **claude-code-guide** | Haiku | - | Answer Claude Code feature questions |

---

## Sources

- [Create custom subagents — Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Subagents Guide — Medium](https://medium.com/@sathishkraju/claude-code-subagents-the-complete-guide-to-ai-agent-delegation-d0a9aba419d0)
- [Subagents in the SDK — Claude Code Docs](https://code.claude.com/docs/en/agent-sdk/subagents)

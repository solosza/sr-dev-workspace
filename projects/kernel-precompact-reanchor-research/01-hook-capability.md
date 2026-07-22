# Hook Capability — PreCompact Re-Anchor Research

## Installed Version

Claude Code **2.1.207** — verified via `claude --version`.

## Supported Hook Event Types (30 total)

Claude Code 2.1.207 supports 30 hook event types across the full agent lifecycle:

| Category | Events |
|----------|--------|
| Session | `SessionStart`, `Setup`, `SessionEnd` |
| User Input | `UserPromptSubmit`, `UserPromptExpansion` |
| Tool Lifecycle | `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied` |
| Agent Lifecycle | `SubagentStart`, `SubagentStop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted` |
| Response | `Stop`, `StopFailure`, `MessageDisplay`, `Notification` |
| Compaction | **`PreCompact`**, **`PostCompact`** |
| Configuration | `ConfigChange`, `InstructionsLoaded`, `CwdChanged`, `FileChanged` |
| Worktree | `WorktreeCreate`, `WorktreeRemove` |
| MCP | `Elicitation`, `ElicitationResult` |

## PreCompact Hook

**When it fires:** Just before Claude Code compacts (summarizes) older conversation turns to reduce token usage.

**Matchers:** `manual` (user invokes `/compact`) or `auto` (automatic compaction triggered by approaching context limit).

**Payload (JSON via stdin):**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/directory",
  "hook_event_name": "PreCompact",
  "source": "manual" | "auto",
  "estimated_token_reduction": 5000,
  "current_turn_count": 42
}
```

**Output capabilities:**
- **Can block compaction** — exit code 2 with `decision: "block"` + `reason` prevents compaction entirely
- **Cannot inject content into the compacted summary** — `additionalContext` in `hookSpecificOutput` is NOT carried into the post-compaction context
- **Side effects only** — can write state files, trigger notifications, persist context externally

**Critical limitation:** PreCompact is a side-effect hook, not a content-injection hook. It can persist state (e.g., write `session_state.json`) before compaction erases the conversation, but it cannot ensure that content appears in the compacted summary itself.

## PostCompact Hook

**When it fires:** After compaction completes successfully.

**Matchers:** `manual` or `auto` (same as PreCompact).

**Payload (JSON via stdin):**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/directory",
  "hook_event_name": "PostCompact",
  "source": "manual" | "auto",
  "tokens_removed": 5000,
  "remaining_turns": 15,
  "summary_length": 2500
}
```

**Output capabilities:** Side-effects only. Cannot modify or append to the compacted summary. Cannot inject context. Intended for logging, cleanup, and metrics.

## SessionStart with `source: "compact"` — The Intended Re-Injection Mechanism

The **designed** path for injecting context after compaction is `SessionStart` with `matcher: "compact"`. The SessionStart hook fires on: `startup`, `resume`, `clear`, `compact`, and `fork`. When matched on `compact`, it fires after compaction completes and its stdout should be injected into Claude's context as fresh information.

**Known bug (GitHub issue #15174, closed as duplicate):** SessionStart hooks with `compact` matcher execute successfully but their stdout output is **not injected into Claude's context**. The hook runs, the script produces output, but the output is silently discarded. This is a documented, unresolved bug as of Claude Code 2.1.207. The workaround cited in the issue is adding critical content to `CLAUDE.md` instead (since CLAUDE.md is auto-loaded after compaction), which defeats the purpose of the hook.

## One-Shot Agent Behavior (`claude -p`)

Both `PreCompact` and `PostCompact` fire in one-shot/print mode (`claude -p`). However, practical relevance is limited:

- One-shot agents typically have shorter lifespans and may not reach the context limit that triggers auto-compaction
- If a one-shot agent does hit the context limit, auto-compaction fires and PreCompact/PostCompact execute
- The kernel's one-shot agents (via `run-task.sh`) execute single tasks and rarely approach compaction thresholds
- For long-running one-shot agents (e.g., complex research tasks), compaction could occur and these hooks would fire

## Summary of Capabilities for Re-Anchoring

| Mechanism | Can Trigger on Compaction | Can Inject Context | Can Block | Status |
|-----------|--------------------------|-------------------|-----------|--------|
| PreCompact | Yes | **No** — side effects only | Yes | Working |
| PostCompact | Yes | **No** — side effects only | No | Working |
| SessionStart (compact) | Yes | **Intended yes, actually no** | No | Bugged (#15174) |
| CLAUDE.md auto-load | Yes (always loaded) | **Yes** — survives compaction | N/A | Working |
| InstructionsLoaded (compact) | Yes | Side effects only | No | Working |

The only reliable mechanism for content injection after compaction is CLAUDE.md, which is auto-discovered and loaded into every turn including post-compaction turns.

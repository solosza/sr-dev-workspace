# Enforcement Loop

The step-by-step flow of how the Isagawa Kernel enforces protocol compliance on every agent action. Shows what happens when the agent writes, edits, or runs commands — and how the system self-corrects on failure.

**Audience:** Implementation practitioners

```mermaid
flowchart TD
    START["Agent Performs Action<br/>(Write / Edit / Bash)"] --> PRE_HOOK

    subgraph "Hook Interception (PreToolUse)"
        PRE_HOOK["PreToolUse Hook Fires"]
        PRE_HOOK --> CHECK_ANCHOR{"Anchored?"}
        CHECK_ANCHOR -->|No| BLOCK_ANCHOR["BLOCKED<br/>Must invoke /kernel/anchor"]
        CHECK_ANCHOR -->|Yes| CHECK_LEARN{"needs_learn?"}
        CHECK_LEARN -->|Yes| BLOCK_LEARN["BLOCKED<br/>Must invoke /kernel/learn"]
        CHECK_LEARN -->|No| CHECK_DOMAIN{"Domain Gate<br/>Passes?"}
        CHECK_DOMAIN -->|No| BLOCK_DOMAIN["BLOCKED<br/>Domain-specific violation"]
        CHECK_DOMAIN -->|Yes| ALLOW["ALLOWED<br/>Action proceeds"]
    end

    BLOCK_ANCHOR --> FIX_ANCHOR["/kernel/anchor<br/>Re-read protocol + lessons<br/>Review inter-anchor work"]
    FIX_ANCHOR --> START
    BLOCK_LEARN --> FIX_LEARN["/kernel/learn<br/>Record lesson from failure<br/>Update hooks if needed"]
    FIX_LEARN --> START
    BLOCK_DOMAIN --> FIX_DOMAIN["Fix violation per<br/>domain protocol"]
    FIX_DOMAIN --> START

    ALLOW --> EXECUTE["Action Executes"]

    subgraph "Hook Tracking (PostToolUse)"
        EXECUTE --> POST_HOOK["PostToolUse Hook Fires"]
        POST_HOOK --> LOG_ACTION["Actions Log Appender<br/>Append to actions.jsonl"]
        POST_HOOK --> INCREMENT["Increment<br/>actions_since_anchor"]
        POST_HOOK --> CHECK_TEST{"Test command<br/>failed?"}
        CHECK_TEST -->|Yes| SET_LEARN["Set needs_learn = true<br/>(Test Failure Detector)"]
        CHECK_TEST -->|No| CHECK_LIMIT{"Counter >=<br/>actions_limit?"}
    end

    SET_LEARN --> NEXT_ACTION
    CHECK_LIMIT -->|Yes| SET_UNANCHOR["Set anchored = false<br/>Next action will be blocked"]
    CHECK_LIMIT -->|No| NEXT_ACTION["Next Action"]
    SET_UNANCHOR --> NEXT_ACTION

    NEXT_ACTION --> START

    subgraph "Completion Gate"
        DONE["/kernel/complete"] --> FINAL_CHECK{"All acceptance<br/>criteria met?"}
        FINAL_CHECK -->|Yes| COMPLETE["Task Complete<br/>Move to next task"]
        FINAL_CHECK -->|No| BACK_TO_WORK["Back to work loop"]
        BACK_TO_WORK --> START
    end

    style BLOCK_ANCHOR fill:#8b1a1a,stroke:#cd3333,color:#fff
    style BLOCK_LEARN fill:#8b1a1a,stroke:#cd3333,color:#fff
    style BLOCK_DOMAIN fill:#8b1a1a,stroke:#cd3333,color:#fff
    style ALLOW fill:#2d5016,stroke:#4a8c2a,color:#fff
    style COMPLETE fill:#2d5016,stroke:#4a8c2a,color:#fff
    style FIX_ANCHOR fill:#1a3a5c,stroke:#2a6496,color:#fff
    style FIX_LEARN fill:#1a3a5c,stroke:#2a6496,color:#fff
```

## How It Works

1. **Every action intercepted** — Write, Edit, and Bash all trigger PreToolUse hooks before execution
2. **Three-gate check** — anchored? → needs_learn clear? → domain gates pass?
3. **Block with guidance** — blocked actions tell the agent exactly what command to run to unblock
4. **Post-action tracking** — every action logged, counter incremented, test failures detected
5. **Self-correcting** — failures trigger `/kernel/learn` which updates hooks and protocol to prevent recurrence
6. **Periodic re-centering** — every N actions, the anchor forces a full protocol re-read and work review

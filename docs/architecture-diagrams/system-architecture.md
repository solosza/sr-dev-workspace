# System Architecture

How all Isagawa Kernel components connect. The kernel is a self-building, self-improving agent framework where the Domain Spec is the source of truth, hooks enforce compliance, and lessons drive continuous improvement.

**Audience:** Architects, technical leads

```mermaid
graph TD
    CLAUDE["CLAUDE.md<br/>(Entry Point)"] -->|loads| KERNEL["Isagawa Kernel"]

    KERNEL -->|reads| PROTOCOL["Domain Spec / Protocol<br/>(Source of Truth)"]
    KERNEL -->|invokes| COMMANDS["Commands"]
    KERNEL -->|enforced by| HOOKS["Hooks"]
    KERNEL -->|uses| SKILLS["Skills"]
    KERNEL -->|reads/writes| STATE["State"]

    subgraph "Commands"
        CMD_SS["session-start"]
        CMD_AN["anchor"]
        CMD_LN["learn"]
        CMD_CP["complete"]
        CMD_FX["fix"]
        CMD_BL["backlog"]
    end

    subgraph "Hooks (Gate Enforcement)"
        HOOK_UGE["Universal Gate Enforcer<br/>(PreToolUse)"]
        HOOK_DGE["Domain Gate Enforcer<br/>(PreToolUse)"]
        HOOK_ALA["Actions Log Appender<br/>(PostToolUse)"]
        HOOK_TFD["Test Failure Detector<br/>(PostToolUse)"]
    end

    subgraph "Skills (Autonomous Capabilities)"
        SK_TB["Task Builder"]
        SK_EP["Execute Pipeline"]
        SK_AC["Autonomous Cycling"]
        SK_PT["Prod Test"]
        SK_DS["Domain Setup"]
    end

    subgraph "State (Persistent)"
        ST_SS["session_state.json"]
        ST_WF["workflow.json"]
        ST_AL["actions.jsonl"]
    end

    subgraph "Self-Improvement Loop"
        LESSONS["lessons.md<br/>(Cheat Sheet)"]
        PROTOCOL -->|informs| LESSONS
        LESSONS -->|updates| HOOKS
        LESSONS -->|updates| PROTOCOL
    end

    HOOKS -->|blocks/allows| AGENT_ACTION["Agent Action<br/>(Write / Edit / Bash)"]
    HOOK_ALA -->|appends to| ST_AL
    HOOK_TFD -->|sets needs_learn| ST_SS

    CMD_AN -->|re-reads| PROTOCOL
    CMD_AN -->|re-reads| LESSONS
    CMD_AN -->|reviews| ST_AL
    CMD_LN -->|updates| LESSONS
    CMD_CP -->|validates| STATE

    SK_EP -->|orchestrates| SK_TB
    SK_TB -->|decomposes into| TASKS["Task Files"]
    SK_AC -->|cycles through| TASKS

    style PROTOCOL fill:#2d5016,stroke:#4a8c2a,color:#fff
    style HOOKS fill:#8b1a1a,stroke:#cd3333,color:#fff
    style LESSONS fill:#1a3a5c,stroke:#2a6496,color:#fff
    style KERNEL fill:#333,stroke:#666,color:#fff
```

## Key Relationships

| From | To | Relationship |
|------|-----|-------------|
| CLAUDE.md | Kernel | Loads the kernel into every session |
| Domain Spec | Protocol | Defines rules, patterns, anti-patterns for a domain |
| Hooks | Agent Actions | Block non-compliant actions before execution |
| Actions Log | Anchor | Reviewed every 10 actions for protocol compliance |
| Test Failures | Learn | Trigger mandatory lesson recording |
| Lessons | Hooks + Protocol | Updated after failures to prevent recurrence |
| Task Builder | Task Files | Decomposes goals into atomic, verifiable tasks |
| Execute Pipeline | Task Builder + Cycling | Orchestrates the full backlog-to-done flow |

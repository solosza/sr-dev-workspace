# Agent Orchestration Framework — Architecture

## Overview

The framework orchestrates autonomous agent execution through a three-phase loop:

```
Phase 1: PLAN          Phase 2: EXECUTE       Phase 3: VERIFY
─────────────────      ──────────────────     ────────────────
Backlog item     →→→   Decompose into    →→→  Run in isolated
(user intent)         atomic tasks           environment
                      (task-builder)         (run-task.sh)
                                                    ↓
                                             Results feed back
                                             to state, next task
```

## Autonomy Contract

The framework is **autonomous by design**. Key properties:

| Property | Meaning | Implication |
|----------|---------|-------------|
| **No pauses** | Agent never stops between tasks to ask user for confirmation | Cycling is uninterrupted; errors trigger recovery, not human intervention |
| **State-driven** | Behavior determined by gate contracts in state, not code logic | Tokens, flags, and schemas control flow; code just reads state and acts |
| **Error recovery** | Failures are recorded but don't halt the loop | Task can be retried 3x, then skipped; cycling continues |
| **Self-reporting** | Results logged to state files; user reviews after completion | No real-time logging; final report generated at end |

## The Loop — Three Layers

### Layer 1: Commands (Entry Points)

Commands are the **top-level entry points**. Each command is a verb (backlog, execute-pipeline, complete, learn, etc.) that the user invokes once. The command is responsible for:

1. Parsing user input
2. Setting up initial state
3. Delegating to skills
4. Reporting results

**Examples:** `/kernel/backlog`, `/kernel/execute-pipeline`, `/kernel/complete`

**Structure:**
```
.claude/commands/
├── kernel/
│   ├── backlog.md                    ← Create backlog item
│   ├── execute-pipeline.md           ← Execute a backlog item (orchestration entry point)
│   ├── complete.md                   ← Mark work done, handle cycling
│   ├── learn.md                      ← Record lesson after failure
│   └── [other commands]
└── domain/
    ├── custom-orchestration.md       ← Project-specific command
    └── [domain-specific commands]
```

### Layer 2: Skills (Orchestrators)

Skills are **multi-step orchestrators** that handle complex workflows. Each skill is decomposed into numbered steps (01, 02, 03...) with clear phase boundaries.

**Key characteristics:**
- Each step has a single responsibility
- Step files are referenced by index from SKILL.md (never duplicated inline)
- Steps may delegate to sub-skills
- State transitions happen at phase boundaries (gate contracts)

**Examples:** task-builder (decomposes goal into atomic tasks), execute-pipeline (runs tasks via run-task.sh)

**Structure:**
```
.claude/skills/
├── execute-pipeline/
│   ├── SKILL.md                       ← Identity, step table, entry point
│   └── references/
│       ├── step-01-parse.md
│       ├── step-02-research.md
│       ├── step-03-task-decompose.md
│       └── [steps...]
├── task-builder/
│   ├── SKILL.md
│   └── references/
│       ├── step-01-parse-goal.md
│       └── [steps...]
└── [other skills]
```

### Layer 3: References (Pattern Libraries)

References are **documentation of patterns and schemas**. They don't execute; they inform how the system should behave.

**Examples:** protocol patterns, code quality guidelines, anti-patterns, data schemas, gate-contract templates

**Structure:**
```
.claude/references/
├── core-philosophy.md                ← Why the system exists
├── agent-autonomy.md                 ← Autonomy assumptions
├── gate-contract-template.md         ← Schema for phase boundaries
├── data-schema-patterns.md           ← State file structure patterns
├── cycling-behavior.md               ← Autonomous loop rules
└── [domain-specific references]
```

## Data Contracts (Gate Contracts)

Gate contracts are **JSON schemas that define what must be true** at each phase boundary. They act as contracts between phases:

- **Input gate:** validates state before a phase starts
- **Output gate:** validates state after a phase ends
- **Recovery gate:** defines what data to preserve if a phase fails

**Example:**
```json
{
  "phase": "execute-pipeline/step-02-research",
  "input_gate": {
    "required_fields": ["backlog_path", "task_folder"],
    "validations": [
      "backlog_path must exist",
      "is_backlog_complex: boolean"
    ]
  },
  "output_gate": {
    "required_fields": ["research_complete", "deliverable_list"],
    "validations": ["deliverable_list length > 0"]
  },
  "recovery_gate": {
    "preserve": ["backlog_path", "backlog_content"],
    "rollback_action": "restore to input_gate state"
  }
}
```

## State Files — The Loop's Memory

State files are JSON objects that track progress, decisions, and results. Three levels:

| File | Scope | Purpose |
|------|-------|---------|
| `session_state.json` | Entire session | Current task, prior context, pending tokens |
| `{domain}_workflow.json` | Domain + task batch | Actions counter, anchor state, cycling progress |
| Task-specific state | Individual task | Attempts, results, gate contract validation |

The loop reads these files to decide what to do next. No hardcoded logic; all behavior is data-driven.

## Execution Model — Run-Task.sh Spawned Agents

When a task executes, the framework spawns a **background agent** (decoupled subprocess) that runs:

```bash
env -u CLAUDECODE bash run-task.sh [task_repo] [iterations] [subfolder]
```

This agent:
1. Reads the task file
2. Executes task steps
3. Runs tests if specified
4. Reports results back to state files
5. Exits (parent process continues to next task)

**Why isolated?** Each task is sandboxed. If a task fails, it doesn't corrupt the parent's session or block the loop.

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ Command: /kernel/execute-pipeline [backlog-number]              │
└────────────────────────┬────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│ Skill: execute-pipeline (orchestrator)                          │
│ Step 1: Parse backlog item                                      │
│ Step 2: Research (gather context)                              │
│ Step 3: Decompose (use task-builder to create N tasks)         │
│ Step 4: Gate check (verify task outputs match contracts)       │
│ Step 5: Run tasks (spawn background agents, collect results)   │
│ Step 6: Report (generate validation summary)                   │
└────────────────────┬──────────┬──────────────────────────────────┘
                     ↓          ↓
        ┌────────────────┐  ┌─────────────────┐
        │ Skill: task-   │  │ Gate Contracts  │
        │ builder        │  │ validate each   │
        │ (decompose)    │  │ phase output    │
        └────────────────┘  └─────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│ For each task:                                                   │
│   Spawn: background Agent running run-task.sh                  │
│   Wait for completion                                          │
│   Read task results from state files                           │
│   Log to action audit trail                                    │
└─────────────────────────────────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│ Command: /kernel/complete (after all tasks done or skipped)    │
│ - Mark backlog item complete                                   │
│ - Generate final report                                        │
│ - Next cycle (if multi-backlog run)                           │
└─────────────────────────────────────────────────────────────────┘
```

## Key Assumptions

1. **Agent never pauses** — No user input during autonomous execution (except initial command)
2. **Tasks are atomic** — One task, one action; tasks don't spawn sub-tasks
3. **Errors don't halt** — Failed task retried 3x, then skipped; loop continues
4. **State is authoritative** — Behavior determined by state files, not code logic
5. **References guide, don't enforce** — Protocols and lessons are soft constraints; gates enforce hard ones
6. **Isolation by design** — Each spawned agent is sandboxed; parent session unaffected

## Comparison to Kernel

The framework extracts the core orchestration loop but **removes kernel dependencies**:

| Aspect | Kernel | Framework |
|--------|--------|-----------|
| Domain protocol | Required (`sr_dev-protocol.md`) | Optional (framework works without it) |
| Hooks enforcement | Yes (gate-enforcer, actions-log-appender) | Movable (hooks are reference implementations) |
| Lessons system | Integrated (`lessons.md`) | Template provided |
| Commands | Kernel-specific | Generic command templates provided |
| Skills | Kernel-specific | Generic skill templates provided |

**Result:** Framework is the orchestration engine. Kernel is one **instance** of the framework configured for AI agent development.

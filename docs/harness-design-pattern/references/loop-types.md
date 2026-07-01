# Loop Types

A **loop** is a complete command → skill → steps → references structure.

## Orchestrator Loops

**Definition:** Calls multiple skills sequentially. Coordinates a domain workflow.

**Example:** `/reddit-pain/analyze` — Orchestrates: validate subreddit → fetch posts → analyze text → generate results

**Pattern:**
```
User invokes → Command reads → Command calls skill 1 → Skill 1 executes →
Command calls skill 2 → Skill 2 executes → Command calls skill 3 →
Skill 3 executes → Command returns results
```

**Structure:**
```
.claude/commands/reddit-pain/analyze.md
(no single skill; command orchestrates multiple skills)
```

**Use case:** Complex multi-phase workflows where each phase is a distinct domain task.

---

## Primitive Loops

**Definition:** Self-contained execution with own steps. Can be called by orchestrator loops or invoked directly by user.

**Canonical example:** `/spawn-subagent [description]` — Spawns a background agent autonomously

**Pattern:**
```
User invokes → Command reads → Skill executes steps 1-4 → Skill returns results
```

**Structure:**
```
.claude/commands/spawn-subagent.md
.claude/skills/spawn-subagent/
├── SKILL.md
└── references/
    ├── step-01-...md
    ├── step-02-...md
    ├── step-03-...md
    ├── step-04-...md
    └── error-handling.md
```

**Characteristics:**
- Self-contained (doesn't call other skills)
- Composable (can be called by orchestrators)
- Modular (can be moved/reused)
- Non-blocking (returns control immediately, executes in background or completes fast)

**Use cases:**
- Standalone utilities (spawn agents, create backlog items, etc.)
- Reusable components that orchestrators call repeatedly
- Tasks that don't fit into larger workflows
- Background execution (spawn-subagent pattern)

---

## Comparison

| Aspect | Orchestrator | Primitive |
|--------|--------------|-----------|
| Skill complexity | Coordinates multiple skills | Single, self-contained skill |
| Entry point | Command only | Command only |
| Reusability | High (orchestrates via commands) | High (can be called by other commands) |
| Autonomy | Coordinates autonomously | Executes autonomously |
| Use case | Domain workflows | Domain utilities |
| Example | `/reddit-pain/analyze` | `/spawn-subagent` |

---

## When to Use Each

### Use Orchestrator Loops When:

- Workflow has 3+ distinct phases (data pipeline, analysis, output)
- Each phase is a separate domain task
- Phases depend on each other (phase 2 uses output of phase 1)
- You need to coordinate multiple autonomous skills

### Use Primitive Loops When:

- Task is self-contained and atomic
- Can be reused by multiple orchestrators
- Doesn't require coordination with other skills
- Utility-like behavior (background spawn, state update, etc.)

---

*Both loop types follow the same architecture (Commands → Skills → Steps → References) and validation patterns (gate contracts, soft/hard gates).*

# Key Insights

Core principles and comparisons.

## Core Principle

**The harness IS the specification. The agent IS the runtime.**

This is fundamentally different from traditional software architecture.

---

## Why Harnesses Are Different

### Traditional Apps (Code-First)

```
Code → Build → Deploy → Run → Output
       (compiled, binary)
```

**Problems:**
- Complex deployment
- Version management
- Library dependencies
- Runtime errors

### Harnesses (Specification-First)

```
Markdown spec → Agent reads → Agent executes → Output
               (interpreted, human-readable)
```

**Benefits:**
- No compilation
- No dependencies
- Human-readable instructions
- Agent can re-read and adjust
- Changes are tracked via git diff

---

## Loops Are the Fundamental Unit

Not functions, classes, or services — **loops**.

A loop is:
- Command entry point
- Skill specification
- Steps (numbered actions)
- References (detailed instructions)
- All in one cohesive unit

**This enables:**
- Clear ownership (one person owns one loop)
- Reusability (compose loops)
- Testing (each loop can be tested independently)
- Portability (move entire folder)

---

## Defense in Depth

### Soft Gates
- Protocol guidelines
- Lessons learned
- Agent self-enforcement

### Hard Gates
- Hooks block operations
- Prevent violations
- Mechanical enforcement

**Both layers work together:**
- Soft gates guide behavior
- Hard gates catch violations
- Violations → lessons → guide future behavior
- Positive feedback loop

---

## Autonomous Execution

Harnesses run **autonomously without pauses:**

```
Agent reads spec → Executes steps → Validates gates → Updates state → Continues
(no user input, no polls, no waiting)
```

**Not:**
```
❌ Agent pauses for user confirmation
❌ Agent checks status and reports
❌ Agent polls external APIs
```

---

## Immutable Deliverables

Final outputs (JSON, Markdown) are generated from state:

```
State file → Rendered as JSON (for machines)
          → Rendered as Markdown (for humans)
```

**Benefits:**
- Single source of truth (state)
- Two renderings (JSON + Markdown)
- No manual sync needed
- Both always consistent

---

## Composition Model

```
Orchestrator loop
  ├─ Calls skill 1 (sequential)
  ├─ Calls skill 2 (sequential)
  └─ Calls skill 3 (sequential)

OR

Orchestrator loop
  ├─ Calls primitive loop 1 (non-blocking)
  ├─ Calls primitive loop 2 (non-blocking)
  └─ Calls primitive loop 3 (non-blocking)
     [all run in parallel]
```

---

## Comparison to Other Architectures

### vs. REST APIs

```
REST API:
User → POST /analyze → Server → Queue → Worker → Return status
     (async, polling required)
     (user must check /status repeatedly)

Harness:
User → /analyze command → Agent orchestration → Return results
     (autonomous, non-blocking)
     (agent runs to completion, returns all results)
```

### vs. Microservices

```
Microservices:
Service 1 → Service 2 → Service 3 → Results
(network calls, versioning, deployment)
(complex debugging, hard to trace)

Harness:
Skill 1 → Skill 2 → Skill 3 → Results
(local orchestration, markdown spec)
(easy debugging, pure text tracing)
```

### vs. Task Queues

```
Task Queue:
User → Enqueue task → Background worker → Update DB → User polls
(async, requires DB, polling)
(eventual consistency)

Harness:
User → /spawn-subagent → Agent runs background → Returns agent_id
(async, no DB, user can check progress)
(immediate status updates)
```

---

## Zero Code Philosophy

**No runtime code means:**

✅ No dependencies to manage
✅ No compilation step
✅ No build pipeline
✅ No deployment complexity
✅ No version conflicts
✅ Git-native (pure text changes)

**How is it possible?**

- Agent interprets markdown
- Agent calls available tools (Bash, LLM, web fetch, etc.)
- Gates validate correctness
- Lessons prevent bad patterns
- Hooks enforce rules mechanically

---

## Scalability

Harnesses scale through **composition**:

```
1 loop → Works
3 loops → Compose into orchestrator → Works
100 loops → Compose orchestrators → Works
```

Each loop is:
- Independent (works on its own)
- Composable (can be called by others)
- Testable (can be validated in isolation)
- Portable (entire folder can move)

---

## The Vision

**Specification-first, agent-driven orchestration.**

Write once in markdown, run everywhere via agent interpretation.

No code, no deployment, no dependencies.

Just:
- Clear specifications (markdown)
- Validation rules (JSON gates)
- Behavioral lessons (markdown)
- Mechanical enforcement (hooks)

The agent is the orchestrator, the harness is the specification, and both live in git.

---

*This is the foundation for all Isagawa harnesses.*

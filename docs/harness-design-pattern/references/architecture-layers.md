# Architecture Layers

All harnesses follow the same 6-layer architecture:

## Layer 1: Commands (Markdown)

**Definition:** Top-level entry point specification. Tells the agent what to do.

**File:** `.claude/commands/[domain]/[command].md`

**Example (orchestrator):**
```markdown
# /reddit-pain/analyze

User provides subreddit URL → agent orchestrates analysis → returns JSON + Markdown results.

## Instructions

1. Parse subreddit URL
2. Validate format
3. Initialize state
4. Call skill: reddit-data-pipeline
5. Call skill: ai-analysis-engine
6. Call skill: results-processor
7. Return results.json + results.md
```

**Example (primitive):**
```markdown
# /spawn-subagent

Spawn an autonomous agent in the background without blocking the user.

## Instructions

1. Parse task description
2. Validate background-safe
3. Invoke Agent tool with run_in_background=true
4. Return agent ID immediately (non-blocking)
```

---

## Layer 2: Skills (Markdown + References)

**Definition:** Multi-step execution specification. Describes how to accomplish a domain task.

**File:** `.claude/skills/[skill-name]/SKILL.md` + `references/` subdirectory

**Structure:**
```
.claude/skills/spawn-subagent/
├── SKILL.md                          (identity, overview, step table)
└── references/
    ├── step-01-parse-description.md
    ├── step-02-validate-background-safe.md
    ├── step-03-invoke-agent.md
    ├── step-04-return-task-id.md
    └── error-handling.md
```

**SKILL.md format:**
```markdown
# Spawn Subagent Skill

## Steps

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Parse task description | → [[references/step-01-parse-description]] |
| 2 | Validate background-safe | → [[references/step-02-validate-background-safe]] |
| 3 | Invoke Agent tool | → [[references/step-03-invoke-agent]] |
| 4 | Return agent ID | → [[references/step-04-return-task-id]] |

## Error Handling

→ [[references/error-handling]]
```

Each step file contains: input gate, action instructions, output gate, error handling.

---

## Layer 3: Data Contracts (JSON Schemas)

**Definition:** Validation rules at phase boundaries. Ensures correctness between loops.

**File:** `.claude/skills/[skill]/references/gate-contract-[N-to-M].json`

**Example:**
```json
{
  "phase": "spawn-subagent/step-1-to-2",
  "input_gate": {
    "required_fields": ["task_description"],
    "validations": [
      "task_description is string",
      "task_description length > 10"
    ]
  },
  "output_gate": {
    "required_fields": ["parsed_description"],
    "validations": [
      "parsed_description is string, non-empty"
    ]
  },
  "failure_action": {
    "retry": false,
    "on_failure": "fail immediately"
  }
}
```

**Validation:** Agent validates data against these schemas at every step boundary.

---

## Layer 4: References (Markdown)

**Definition:** Pattern guidelines, domain knowledge, and soft constraints.

**Files:**
- `.claude/references/core-philosophy.md` — Why the harness exists
- `.claude/references/autonomy-contract.md` — Behavioral rules
- `.claude/references/cost-optimization.md` — Budget guidelines
- `.claude/skills/[skill]/references/step-*.md` — Step instructions
- `.claude/skills/[skill]/references/error-handling.md` — Error recovery

**Enforcement:** Agent reads these and follows them. If violated, agent learns via `/kernel/learn`.

---

## Layer 5: Protocol (Markdown Index)

**Definition:** Indexed specification of the harness. Links to all other files.

**File:** `.claude/protocols/[domain]-protocol.md`

**Example:**
```markdown
# Sr Dev Protocol

## References

### Development Standards
| Reference | File |
|-----------|------|
| Core Philosophy | `.claude/references/core-philosophy.md` |

### Kernel
| Reference | File |
|-----------|------|
| Spawn Subagent Skill | `.claude/skills/spawn-subagent/SKILL.md` |
| Domain Gate Enforcer | `.claude/hooks/sr_dev-gate-enforcer.py` |

### Lessons Learned
→ `.claude/lessons/lessons.md`
```

**Purpose:** Agent reads protocol first, then follows wikilinks to specific files.

---

## Layer 6: State Files (JSON)

**Definition:** Runtime state that tracks progress. Passed between loops.

**Files:**
- `.claude/state/session_state.json` — Current session context
- `.claude/state/[domain]_workflow.json` — Job progress and metadata
- `[domain]_job_state.json` (optional) — Phase-specific state passed between skills

**Example:**
```json
{
  "job_id": "uuid-123",
  "status": "EXECUTING",
  "current_step": "spawn-subagent/step-2",
  "steps_completed": ["step-1"],
  "data": {
    "task_description": "Build test harness",
    "parsed_description": "Build test harness",
    "quality_issues": []
  }
}
```

**Updates:** Agent updates state after each step completes, validating against output gates.

---

## Complete Flow

```
1. Protocol (index)
   ↓
2. Command (entry point)
   ↓
3. Skill (step table)
   ↓
4. Step file (action instructions)
   ↓
5. Input gate (validate preconditions)
   ↓
6. Step execution (agent follows markdown)
   ↓
7. Output gate (validate results)
   ↓
8. State update (persist progress)
   ↓
9. Next step or skill
```

---

*All harnesses use this same 6-layer structure, ensuring consistency and portability.*

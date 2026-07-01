# Harness Design Pattern — Agent-Driven Orchestration

**Version:** 1.0
**Date:** 2026-06-13
**Core Principle:** Agent reads specification, executes autonomously. No code. Pure specification + state.

---

## What is a Harness?

A **harness** is a domain-specific agent orchestration specification built on **loops, data contracts, and defense-in-depth gates**.

A harness:
- Has ONE main **command** (markdown file describing what to do)
- Specifies a workflow via **outer loop** (numbered steps)
- Calls **inner loops** (skills) as sub-orchestrators
- Validates data at every boundary via **gate contracts** (JSON schemas)
- Enforces rules via **soft gates** (protocol, lessons) and **hard gates** (hooks)
- Produces **deliverables** as JSON + Markdown
- Runs **autonomously** (agent reads spec and executes, no pauses)

**The agent is the orchestrator.** The harness is the specification.

---

## Architecture: Specification Only (No Code)

### Layer 1: Commands (Markdown)

**Definition:** Top-level entry point specification. Tells the agent what to do.

**Example:** `.claude/commands/reddit-pain/analyze.md`

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

**Agent reads this file and executes each step in order.**

---

### Layer 2: Skills (Markdown + Step References)

**Definition:** Multi-step sub-orchestrator specification. Describes how to accomplish a domain task.

**Structure:**
```
.claude/skills/reddit-data-pipeline/
├── SKILL.md                    (identity, philosophy, step table)
└── references/
    ├── step-01-validate.md     (detailed instructions for step 1)
    ├── step-02-fetch.md        (detailed instructions for step 2)
    └── step-03-extract.md      (detailed instructions for step 3)
```

**SKILL.md format:**
```markdown
# Reddit Data Pipeline Skill

**Purpose:** Fetch Reddit posts and prepare text for analysis.

## Steps

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Validate subreddit | → [[step-01-validate]] |
| 2 | Fetch posts | → [[step-02-fetch]] |
| 3 | Extract text | → [[step-03-extract]] |

## Entry Point

When called from outer loop, execute steps 1-3 in order.
```

**step-01-validate.md:**
```markdown
# Step 1: Validate Subreddit

## Input Gate

Required: subreddit_url (string)
Validations:
  - Valid URL format (https://reddit.com/r/[name])
  - Subreddit name matches [a-z0-9_]+

## Action

1. Parse subreddit name from URL
2. Use Playwright to navigate to subreddit
3. Check if page loads (not 404)
4. Verify it's public (readable)

## Output Gate

Required: subreddit_valid (boolean)
Validations:
  - subreddit_valid = true
  - subreddit_name populated
  - subscriber_count populated (if available)

## Error Handling

If subreddit not found: Fail immediately, report to user
If private: Fail immediately, report to user
If network error: Retry 3x with backoff
```

**Agent reads the markdown and executes the action described in English.**

---

### Layer 3: Data Contracts (JSON Schemas)

**Definition:** Validation rules at phase boundaries. Ensures correctness between loops.

**File:** `.claude/skills/reddit-data-pipeline/references/gate-contract-1-to-2.json`

```json
{
  "phase": "reddit-data-pipeline/step-1-to-2",
  "input_gate": {
    "required_fields": ["subreddit_url"],
    "validations": [
      "subreddit_url is string",
      "subreddit_url matches /^https:\/\/reddit\.com\/r\/[a-z0-9_]+$/",
      "subreddit_url not empty"
    ]
  },
  "output_gate": {
    "required_fields": ["subreddit_valid", "subreddit_name"],
    "validations": [
      "subreddit_valid is boolean, value true",
      "subreddit_name is string, not empty",
      "subreddit_name matches /^[a-z0-9_]+$/"
    ]
  },
  "failure_action": {
    "retry": false,
    "on_failure": "fail immediately, report to user"
  }
}
```

**Agent validates data against these schemas.**

---

### Layer 4: References (Markdown)

**Definition:** Pattern guidelines and domain knowledge. Soft constraints.

**Examples:**
- `.claude/references/core-philosophy.md` — Why the harness exists
- `.claude/references/autonomy-contract.md` — No pauses during execution
- `.claude/references/cost-optimization.md` — Budget guidelines
- `.claude/references/data-schema-patterns.md` — How to structure state

**Agent reads these and follows them. If violated, agent learns via `/kernel/learn`.**

---

### Layer 5: Protocol (Markdown Index)

**Definition:** Indexed specification of the harness. Links to all other files.

**File:** `.claude/protocols/reddit-pain-analyzer-protocol.md`

```markdown
# Reddit Pain Analyzer Harness Protocol

## Entry Point
→ [[../commands/reddit-pain/analyze.md]]

## Skills
→ [[../skills/reddit-data-pipeline/SKILL.md]]
→ [[../skills/ai-analysis-engine/SKILL.md]]
→ [[../skills/results-processor/SKILL.md]]

## References
→ [[../references/autonomy-contract.md]]
→ [[../references/cost-optimization.md]]
→ [[../references/data-schema-patterns.md]]

## Lessons
→ [[../lessons/lessons.md]]
```

**Agent reads protocol first, then follows wikilinks to specifications.**

---

### Layer 6: State Files (JSON)

**Definition:** Runtime state that tracks progress. Passed between loops.

**No code, just JSON.**

```json
{
  "job_id": "uuid-123",
  "status": "EXECUTING",
  "current_step": "reddit-data-pipeline/step-2",
  "steps_completed": ["step-1"],
  "data": {
    "subreddit_url": "https://reddit.com/r/entrepreneur",
    "subreddit_name": "entrepreneur",
    "subreddit_valid": true
  }
}
```

**Agent updates state as it progresses.**

---

## Orchestration Flow (Agent Reads & Executes)

```
Agent invokes: /reddit-pain/analyze r/entrepreneur

1. Agent reads: .claude/protocols/reddit-pain-analyzer-protocol.md
2. Agent reads: .claude/commands/reddit-pain/analyze.md
3. Agent executes step-by-step (English instructions)
4. Agent reads: .claude/skills/reddit-data-pipeline/SKILL.md
5. Agent reads: .claude/skills/reddit-data-pipeline/references/step-01-validate.md
6. Agent validates input against gate contract
7. Agent executes action (follow English instructions)
8. Agent validates output against gate contract
9. Agent updates state.json
10. Agent repeats steps 4-9 for step-02, step-03, etc.
11. Agent calls next skill (ai-analysis-engine)
12. [Repeats for all skills]
13. Agent generates results.json + results.md
14. Agent reports completion
```

**The specification drives the agent. The agent is the runtime.**

---

## No Code in the Harness

The harness contains **ZERO runtime code**:

❌ No Python files
❌ No JavaScript files
❌ No compiled code
❌ No libraries
❌ No dependencies

✅ Markdown (specifications)
✅ JSON (schemas, state)
✅ Wikilinks (connections)

---

## Defense in Depth: Soft + Hard Gates

### Soft Gates (Agent-Enforced)

**Definition:** Protocol and lessons that guide agent behavior.

**File:** `.claude/protocols/reddit-pain-analyzer-protocol.md`

```markdown
## Rules

- Always validate subreddit before fetching posts
- Never attempt analysis on private subreddits
- Cost must stay below €0.50 per analysis
- Cache results for 7 days (avoid re-analyzing)
```

**Enforcement:** Agent reads rules and follows them. If violated, agent learns.

---

### Hard Gates (Hook-Enforced)

**Definition:** Mechanical enforcement rules that **block** operations.

**File:** `.claude/hooks/cost-limiter.py`

```python
# Pseudo-code (this is a hook, not in harness)
def pre_analyze_check(state):
    if state['estimated_cost'] > 0.50:
        raise CostLimitExceeded(...)
```

**Enforcement:** Hook blocks execution if cost exceeds threshold.

---

## State Management (Agent-Driven)

**Level 1: Session state** (session_state.json)
- Current task, context, pending actions
- Agent reads/updates

**Level 2: Workflow state** (reddit-pain-analyzer_workflow.json)
- Job progress, steps completed, results
- Agent reads/updates

**Level 3: Phase state** (passed between skills)
- Input/output at each phase
- Agent validates against gate contracts

---

## Example: Full Execution

### Files in Harness

```
reddit-pain-analyzer-harness/
├── .claude/
│   ├── protocols/
│   │   └── reddit-pain-analyzer-protocol.md (INDEX)
│   ├── commands/reddit-pain/
│   │   ├── analyze.md (main entry)
│   │   ├── status.md
│   │   └── export.md
│   ├── skills/
│   │   ├── reddit-data-pipeline/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       ├── step-01-validate.md
│   │   │       ├── step-02-fetch.md
│   │   │       ├── step-03-extract.md
│   │   │       └── gate-contract-1-to-2.json
│   │   ├── ai-analysis-engine/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       ├── step-01-pain-points.md
│   │   │       ├── step-02-ideas.md
│   │   │       ├── step-03-scores.md
│   │   │       └── gate-contracts.json
│   │   └── results-processor/
│   │       ├── SKILL.md
│   │       └── references/
│   │           ├── step-01-validate.md
│   │           ├── step-02-store.md
│   │           ├── step-03-export.md
│   │           └── gate-contracts.json
│   ├── references/
│   │   ├── autonomy-contract.md
│   │   ├── cost-optimization.md
│   │   └── data-schema-patterns.md
│   ├── lessons/
│   │   └── lessons.md
│   ├── hooks/
│   │   ├── universal-gate-enforcer.py
│   │   └── cost-limiter.py
│   └── state/
│       └── reddit-pain-analyzer_workflow.json
└── docs/
    └── (harness design documentation)
```

**Total size:** ~50KB (all text files, pure specification)

### Agent Execution

```
Agent: /reddit-pain/analyze r/entrepreneur

[Agent reads protocol.md]
[Agent reads analyze.md command]
[Agent reads reddit-data-pipeline/SKILL.md]
[Agent reads reddit-data-pipeline/references/step-01-validate.md]
[Agent reads gate-contract-1-to-2.json]

Agent: Parsing subreddit URL...
Agent: Validating against input gate... ✓
Agent: Navigating to https://reddit.com/r/entrepreneur
Agent: Checking if page loads... ✓
Agent: Verifying public/readable... ✓
Agent: Validating against output gate... ✓

[Agent updates state.json with step-1 complete]
[Agent reads step-02-fetch.md]
[Agent fetches posts...]
[Repeats for all steps]

Agent: All skills complete
Agent: Generating results.json...
Agent: Generating results.md...
Agent: Analysis complete!
```

**No code executed. Agent reads specs and follows instructions.**

---

## Key Insight

**The harness IS the specification. The agent IS the runtime.**

This is fundamentally different from:
- Traditional apps (code-first)
- APIs (request-response)
- Microservices (distributed execution)

**Harness = Specification-first, agent-driven orchestration.**

---

*This pattern is the foundation for all Isagawa harnesses.*

# Skills Modular Design — Step-Based Architecture

## What is a Skill?

A skill is a **multi-step orchestrator** that handles complex workflows. Each skill is a folder with:

1. **SKILL.md** — Identity, philosophy, step table, entry point
2. **references/** — Numbered step files (01, 02, 03...)
3. **[optional]** Test fixtures, examples

Skills are designed to be **composable** — one skill can call another skill within its steps.

## Directory Structure

```
.claude/skills/execute-pipeline/
├── SKILL.md                          ← Entry point + identity
├── references/
│   ├── step-01-parse-backlog.md
│   ├── step-02-research.md
│   ├── step-03-decompose-tasks.md
│   ├── step-04-gate-validation.md
│   ├── step-05-execute-tasks.md
│   ├── step-06-report-results.md
│   └── step-07-error-handling.md      (optional, referenced as needed)
└── fixtures/                          (optional)
    ├── sample-backlog.json
    └── expected-output.json
```

## SKILL.md — The Index

SKILL.md is a **skill's manifest**. It contains:

1. **Skill Identity** — Name, purpose, version
2. **Philosophy** — Why this skill exists, core design decisions
3. **Step Table** — Index of all steps with one-line descriptions

Example structure:

```markdown
# Execute Pipeline Skill

**Purpose:** Orchestrate autonomous execution of a backlog item into atomic tasks.

**Philosophy:**
- Autonomy by default (never pause for user confirmation)
- State-driven (behavior from state files, not code)
- Error recovery (retry 3x, then skip; don't halt)

## Step Table

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Parse backlog item → extract scope, requirements | [[step-01-parse-backlog]] |
| 2 | Research context (read related files, gather inputs) | [[step-02-research]] |
| 3 | Decompose into atomic tasks (via task-builder) | [[step-03-decompose-tasks]] |
| 4 | Validate tasks against gate contracts | [[step-04-gate-validation]] |
| 5 | Execute tasks (spawn background agents, collect results) | [[step-05-execute-tasks]] |
| 6 | Generate validation + results report | [[step-06-report-results]] |

## Entry Point

When a user invokes `/kernel/execute-pipeline [backlog-number]`:

1. Agent reads this SKILL.md
2. Agent follows the step table in order
3. For each step, agent reads the referenced step file
4. Agent executes steps sequentially (or with specified parallelism)
```

## The Wikilink Pattern

Step files are referenced using **wikilinks** (double brackets):

```
[[step-01-parse-backlog]]     → resolves to references/step-01-parse-backlog.md
[[execute-pipeline/step-02]]  → resolve from another skill folder
[[../references/pattern.md]]  → cross-folder reference
```

Wikilinks are **not file paths**. They're symbolic references that the framework resolves.

## Step Files — Implementation

Each step file is **self-contained documentation** of what to do. Structure:

```markdown
# Step 1: Parse Backlog Item

## Input Gate

What must be true before this step runs:
- `backlog_path` field in session_state.json
- File at that path exists
- File is valid JSON/markdown

If gate fails: Report error, do NOT continue.

## Action

1. Read the backlog file
2. Extract required fields: title, scope, deliverable, constraints
3. Store parsed content in session_state.json under `context.parsed_backlog`

## Output Gate

What must be true after this step runs:
- `context.parsed_backlog` field populated
- All required fields extracted
- No parsing errors

If gate fails: Report error, do NOT continue to next step.

## Error Handling

If backlog file is malformed:
1. Report error (field X missing, syntax invalid)
2. Do NOT attempt recovery
3. Stop execution
```

## Step Ordering — Phase Boundaries

Steps are **numbered** (01, 02, 03) and executed in order. No branching; every step runs unless:

- Input gate fails (stop + report)
- Output gate fails (stop + report)
- Step is marked optional and skipped by user request

Phase boundaries are where **state transitions** happen:

```
Step 1 (Parse)
    ↓ [Output gate validation]
    └→ State: parsed_backlog ✓

Step 2 (Research)
    ↓ [Output gate validation]
    └→ State: research_complete ✓

Step 3 (Decompose)
    ↓ [Output gate validation]
    └→ State: tasks_created ✓

Step 4 (Execute)
    ↓ [Output gate validation]
    └→ State: all_tasks_done ✓ (or some_skipped)
```

Each phase boundary is a **commit point** — if a later step fails, you can roll back to the last good boundary.

## Skill Composition — Skills Calling Skills

Complex skills can delegate to sub-skills. Example:

```markdown
# Step 3: Decompose Tasks

Within execute-pipeline, invoke task-builder:

1. Call `/kernel/task-builder` with:
   - `parsed_backlog` from session_state.json
   - Output location: `context.tasks_folder`

2. Task-builder reads its own SKILL.md and executes steps 1-6

3. Returns: List of task files created

4. Validate output against task schema

5. Continue with Step 4 (validation)
```

The orchestration is **hierarchical** — one skill calls another, which calls another. The top-level command (e.g., `/kernel/execute-pipeline`) drives the entire flow.

## State Management Across Steps

Steps share state through **session_state.json**:

```json
{
  "context": {
    "parsed_backlog": { ... },        // Step 1 output
    "research_complete": true,         // Step 2 output
    "tasks_folder": "tasks/...",       // Step 3 output
    "task_list": [...]                 // Step 4 output
  }
}
```

Each step **reads input** from prior steps' outputs and **writes output** to context.

## Atomicity — One Step, One Responsibility

Each step does **one thing**:

- Step 1: Parse only (no research, no decomposition)
- Step 2: Research only (no task creation)
- Step 3: Decompose only (no execution)

This makes steps:
- Testable in isolation
- Debuggable (know exactly which step failed)
- Recoverable (rerun a step without affecting others)

## Examples to Extract from Kernel

When building the framework, extract these skill implementations:

1. **execute-pipeline** — Complex orchestrator (6+ steps, error handling, cycling)
2. **task-builder** — Intermediate skill (5 steps, uses sub-agents, produces artifacts)
3. **prod-test** — Advanced skill (multi-phase, setup + execution + cleanup)
4. **autonomous-cycling** — Reference for looping behavior (state-driven)

Each becomes a **reference implementation** showing how to structure modular skills.

## Testing Skills

Each skill should include test fixtures showing:

1. **Valid input** — Example backlog, example state
2. **Expected output** — Example task file, example state after execution
3. **Error cases** — Missing input, malformed data, validation failures

This lets developers test the skill in isolation before using it in production.

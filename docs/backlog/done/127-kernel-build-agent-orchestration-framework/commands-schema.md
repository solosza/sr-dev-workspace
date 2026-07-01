# Commands Schema — Structure and Registry

## What is a Command?

A command is a **user-facing entry point** that performs one orchestration action. Commands are markdown files in `.claude/commands/` that describe:

1. What the command does
2. How to invoke it (syntax)
3. Step-by-step instructions for the agent

**Commands are not executable.** They are prescriptive documents that the agent reads and follows. The agent is responsible for implementing the behavior.

## Command Structure

Every command follows this standard template:

```markdown
# /[namespace]/[verb]

[One-sentence summary of what this command does]

## Usage

```
/[namespace]/[verb] [required argument 1] [required argument 2]
/[namespace]/[verb] [example 2]
```

## Instructions

1. **[Step 1 title]:** [What to do]
   - Sub-point A
   - Sub-point B

2. **[Step 2 title]:** [What to do]
   ...

3. **[Report]:** [Output format for user]
```

## Naming Convention

```
/[namespace]/[verb]

namespace: kernel, domain, project name, etc.
verb: backlog, execute-pipeline, complete, learn, audit-workflow, etc.
```

**Examples:**
- `/kernel/backlog` — Create a new backlog item
- `/kernel/execute-pipeline` — Execute a backlog item end-to-end
- `/kernel/complete` — Mark work done, handle cycling transition
- `/domain/custom-command` — Project-specific command

## The Command Namespace

Commands are organized by namespace:

| Namespace | Purpose | Location |
|-----------|---------|----------|
| `kernel` | Core orchestration, universal commands | `.claude/commands/kernel/` |
| `domain` | Domain-specific commands (domain-setup, audit-workflow, etc.) | `.claude/commands/kernel/` (or domain-specific folder) |
| Project-specific | Project's own commands | `.claude/commands/[project-name]/` |

## Registry Pattern

Commands are discovered via filesystem scan. No explicit registry needed — the system finds all `.md` files in `.claude/commands/` and indexes them.

**Discovery:**
```bash
find .claude/commands -name "*.md" -type f | sort
```

**Result:** Flat list of available commands, grouped by folder name

## Lifecycle — What a Command Does

When a user invokes `/kernel/backlog Research something`:

1. **Agent reads** `.claude/commands/kernel/backlog.md`
2. **Agent extracts** instructions section (numbered steps)
3. **Agent follows** each step in order
4. **Agent produces** output (file created, state updated, report displayed)

The command document is a **specification**. The agent is the executor.

## Design — What Commands Should Contain

Each command should include:

### 1. Usage Section
Clear examples showing how to invoke. Should be copy-paste ready.

```
/kernel/backlog Research AI opportunities for Roberts Hawaii
/kernel/execute-pipeline 029
/kernel/complete
```

### 2. Instructions Section
Numbered steps that the agent follows. Each step should:
- Have a clear title (verb + object)
- State what to do (imperative)
- Include decision logic if branches exist
- Point to references or skills if complex

**Good:** "Read `.claude/protocols/sr_dev-protocol.md` using the Read tool"
**Bad:** "Understand the protocol"

### 3. Error Handling Section (if applicable)
When things go wrong, what should the agent do?

```markdown
## Error Handling

- If backlog file already exists: append to existing backlog
- If network error during push: retry 3x with exponential backoff
- If user input is ambiguous: ask for clarification
```

### 4. Report Section
What output does the user see when done?

```markdown
## Report

Format:
```
BACKLOG ITEM CREATED

File: docs/backlog/NNN-tag-verb-object.md
Title: [title]
Status: [status]

Ready for /kernel/execute-pipeline.
```

## Commands as Skills Orchestrators

Some commands are **lightweight** (backlog, complete) while others are **heavy** (execute-pipeline, task-builder). Heavy commands delegate to skills.

| Command | Complexity | Delegates to | Example |
|---------|-----------|--------------|---------|
| `/kernel/backlog` | Lightweight | None (writes files directly) | Create backlog item |
| `/kernel/execute-pipeline` | Heavy | task-builder skill (step 3) | Orchestrate entire execution |
| `/kernel/complete` | Lightweight | None (updates state, reports) | Mark work done |
| `/kernel/learn` | Lightweight | None (updates lessons.md) | Record lesson |
| `/kernel/audit-workflow` | Heavy | Multiple skills | Scan gaps, generate fixes |

## State Handoff — Commands and Workflows

When a command finishes, it updates state files so the next command (or cycling) knows what happened.

**Example: /kernel/execute-pipeline state lifecycle**

```
1. Before: session_state.json has context + pending backlog
2. During:
   - Parse backlog item
   - Task-builder creates tasks + state
   - Run-task.sh executes tasks, updates state
3. After: session_state.json has completed_tasks list + results
         + next_step field points to /kernel/complete
```

The next command reads that state and continues from there.

## Validation — Gate Contracts for Commands

Each command should specify **input gates** (what must be true before running):

```markdown
## Input Gate

Command requires:
- `session_state.json` exists
- `current_backlog` field is set
- Task folder path is valid

If input gate fails:
1. Stop
2. Report what's missing
3. Do NOT attempt recovery
```

This prevents commands from running in invalid states.

## Examples to Extract from Kernel

When building the framework, extract these command implementations:

1. `/kernel/backlog` — Template for simple command (backlog.md)
2. `/kernel/execute-pipeline` — Template for complex command (orchestrator, calls skills)
3. `/kernel/complete` — Template for state transition command
4. `/kernel/learn` — Template for knowledge-record command
5. `/kernel/anchor` — Template for protocol-refresh command (reads files, computes hashes)

Each becomes a **reference implementation** showing how to structure and implement commands in the framework.

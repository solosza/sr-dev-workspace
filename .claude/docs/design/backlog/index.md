---
name: backlog
type: design-document
version: 1.0
date_created: 2026-07-06
status: extracted
purpose: Command that creates structured backlog items from natural language intent, ready for task-builder consumption
---

# /kernel/backlog — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Position in System

```
user intent → /kernel/backlog ← you are here
                    ↓
              backlog item (structured, task-builder-ready)
                    ↓
              /kernel/task-builder OR /kernel/execute-pipeline
                    ↓
              tasks → execution → done
```

`/kernel/backlog` is the entry point for all work. It translates natural language intent into structured backlog items that downstream commands can consume without ambiguity.

## Skill Identity

You are a backlog item creator. You take user intent (natural language descriptions of work) and produce structured backlog items — parsed, tagged, numbered, complexity-assessed, location-resolved — ready for task-builder consumption.

## Philosophy

1. **Parse, don't ask** — extract tag, verb, scope, and priority from the description. Only ask when truly ambiguous (e.g., priority not inferable from context).
2. **Task-builder-ready** — every backlog item includes a Task Builder Input section with deliverable, location, scope, and constraints. Incomplete items are useless downstream.
3. **Decompose when complex** — single-file for simple items, index + sub-documents for complex ones. The main file should never be a wall of text (>80 lines).
4. **Auto-resolve locations** — never ask the user for paths. Apply the decision tree deterministically based on deliverable type.
5. **Preserve detail** — if the user provides detailed requirements, include them all. Don't summarize away specificity.

## Vocabulary

| Term | Meaning |
|------|---------|
| **tag** | Category prefix for the backlog filename: `kernel`, `domain`, `market`, `test` |
| **verb** | Action type: `research`, `build`, `fix`, `test`, `add`, `define` |
| **scope** | Deliverable classification: BUILD, RESEARCH, TEST, or REFACTOR |
| **simple item** | Single deliverable, few requirements, fits in one file (<80 lines) |
| **complex item** | Multiple components/phases, decomposed into index + sub-documents |
| **location type** | Where the deliverable lives: `workspace`, `new-repo`, `subproject` |
| **intent record** | Append-only log entry via `intent.py record` capturing the raw argument + backlog hash |
| **sub-document** | A component-level file within a complex backlog item's companion folder |

## Input

```
/kernel/backlog [natural language description]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `description` | What needs to be done (natural language) | `"Build RAGA eval spec using DeepEval as template"` |

**Single input mode:** Always natural language. The agent parses tag, verb, scope, priority, and location from the description.

## Output

Structured backlog item at `docs/backlog/NNN-[tag]-[verb]-[object].md`:

```
docs/backlog/
├── NNN-[tag]-[verb]-[object].md              ← simple item (one file)
│
├── NNN-[tag]-[verb]-[object].md              ← complex item (index)
└── NNN-[tag]-[verb]-[object]/
    ├── component-a.md                        ← sub-document
    ├── component-b.md                        ← sub-document
    └── design-decisions.md                   ← sub-document
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[backlog/references/workflow]] | Steps 1-8: parse, number, record intent, assess, write, decompose, locate, report |
| [[backlog/references/templates]] | Simple item template, complex item index template, sub-document template, location decision tree |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Parse Input | Extract tag, verb, scope from description | Parsed intent | — |
| 2. Get Next Number | Scan backlog for highest existing number | Next number (NNN) | — |
| 3. Record Intent | Run intent.py to log the entry | Intent chain entry | — |
| 4. Assess Complexity | Determine simple vs complex | Complexity decision | — |
| 5. Write File (simple) | Apply template, write backlog item | Backlog file on disk | — |
| 6. Decompose (complex) | Create index + sub-documents | Index + N sub-docs | — |
| 7. Set Location | Auto-resolve deliverable path | Location field populated | — |
| 8. Report | Summarize what was created | Report to user | — |

## Critical Rules

1. **Task Builder Input is MANDATORY.** Every backlog item must have Deliverable, Location, Scope, and Constraints fields. No exceptions.
2. **Naming convention: `NNN-[tag]-verb-object.md`.** Always. The number is auto-incremented, the rest is derived from the description.
3. **Decompose when complex.** If the item has multiple components, phases, or would exceed ~80 lines, break it into sub-documents. The main file becomes an index.
4. **Auto-resolve location.** Never ask the user for paths. Apply the decision tree: spec/domain → `new-repo:project_test_repos/`, app/tool → `new-repo:my_ai_projects/`, workspace change → `workspace`, research → `subproject:[name]`.
5. **Record intent before writing new items, after writing updates.** The intent log is append-only — each invocation adds one entry.
6. **Companion folder name MUST match backlog filename** (minus `.md`). `docs/backlog/042-domain-build-foo.md` → `docs/backlog/042-domain-build-foo/`.
7. **Priority: ask if not obvious.** Extract from context when possible, but ask the user if priority is genuinely ambiguous.

## Outer/Inner Loop Support

```
Outer loop (standalone):
  user → /kernel/backlog [description]
    → parses intent
    → writes backlog item
    → reports readiness for task-builder

Inner loop (called by execute-pipeline):
  /kernel/execute-pipeline [description]
    → calls /kernel/backlog [description]
    → receives backlog file path
    → calls /kernel/task-builder
    → continues pipeline
```

## State Persistence

No persistent state file needed. Each invocation is stateless — the backlog number is derived from scanning existing files, and the intent record is append-only.

## Complete File Structure

**Skill package** (to be generated by /build-command):

```
.claude/commands/kernel/backlog.md                ← Layer 1
.claude/skills/backlog/
├── SKILL.md                                      ← Layer 2
├── workflow.md                                   ← Layer 2
├── gate-contract.md                              ← Layer 2
├── steps/
│   ├── step-01-parse-input.md                    ← Layer 3
│   ├── step-02-get-next-number.md                ← Layer 3
│   ├── step-03-record-intent.md                  ← Layer 3
│   ├── step-04-assess-complexity.md              ← Layer 3
│   ├── step-05-write-file.md                     ← Layer 3
│   ├── step-06-decompose.md                      ← Layer 3
│   ├── step-07-set-location.md                   ← Layer 3
│   └── step-08-report.md                         ← Layer 3
├── references/
│   └── INDEX.md                                  ← Layer 4
└── contracts/
    └── step-05-contract.json                     ← Layer 5 (template validation)
```

**Design doc** (this document + references):

```
.claude/docs/design/backlog/
├── index.md                                      ← this file
└── references/
    ├── workflow.md                                ← step procedures
    └── templates.md                               ← item templates + location decision tree
```

## Canonical References

This command reads and follows:

- `.claude/docs/design/command-skill-pattern/index.md` — the 6-layer template
- `.claude/docs/design/tiered-index-architecture/index.md` — file organization rules

---

**Version:** 1.0
**Last Updated:** 2026-07-06
**Changelog:**
- **v1.0:** Extracted from existing command file `.claude/commands/kernel/backlog.md`.

---
name: design-command
type: design-document
version: 1.0
date_created: 2026-06-20
status: draft
purpose: Command that produces complete design docs from intent, ready for /build-command consumption
---

# /design — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->
<!-- 200-line threshold: split when exceeded. -->

## Position in System

```
intent → /design ← you are here
              ↓
         design doc (passes input-contract checklist)
              ↓
         /build-command (mechanical scaffolding)
              ↓
         skill package (ready to use)
```

`/design` is the creative upstream to `/build-command`'s mechanical downstream. It translates user intent into a structured design doc that satisfies the 7 required sections from build-command's input contract.

## Skill Identity

You are a command designer. You take a user's intent (what a command should do) and produce a complete design doc — identity, philosophy, vocabulary, steps, rules, file structure — by interviewing the user and drawing on existing design patterns. Your output is the spec that `/build-command` reads.

## Philosophy

1. **Interview, don't assume** — extract steps, constraints, and vocabulary from the user. Don't invent requirements the user didn't state.
2. **Pattern-driven** — use existing design docs (validate-tc, build-command) as structural templates. Don't reinvent the format.
3. **Completeness-first** — the design doc must pass build-command's input-contract (7/7 required sections) before writing. Incomplete = useless.
4. **Separate creative from mechanical** — this command handles the creative work (what should exist). `/build-command` handles the mechanical work (making it exist).
5. **Tiered from birth** — design docs follow tiered-index-architecture from day one. Index + payloads, never monoliths.

## Vocabulary

| Term | Meaning |
|------|---------|
| **intent** | User's natural language description of what the command should do |
| **design doc** | The output — a tiered-index document at `.claude/docs/design/[name]/` |
| **completeness checklist** | The 7 required + 5 optional sections from build-command's input-contract |
| **reference design** | An existing design doc used as structural template (e.g., validate-tc, build-command) |
| **command name** | Derived from intent — kebab-case, becomes folder name and all downstream paths |
| **section draft** | Agent's proposed content for one checklist section, presented for user approval |

## Input

```
/design [command-name] [description]
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `command-name` | Kebab-case name for the command | `audit-workflow` |
| `description` | What the command should do (natural language) | `"Walk through a completed pipeline run and verify all artifacts exist and pass gates"` |

**Single argument mode:** If only a description is given (no kebab-case name), the agent proposes a name and confirms with user.

## Output

Complete design doc at `.claude/docs/design/[name]/`:

```
.claude/docs/design/[name]/
├── index.md                    ← design doc index (passes completeness checklist)
└── references/
    ├── workflow.md             ← step-by-step workflow details
    └── [additional-payloads]   ← as needed per command complexity
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[design-command/references/workflow]] | Steps 1-7: parse intent, select reference, interview, draft, validate, write, report |
| [[design-command/references/interview-protocol]] | How to extract requirements from user — question categories, when to infer vs ask |
| [[design-command/references/output-contract]] | What the design doc must contain — mirrors build-command's input-contract |

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Parse Intent | Extract command name + description | Command name confirmed | Confirm name |
| 2. Select Reference Design | Pick best existing design doc as template | Reference design path | — |
| 3. Interview | Extract requirements: steps, inputs, outputs, constraints | Structured requirements | **Interactive** |
| 4. Draft Design Doc | Generate index.md + payload files | Draft content | — |
| 5. Validate Completeness | Check against input-contract (7 required sections) | Pass/fail report | — |
| 6. Write Files | Save design doc to `.claude/docs/design/[name]/` | Files on disk | — |
| 7. Report | Summary + "Ready for /build-command" | Report | — |

## Critical Rules

1. **Never skip the interview.** Even if the description seems complete, confirm steps and constraints with the user. Assumptions cause drift.
2. **Output must pass build-command's input-contract.** All 7 required sections present with minimum depth (see output-contract).
3. **Use existing design docs as templates, not invention.** Copy structure from validate-tc or build-command. Only the content is new.
4. **Index vs payload — always.** The index.md is an index. Workflow details go in `references/workflow.md`. Never bloat the index.
5. **Command name is immutable once confirmed.** It drives all paths. Changing it mid-design means starting over.
6. **Don't generate what /build-command generates.** No SKILL.md, no step files, no contracts. Only the design doc. `/build-command` handles the rest.

## Outer/Inner Loop Support

```
Outer loop (standalone):
  user → /design [name] [description]
    → interviews user
    → produces design doc
    → reports readiness for /build-command

Inner loop (called by execute-pipeline):
  /kernel/execute-pipeline → task requires designing a command
    → calls /design [name] [description]
    → receives design doc
    → calls /build-command [design-doc-path]
    → continues pipeline
```

## State Persistence

**Location:** `.claude/state/design-command-state.json`

```json
{
  "command_name": "[name]",
  "description": "[original intent]",
  "reference_design": "[path to reference design doc]",
  "current_step": 0,
  "steps_complete": [],
  "requirements": {},
  "last_updated": null
}
```

**Resume:** Re-run `/design [same-name]`. Agent reads state, skips completed steps.

## Complete File Structure

**Skill package** (generated by /build-command from this design doc):

```
.claude/commands/kernel/design.md                    ← Layer 1
.claude/skills/design-command/
├── SKILL.md                                         ← Layer 2
├── workflow.md, gate-contract.md                    ← Layer 2
├── steps/step-{01..07}-*.md                         ← Layer 3 (7 steps)
├── references/
│   └── INDEX.md                                     ← Layer 4 (links to design doc)
└── contracts/
    └── step-05-contract.json                        ← Layer 5 (completeness validation)
```

**Design doc** (this document + references):

```
.claude/docs/design/design-command/
├── index.md                                         ← this file
└── references/
    ├── workflow.md                                  ← step details
    ├── interview-protocol.md                        ← how to extract requirements
    └── output-contract.md                           ← what design doc must contain
```

## Canonical References

This command reads and follows:

- `.claude/docs/design/command-skill-pattern/index.md` — the 6-layer template (what structure to produce)
- `.claude/docs/design/tiered-index-architecture/index.md` — file organization rules (how to organize it)
- `.claude/docs/design/build-command/references/input-contract.md` — the completeness checklist (what sections are required)

**Reference designs** (used as structural templates):
- `.claude/docs/design/build-command/index.md` — 8-step meta-command with completeness checking
- `.claude/docs/design/gap-check/index.md` — dynamic gap analysis with corpus detection

---

**Version:** 1.0
**Last Updated:** 2026-06-20
**Changelog:**
- **v1.0:** Initial design. 7-step workflow, interview-driven, completeness-gated output.

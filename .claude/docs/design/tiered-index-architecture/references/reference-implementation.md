# Reference Implementation: Multi-Step Artifact Generation Skill

<!-- Payload of: tiered-index-architecture.md -->

Complete worked example showing all 3 layers in a skill that generates artifacts through a multi-step pipeline. This is the canonical pattern for any skill that reads input, generates output, and validates results.

---

## Skill Folder Structure (Layer 1)

```
.claude/skills/[skill-name]/
├── SKILL.md                              ← INDEX (entry point, points to everything)
├── workflow.md                           ← INDEX (step-by-step pipeline, points to references + contracts)
├── gate-contract.md                      ← PAYLOAD (gate specification — how validation works)
├── contracts/                            ← PAYLOAD folder
│   ├── step-01-[artifact]-contract.json  ← Layer 3: validation rules for step 1
│   ├── step-02-[artifact]-contract.json  ← Layer 3: validation rules for step 2
│   └── ...
└── references/                           ← PAYLOAD folder
    ├── INDEX.md                          ← INDEX (reference navigation)
    ├── [shared-reference].md             ← PAYLOAD (cross-step reference)
    ├── step-02/
    │   └── [example-artifact]            ← PAYLOAD (Layer 2: canonical reference)
    ├── step-05/
    │   └── [example-artifact]            ← PAYLOAD (Layer 2: canonical reference)
    └── ...
```

**Index chain:** SKILL.md → workflow.md → references/INDEX.md
Each file is either index (points to others) or payload (contains content). No file is both.

---

## Workflow as Index (Layer 1 + Layer 2)

The workflow file is an index that also embeds Layer 2 checkpoints:

```markdown
### Step 2: Generate [Artifact]

**Pre-generation checkpoint:**
- Read canonical reference: `references/step-02/[example]`
- Read contract: `contracts/step-02-[artifact]-contract.json`
- Read output from Step 1

**How agent uses the reference:**
1. Agent reads reference — sees the exact format
2. Agent reads input — knows the content to generate
3. Agent generates artifact matching reference pattern

**Output:** `[artifact-file]`

**Success criteria:**
- ✓ [Criteria derived from contract]
```

Each step declares its reading list (Layer 2) and points to the payloads the agent must load (Layer 1).

---

## Contract JSON (Layer 3)

Each step has a contract with both gate types:

```json
{
  "contract_version": "1.0",
  "artifact": "[output-file]",
  "step": 2,
  "dependencies": ["step-01"],

  "soft_validation_rules": [
    {
      "rule_id": "SV-001",
      "name": "[Rule Name]",
      "description": "[What the rule checks]",
      "check": "[How to verify]",
      "reference": "references/step-02/[example]",
      "on_violation": "log error, invoke /kernel/learn, STOP"
    }
  ],

  "mechanical_validations": [
    {
      "rule_id": "MV-001",
      "name": "[Rule Name]",
      "method": "grep",
      "pattern": "[regex pattern]",
      "min_count": 1,
      "on_violation": "block write"
    }
  ],

  "canonical_reference": "references/step-02/[example]",
  "success_criteria": ["[Criteria 1]", "[Criteria 2]"]
}
```

---

## Full Execution Flow (All 3 Layers)

```
Agent receives command
    │
    ▼
Reads SKILL.md (Layer 1: index)
    → finds workflow.md
    │
    ▼
Reads workflow.md (Layer 1: index → step definitions)
    → Step 1: extract input
    → Step 2: generate artifact A
    → Step 3: generate artifact B
    → ...
    │
    ▼
For each step:
    │
    ├─ Layer 2: Read checkpoint
    │   ├── Read references/step-N/[example]    ← canonical pattern
    │   ├── Read contracts/step-N-contract.json  ← validation rules
    │   └── Read output from prior step          ← input data
    │
    ├─ Generate: Create artifact matching reference
    │
    ├─ Layer 3: Soft gate
    │   ├── Agent reads contract soft rules
    │   ├── Compares artifact to rules + reference
    │   └── If violation → learn + fix + retry
    │
    └─ Layer 3: Hard gate
        ├── Hook intercepts write
        ├── Applies mechanical validations
        └── If violation → block write → agent fixes → retry
```

---

## What Makes This Pattern Portable

This pattern works in any repo because:

1. **Layer 1** is just file organization — any repo can use index/payload split
2. **Layer 2** checkpoints are embedded in workflow.md — they travel with the skill
3. **Layer 3** contracts are JSON files in the skill folder — self-contained validation rules
4. **References** are golden files in the skill folder — proven outputs that define correct patterns

No external dependencies. The entire skill is a self-contained folder that can be copied to any repo and work the same way.

---

## Adapting for New Skills

To create a new skill following this pattern:

1. **Create SKILL.md** (index) — point to workflow + references
2. **Create workflow.md** — define steps with Layer 2 checkpoints
3. **Create references/** — add canonical examples for each step's output
4. **Create contracts/** — define soft + hard validation rules per step
5. **Test** — run the skill, verify gates catch violations, record lessons

# Architecture Layers

<!-- Payload of: command-skill-pattern/index.md -->

## Layer 1: Command

**Location:** `.claude/commands/kernel/[command-name].md`
**Purpose:** User-facing entry point. Defines signature, input modes, examples.

**Responsibilities:**
- Parse user input
- Route to skill
- Report results

**Structure:**
```yaml
---
name: [command-name]
version: 1.0
status: stable
type: command
---

# /[command-name]

## Usage
/[command-name] [input]

## Input Modes
(describe how input is interpreted)

## Examples
(show usage)

## Design Reference
Link to: `.claude/docs/design/[command-name]/index.md`
```

---

## Layer 2: Skill

**Location:** `.claude/skills/[command-name]/SKILL.md`
**Purpose:** Orchestrator. Defines the workflow, vocabulary, critical rules.

**Responsibilities:**
- Define workflow phases/steps
- Enforce phase gates
- Manage state
- Call step procedures

**Structure:**
```markdown
# [Command Name] Skill

## Identity
(who you are, what you do)

## Philosophy
(guiding principles)

## Vocabulary
(domain-specific terms)

## Workflow
(steps 1 through N)

## Critical Rules
(hard constraints)

## File Index
(all files in this skill package)
```

---

## Layer 3: Steps

**Location:** `.claude/skills/[command-name]/steps/step-NN-[name].md`
**Purpose:** Individual workflow step with specific responsibilities.

**Responsibilities:**
- Define step input/output
- Load contracts for this step
- Call references as needed
- Perform step logic
- Report results

**Structure:**
```markdown
# Step N: [Step Name]

## Purpose
## Input
## Output
## Acceptance Criteria
## References
## Procedure
## Verification
## Failure Recovery
```

---

## Layer 4: References

**Location:** `.claude/skills/[command-name]/references/`
**Purpose:** Canonical examples, patterns, templates for each step.

**Organization (Tiered Indexing):**
```
references/
|-- INDEX.md
|-- step-01/
|   |-- canonical-example-1.md
|   +-- [reference materials]
|-- step-02/
|   +-- canonical-example.md
+-- step-N/
    +-- [reference materials]
```

**INDEX.md** has sections: Quick Links, By Step, By Artifact Type.

**Reference file frontmatter:**
```yaml
---
artifact_type: [markdown|sql|json|excel]
related_step: N
purpose: [what this example shows]
source: [where this came from]
canonical_hash: [sha256 hash]
---
```

---

## Layer 5: Contracts

**Location:** `.claude/skills/[command-name]/contracts/`
**Purpose:** JSON specifications defining valid artifact structure and validation rules.

One contract per step artifact. Both soft gate (agent-driven) and hard gate (hook-driven) read the same contract.

-> See `contract-schema.md` for full JSON schema and dual validation details.

---

## Layer 6: Hooks

**Location:** `.claude/hooks/[hook-name].py`
**Purpose:** Hard gate validation. Blocks invalid artifacts at write time.

**Responsibilities:**
- Intercept file write
- Load matching contract for artifact
- Run mechanical_validations deterministically
- Block (severity=BLOCK) or warn (severity=WARN)
- Report error with guidance + canonical reference

Hooks read contracts instead of being hardcoded. Same validation rules for soft and hard gates. Single source of truth: the contract JSON.

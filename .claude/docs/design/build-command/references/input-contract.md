# Input Contract: Design Doc Completeness

**Purpose:** Defines what a design doc must contain before `/build-command` can scaffold from it. This is the formal input spec — Step 1 validates against it.

**Source:** Derived from command-skill-pattern's Design Doc Completeness Checklist.

---

## Required Sections

These must be present in the design doc (index + payload files). If any is missing, Step 1 fails.

| # | Section | Where to Find | Maps To |
|---|---------|---------------|---------|
| 1 | **Skill Identity** | Index or SKILL.md-equivalent section. One sentence: "You are a [role]." | Layer 2: SKILL.md `## Identity` |
| 2 | **Philosophy** | Index or payload. 3-5 numbered guiding principles. | Layer 2: SKILL.md `## Philosophy` |
| 3 | **Vocabulary** | Index or payload. Table with Term + Meaning columns. | Layer 2: SKILL.md `## Vocabulary` |
| 4 | **Critical Rules** | Index or payload. Numbered hard constraints. | Layer 2: SKILL.md `## Critical Rules` |
| 5 | **Workflow Summary** | Index. Table with Step + Responsibility + Output + HITL columns. | Layer 2: workflow.md |
| 6 | **Step File Specs** | Payload files (one per step or grouped). Per-step minimum: Purpose + Procedure. Full spec: + Input, Output, Acceptance Criteria, Verification, Failure Recovery. Missing fields generated as stubs. | Layer 3: step files |
| 7 | **Complete File Structure** | Index or payload. Full `.claude/` tree showing every file the skill will create. | All layers |

## Optional Sections

These enhance the build but aren't required. If missing, the build proceeds with warnings.

| # | Section | Where to Find | Maps To |
|---|---------|---------------|---------|
| 8 | **Reference File Frontmatter** | Payload. Per-reference: artifact_type, related_step, purpose, source, canonical_hash. | Layer 4: reference files |
| 9 | **INDEX.md Structure** | Payload. Wikilink format, organized by step and artifact type. | Layer 4: references/INDEX.md |
| 10 | **Contract Definitions** | Payload. Per-step: validation rules, mechanical checks, canonical reference pointers. | Layer 5: contract JSONs |
| 11 | **State Persistence Schema** | Payload. What gets saved, where, what triggers save. | Layer 2: workflow.md state section |
| 12 | **Hook Specifications** | Payload. Mechanical validations that need hard gate enforcement. | Layer 6: hook files |

## How to Validate

For each section in the required list:

1. **Search the design doc index** for the section header or equivalent content
2. **Follow wikilinks** to payload files if the index is a pointer
3. **Check content depth:**
   - Identity: at least one sentence describing the agent's role
   - Philosophy: at least 3 principles
   - Vocabulary: at least 3 terms defined
   - Critical rules: at least 2 rules
   - Workflow: at least 2 steps with all 4 columns filled
   - Step specs: each step has at minimum Purpose + Procedure
   - File structure: shows at least skills/ directory tree

## Failure Modes

| Missing Section | Impact | Recovery |
|----------------|--------|----------|
| Identity | Can't write SKILL.md — agent role unknown | Ask user to add identity to design doc |
| Philosophy | Can't write SKILL.md — no guiding principles | Ask user to add 3-5 principles |
| Vocabulary | Ambiguous terms during execution | Generate with warning — terms may be unclear |
| Critical rules | No hard constraints | Generate with warning — no guardrails |
| Workflow summary | Can't determine step count or structure | STOP — this is the skeleton |
| Step specs | Can't generate step files | STOP — steps are the core |
| File structure | Can't verify completeness in Step 8 | Generate best-guess structure, warn |

## Example: Passing Validation

Design doc: `.claude/docs/design/validate-tc/index.md`

```
✓ Skill Identity: "You are a test case data validator..."
✓ Philosophy: 5 principles (one TC at a time, isolate test variable, ...)
✓ Vocabulary: 7 terms defined (corpus, truth table, data component, ...)
✓ Critical Rules: 5 rules (never validate two TCs, always verify MDC, ...)
✓ Workflow Summary: 10 steps with Responsibility + Output + HITL columns
✓ Step Specs: in references/workflow.md — all steps have Purpose + Procedure
✓ File Structure: in references/rules-and-state.md — full tree shown

Optional:
⚠ Reference Frontmatter: not specified (will generate stubs)
⚠ Contract Definitions: not specified (will skip Layer 5)
✓ State Persistence: in references/rules-and-state.md

RESULT: PASS (7/7 required, 2/5 optional)
```

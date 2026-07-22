# Workflow: Steps 1-8

**Cross-cutting rules (read first):** See [[build-command/references/cross-cutting-rules]] — no-code rule, name extraction, rebuild handling, failure recovery, 200-line threshold, reference linking, HITL modes.

---

## Step 1: Validate Design Doc

**Purpose:** Verify the design doc has all required sections before generating anything.

**Procedure:**
1. Extract command name from design doc path (parent folder name)
2. Check if `.claude/skills/[name]/` exists → if yes, warn rebuild
3. Initialize state file at `.claude/state/build-command-state.json`
4. Read the design doc index file at the given path
5. Follow wikilinks to read all referenced payload files
6. Check each section against the completeness checklist — see [[build-command/references/input-contract]]
7. For each section: present (with location) or missing

**Output:** Completeness report.

**HITL: FULL STOP.** Present the completeness report to the user:

```
DESIGN DOC VALIDATION: [design-doc-path]

Required (must have all 7):
  ✓ Skill Identity — [location]
  ✓ Philosophy — [location]
  ✗ Vocabulary — MISSING
  ...

Optional (enhances build):
  ⚠ Contract Definitions — not specified (Layer 5 will be skipped)
  ...

RESULT: [PASS | FAIL — N/7 required sections missing]
```

| Result | User Options |
|--------|-------------|
| **All 7 required present** | `proceed` — start generating. `review` — user wants to read design doc first. |
| **Required sections missing** | `update` — user will update design doc, then re-run Step 1. `proceed anyway` — generate what's possible, skip missing layers. `stop` — abort. |
| **Optional sections missing** | Noted as warnings. Agent proposes: generate stubs for missing optional layers? User confirms. |

**No autonomous continuation.** The user must see what the corpus (design doc) contains before the agent generates anything from it.

---

## Step 2: Generate SKILL.md (Layer 2)

**Purpose:** Create the skill orchestrator from design doc's identity, philosophy, vocabulary, and critical rules.

**Procedure:**
1. Read the design doc's Skill Identity section → write `## Identity`
2. Read Philosophy → write `## Philosophy`
3. Read Vocabulary → write `## Vocabulary`
4. Read Critical Rules → write `## Critical Rules`
5. Read the workflow summary → write `## Workflow` (overview only — details go in workflow.md)
6. Generate `## File Index` listing all files that will be created

**Input:** Design doc sections: identity, philosophy, vocabulary, critical rules, workflow summary.

**Output:** `.claude/skills/[name]/SKILL.md`

**Template:** See [[build-command/references/layer-templates#SKILL.md]]

**HITL: CHECKPOINT.** Present the generated SKILL.md content to the user before writing. This is the foundation — identity, philosophy, vocabulary, rules. If these are wrong, every downstream file inherits the error.

```
SKILL.md PREVIEW: /[command-name]

Identity: [one sentence]
Philosophy: [N principles]
Vocabulary: [N terms]
Critical Rules: [N rules]
Steps: [N steps listed]

Approve? (approve / modify / stop)
```

| Response | Action |
|----------|--------|
| **approve** | Write SKILL.md, proceed to Step 3 |
| **modify** | User provides corrections, agent updates, re-presents |
| **stop** | Abort build |

---

## Step 3: Generate Workflow + Gates (Layer 2)

**Purpose:** Create workflow definition and phase gate contract.

**Procedure:**
1. Read workflow/step summary → write phase definitions
2. Read state persistence schema → write state section
3. Read phase gates (if specified) → write gate-contract.md
4. Document HITL stops if design doc specifies them

**Output:** `.claude/skills/[name]/workflow.md` + `gate-contract.md`

---

## Step 4: Generate Steps (Layer 3)

**Purpose:** Create one step file per workflow step from the design doc's step file specs.

**Procedure:**
For each step in the design doc:
1. Read the step spec (Purpose, Input, Output, Acceptance Criteria, Procedure, Verification, Failure Recovery)
2. Write `step-NN-[name].md` with all sections
3. Add References section pointing to relevant reference files (from design doc)

**Input:** Design doc section: step file specs.

**Output:** `.claude/skills/[name]/steps/step-NN-[name].md` (one per step)

**Template:** See [[build-command/references/layer-templates#Step Files]]

**Rule:** Step count must match design doc exactly. If the design doc specifies 5 steps, generate 5 step files. Not 4, not 6.

---

## Step 5: Generate References (Layer 4)

**Purpose:** Create the reference index that links back to design doc references. No content duplication.

**Procedure:**
1. Read the design doc's Design Documents table to find all reference payloads
2. Create `references/INDEX.md` with wikilinks pointing to design doc references:
   - Format: `→ .claude/docs/design/[name]/references/[file].md` (absolute path)
   - Organized by step and by artifact type
3. If the design doc specifies additional canonical examples not in its own references:
   - Create stub files with frontmatter + "Content to be added from [source]"
4. Do NOT copy design doc reference content into skill references

**Input:** Design doc's Design Documents table + reference file frontmatter (if specified).

**Output:**
- `.claude/skills/[name]/references/INDEX.md` (links to design doc references)
- Stub files only if new canonical examples are needed

**Rule:** The design doc is the source of truth for reference content. The skill's INDEX.md is a routing table, not a content store.

---

## Step 6: Generate Contracts (Layer 5)

**Purpose:** Create validation contract JSON files from the design doc's contract definitions.

**Procedure:** For each step with contract definitions: read spec → write `contracts/step-NN-contract.json` with contract_metadata, validations (soft gate), and mechanical_validations (hard gate). Follow schema from command-skill-pattern.

**Output:** `.claude/skills/[name]/contracts/step-NN-contract.json` (one per step with contracts)

**Rule:** Only generate contracts for steps that specify them. Not every step needs one.

---

## Step 7: Generate Command Entry Point (Layer 1)

**Purpose:** Create the user-facing command file that routes to the skill.

**Procedure:**
1. Read the design doc's input/output spec and usage examples
2. Write `.claude/commands/kernel/[name].md` with:
   - Usage section (signature, arguments)
   - Input modes (if multiple)
   - Examples
   - Link to design doc
   - Link to skill

**Input:** Design doc sections: input, output, usage examples (if any).

**Output:** `.claude/commands/kernel/[name].md`

**Template:** See [[build-command/references/layer-templates#Command Entry Point]]

---

## Step 8: Verify Build

**Purpose:** Check all generated files against command-skill-pattern requirements and tiered-index thresholds.

**Procedure:**
1. List all generated files (from `files_written` in state)
2. Per-layer checks: command has Usage/Examples/Design Reference link; SKILL.md has all 5 sections; workflow has phases + state; step count matches design doc; INDEX.md wikilinks resolve; contract JSON is valid; hooks only if specified
3. **200-line threshold:** verify every generated file ≤ 200 lines. Flag violations.
4. **Staleness hash:** compute sha256 of design doc index. Write to SKILL.md frontmatter as `design_doc_hash`. Future rebuilds compare this to detect drift.
5. All pass → delete state file. Any fail → report + keep state for re-run.

**Output:**
```
BUILD COMPLETE: /[command-name]
Design doc: [path] (hash: [sha256])
Files created: N | 200-line check: ✓ | Warnings: [count]
  L1 Command ✓ | L2 Skill ✓ | L3 Steps ✓ | L4 Refs ✓ | L5 Contracts ✓ | L6 Hooks ✓/skipped
```

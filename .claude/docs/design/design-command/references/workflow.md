# Workflow: Steps 1-7

---

## Step 1: Parse Intent

**Purpose:** Extract command name and description from user input.

**Procedure:**
1. Read the argument — split into command name (kebab-case) and description
2. If only description given, propose a name: derive from key verbs + nouns, kebab-case
3. Verify name doesn't conflict: check `.claude/docs/design/[name]/` doesn't exist
4. If exists, offer: `overwrite` (rebuild), `rename`, or `stop`
5. Confirm name with user

**Output:** Confirmed command name + description.

**HITL:** Confirm command name before proceeding.

---

## Step 2: Select Reference Design

**Purpose:** Pick the best existing design doc to use as structural template.

**Procedure:**
1. Read all existing design doc indexes:
   - `.claude/docs/design/build-command/index.md`
   - (and any others found via glob)
2. Compare description to each reference design:
   - Data processing / validation → gap-check (corpus detection, per-item loops)
   - Code generation / scaffolding → build-command (input validation, file generation)
   - Pipeline / orchestration → execute-pipeline or spawn-agent-swarm patterns
3. Select best match based on workflow similarity
4. Read the selected reference design fully (index + all payloads)

**Output:** Reference design path + rationale.

**Rule:** Always select a reference. Never design from scratch.

---

## Step 3: Interview

**Purpose:** Extract structured requirements from the user through targeted questions.

**Procedure:**
1. Present the reference design's workflow summary as a starting point
2. Ask the user to describe their command's workflow in similar terms
3. For each requirement category, extract or confirm:
   - **Steps:** What are the phases? What order?
   - **Inputs:** What does the command take? File paths? Names? Modes?
   - **Outputs:** What does it produce? Files? Reports? State changes?
   - **Constraints:** What must never happen? What are the hard rules?
   - **HITL:** Where does the user need to approve before continuing?
   - **State:** What needs to persist for resume?
4. Organize into structured format matching the completeness checklist

**Output:** Structured requirements object covering all 7 required sections.

**HITL:** This step IS the interview — fully interactive. See [[design-command/references/interview-protocol]].

**Rule:** If the user gives a comprehensive description upfront, don't ask redundant questions. Extract what's there, confirm gaps only.

---

## Step 4: Draft Design Doc

**Purpose:** Generate the complete design doc content from structured requirements.

**Procedure:**
1. Read the reference design's index.md — use as structural template
2. Read command-skill-pattern completeness checklist
3. For each required section, generate content from interview results:
   - **Skill Identity:** One sentence from description + interview
   - **Philosophy:** 3-5 principles from constraints + user values
   - **Vocabulary:** Terms that emerged during interview
   - **Critical Rules:** Hard constraints from interview
   - **Workflow Summary:** Steps table from interview
   - **Step Specs:** Per-step Purpose + Procedure (in workflow.md payload)
   - **File Structure:** Derive from step count + whether contracts/hooks needed
4. For optional sections, generate if requirements exist:
   - Contract definitions (if user specified validation rules)
   - State persistence (if resume needed)
   - Hook specs (if mechanical gates needed)
5. Split into index.md (overview, tables, links) + references/ payloads (details)

**Output:** Draft content for all files.

**Rule:** Follow tiered-index-architecture. Index stays under 200 lines. Details go to payloads.

---

## Step 5: Validate Completeness

**Purpose:** Check the draft against build-command's input-contract before writing.

**Procedure:**
1. Read `.claude/docs/design/build-command/references/input-contract.md`
2. For each of the 7 required sections, verify:
   - Present in draft (index or payload)
   - Meets minimum depth (identity: 1 sentence, philosophy: 3+ principles, vocabulary: 3+ terms, rules: 2+ rules, workflow: 2+ steps, step specs: purpose + procedure each, file structure: shows skills/ tree)
3. For each of the 5 optional sections, note presence/absence
4. Report results

**Output:**
```
COMPLETENESS CHECK: /[command-name]

Required (7/7):
  ✓ Skill Identity — index.md
  ✓ Philosophy — index.md (4 principles)
  ✓ Vocabulary — index.md (6 terms)
  ✓ Critical Rules — index.md (5 rules)
  ✓ Workflow Summary — index.md (7 steps)
  ✓ Step Specs — references/workflow.md
  ✓ File Structure — index.md

Optional (2/5):
  ✓ State Persistence — references/workflow.md
  ✓ Contract Definitions — references/workflow.md
  ⚠ Reference Frontmatter — not specified
  ⚠ INDEX.md Structure — not specified
  ⚠ Hook Specifications — not specified

RESULT: PASS (7/7 required)
```

**Failure:** If any required section is missing, loop back to Step 3 to fill the gap.

---

## Step 6: Write Files

**Purpose:** Save the validated design doc to disk.

**Procedure:**
1. Create directory: `.claude/docs/design/[name]/references/`
2. Write `index.md` (the index file)
3. Write `references/workflow.md` (step details)
4. Write any additional payload files identified in Step 4
5. Verify all files written successfully

**Output:** Files on disk at `.claude/docs/design/[name]/`.

---

## Step 7: Report

**Purpose:** Summarize what was created and next steps.

**Output:**
```
DESIGN DOC CREATED: /[command-name]

Path: .claude/docs/design/[name]/index.md
Reference design: [which existing design was used as template]
Completeness: 7/7 required, N/5 optional
Files: N files written
Steps: M workflow steps defined

Ready for: /build-command .claude/docs/design/[name]/index.md
```

**State cleanup:** Delete `.claude/state/design-command-state.json` if it exists.

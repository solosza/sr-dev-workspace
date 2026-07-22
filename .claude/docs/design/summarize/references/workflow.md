# Workflow — /summarize

## Step 1: Resolve Target

**Purpose:** Parse user input and locate all source files for summarization.

**Procedure:**
1. Parse input mode:
   - Number (e.g., `188`) → resolve to `docs/backlog/done/188-*.md` or `docs/backlog/188-*.md`
   - Path (e.g., `projects/ssh-*`) → glob-expand, use as deliverable folder
   - Empty → scan review-status.json for unreviewed items, pick next
2. For backlog mode: locate related files:
   - Backlog file: `docs/backlog/done/NNN-*.md` or `docs/backlog/NNN-*.md`
   - Task folder: `tasks/completed/[project-name]/` or `tasks/[project-name]/`
   - Deliverable folder: `projects/[project-name]/` or path from backlog Location field
   - Agent state: `.claude/state/agent-[project-name]-*.json`
3. Output: structured paths object

**Pre-generation checkpoint:**
- Read `review-status.json` to check if summary already exists for this target
- Read backlog file to confirm it exists and extract the project name

## Step 2: Gather Sources

**Purpose:** Read all source files into structured data for diffing.

**Procedure:**
1. Read backlog file → extract Requirements section (each bullet/checkbox is a requirement)
2. Read task index (`000-index.md`) → extract task list with completion status
3. Read deliverable files → build inventory (path, type, brief description from first lines)
4. Read agent state → extract completion status, errors, skipped tasks

**Pre-generation checkpoint:**
- Verify backlog requirements are parseable (have clear bullet points or checkboxes)
- Verify at least one deliverable file exists

## Step 3: Diff Requirements

**Purpose:** Check each backlog requirement against deliverables.

**Procedure:**
1. For each requirement from the backlog:
   - Search deliverables for evidence that the requirement is met
   - Evidence: file exists at specified path, content matches description, test passes
2. Assign status per requirement:
   - **Met** — deliverable clearly satisfies the requirement (include file path as evidence)
   - **Partial** — some aspects addressed, others missing (include notes on what's missing)
   - **Not addressed** — no deliverable maps to this requirement
3. Output: requirement diff table

## Step 4: Classify Findings

**Purpose:** Separate items that need human decisions from informational items.

**Procedure:**
1. Scan deliverables and agent state for:
   - Recommendations with multiple options → **Decision needed**
   - Open questions or trade-offs → **Decision needed**
   - Completions, findings, facts → **Informational**
   - Failures, skips, blockers → **Problem**
2. Group into three categories: decisions, informational, problems

## Step 5: Format Summary

**Purpose:** Produce the dynamic summary report.

**Procedure:**
1. Assemble sections using the summary format template (→ `summary-format.md`)
2. Dynamic sizing: include all items in each section. No truncation.
3. For backlog summaries: include the requirement diff table
4. For project folder summaries: include deliverable inventory only (no requirement diff)

## Step 6: Write + Report

**Purpose:** Persist the summary and display it.

**Procedure:**
1. **Integrated mode** (called by `/kernel/complete`):
   - Read review-status.json
   - Add/update the backlog entry with a `summary` key containing the formatted summary
   - Write review-status.json
2. **Standalone mode** (called by user):
   - Display summary in conversation output
   - Optionally write to review-status.json if the backlog has an entry
3. Report: show the summary

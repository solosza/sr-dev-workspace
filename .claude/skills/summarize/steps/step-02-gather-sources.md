# Step 2: Gather Sources

## Purpose

Read all source files into structured data for diffing and summarization.

## Procedure

1. **Read backlog file** (if backlog mode):
   - Extract title (first heading)
   - Extract scope (BUILD/RESEARCH/REFACTOR)
   - Extract Requirements section — each bullet/checkbox is one requirement
   - Extract Location field (deliverable paths)

2. **Read task index** (if task folder exists):
   - Read `000-index.md` for task list
   - Count total tasks, completed tasks, skipped tasks
   - Read `gate-contract.md` if present

3. **Read deliverable files:**
   - Inventory all files in deliverable paths
   - For each file: record path, type (created/modified), brief description from first lines
   - For BUILD scope: check `.claude/skills/`, `.claude/commands/`, `.claude/docs/design/`
   - For RESEARCH scope: check `projects/[slug]/`

4. **Read agent state** (if exists):
   - Extract `completed_tasks`, `skipped_tasks`, errors
   - Check for `complete: true` or `cycling_complete: true`

## Acceptance Criteria

- [ ] Backlog requirements parsed into list (if backlog mode)
- [ ] Deliverable inventory built with file paths and descriptions
- [ ] Task completion status known (if task folder exists)

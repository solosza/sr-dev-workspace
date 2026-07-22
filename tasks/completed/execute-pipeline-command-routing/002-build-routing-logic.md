# Task 002: Build Routing Logic

## Objective
Add command/skill detection and routing to execute-pipeline so it invokes `/design` → `/build-command` for command builds instead of task-builder.

## Instructions

1. Modify the execute-pipeline skill at the routing insertion point identified in task 001
2. Add detection logic after backlog is read (Step 1/2) but before task-builder (Step 3):

   **Detection signals (any of these = command route):**
   - Backlog `Scope: BUILD` AND deliverable mentions "command", "skill", or "/kernel/"
   - Backlog `Location` targets `.claude/commands/` or `.claude/skills/`
   - Backlog title contains "build [name] command" or "build [name] skill"

3. **Command route (new path):**
   - Extract command name and description from backlog
   - Invoke `/design [name] [description]` (produces design doc)
   - Invoke `/build-command` with the design doc path (produces skill package)
   - Skip task-builder entirely
   - Proceed to Step 5 (validate + report)

4. **Default route (existing path, unchanged):**
   - If detection signals are absent, proceed through task-builder as before
   - No changes to existing behavior

5. Update SKILL.md to document the routing:
   - Add a "Routing" section explaining the two paths
   - Update the step table to show the branch point

## Acceptance Criteria
- [ ] Detection logic added to execute-pipeline skill
- [ ] Command route invokes /design then /build-command
- [ ] Default route unchanged (task-builder path)
- [ ] SKILL.md updated with routing documentation
- [ ] No existing execute-pipeline tests broken

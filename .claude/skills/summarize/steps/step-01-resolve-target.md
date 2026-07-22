# Step 1: Resolve Target

## Purpose

Parse the user input and locate all source files needed for summarization.

## Procedure

1. **Parse input mode:**
   - Number (e.g., `188`) → backlog mode
   - Path (e.g., `projects/ssh-*`) → path mode
   - Empty → batch mode (find unreviewed completions)

2. **Backlog mode:**
   - Glob `docs/backlog/done/NNN-*.md` first, then `docs/backlog/NNN-*.md`
   - Extract slug from filename (strip scope prefix: `kernel-research-`, `domain-build-`, etc.)
   - Find task folder: `tasks/completed/[slug]/` or `tasks/[slug]/`
   - Find deliverables: `projects/[slug]/` or path from backlog Location field
   - Find agent state: `.claude/state/agent-[slug]-*.json`

3. **Path mode:**
   - Glob-expand the input path
   - Search `docs/backlog/done/` for backlogs referencing the project folder
   - Find related task folder and agent state

4. **Batch mode:**
   - Read `.claude/state/review-status.json`
   - Scan `docs/backlog/done/` for all completed backlogs
   - Find backlogs NOT in review-status.json or with unreviewed status
   - Pick next by priority (same as review-queue ordering)
   - Resolve using backlog mode

5. **Output:** Structured paths object:
   ```
   backlog_path: [path or null]
   task_folder: [path or null]
   deliverable_paths: [array of paths]
   agent_state_path: [path or null]
   mode: [backlog | path | batch]
   ```

## Acceptance Criteria

- [ ] Input mode correctly detected
- [ ] At least one source file found
- [ ] Paths validated (files exist)

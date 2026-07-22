# Step 3c: Run Command Build (Command Route Only)

Invoke `/design` then `/build-command` to produce a complete skill package. **Only runs when `pipeline_state.route` is `command`.**

## Skip Check

1. Read `pipeline_state.route` from `session_state.json`
2. If `default` → skip this step, proceed to step 3 (task-builder)
3. If `command` → continue below

## Process

1. **Invoke `/design` inline:**

   Pass the command name and description from pipeline state:
   ```
   /design [pipeline_state.command_name] [pipeline_state.command_description]
   ```

   /design will:
   - Parse the intent (step 1)
   - Select a reference design (step 2)
   - Interview for requirements (step 3) — in pipeline mode, extract from backlog instead of interactive interview
   - Draft the design doc (step 4)
   - Validate completeness (step 5)
   - Write files to `.claude/docs/design/[name]/` (step 6)
   - Report (step 7)

   **Pipeline adaptation:** When running inside execute-pipeline, /design should extract requirements from the backlog file (`pipeline_state.backlog_path`) instead of conducting an interactive interview. The backlog's Requirements and Task Builder Input sections contain the structured requirements.

2. **Capture design doc path:**
   - The design doc will be at `.claude/docs/design/[command_name]/index.md`
   - Update pipeline state with the path

3. **Invoke `/build-command` inline:**

   Pass the design doc path:
   ```
   /build-command .claude/docs/design/[command_name]/index.md
   ```

   /build-command will:
   - Validate the design doc (step 1)
   - Generate SKILL.md (step 2)
   - Generate workflow + gates (step 3)
   - Generate step files (step 4)
   - Generate references (step 5)
   - Generate contracts (step 6)
   - Generate command entry point (step 7)
   - Verify the build (step 8)

4. **Update pipeline state:**

   Merge into `session_state.json`:
   ```json
   {
     "pipeline_state": {
       "design_doc_path": ".claude/docs/design/[name]/index.md",
       "skill_path": ".claude/skills/[name]/SKILL.md",
       "command_path": ".claude/commands/kernel/[name].md"
     }
   }
   ```

5. **Skip step 3 and step 4 — proceed directly to step 5 (validate + report).**

   The command route does not produce task files or use run-task.sh. The deliverables are the design doc and skill package, validated by /build-command's step 8 verification.

## Output

```
PIPELINE — COMMAND BUILD COMPLETE

Design doc: .claude/docs/design/[name]/index.md
Skill package: .claude/skills/[name]/
Command: .claude/commands/kernel/[name].md

Proceeding to step 5 (validate + report).
```

## Rules

- This step replaces BOTH step 3 (task-builder) and step 4 (execute-tasks) for command route
- /design and /build-command run inline — no background agents, no run-task.sh
- If /design fails (incomplete requirements), stop pipeline and report — do not proceed to /build-command
- If /build-command fails (verification errors), report failures in step 5
- The command route is fully autonomous — no user prompts between /design and /build-command

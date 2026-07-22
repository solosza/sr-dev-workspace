# Step 2b: Detect Route

Determine whether the backlog deliverable is a command/skill (command route) or something else (default route).

## Process

1. **Read the backlog file:**
   - Read `pipeline_state.backlog_path` from `session_state.json`
   - Read the backlog file contents

2. **Check detection signals:**

   Any of these signals = **command route**:

   | Signal | Where to check |
   |--------|---------------|
   | `Scope: BUILD` AND deliverable mentions "command", "skill", or "/kernel/" | Summary, Requirements, or Task Builder Input sections |
   | `Location` targets `.claude/commands/` or `.claude/skills/` | Location field in Task Builder Input |
   | Title contains "build [name] command" or "build [name] skill" | Backlog title (first heading) |
   | Deliverable explicitly says "command entry point" or "skill package" | Requirements or Task Builder Input |

3. **If command route detected, extract command name:**
   - From title: "Build [name] Command" → name is `[name]` in kebab-case
   - From deliverable description: look for the command/skill name
   - From Location field: `.claude/skills/[name]/` → name is `[name]`

4. **Set route in pipeline state:**

   Merge into `session_state.json`:
   ```json
   {
     "pipeline_state": {
       "route": "command | default",
       "command_name": "[name] (only if command route)",
       "command_description": "[description extracted from backlog] (only if command route)"
     }
   }
   ```

## Output

```
PIPELINE — ROUTE DETECTED

Route: [command | default]
[If command:] Command name: [name]
[If command:] Description: [one-line summary]
Reason: [which signal matched]

Proceeding to [step 3c (command build) | step 3 (task-builder)].
```

## Rules

- Default to **default route** when no signals match — this preserves existing behavior
- Detection is conservative: all signals must be unambiguous. If uncertain, use default route
- The command name extracted here drives `/design` input in step 3c
- Do NOT modify the backlog file — detection is read-only

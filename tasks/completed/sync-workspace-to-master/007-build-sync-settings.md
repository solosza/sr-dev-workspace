# Task 007: Build — Update settings.local.json Hook Registration

## Objective
Update master's settings.local.json to register all 6 hooks with correct matchers.

## Instructions

1. Read current `D:/my_ai_projects/isagawa-kernel/.claude/settings.local.json`
2. Preserve the `permissions` section (deny/allow lists)
3. Replace the `hooks` section with full registration:
   ```json
   {
     "hooks": {
       "PreToolUse": [
         {
           "matcher": "Edit|Write|Bash",
           "hooks": [
             {
               "type": "command",
               "command": "python .claude/hooks/universal-gate-enforcer.py"
             }
           ]
         },
         {
           "matcher": "Agent",
           "hooks": [
             {
               "type": "command",
               "command": "python .claude/hooks/agent-inline-execution-blocker.py"
             }
           ]
         },
         {
           "matcher": "Write|Edit",
           "hooks": [
             {
               "type": "command",
               "command": "python .claude/hooks/auto-approve-claude-writes.py"
             }
           ]
         }
       ],
       "PostToolUse": [
         {
           "matcher": "Bash",
           "hooks": [
             {
               "type": "command",
               "command": "python .claude/hooks/test-failure-detector.py"
             }
           ]
         },
         {
           "matcher": "Edit|Write|Bash",
           "hooks": [
             {
               "type": "command",
               "command": "python .claude/hooks/actions-log-appender.py"
             }
           ]
         }
       ]
     }
   }
   ```
4. Write the merged file back

## Acceptance Criteria
- settings.local.json has 5 hook entries (3 PreToolUse + 2 PostToolUse)
- Permissions section preserved

## Gate
BUILD-07

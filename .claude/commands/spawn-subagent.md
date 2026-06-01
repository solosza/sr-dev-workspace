---
name: spawn-subagent
type: command
domain: kernel
---

# /spawn-subagent

Spawn an autonomous agent to run in the background. You continue working while the agent executes.

## Usage

```
/spawn-subagent [description of what to do]
```

## Examples

```
/spawn-subagent Test H2 adventure with creature corpus fixes
/spawn-subagent Validate campaign-start and campaign-resume commands
/spawn-subagent Build H3 Pyramid of Shadows adventure pack
/spawn-subagent Run scaling skill production tests
```

## What Happens

1. Agent spawns with your description
2. Runs in background (you don't wait for it)
3. You can continue working on other things
4. System notifies you when agent completes
5. You can check results whenever ready

## When to Use

- Multi-hour tasks (adventure builds, comprehensive tests)
- Parallel work (spawn 2+ agents, work on something else)
- Anything you don't need the result for immediately

## Return Value

You'll get a task ID so you can check progress later:
```
TaskOutput(task_id: "a60aa6d480b923290", block: false)
```

---

**Status:** Ready for use

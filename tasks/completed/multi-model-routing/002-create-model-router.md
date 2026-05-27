# Task 002: Create model-router.sh

**Type:** BUILD
**Action:** Create shell library with route_model function

## What

Create `lib/model-router.sh` — a sourceable shell library that exports a `route_model` function.

The function:
1. Reads the task file path as argument
2. Checks for explicit `model:` frontmatter override in the task file
3. If no override, reads the task content and applies routing heuristics:
   - Count acceptance criteria (lines matching `- [ ]`)
   - Check for haiku keywords (copy, scaffold, format, simple, trivial, rename, move)
   - Check for opus keywords (architecture, refactor, security, migration, multi-file, production, critical)
   - Check task type from header (BUILD, TEST, RESEARCH)
4. Returns model ID to stdout

Fallback: if config missing or routing fails, return default (opus).

```bash
#!/bin/bash
# model-router.sh — Route tasks to appropriate Claude model tier
#
# Usage: source lib/model-router.sh
#        MODEL=$(route_model "path/to/task.md")

route_model() {
  local task_file="$1"
  local config_file="${2:-lib/model-routing-config.json}"

  # Fallback if config missing
  if [ ! -f "$config_file" ]; then
    echo "claude-opus-4-6"
    return
  fi

  # Fallback if task file missing
  if [ ! -f "$task_file" ]; then
    echo "claude-opus-4-6"
    return
  fi

  # Use Python for JSON parsing + routing logic
  $PYTHON_CMD -c "
import json, re, sys

config = json.load(open('$config_file'))
task = open('$task_file').read()

# Check explicit override
override = re.search(r'^model:\s*(\S+)', task, re.MULTILINE)
if override:
    print(override.group(1))
    sys.exit(0)

# Count acceptance criteria
criteria = len(re.findall(r'- \[ \]', task))

# Check keywords (case-insensitive)
task_lower = task.lower()
haiku_keywords = config['tiers']['haiku']['keywords']
opus_keywords = config['tiers']['opus']['keywords']

haiku_hits = sum(1 for k in haiku_keywords if k in task_lower)
opus_hits = sum(1 for k in opus_keywords if k in task_lower)

# Routing decision
rules = config.get('routing_rules', {})

# Explicit complexity signals win
if criteria >= rules.get('opus_if_criteria_above', 5) or opus_hits >= 2:
    print(config['tiers']['opus']['model_id'])
elif criteria <= rules.get('haiku_if_criteria_below', 2) and haiku_hits >= 1 and opus_hits == 0:
    print(config['tiers']['haiku']['model_id'])
else:
    # Default tier: sonnet for standard work
    print(config['tiers']['sonnet']['model_id'])
" 2>/dev/null || echo "claude-opus-4-6"
}
```

## Acceptance Criteria

- [ ] File exists at `lib/model-router.sh`
- [ ] `bash -c "source lib/model-router.sh && type route_model"` exits 0

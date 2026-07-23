#!/bin/bash
#
# model-router.sh — Route tasks to appropriate Claude model tier
#
# Usage: source lib/model-router.sh
#        MODEL=$(route_model "path/to/task.md" "path/to/config.json")

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

  # Resolve Python command (PYTHON_CMD set by common.sh, fallback to python)
  local py="${PYTHON_CMD:-python}"

  # Convert MSYS paths to Windows paths for Python (MSYS /tmp → C:/Users/.../Temp)
  if command -v cygpath &>/dev/null; then
    config_file=$(cygpath -m "$config_file")
    task_file=$(cygpath -m "$task_file")
  fi

  # Normalize paths (Windows backslashes break Python string literals)
  local config_norm="${config_file//\\//}"
  local task_norm="${task_file//\\//}"

  # Use Python for JSON parsing + routing logic
  $py -c "
import json, re, sys

config = json.load(open('$config_norm'))
task = open('$task_norm').read()

# Check explicit override (frontmatter: model: <model-id>)
override = re.search(r'^model:\s*(\S+)', task, re.MULTILINE)
if override:
    print(override.group(1))
    sys.exit(0)

# Count acceptance criteria
criteria = len(re.findall(r'- \[ \]', task))

# Check keywords (case-insensitive)
task_lower = task.lower()
haiku_keywords = config['tiers']['haiku']['keywords']
sonnet_keywords = config['tiers']['sonnet']['keywords']
opus_keywords = config['tiers']['opus']['keywords']

haiku_hits = sum(1 for k in haiku_keywords if k in task_lower)
sonnet_hits = sum(1 for k in sonnet_keywords if k in task_lower)
opus_hits = sum(1 for k in opus_keywords if k in task_lower)

# Routing decision
rules = config.get('routing_rules', {})

# Precedence: opus > sonnet > haiku — on a multi-tier keyword match, the
# HIGHER tier always wins (e.g. 'copy then adapt' hits both haiku ('copy')
# and sonnet ('adapt') -> sonnet). Haiku only fires on an UNAMBIGUOUS
# mechanical match (no sonnet or opus keyword present). Unmatched tasks
# (no keyword hits in any tier) fall through to the sonnet default below —
# no silent cheapest-tier routing.
if criteria >= rules.get('opus_if_criteria_above', 5) or opus_hits >= 2:
    print(config['tiers']['opus']['model_id'])
elif criteria <= rules.get('haiku_if_criteria_below', 2) and haiku_hits >= 1 and opus_hits == 0 and sonnet_hits == 0:
    print(config['tiers']['haiku']['model_id'])
else:
    # Default tier: sonnet — standard work, ties, and unmatched tasks
    print(config['tiers']['sonnet']['model_id'])
" 2>/dev/null || echo "claude-opus-4-6"
}

upgrade_model() {
  local current="$1"
  case "$current" in
    *haiku*) echo "claude-sonnet-4-6" ;;
    *sonnet*) echo "claude-opus-4-6" ;;
    *) echo "$current" ;;  # Already opus or unknown
  esac
}

#!/usr/bin/env python3
"""Sr Dev Gate Enforcer - thin orchestrator using shared validators."""

import json
import os
import sys
from pathlib import Path

_HOOK_DIR = Path(__file__).resolve().parent          # .claude/hooks/
_WORKSPACE_ROOT = _HOOK_DIR.parent.parent            # workspace root
STATE_DIR = _WORKSPACE_ROOT / '.claude' / 'state'

_agent_id = os.environ.get('KERNEL_AGENT_ID')
if _agent_id:
    SESSION_STATE = STATE_DIR / f'agent-{_agent_id}-session-state.json'
else:
    SESSION_STATE = STATE_DIR / 'session_state.json'

sys.path.insert(0, str(_HOOK_DIR))
from state_io import atomic_write_json

# Resolve isagawa-kernel path by walking up from hook file until we find the
# directory containing isagawa-kernel (works in both main workspace and worktrees)
_search = _HOOK_DIR
while _search != _search.parent:
    _candidate = _search.parent / 'isagawa-kernel'
    if _candidate.is_dir():
        kernel_path = str(_candidate)
        break
    _search = _search.parent
else:
    kernel_path = ''
sys.path.insert(0, kernel_path)

try:
    from lib.validators import code_quality, state_validation, bash_validation, common
except ImportError:
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {})

    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\', '/')
        if common.should_skip(file_path):
            sys.exit(0)

        violations = state_validation.check(str(SESSION_STATE))
        if violations:
            common.state_block(violations)

        content = tool_input.get('content', '') or tool_input.get('new_string', '')
        if content:
            violations = code_quality.check(file_path, content)
            if violations:
                common.smart_block(violations, "Code quality")

    elif tool_name == 'Bash':
        command = tool_input.get('command', '')
        violations = bash_validation.check(command)
        if violations:
            common.bash_block(violations)

    sys.exit(0)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""PreCompact hook: invalidate anchor so the next action triggers full re-anchor."""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_HOOK_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_HOOK_DIR))
from state_io import atomic_write_json, read_json

_WORKSPACE = _HOOK_DIR.parent.parent
STATE_DIR = _WORKSPACE / '.claude' / 'state'


def resolve_paths():
    """Resolve session state and workflow paths with KERNEL_AGENT_ID routing."""
    kid = os.environ.get('KERNEL_AGENT_ID', '').strip()
    if kid:
        ss_path = STATE_DIR / f'agent-{kid}-session-state.json'
        wf_path = STATE_DIR / f'agent-{kid}-workflow.json'
        return ss_path, wf_path
    return STATE_DIR / 'session_state.json', None


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        event = {}
    trigger = event.get('trigger', 'unknown')

    ss_path, agent_wf_path = resolve_paths()
    ss = read_json(ss_path)
    if not ss or not ss.get('domain'):
        sys.exit(0)

    domain = ss['domain']
    if agent_wf_path and agent_wf_path.exists():
        wf_path = agent_wf_path
    else:
        agent_id = ss.get('agent_id', '')
        if agent_id:
            candidate = STATE_DIR / f'agent-{agent_id}-workflow.json'
            wf_path = candidate if candidate.exists() else STATE_DIR / f'{domain}_workflow.json'
        else:
            wf_path = STATE_DIR / f'{domain}_workflow.json'

    wf = read_json(wf_path)
    if not wf:
        sys.exit(0)

    wf['anchored'] = False
    atomic_write_json(wf_path, wf, "workflow")

    ss['compaction_anchor_reason'] = f'{trigger}_compaction'
    ss['compaction_timestamp'] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(ss_path, ss, "session_state")

    sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit(0)

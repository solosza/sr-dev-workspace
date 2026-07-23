"""Queryable run-status view for the Isagawa Kernel runner (backlog 276, OBS-04).

The 'operator reads status without tailing raw JSONL' deliverable — the
missing 5th harness layer. Composes 001 (completion_truth), 002
(banner_vs_reality's authoritative-signal pattern) and 003 (liveness_check,
stranded_deliverables) from observability.py; does not re-implement their
detection logic. Read-only: no state writes.
"""

import argparse
import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from observability import _read_json_utf8sig, liveness_check, stranded_deliverables


def _agent_id_from_workflow_name(name):
    """'agent-{id}-workflow.json' -> {id}; '{domain}_workflow.json' -> {domain} (parent/no agent prefix)."""
    if name.startswith('agent-') and name.endswith('-workflow.json'):
        return name[len('agent-'):-len('-workflow.json')], True
    if name.endswith('_workflow.json'):
        return name[:-len('_workflow.json')], False
    return name, False


def _task_progress(workflow):
    total = workflow.get('total_tasks') or 0
    done = len(set(workflow.get('completed_tasks', []) + workflow.get('skipped_tasks', [])))
    if total:
        return f'{done}/{total}'
    return f'{len(workflow.get("completed_tasks", []))} done'


def _is_complete(workflow):
    if workflow.get('complete') is True:
        return True
    total = workflow.get('total_tasks') or 0
    done = len(set(workflow.get('completed_tasks', []) + workflow.get('skipped_tasks', [])))
    return total > 0 and done >= total


def _last_activity(heartbeat_path, workflow_path):
    for p in (heartbeat_path, workflow_path):
        fp = pathlib.Path(p)
        if fp.exists():
            return datetime.datetime.fromtimestamp(
                fp.stat().st_mtime, tz=datetime.timezone.utc
            ).strftime('%Y-%m-%dT%H:%M:%SZ')
    return 'unknown'


def _stranded_index(repo_root, main_branch, branch_prefix):
    """workflow filename -> [branch, ...] for branches whose committed routed
    state names this workflow file with complete=true (best-effort; empty is
    common and expected per observability.stranded_deliverables docstring)."""
    result = stranded_deliverables(repo_root, main_branch=main_branch, branch_prefix=branch_prefix)
    index = {}
    for candidate in result['stranded']:
        for filename in candidate['routed_complete_evidence']:
            index.setdefault(filename, []).append(candidate['branch'])
    return result, index


def build_status_rows(repo_root, state_dir=None, main_branch='main', branch_prefix='worktree-agent-',
                       threshold_seconds=300, dead_multiplier=3):
    repo_root = pathlib.Path(repo_root)
    state_dir = pathlib.Path(state_dir) if state_dir else repo_root / '.claude' / 'state'

    stranded_result, stranded_by_filename = _stranded_index(repo_root, main_branch, branch_prefix)

    rows = []
    for wf_path in sorted(state_dir.glob('*_workflow.json')) + sorted(state_dir.glob('agent-*-workflow.json')):
        name = wf_path.name
        agent_id, is_agent = _agent_id_from_workflow_name(name)
        if not is_agent and not name.endswith('_workflow.json'):
            continue

        try:
            workflow = _read_json_utf8sig(wf_path)
        except (json.JSONDecodeError, OSError) as exc:
            rows.append({
                'agent': agent_id, 'status': 'unreadable', 'last_activity': 'unknown',
                'progress': 'n/a', 'detail': str(exc),
            })
            continue

        heartbeat_path = state_dir / f'{agent_id}_runner-heartbeat.json'
        liveness = liveness_check(heartbeat_path, workflow_path=wf_path,
                                   threshold_seconds=threshold_seconds, dead_multiplier=dead_multiplier)

        if _is_complete(workflow):
            branches = stranded_by_filename.get(name)
            status = 'complete-unmerged' if branches else 'merged'
            detail = f'unmerged on: {", ".join(branches)}' if branches else ''
        elif liveness['status'] == 'dead':
            status, detail = 'dead', liveness['message']
        elif liveness['status'] == 'stalled':
            status, detail = 'stalled', liveness['message']
        else:
            status, detail = 'running', liveness.get('message', 'no heartbeat yet')

        rows.append({
            'agent': agent_id,
            'status': status,
            'last_activity': _last_activity(heartbeat_path, wf_path),
            'progress': _task_progress(workflow),
            'detail': detail,
        })

    return rows, stranded_result


def format_table(rows):
    if not rows:
        return '(no agent/pipeline workflow state found)'

    headers = ('AGENT/PIPELINE', 'STATUS', 'LAST-ACTIVITY', 'PROGRESS', 'DETAIL')
    widths = [len(h) for h in headers]
    for r in rows:
        vals = (r['agent'], r['status'], r['last_activity'], r['progress'], r['detail'])
        widths = [max(w, len(str(v))) for w, v in zip(widths, vals)]

    def fmt_row(vals):
        return '  '.join(str(v).ljust(w) for v, w in zip(vals, widths))

    lines = [fmt_row(headers), fmt_row(['-' * w for w in widths])]
    for r in rows:
        lines.append(fmt_row((r['agent'], r['status'], r['last_activity'], r['progress'], r['detail'])))
    return '\n'.join(lines)


def _main():
    parser = argparse.ArgumentParser(description='Kernel run-status view (backlog 276, OBS-04)')
    parser.add_argument('--repo', default='.', help='repo root containing .claude/state')
    parser.add_argument('--state-dir', default=None, help='override state dir (default: <repo>/.claude/state)')
    parser.add_argument('--main-branch', default='main')
    parser.add_argument('--branch-prefix', default='worktree-agent-')
    parser.add_argument('--threshold-seconds', type=int, default=300)
    parser.add_argument('--dead-multiplier', type=int, default=3)
    parser.add_argument('--json', action='store_true', help='emit JSON instead of a table')
    args = parser.parse_args()

    rows, stranded_result = build_status_rows(
        args.repo, state_dir=args.state_dir, main_branch=args.main_branch,
        branch_prefix=args.branch_prefix, threshold_seconds=args.threshold_seconds,
        dead_multiplier=args.dead_multiplier,
    )

    if args.json:
        print(json.dumps({'rows': rows, 'stranded_summary': stranded_result}, indent=2))
        return

    print(format_table(rows))
    print(f"\n{len(rows)} agent/pipeline row(s); {stranded_result['stranded_count']} unmerged branch(es) with deliverables")


if __name__ == '__main__':
    _main()

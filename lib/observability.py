"""Observability helpers for the Isagawa Kernel runner (backlog 276).

Detects divergence between claimed state (routed workflow.json) and
ground-truth evidence (git commits + artifacts). Composes with 270's
verify_completion_write (which prevents divergence) and 271 (state
routing) — this module DETECTS what those PREVENT, it does not
re-implement their write-path logic.
"""

import json
import pathlib
import subprocess
import time


def _read_json_utf8sig(path):
    """Read JSON defensively — a prior session's PowerShell writes left a
    UTF-8 BOM that breaks strict-utf-8 parsing (lesson 2026-07-22)."""
    return json.loads(pathlib.Path(path).read_text(encoding='utf-8-sig'))


def _artifact_evidence(paths):
    for p in paths:
        fp = pathlib.Path(p)
        if fp.is_file() and fp.stat().st_size > 0:
            return True
        if fp.is_dir() and any(f.is_file() and f.stat().st_size > 0 for f in fp.rglob('*')):
            return True
    return False


def _commit_evidence(repo_root, paths):
    for p in paths:
        result = subprocess.run(
            ['git', 'log', '--oneline', '-1', '--', p],
            cwd=repo_root, capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return True
    return False


def completion_truth(workflow_path, repo_root, deliverable_paths=None, task_paths=None):
    """Reconcile claimed completion against ground-truth evidence.

    workflow_path: path to the routed workflow.json (agent-{id}-workflow.json
        or {domain}_workflow.json)
    repo_root: repo root to run git commands in
    deliverable_paths: default list of paths checked for every claimed task
    task_paths: optional {task_name: [paths]} override for specific tasks

    Returns a structured verdict; never trusts the banner or self-report —
    only commit history and non-empty artifacts count as evidence.
    """
    task_paths = task_paths or {}
    wf = pathlib.Path(workflow_path)
    if not wf.exists():
        return {'claimed_tasks': [], 'verdicts': {}, 'divergences': [],
                'error': f'workflow file not found: {workflow_path}'}

    w = _read_json_utf8sig(wf)
    claimed = list(w.get('completed_tasks', []))

    verdicts = {}
    divergences = []
    for task in claimed:
        paths = task_paths.get(task, deliverable_paths)
        if not paths:
            verdicts[task] = {'evidence': None, 'reason': 'no deliverable path provided'}
            continue
        artifact_ok = _artifact_evidence(paths)
        commit_ok = _commit_evidence(repo_root, paths)
        has_evidence = artifact_ok or commit_ok
        verdicts[task] = {
            'evidence': has_evidence,
            'commit_evidence': commit_ok,
            'artifact_evidence': artifact_ok,
            'paths_checked': paths,
        }
        if not has_evidence:
            divergences.append(task)

    return {'claimed_tasks': claimed, 'verdicts': verdicts, 'divergences': divergences}


_COMPLETION_MARKERS = ('ALL_TASKS_COMPLETE', 'STEP_COMPLETE', 'ONE_SHOT_COMPLETE')


def _iteration_log_evidence(log_paths):
    """Check iteration logs for non-empty content bearing a completion marker.

    Returns {path: bool} — True means the log is authoritative evidence the
    run actually progressed, independent of what the wrapper banner claims
    (guards the empty-stdout false-fail class, lesson 261).
    """
    evidence = {}
    for p in log_paths or []:
        fp = pathlib.Path(p)
        if fp.is_file() and fp.stat().st_size > 0:
            text = fp.read_text(encoding='utf-8', errors='replace')
            evidence[str(fp)] = any(m in text for m in _COMPLETION_MARKERS)
        else:
            evidence[str(fp)] = False
    return evidence


def banner_vs_reality(workflow_path, repo_root, banner_completed, banner_failed,
                       deliverable_paths=None, task_paths=None, iteration_log_paths=None):
    """Compute a run's TRUE outcome from authoritative signals and surface
    disagreement with the wrapper banner as a first-class alert.

    Authoritative signals: routed workflow state (completed_tasks/skipped_tasks)
    + artifact/commit evidence (via completion_truth) + iteration log completion
    markers. The banner (banner_completed/banner_failed, as reported by
    run-task.sh's "Completed: N / Failed: N" lines) is never trusted on its own —
    this is the anti-'banner lies' primitive (the 261 case: banner '3 failed'
    while state shows all complete + artifacts written).
    """
    wf = pathlib.Path(workflow_path)
    skipped = []
    if wf.exists():
        skipped = list(_read_json_utf8sig(wf).get('skipped_tasks', []))

    truth = completion_truth(workflow_path, repo_root, deliverable_paths, task_paths)
    true_completed = len(truth['claimed_tasks']) - len(truth['divergences'])
    true_failed = len(skipped) + len(truth['divergences'])
    log_evidence = _iteration_log_evidence(iteration_log_paths)

    alerts = []
    if banner_completed != true_completed:
        alerts.append(
            f"DISAGREEMENT: banner reported {banner_completed} completed, "
            f"true evidence shows {true_completed} completed "
            f"(divergences: {truth['divergences']})"
        )
    if banner_failed != true_failed:
        alerts.append(
            f"DISAGREEMENT: banner reported {banner_failed} failed, "
            f"true evidence shows {true_failed} failed (skipped: {skipped})"
        )

    return {
        'true_outcome': {
            'completed': true_completed,
            'failed': true_failed,
            'divergences': truth['divergences'],
            'skipped': skipped,
        },
        'banner_reported': {'completed': banner_completed, 'failed': banner_failed},
        'log_evidence': log_evidence,
        'disagreement': bool(alerts),
        'alerts': alerts,
    }


def liveness_check(heartbeat_path, workflow_path=None, threshold_seconds=300, dead_multiplier=3):
    """Read-only liveness classifier consuming the 262 heartbeat.

    Unlike common.sh's check_stall (RH-02, in-loop, self-reported by the still-
    running runner), this is an EXTERNAL read of the heartbeat file's mtime —
    it works even after the runner process is gone (the factory-died-at-step-N
    class, where nothing is left to call check_stall again). Never mutates
    state; the "visible signal" is the returned status/message, surfaced by
    the caller (e.g. the OBS-04 status view), not a silent file write.

    Returns {status, age_seconds, threshold_seconds, message} where status is
    one of: 'no_heartbeat', 'complete', 'healthy', 'stalled', 'dead'.
    """
    hb = pathlib.Path(heartbeat_path)
    if not hb.exists():
        return {'status': 'no_heartbeat', 'message': f'no heartbeat file at {heartbeat_path}'}

    age = time.time() - hb.stat().st_mtime

    remaining = True
    if workflow_path and pathlib.Path(workflow_path).exists():
        w = _read_json_utf8sig(workflow_path)
        total = w.get('total_tasks', 0) or 0
        done = len(set(w.get('completed_tasks', []) + w.get('skipped_tasks', [])))
        remaining = not (total > 0 and done >= total)

    if not remaining:
        return {'status': 'complete', 'age_seconds': age,
                'message': 'all tasks complete; heartbeat age is not a liveness concern'}

    if age <= threshold_seconds:
        return {'status': 'healthy', 'age_seconds': age, 'threshold_seconds': threshold_seconds,
                'message': f'heartbeat fresh ({age:.0f}s old)'}

    if age > threshold_seconds * dead_multiplier:
        return {
            'status': 'dead', 'age_seconds': age, 'threshold_seconds': threshold_seconds,
            'message': (f'DEAD: heartbeat stale {age:.0f}s '
                        f'(> {dead_multiplier}x threshold {threshold_seconds}s) with work remaining'),
        }

    return {
        'status': 'stalled', 'age_seconds': age, 'threshold_seconds': threshold_seconds,
        'message': f'STALLED: heartbeat stale {age:.0f}s (threshold {threshold_seconds}s) with work remaining',
    }


def _git_branches(repo_root, no_merged_into=None):
    args = ['git', 'branch', '--list']
    if no_merged_into:
        args = ['git', 'branch', '--no-merged', no_merged_into]
    result = subprocess.run(args, cwd=repo_root, capture_output=True, text=True)
    branches = []
    for line in result.stdout.splitlines():
        name = line.strip().lstrip('+*').strip()
        if name:
            branches.append(name)
    return branches


def _worktree_paths(repo_root):
    """Map branch name -> worktree path, from `git worktree list --porcelain`."""
    result = subprocess.run(['git', 'worktree', 'list', '--porcelain'],
                             cwd=repo_root, capture_output=True, text=True)
    mapping = {}
    current_path = None
    for line in result.stdout.splitlines():
        if line.startswith('worktree '):
            current_path = line[len('worktree '):].strip()
        elif line.startswith('branch ') and current_path:
            branch = line[len('branch '):].strip()
            if branch.startswith('refs/heads/'):
                branch = branch[len('refs/heads/'):]
            mapping[branch] = current_path
    return mapping


def _routed_completion_evidence(repo_root, branch, changed_files):
    """Best-effort corroboration: of the files THIS branch actually changed
    vs main, do any routed workflow.json blobs (committed on the branch) claim
    complete=true? Deliberately scoped to the branch's own diff, not a
    filesystem glob of the worktree's checked-out state dir — a worktree
    inherits hundreds of unrelated agent-*-workflow.json files from the base
    branch at creation time, and globbing them all is noise, not evidence.
    Empty result is common and honest: most branches never commit their
    routed state at all, so the git-diff signal in stranded_deliverables
    remains the primary evidence either way."""
    hits = []
    for f in changed_files:
        name = pathlib.Path(f).name
        if not (name.startswith('agent-') and name.endswith('-workflow.json')):
            continue
        result = subprocess.run(['git', 'show', f'{branch}:{f}'],
                                 cwd=repo_root, capture_output=True, text=True)
        if result.returncode != 0:
            continue
        try:
            w = json.loads(result.stdout.encode().decode('utf-8-sig'))
        except json.JSONDecodeError:
            continue
        if w.get('complete') is True:
            hits.append(name)
    return hits


def stranded_deliverables(repo_root, main_branch='main', branch_prefix='worktree-agent-'):
    """Detect completed-but-unmerged worktree deliverables — the 275/269 class
    of failure, where a branch finished real work that was never merged or
    ported to main.

    Ground truth is git-level, not self-reported: a branch is a candidate only
    if (a) it is NOT an ancestor of main (--no-merged) AND (b) its diff against
    main touches real deliverable files, not just runtime state noise
    (.claude/state/*). Routed-state complete=true is attached as best-effort
    corroboration where discoverable, but is not required — the git evidence
    alone is what actually happened this session (282/275/269 all showed real
    committed content on unmerged branches).
    """
    worktrees = _worktree_paths(repo_root)
    candidates = []
    for branch in _git_branches(repo_root, no_merged_into=main_branch):
        if not branch.startswith(branch_prefix):
            continue
        diff = subprocess.run(
            ['git', 'diff', '--name-only', f'{main_branch}...{branch}'],
            cwd=repo_root, capture_output=True, text=True,
        )
        changed = [f for f in diff.stdout.splitlines() if f.strip()]
        deliverable_files = [f for f in changed if not f.startswith('.claude/state/')]
        if not deliverable_files:
            continue

        entry = {
            'branch': branch,
            'worktree_path': worktrees.get(branch),
            'merged_into_main': False,
            'deliverable_files': deliverable_files,
            'changed_files_count': len(changed),
            'routed_complete_evidence': _routed_completion_evidence(repo_root, branch, changed),
        }
        candidates.append(entry)

    return {
        'main_branch': main_branch,
        'stranded_count': len(candidates),
        'stranded': candidates,
    }


def _main():
    import argparse
    parser = argparse.ArgumentParser(description='Observability helpers (backlog 276)')
    sub = parser.add_subparsers(dest='cmd', required=True)

    oracle = sub.add_parser('completion-truth', help='OBS-01 completion-truth oracle')
    oracle.add_argument('--workflow', required=True, help='path to routed workflow.json')
    oracle.add_argument('--repo', required=True, help='repo root for git commands')
    oracle.add_argument('--paths', nargs='+', required=True, help='deliverable path(s) to check')

    banner = sub.add_parser('banner-vs-reality', help='OBS-02 banner/reality reconciliation')
    banner.add_argument('--workflow', required=True, help='path to routed workflow.json')
    banner.add_argument('--repo', required=True, help='repo root for git commands')
    banner.add_argument('--paths', nargs='+', required=True, help='deliverable path(s) to check')
    banner.add_argument('--banner-completed', type=int, required=True)
    banner.add_argument('--banner-failed', type=int, required=True)
    banner.add_argument('--logs', nargs='*', default=[], help='iteration log path(s) to check')

    liveness = sub.add_parser('liveness', help='OBS-03 liveness/stall/death classifier')
    liveness.add_argument('--heartbeat', required=True, help='path to the runner heartbeat file')
    liveness.add_argument('--workflow', help='path to routed workflow.json (for remaining-work check)')
    liveness.add_argument('--threshold-seconds', type=int, default=300)
    liveness.add_argument('--dead-multiplier', type=int, default=3)

    stranded = sub.add_parser('stranded', help='OBS-03 stranded-deliverable detector')
    stranded.add_argument('--repo', required=True, help='repo root for git commands')
    stranded.add_argument('--main-branch', default='main')
    stranded.add_argument('--branch-prefix', default='worktree-agent-')

    args = parser.parse_args()

    if args.cmd == 'completion-truth':
        verdict = completion_truth(args.workflow, args.repo, deliverable_paths=args.paths)
        print(json.dumps(verdict, indent=2))
        if verdict.get('divergences'):
            raise SystemExit(1)
    elif args.cmd == 'banner-vs-reality':
        verdict = banner_vs_reality(
            args.workflow, args.repo, args.banner_completed, args.banner_failed,
            deliverable_paths=args.paths, iteration_log_paths=args.logs,
        )
        print(json.dumps(verdict, indent=2))
        if verdict.get('disagreement'):
            raise SystemExit(1)
    elif args.cmd == 'liveness':
        verdict = liveness_check(
            args.heartbeat, workflow_path=args.workflow,
            threshold_seconds=args.threshold_seconds, dead_multiplier=args.dead_multiplier,
        )
        print(f"[LIVENESS] {verdict['status'].upper()}: {verdict['message']}")
        print(json.dumps(verdict, indent=2))
        if verdict['status'] in ('stalled', 'dead'):
            raise SystemExit(1)
    elif args.cmd == 'stranded':
        verdict = stranded_deliverables(args.repo, main_branch=args.main_branch,
                                         branch_prefix=args.branch_prefix)
        print(json.dumps(verdict, indent=2))
        if verdict['stranded_count']:
            print(f"[STRANDED] {verdict['stranded_count']} unmerged branch(es) with committed deliverables")
            raise SystemExit(1)


if __name__ == '__main__':
    _main()

"""L2/L3 tests reproducing this session's four observability failure cases
(backlog 276, task 005, gate OBS-05).

LIVE, not simulated: real git repos and real files built under mktemp, real
subprocess git commands, real file mtimes. The helpers under test (lib/
observability.py) are exercised directly, never mocked. Fixtures never touch
this repo's own git history or .claude/state/ files.
"""

import json
import os
import pathlib
import subprocess
import sys
import tempfile
import time

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / 'lib'))

from observability import (  # noqa: E402
    banner_vs_reality,
    completion_truth,
    liveness_check,
    stranded_deliverables,
)


def _write_json(path, data):
    path.write_text(json.dumps(data), encoding='utf-8')


def _init_git_repo(root):
    subprocess.run(['git', 'init', '-q', '-b', 'main'], cwd=root, check=True)
    subprocess.run(['git', 'config', 'user.email', 'test@example.com'], cwd=root, check=True)
    subprocess.run(['git', 'config', 'user.name', 'Test'], cwd=root, check=True)


def _commit(root, message):
    subprocess.run(['git', 'add', '-A'], cwd=root, check=True)
    subprocess.run(['git', 'commit', '-q', '-m', message], cwd=root, check=True)


def test_a_claimed_done_no_artifact_flagged_by_oracle():
    """OBS-01: routed state claims a task complete, but the deliverable path
    has no commit and no non-empty artifact -> completion_truth flags it."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = pathlib.Path(tmp)
        _init_git_repo(repo)
        (repo / 'README.md').write_text('seed', encoding='utf-8')
        _commit(repo, 'seed')

        workflow_path = repo / 'agent-fake-workflow.json'
        _write_json(workflow_path, {'completed_tasks': ['001-fake-task.md'], 'skipped_tasks': []})

        deliverable = repo / 'lib' / 'never_written.py'  # never created, never committed

        verdict = completion_truth(str(workflow_path), str(repo), deliverable_paths=[str(deliverable)])

        assert verdict['divergences'] == ['001-fake-task.md']
        assert verdict['verdicts']['001-fake-task.md']['evidence'] is False


def test_b_banner_says_failed_but_completed_flagged_by_reconciliation():
    """OBS-02: state + artifacts show real completion, but the wrapper
    banner reports a failure -> banner_vs_reality surfaces the disagreement
    (the 261 false-'failed' class)."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = pathlib.Path(tmp)
        _init_git_repo(repo)
        deliverable = repo / 'lib' / 'real_deliverable.py'
        deliverable.parent.mkdir(parents=True, exist_ok=True)
        deliverable.write_text('def real(): return 1\n', encoding='utf-8')
        _commit(repo, 'ship real_deliverable')

        workflow_path = repo / 'agent-fake-workflow.json'
        _write_json(workflow_path, {'completed_tasks': ['001-real-task.md'], 'skipped_tasks': []})

        verdict = banner_vs_reality(
            str(workflow_path), str(repo),
            banner_completed=0, banner_failed=1,
            deliverable_paths=[str(deliverable)],
        )

        assert verdict['true_outcome']['completed'] == 1
        assert verdict['true_outcome']['failed'] == 0
        assert verdict['disagreement'] is True
        assert any('banner reported 0 completed' in a for a in verdict['alerts'])
        assert any('banner reported 1 failed' in a for a in verdict['alerts'])


def test_c_complete_but_unmerged_worktree_listed_as_stranded():
    """OBS-03: a branch finished real committed work but was never merged
    into main -> stranded_deliverables lists it (the 275/269 class)."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = pathlib.Path(tmp)
        _init_git_repo(repo)
        (repo / 'README.md').write_text('seed', encoding='utf-8')
        _commit(repo, 'seed')

        branch = 'worktree-agent-strandedtest'
        subprocess.run(['git', 'checkout', '-q', '-b', branch], cwd=repo, check=True)
        (repo / 'deliverable.py').write_text('done = True\n', encoding='utf-8')
        _commit(repo, 'complete deliverable, never merged')
        subprocess.run(['git', 'checkout', '-q', 'main'], cwd=repo, check=True)

        result = stranded_deliverables(str(repo), main_branch='main', branch_prefix='worktree-agent-')

        branches = [c['branch'] for c in result['stranded']]
        assert branch in branches
        matched = next(c for c in result['stranded'] if c['branch'] == branch)
        assert 'deliverable.py' in matched['deliverable_files']


def test_d_stale_heartbeat_flagged_as_stalled():
    """OBS-03: a heartbeat file older than the threshold, with tasks still
    remaining -> liveness_check classifies it as stalled (a visible signal,
    not just a file the operator has to notice went quiet)."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = pathlib.Path(tmp)
        heartbeat = repo / 'runner-heartbeat.json'
        heartbeat.write_text('{}', encoding='utf-8')

        stale_time = time.time() - 600  # 600s old: > 300s threshold, < 900s dead cutoff
        os.utime(heartbeat, (stale_time, stale_time))

        workflow_path = repo / 'agent-fake-workflow.json'
        _write_json(workflow_path, {
            'total_tasks': 5,
            'completed_tasks': ['001.md', '002.md'],
            'skipped_tasks': [],
        })

        verdict = liveness_check(str(heartbeat), workflow_path=str(workflow_path),
                                  threshold_seconds=300, dead_multiplier=3)

        assert verdict['status'] == 'stalled'

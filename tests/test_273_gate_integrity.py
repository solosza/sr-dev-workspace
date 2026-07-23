"""Live regression for the three gate-integrity helpers (backlog 273, task
004, gate GI-04).

LIVE, not simulated: real files under mktemp, real reads. The helpers under
test (lib/gate_integrity.py) are exercised directly, never mocked. Fixtures
never touch this repo's own git history or .claude/state/ files.
"""

import pathlib
import sys
import tempfile

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / 'lib'))

from gate_integrity import (  # noqa: E402
    check_absolute_claims,
    classify_gate_evidence,
    is_defect,
    lint_fixture_portability,
)


def test_a_simulated_and_empty_gate_evidence_rejected():
    """GI-01: a simulated-narrative log and a 0-byte log both classify as
    defects, never a live pass (reaffirms lessons #39/#49 — the 247 L3
    simulation + 208 UT-04 0-byte-log shapes)."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)

        sim_log = tmp / 'sim.log'
        sim_log.write_text(
            'Dependent swarm run: would run 5 agents in parallel (simulated, not executed)',
            encoding='utf-8',
        )
        verdict = classify_gate_evidence(str(sim_log))
        assert verdict == 'simulated'
        assert is_defect(verdict)

        empty_log = tmp / 'empty.log'
        empty_log.write_text('', encoding='utf-8')
        verdict = classify_gate_evidence(str(empty_log))
        assert verdict == 'empty'
        assert is_defect(verdict)

        live_log = tmp / 'live.log'
        live_log.write_text('$ pytest tests/test_foo.py\n5 passed in 1.23s\n', encoding='utf-8')
        verdict = classify_gate_evidence(str(live_log))
        assert verdict == 'live'
        assert not is_defect(verdict)


def test_b_relative_database_url_flagged_and_portable_fixture_clean():
    """GI-02: a fixture with a relative DATABASE_URL and no PYTHONPATH is
    flagged (the 222 relative-URL / lesson #47 class); a 223-style portable
    fixture (absolute + env-driven DATABASE_URL, explicit PYTHONPATH)
    passes clean."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)

        bad = tmp / 'bad_conftest.py'
        bad.write_text(
            'import pytest\n'
            'from framework.db import connect\n'
            'DATABASE_URL = "sqlite:///./test.db"\n',
            encoding='utf-8',
        )
        violations = lint_fixture_portability(str(bad))
        kinds = {v['kind'] for v in violations}
        assert kinds == {'relative_database_url', 'missing_pythonpath'}

        good = tmp / 'good_conftest.py'
        good.write_text(
            '# PYTHONPATH=D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework\n'
            'import os\n'
            'import pytest\n'
            'from framework.db import connect\n'
            'DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///D:/my_ai_projects/hmsa/app.db")\n'
            'HOST = os.environ.get("DB_HOST", "localhost")\n'
            'PORT = os.environ.get("DB_PORT", "1433")\n',
            encoding='utf-8',
        )
        assert lint_fixture_portability(str(good)) == []


def test_c_css_max_width_not_fp_but_real_absolute_claim_caught():
    """GI-03: strip_markup_then_grep's absolute-claims retrofit does not
    fire on CSS max-width:100% inside a <style> block, but DOES fire on a
    real absolute claim ('100% accurate') in body text (pipelines
    255/256/258 CSS false-positive class)."""
    html = (
        '<html><head><style>.card img { max-width:100%; height:auto; }</style></head>'
        '<body><p>Our results are 100% accurate every time.</p>'
        '<div style="max-width:100%;">no claim here</div></body></html>'
    )

    matches = check_absolute_claims(html)

    assert len(matches) == 1
    assert 'accurate' in matches[0]['match'].lower()

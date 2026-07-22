"""Tests for page v2 rendering — reply-channel behaviors (static/JS assertions).

Task 006 of backlog 233 (render-reply-channel).
Gate: RC-03.
"""

import json
import os
import re
import subprocess
import sys
import tempfile

import pytest

GENERATE_SCRIPT = os.path.normpath(os.path.join(
    os.path.dirname(__file__), os.pardir,
    ".claude", "skills", "render", "templates", "review-board", "generate.py",
))

SAMPLE_ITEMS = [
    {"number": 1, "title": "First item", "scope": "backend", "priority": "high", "summary": "Summary one"},
    {"number": 2, "title": "Second item", "scope": "frontend", "priority": "normal", "summary": "Summary two"},
    {"number": 3, "title": "Third item", "scope": "infra", "priority": "low", "summary": "Summary three"},
]


@pytest.fixture(scope="module")
def page_html():
    with tempfile.TemporaryDirectory() as td:
        items_path = os.path.join(td, "items.json")
        with open(items_path, "w") as f:
            json.dump(SAMPLE_ITEMS, f)
        result = subprocess.run(
            [sys.executable, GENERATE_SCRIPT, items_path, td],
            capture_output=True, text=True,
        )
        assert result.returncode == 0, f"generate.py failed: {result.stderr}"
        page_path = os.path.join(td, "page.html")
        assert os.path.isfile(page_path), "page.html not created"
        with open(page_path, "r", encoding="utf-8") as f:
            yield f.read()


@pytest.fixture(scope="module")
def js_block(page_html):
    match = re.search(r"<script>(.*?)</script>", page_html, re.DOTALL)
    assert match, "No inline <script> block found"
    return match.group(1)


def _fn_body(js, name, window=800):
    start = js.find(f"function {name}")
    if start == -1:
        start = js.find(f"async function {name}")
    assert start != -1, f"function {name} not found"
    return js[start : start + window]


# ── Card generation ─────────────────────────────────────────────────

def test_three_cards_generated(page_html):
    for item in SAMPLE_ITEMS:
        n = item["number"]
        assert f'data-number="{n}"' in page_html
        assert f'id="card-{n}"' in page_html


# ── /status poll with interval ──────────────────────────────────────

def test_status_poll_fetch(js_block):
    body = _fn_body(js_block, "pollStatus")
    assert "fetch('/status')" in body or 'fetch("/status")' in body


def test_status_poll_interval(js_block):
    assert re.search(r"setInterval\s*\(\s*pollStatus\s*,\s*2000\s*\)", js_block)


def test_status_strip_elements(page_html):
    assert 'id="status-strip"' in page_html
    assert 'id="status-dot"' in page_html
    assert 'id="status-label"' in page_html


# ── Confirm-bar rendering keyed by confirms[].target ────────────────

def test_confirm_bar_renderer_exists(js_block):
    assert "function renderConfirmBar" in js_block


def test_confirm_bar_targets_card(js_block):
    body = _fn_body(js_block, "renderConfirmBar")
    assert re.search(r"""getElementById\s*\(\s*['"]card-['"]\s*\+\s*target""", body)


def test_confirm_dispatches_confirm_action(js_block):
    body = _fn_body(js_block, "renderConfirmBar")
    assert re.search(r"""answerConfirm\s*\(\s*target\s*,\s*['"]confirm['"]""", body)


def test_confirm_dispatches_cancel_action(js_block):
    body = _fn_body(js_block, "renderConfirmBar", window=1200)
    assert re.search(r"""answerConfirm\s*\(\s*target\s*,\s*['"]cancel['"]""", body)


def test_answer_confirm_posts_annotate(js_block):
    body = _fn_body(js_block, "answerConfirm")
    assert "fetch('/annotate'" in body or 'fetch("/annotate"' in body


def test_render_reply_iterates_confirms(js_block):
    body = _fn_body(js_block, "renderReply", window=1200)
    assert "confirms" in body
    assert "renderConfirmBar" in body


# ── Results[] outcome flip ──────────────────────────────────────────

def test_render_result_exists(js_block):
    assert "function renderResult" in js_block


def test_result_accepted(js_block):
    body = _fn_body(js_block, "renderResult")
    assert re.search(r"""outcome\s*===?\s*['"]accepted['"]""", body)


def test_result_rejected(js_block):
    body = _fn_body(js_block, "renderResult")
    assert "rejected" in body


def test_result_removes_controls(js_block):
    body = _fn_body(js_block, "renderResult")
    assert ".remove()" in body


# ── Dry-run toggle wiring test:true ─────────────────────────────────

def test_dry_run_toggle_element(page_html):
    assert 'id="dry-run-toggle"' in page_html
    assert 'type="checkbox"' in page_html


def test_dry_run_label_text(page_html):
    assert "nothing will be routed" in page_html


def test_dry_run_sets_test_flag(js_block):
    body = _fn_body(js_block, "act", window=900)
    assert "dry-run-toggle" in body
    assert re.search(r"\.test\s*=\s*true", body)


def test_dry_run_ack_renderer(js_block):
    assert "renderDryRunAck" in js_block
    body = _fn_body(js_block, "renderDryRunAck", window=400)
    assert "dry run" in body.lower()
    assert "not routed" in body.lower()


# ── Malformed-reply degradation to idle ─────────────────────────────

def test_poll_catch_degrades_to_idle(js_block):
    body = _fn_body(js_block, "pollStatus")
    assert "catch" in body
    assert re.search(r"""status:\s*['"]idle['"]""", body)


# ── Self-containment: zero external host refs ───────────────────────

def test_no_external_script_src(page_html):
    hits = re.findall(r"<script\s+[^>]*src\s*=", page_html, re.IGNORECASE)
    assert not hits, f"External <script src> tags found: {hits}"


def test_no_external_link_href(page_html):
    hits = re.findall(r"<link\s+[^>]*href\s*=", page_html, re.IGNORECASE)
    assert not hits, f"External <link href> tags found: {hits}"


def test_no_external_urls(page_html):
    urls = re.findall(r"https?://[^\s\"'<>]+", page_html)
    external = [u for u in urls if not re.match(r"https?://(?:localhost|127\.0\.0\.1)", u)]
    assert not external, f"External URLs found: {external}"


def test_no_protocol_relative_external(page_html):
    hits = re.findall(r"(?<![=:])//[a-zA-Z][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page_html)
    assert not hits, f"Protocol-relative external URLs: {hits}"


# ── v1 mechanics intact ────────────────────────────────────────────

def test_v1_queue_variable(js_block):
    assert re.search(r"var\s+queue\s*=\s*\{\s*\}", js_block)


def test_v1_act_function(js_block):
    assert "function act(" in js_block


def test_v1_send_posts_one_at_a_time(js_block):
    body = _fn_body(js_block, "sendAll")
    assert "for" in body
    assert "fetch('/annotate'" in body or 'fetch("/annotate"' in body


def test_v1_action_buttons_present(page_html):
    for action in ["accept", "iterate", "reject", "skip", "defer"]:
        assert f"'{action}')" in page_html, f"Action button '{action}' not wired"


def test_v1_notes_rows(page_html):
    for item in SAMPLE_ITEMS:
        n = item["number"]
        assert f'id="notes-row-{n}"' in page_html
        assert f'id="notes-{n}"' in page_html


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))

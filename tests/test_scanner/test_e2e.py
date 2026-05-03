"""End-to-end scanner test — full pipeline in mock mode."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pytest
from scanner.config import ScannerConfig
from scanner.fetcher import BookmarkFetcher
from scanner.analyzer import filter_relevant
from scanner.backlog_gen import generate_backlog_item, should_generate_backlog
from scanner.notifier import format_report, send_notification
from scanner.state import BookmarkState


@pytest.fixture
def config():
    return ScannerConfig(mock_mode=True)


@pytest.fixture
def state(tmp_path):
    return BookmarkState(state_path=tmp_path / "e2e_state.json")


def test_full_pipeline_mock_mode(config, state):
    fetcher = BookmarkFetcher(config)
    bookmarks = fetcher.fetch_bookmarks()
    assert len(bookmarks) >= 3

    new_bookmarks = [b for b in bookmarks if not state.is_processed(b["post_id"])]
    assert len(new_bookmarks) == len(bookmarks)

    analyses = filter_relevant(new_bookmarks, config)
    assert len(analyses) > 0

    for analysis in analyses:
        if should_generate_backlog(analysis):
            item = generate_backlog_item(analysis)
            assert "## Status" in item
            assert "PROPOSED" in item

    report = format_report(analyses)
    assert "Scan Report" in report
    result = send_notification(report, "console")
    assert result is True

    for analysis in analyses:
        state.mark_processed(analysis["post_id"], analysis["summary"])
    state.set_last_scan_date()
    assert state.get_processed_count() == len(analyses)
    assert state.get_last_scan_date() is not None


def test_idempotent_rerun(config, state):
    fetcher = BookmarkFetcher(config)
    bookmarks = fetcher.fetch_bookmarks()

    analyses = filter_relevant(bookmarks, config)
    for analysis in analyses:
        state.mark_processed(analysis["post_id"], analysis["summary"])

    new_bookmarks = [b for b in bookmarks if not state.is_processed(b["post_id"])]
    new_analyses = filter_relevant(new_bookmarks, config)
    processed_ids = {a["post_id"] for a in analyses}
    truly_new_relevant = [a for a in new_analyses if a["post_id"] not in processed_ids]
    assert len(truly_new_relevant) == 0

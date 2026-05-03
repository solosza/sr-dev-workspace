"""Tests for scanner.state — BookmarkState CRUD operations."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pytest
from scanner.state import BookmarkState


@pytest.fixture
def tmp_state(tmp_path):
    state_path = tmp_path / "test_state.json"
    return BookmarkState(state_path=state_path)


def test_initial_state_empty(tmp_state):
    assert tmp_state.get_processed_count() == 0
    assert tmp_state.get_last_scan_date() is None


def test_mark_processed(tmp_state):
    tmp_state.mark_processed("post_001", summary="Test post")
    assert tmp_state.is_processed("post_001")
    assert tmp_state.get_processed_count() == 1


def test_is_processed_returns_false_for_unknown(tmp_state):
    assert not tmp_state.is_processed("nonexistent")


def test_set_last_scan_date(tmp_state):
    tmp_state.set_last_scan_date("2026-04-05T12:00:00")
    assert tmp_state.get_last_scan_date() == "2026-04-05T12:00:00"


def test_state_persists_to_disk(tmp_path):
    state_path = tmp_path / "persist_test.json"
    state1 = BookmarkState(state_path=state_path)
    state1.mark_processed("abc", summary="persisted")
    state2 = BookmarkState(state_path=state_path)
    assert state2.is_processed("abc")
    assert state2.get_processed_count() == 1


def test_multiple_posts(tmp_state):
    tmp_state.mark_processed("a", summary="first")
    tmp_state.mark_processed("b", summary="second")
    tmp_state.mark_processed("c", summary="third")
    assert tmp_state.get_processed_count() == 3
    assert tmp_state.is_processed("a")
    assert tmp_state.is_processed("b")
    assert tmp_state.is_processed("c")
    assert not tmp_state.is_processed("d")

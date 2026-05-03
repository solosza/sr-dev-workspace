"""Tests for scanner.analyzer."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pytest
from scanner.analyzer import analyze_post, filter_relevant, generate_assessment
from scanner.config import ScannerConfig


@pytest.fixture
def config():
    return ScannerConfig()


@pytest.fixture
def ai_post():
    return {
        "post_id": "t001", "author": "researcher",
        "text": "New autonomous agent framework with self-improving evaluation loops and RAG memory.",
        "url": "https://x.com/researcher/status/t001",
        "timestamp": "2026-04-01T10:00:00Z", "links": [],
    }


@pytest.fixture
def irrelevant_post():
    return {
        "post_id": "t002", "author": "foodie",
        "text": "Best tacos in the city, highly recommend the al pastor.",
        "url": "https://x.com/foodie/status/t002",
        "timestamp": "2026-04-01T11:00:00Z", "links": [],
    }


def test_analyze_relevant_post(ai_post, config):
    result = analyze_post(ai_post, config)
    assert result["relevant"] is True
    assert result["post_id"] == "t001"


def test_analyze_irrelevant_post(irrelevant_post, config):
    result = analyze_post(irrelevant_post, config)
    assert result["relevant"] is False
    assert result["borrowable"] is False


def test_filter_relevant_keeps_only_ai_posts(ai_post, irrelevant_post, config):
    results = filter_relevant([ai_post, irrelevant_post], config)
    assert len(results) == 1
    assert results[0]["post_id"] == "t001"


def test_product_match_detected(config):
    post = {
        "post_id": "t003", "author": "tester",
        "text": "LLM evaluation benchmark suite for agentic tool use testing.",
        "url": "https://x.com/tester/status/t003",
        "timestamp": "2026-04-01T12:00:00Z", "links": [],
    }
    result = analyze_post(post, config)
    assert result["relevant"] is True
    assert result["product_match"] != ""


def test_borrowable_with_multiple_keywords(config):
    post = {
        "post_id": "t004", "author": "dev",
        "text": "Building an autonomous agent with RAG memory and LLM evaluation framework architecture.",
        "url": "https://x.com/dev/status/t004",
        "timestamp": "2026-04-02T10:00:00Z", "links": [],
    }
    result = analyze_post(post, config)
    assert result["relevant"] is True
    assert result["borrowable"] is True

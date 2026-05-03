"""Bookmark fetcher — retrieves X bookmarks in mock or real mode."""

from dataclasses import dataclass
from typing import List

from scanner.config import ScannerConfig


# Sample bookmarks for testing without browser access
MOCK_BOOKMARKS = [
    {
        "post_id": "mock_001",
        "author": "karpathy",
        "text": (
            "New paper on self-improving agents that use evaluation loops "
            "to autonomously refine their own prompts. Reminds me of "
            "constitutional AI but applied to agentic workflows."
        ),
        "url": "https://x.com/karpathy/status/mock_001",
        "timestamp": "2026-04-01T10:30:00Z",
        "links": ["https://arxiv.org/abs/2026.12345"],
    },
    {
        "post_id": "mock_002",
        "author": "swyx",
        "text": (
            "RAG is dead, long live knowledge graphs. Temporal knowledge "
            "graphs with decay functions outperform naive RAG by 40% on "
            "long-context benchmarks. Fine-tuning still wins for domain tasks."
        ),
        "url": "https://x.com/swyx/status/mock_002",
        "timestamp": "2026-04-02T14:15:00Z",
        "links": [],
    },
    {
        "post_id": "mock_003",
        "author": "emilyjbache",
        "text": (
            "Hot take: most LLM evaluation frameworks are just vibes. "
            "We need deterministic benchmark suites that test agentic "
            "tool use, not just text generation quality."
        ),
        "url": "https://x.com/emilyjbache/status/mock_003",
        "timestamp": "2026-04-03T09:00:00Z",
        "links": ["https://github.com/example/eval-bench"],
    },
    {
        "post_id": "mock_004",
        "author": "random_user",
        "text": (
            "Just had the best pizza in Brooklyn. No AI involved, "
            "just good dough and a wood-fired oven."
        ),
        "url": "https://x.com/random_user/status/mock_004",
        "timestamp": "2026-04-03T12:00:00Z",
        "links": [],
    },
    {
        "post_id": "mock_005",
        "author": "simonw",
        "text": (
            "Building an autonomous agent that delegates sub-tasks to "
            "other repos via subprocess spawning. Memory persistence "
            "across sessions is the hard part — considering Zep Cloud."
        ),
        "url": "https://x.com/simonw/status/mock_005",
        "timestamp": "2026-04-04T16:45:00Z",
        "links": ["https://docs.zep.ai"],
    },
]


class BookmarkFetcher:
    """Fetches X bookmarks in mock or real mode.

    Args:
        config: Scanner configuration.
    """

    def __init__(self, config: ScannerConfig):
        self.config = config

    def fetch_bookmarks(self) -> List[dict]:
        """Fetch bookmarks from X.

        In mock mode, returns MOCK_BOOKMARKS.
        In real mode, would use Playwright to scrape bookmarks.
        Real mode is not implemented — requires HUMAN REQUIRED for credentials.

        Returns:
            List of bookmark dicts with keys:
            post_id, author, text, url, timestamp, links.
        """
        if self.config.mock_mode:
            return list(MOCK_BOOKMARKS)

        # Real mode placeholder — requires Playwright + authenticated session
        raise NotImplementedError(
            "Real mode requires Playwright integration and X credentials. "
            "Set mock_mode=True for testing."
        )

"""Scanner configuration and constants."""

import os
from dataclasses import dataclass, field
from typing import List


# Isagawa product names for competitive comparison
ISAGAWA_PRODUCTS = [
    "kernel",
    "qa-platform",
    "spec-factory",
    "eval-specs",
    "run-task",
]

# AI/agent keywords for filtering bookmarks
AI_KEYWORDS = [
    "ai", "agent", "llm", "evaluation", "self-improving", "autonomous",
    "machine learning", "gpt", "claude", "prompt", "rag", "memory",
    "knowledge graph", "fine-tuning", "benchmark", "agentic",
]


@dataclass
class ScannerConfig:
    """Configuration for the bookmark scanner.

    Attributes:
        scan_days: Number of days back to scan. Default 3.
        max_posts: Maximum posts to process per run. Default 50.
        products: Isagawa products to compare against.
        ai_keywords: Keywords for filtering AI-relevant content.
        x_username: X account username (from env var).
        x_password: X account password (from env var).
        mock_mode: If True, use mock data instead of browser. Default True.
        notification_method: "console", "email", or "sms". Default "console".
    """
    scan_days: int = 3
    max_posts: int = 50
    products: List[str] = field(default_factory=lambda: list(ISAGAWA_PRODUCTS))
    ai_keywords: List[str] = field(default_factory=lambda: list(AI_KEYWORDS))
    x_username: str = field(default_factory=lambda: os.environ.get("X_USERNAME", ""))
    x_password: str = field(default_factory=lambda: os.environ.get("X_PASSWORD", ""))
    mock_mode: bool = True
    notification_method: str = "console"

"""Content analyzer — filters and analyzes bookmarks for competitive intelligence."""

from typing import List, Optional

from scanner.config import ScannerConfig


def analyze_post(post: dict, config: ScannerConfig) -> dict:
    """Analyze a single bookmark post for AI relevance and product comparison.

    Args:
        post: Bookmark dict with keys: post_id, author, text, url, timestamp, links.
        config: Scanner configuration with ai_keywords and products.

    Returns:
        Analysis dict with keys:
        - relevant: bool — whether the post is AI-relevant
        - product_match: str — which Isagawa product it relates to (or "")
        - assessment: str — competitive comparison assessment
        - borrowable: bool — whether ideas can be borrowed
        - summary: str — one-line summary
        - post_id: str — original post ID
        - author: str — original author
        - url: str — original URL
    """
    text_lower = post.get("text", "").lower()

    # Check AI relevance
    matched_keywords = [kw for kw in config.ai_keywords if kw in text_lower]
    relevant = len(matched_keywords) > 0

    # Find product match
    product_match = _find_product_match(text_lower, config.products)

    # Generate assessment
    assessment = ""
    borrowable = False
    if relevant:
        assessment = generate_assessment(post, product_match)
        borrowable = _is_borrowable(text_lower, matched_keywords)

    # Build summary
    text = post.get("text", "")
    summary = text[:80] + "..." if len(text) > 80 else text

    return {
        "relevant": relevant,
        "product_match": product_match,
        "assessment": assessment,
        "borrowable": borrowable,
        "summary": summary,
        "post_id": post.get("post_id", ""),
        "author": post.get("author", ""),
        "url": post.get("url", ""),
    }


def filter_relevant(posts: List[dict], config: ScannerConfig) -> List[dict]:
    """Filter a list of posts to only AI-relevant ones.

    Args:
        posts: List of bookmark dicts.
        config: Scanner configuration.

    Returns:
        List of analysis dicts where relevant=True.
    """
    analyses = [analyze_post(post, config) for post in posts]
    return [a for a in analyses if a["relevant"]]


def generate_assessment(post: dict, product: str) -> str:
    """Generate a competitive comparison assessment.

    Args:
        post: Bookmark dict.
        product: Matched Isagawa product name (or empty string).

    Returns:
        Assessment string describing competitive relevance.
    """
    text_lower = post.get("text", "").lower()

    if product:
        assessment = f"Relevant to Isagawa '{product}'. "
    else:
        assessment = "General AI/agent intelligence. "

    # Detect specific themes
    themes = []
    if "eval" in text_lower or "benchmark" in text_lower:
        themes.append("evaluation methodology")
    if "memory" in text_lower or "knowledge graph" in text_lower:
        themes.append("memory/knowledge architecture")
    if "agent" in text_lower or "autonomous" in text_lower:
        themes.append("agentic workflows")
    if "rag" in text_lower:
        themes.append("RAG patterns")
    if "self-improving" in text_lower:
        themes.append("self-improvement loops")

    if themes:
        assessment += "Themes: " + ", ".join(themes) + "."

    return assessment


def _find_product_match(text_lower: str, products: List[str]) -> str:
    """Find which Isagawa product a post relates to based on text content."""
    # Direct product name mentions
    for product in products:
        if product in text_lower:
            return product

    # Thematic mapping
    theme_map = {
        "eval-specs": ["eval", "benchmark", "evaluation", "test"],
        "kernel": ["self-improving", "autonomous", "agent", "memory"],
        "qa-platform": ["testing", "qa", "quality"],
        "run-task": ["task", "delegation", "subprocess"],
        "spec-factory": ["spec", "specification", "requirement"],
    }
    for product, keywords in theme_map.items():
        if any(kw in text_lower for kw in keywords):
            return product

    return ""


def _is_borrowable(text_lower: str, matched_keywords: List[str]) -> bool:
    """Determine if ideas from a post can be borrowed for Isagawa."""
    # Posts with multiple keyword matches or specific actionable themes
    if len(matched_keywords) >= 2:
        return True
    actionable = ["framework", "architecture", "pattern", "technique", "approach"]
    return any(word in text_lower for word in actionable)

"""Backlog generator — creates kernel backlog items from scan analyses."""

from datetime import datetime


def should_generate_backlog(analysis: dict) -> bool:
    """Determine if an analysis warrants a backlog item.

    Args:
        analysis: Analysis dict from analyzer.analyze_post.

    Returns:
        True if the analysis is relevant and borrowable.
    """
    return analysis.get("relevant", False) and analysis.get("borrowable", False)


def generate_backlog_item(analysis: dict) -> str:
    """Generate a markdown backlog item from a scan analysis.

    Follows kernel backlog format: title, status, summary, requirements, source.

    Args:
        analysis: Analysis dict from analyzer.analyze_post.

    Returns:
        Markdown string for the backlog item.
    """
    product = analysis.get("product_match", "general")
    author = analysis.get("author", "unknown")
    summary = analysis.get("summary", "")
    assessment = analysis.get("assessment", "")
    url = analysis.get("url", "")
    post_id = analysis.get("post_id", "unknown")
    date = datetime.now().strftime("%Y-%m-%d")

    title = _generate_title(analysis)

    return f"""# {title}

## Status
PROPOSED

## Source
- Author: @{author}
- URL: {url}
- Post ID: {post_id}
- Scanned: {date}

## Summary
{summary}

## Assessment
{assessment}

## Product Match
{product}

## Requirements
- [ ] Review source material
- [ ] Evaluate applicability to Isagawa {product}
- [ ] Draft implementation plan if approved

## Priority
AUTO-GENERATED — requires human review
"""


def _generate_title(analysis: dict) -> str:
    """Generate a concise title for the backlog item."""
    product = analysis.get("product_match", "")
    assessment = analysis.get("assessment", "")

    # Extract first theme if available
    if "Themes:" in assessment:
        themes_part = assessment.split("Themes:")[1].strip().rstrip(".")
        first_theme = themes_part.split(",")[0].strip()
        if product:
            return f"Investigate {first_theme} for {product}"
        return f"Investigate {first_theme}"

    if product:
        return f"Competitive intel for {product}"
    return "Competitive intelligence item"

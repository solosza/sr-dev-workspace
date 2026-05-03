"""Notifier — formats and sends scan reports."""

import sys
from datetime import datetime
from typing import List


def format_report(analyses: List[dict]) -> str:
    """Format scan results as a concise report.

    Args:
        analyses: List of analysis dicts from analyzer.analyze_post.

    Returns:
        Formatted report string.
    """
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = len(analyses)
    relevant = [a for a in analyses if a.get("relevant", False)]
    borrowable = [a for a in analyses if a.get("borrowable", False)]

    lines = [
        f"=== X Bookmark Scan Report ===",
        f"Date: {date}",
        f"Posts scanned: {total}",
        f"Relevant: {len(relevant)}",
        f"Borrowable: {len(borrowable)}",
        "",
    ]

    if relevant:
        lines.append("--- Relevant Posts ---")
        for i, a in enumerate(relevant, 1):
            lines.append(f"\n{i}. @{a.get('author', '?')} — {a.get('summary', 'N/A')}")
            if a.get("product_match"):
                lines.append(f"   Product: {a['product_match']}")
            if a.get("assessment"):
                lines.append(f"   Assessment: {a['assessment']}")
            if a.get("borrowable"):
                lines.append("   >> ACTION: Borrowable — consider backlog item")
            lines.append(f"   URL: {a.get('url', 'N/A')}")
    else:
        lines.append("No relevant posts found.")

    lines.append("\n=== End Report ===")
    return "\n".join(lines)


def send_notification(report: str, method: str = "console") -> bool:
    """Send a scan report via the specified method.

    Args:
        report: Formatted report string.
        method: Notification method — "console", "email", or "sms".

    Returns:
        True if notification was sent successfully.
    """
    if method == "console":
        sys.stdout.write(report + "\n")
        return True

    if method == "email":
        # Placeholder for Gmail MCP integration
        return False

    if method == "sms":
        # Placeholder for Twilio/SMS MCP integration
        return False

    return False

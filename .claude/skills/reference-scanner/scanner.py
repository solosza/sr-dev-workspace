"""Reference Scanner: Discovers and catalogs payload files from tiered-index structures.

Reads index.md files, follows wikilinks to sub-indexes and payloads,
extracts topic metadata, and builds a payload catalog for just-in-time
knowledge loading by kernel commands.
"""

import re
import warnings
from pathlib import Path
from typing import Optional


def scan_index(
    index_path: str | Path,
    _depth: int = 0,
    _seen: Optional[set] = None,
) -> list[dict]:
    """Scan a tiered-index file and return a payload catalog.

    Args:
        index_path: Path to the root index.md file.
        _depth: Current recursion depth (internal).
        _seen: Set of already-visited index paths (internal).

    Returns:
        List of payload entries:
        [{"path": str, "topics": list[str], "source_index": str}, ...]
    """
    MAX_DEPTH = 5

    if _depth > MAX_DEPTH:
        warnings.warn(f"Max recursion depth ({MAX_DEPTH}) reached at {index_path}")
        return []

    if _seen is None:
        _seen = set()

    index_path = Path(index_path).resolve()

    if not index_path.exists():
        warnings.warn(f"Index file not found: {index_path}")
        return []

    if str(index_path) in _seen:
        return []
    _seen.add(str(index_path))

    index_dir = index_path.parent
    text = index_path.read_text(encoding="utf-8", errors="replace")

    entries = _parse_index(text, index_dir)
    catalog: dict[str, dict] = {}

    for entry in entries:
        file_path = entry["path"]
        topics = entry["topics"]

        if not file_path.exists():
            warnings.warn(f"Broken link: {file_path} (from {index_path})")
            continue

        resolved = str(file_path.resolve())

        if _is_sub_index(file_path):
            sub_payloads = scan_index(file_path, _depth + 1, _seen)
            for payload in sub_payloads:
                key = payload["path"]
                if key in catalog:
                    catalog[key]["topics"] = _merge_topics(
                        catalog[key]["topics"], payload["topics"]
                    )
                else:
                    catalog[key] = payload
        else:
            if resolved in catalog:
                catalog[resolved]["topics"] = _merge_topics(
                    catalog[resolved]["topics"], topics
                )
            else:
                payload_entry = {
                    "path": resolved,
                    "topics": topics,
                    "source_index": str(index_path),
                }
                if file_path.suffix == ".md":
                    heading_topics = _extract_heading_topics(file_path)
                    payload_entry["topics"] = _merge_topics(
                        payload_entry["topics"], heading_topics
                    )
                else:
                    filename_topics = _topics_from_filename(file_path.stem)
                    payload_entry["topics"] = _merge_topics(
                        payload_entry["topics"], filename_topics
                    )
                catalog[resolved] = payload_entry

    return list(catalog.values())


def _parse_index(text: str, index_dir: Path) -> list[dict]:
    """Parse an index file for table rows and wikilinks, returning raw entries."""
    entries = []
    current_heading_topics: list[str] = []

    for line in text.splitlines():
        heading_match = re.match(r"^#{2,3}\s+(.+)$", line)
        if heading_match:
            current_heading_topics = _topics_from_heading(heading_match.group(1))
            continue

        table_entry = _parse_table_row(line, index_dir)
        if table_entry:
            table_entry["topics"] = _merge_topics(
                table_entry["topics"], current_heading_topics
            )
            entries.append(table_entry)
            continue

        wikilink_entries = _parse_wikilinks(line, index_dir)
        for wl in wikilink_entries:
            wl["topics"] = _merge_topics(wl["topics"], current_heading_topics)
            entries.append(wl)

    return entries


def _parse_table_row(line: str, index_dir: Path) -> Optional[dict]:
    """Parse a markdown table row for file references and topics."""
    if not line.strip().startswith("|"):
        return None

    cells = [c.strip() for c in line.split("|")]
    cells = [c for c in cells if c]

    if len(cells) < 2:
        return None

    if all(set(c) <= {"-", ":", " "} for c in cells):
        return None

    file_path = None
    topics = []

    for cell in cells:
        wl_match = re.search(r"\[\[([^\]]+)\]\]", cell)
        if wl_match:
            file_path = _resolve_link(wl_match.group(1), index_dir)
            continue

        md_match = re.search(r"\[([^\]]*)\]\(([^)]+)\)", cell)
        if md_match:
            file_path = _resolve_link(md_match.group(2), index_dir)
            continue

        if cell and not file_path:
            topics.extend(_topics_from_heading(cell))

    if file_path is None:
        return None

    if not topics:
        topics = _topics_from_filename(file_path.stem)

    return {"path": file_path, "topics": topics}


def _parse_wikilinks(line: str, index_dir: Path) -> list[dict]:
    """Extract all wikilinks and markdown links from a non-table line."""
    entries = []

    for match in re.finditer(r"\[\[([^\]]+)\]\]", line):
        link_path = _resolve_link(match.group(1), index_dir)
        entries.append({
            "path": link_path,
            "topics": _topics_from_filename(link_path.stem),
        })

    for match in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", line):
        link_path = _resolve_link(match.group(2), index_dir)
        topics = _topics_from_filename(link_path.stem)
        if match.group(1):
            topics = _merge_topics(topics, _topics_from_heading(match.group(1)))
        entries.append({"path": link_path, "topics": topics})

    return entries


def _resolve_link(raw: str, base_dir: Path) -> Path:
    """Resolve a wikilink or relative path to an absolute Path."""
    raw = raw.strip()
    if raw.startswith("/"):
        return Path(raw)

    candidate = base_dir / raw
    if candidate.exists():
        return candidate

    if not candidate.suffix:
        md_candidate = base_dir / (raw + ".md")
        if md_candidate.exists():
            return md_candidate

    return candidate


def _is_sub_index(path: Path) -> bool:
    """Determine if a path is a sub-index (another index.md) vs a payload."""
    return path.name == "index.md"


def _extract_heading_topics(path: Path) -> list[str]:
    """Extract topics from H2/H3 headings in a markdown payload file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    topics = []
    for match in re.finditer(r"^#{2,3}\s+(.+)$", text, re.MULTILINE):
        topics.extend(_topics_from_heading(match.group(1)))

    return topics


def _topics_from_heading(heading: str) -> list[str]:
    """Convert a heading string into normalized topic tokens."""
    heading = re.sub(r"[^\w\s-]", "", heading.lower())
    tokens = re.split(r"[\s_]+", heading.strip())
    tokens = [t for t in tokens if t and len(t) > 1]
    return tokens


def _topics_from_filename(stem: str) -> list[str]:
    """Extract topic tokens from a filename stem."""
    tokens = re.split(r"[-_]+", stem.lower())
    tokens = [t for t in tokens if t and len(t) > 1]
    return tokens


def _merge_topics(existing: list[str], new: list[str]) -> list[str]:
    """Merge two topic lists, preserving order and removing duplicates."""
    seen = set(existing)
    merged = list(existing)
    for t in new:
        if t not in seen:
            seen.add(t)
            merged.append(t)
    return merged


def parse_step_topics(step_file_path: str | Path) -> list[str]:
    """Extract topic interests from a step file.

    Reads three sources (in priority order, all merged):
    1. YAML frontmatter: ``topics: [rules, drg-mapping]``
    2. ``## Topics`` section with bullet list
    3. References section — infer topics from listed reference filenames

    Args:
        step_file_path: Path to the step markdown file.

    Returns:
        Deduplicated list of topic interest strings.
    """
    step_path = Path(step_file_path)
    if not step_path.exists():
        warnings.warn(f"Step file not found: {step_path}")
        return []

    text = step_path.read_text(encoding="utf-8", errors="replace")
    interests: list[str] = []

    # 1. YAML frontmatter topics
    fm_match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        topics_match = re.search(
            r"^topics:\s*\[([^\]]*)\]", fm_text, re.MULTILINE
        )
        if topics_match:
            raw = topics_match.group(1)
            interests.extend(
                t.strip().lower() for t in raw.split(",") if t.strip()
            )

    # 2. ## Topics section with bullet list
    topics_section = re.search(
        r"^##\s+Topics\s*\n((?:\s*[-*]\s+.+\n?)+)", text, re.MULTILINE
    )
    if topics_section:
        for bullet in re.finditer(r"[-*]\s+(.+)", topics_section.group(1)):
            topic = bullet.group(1).strip().lower()
            if topic:
                interests.append(topic)

    # 3. References section — infer topics from filenames
    refs_section = re.search(
        r"^##\s+References\s*\n((?:.*\n?)*?)(?=^##|\Z)", text, re.MULTILINE
    )
    if refs_section:
        block = refs_section.group(1)
        for link in re.finditer(r"\[\[([^\]]+)\]\]", block):
            ref_stem = Path(link.group(1)).stem
            interests.extend(_topics_from_filename(ref_stem))
        for link in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", block):
            ref_stem = Path(link.group(2)).stem
            interests.extend(_topics_from_filename(ref_stem))

    # Deduplicate preserving order
    seen: set[str] = set()
    deduped: list[str] = []
    for t in interests:
        if t not in seen:
            seen.add(t)
            deduped.append(t)
    return deduped


def match_payloads_to_steps(
    payload_catalog: list[dict],
    step_files: list[str | Path],
) -> dict[str, list[dict]]:
    """Match payloads to steps by topic intersection.

    Args:
        payload_catalog: List of payload dicts from ``scan_index()``,
            each with ``"path"``, ``"topics"``, ``"source_index"`` keys.
        step_files: List of paths to step markdown files.

    Returns:
        Dict mapping each step file path (str) to a list of matched
        payload entries. Steps with no matches get an empty list.
    """
    result: dict[str, list[dict]] = {}

    for step_file in step_files:
        step_path = str(Path(step_file).resolve())
        interests = parse_step_topics(step_file)
        interest_set = set(interests)
        has_all = "all" in interest_set

        matched: list[dict] = []
        for payload in payload_catalog:
            payload_topic_set = set(payload.get("topics", []))

            # Special topic: "all" in payload topics maps to every step
            if "all" in payload_topic_set:
                matched.append(payload)
                continue

            # Special topic: "all" in step interests pulls every payload
            if has_all:
                matched.append(payload)
                continue

            # Standard intersection match
            if interest_set & payload_topic_set:
                matched.append(payload)

        result[step_path] = matched

    return result

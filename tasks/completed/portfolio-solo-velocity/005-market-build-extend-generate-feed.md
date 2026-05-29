# Build: Extend generate-feed.py for story.html

**Type:** BUILD
**Phase:** 2
**Depends on:** 004

## Goal

Edit `D:\my_ai_projects\isagawa-co.github.io\generate-feed.py` to also inject the latest 10 feed entries into `story.html`, using the same `<!-- FEED_STATIC -->` pattern already used for `feed.html`.

## What to Change

Add a new function `inject_story_feed(entries, output_dir)` and call it from `main()`.

### New function to add (after `inject_static_feed`):

```python
def inject_story_feed(entries, output_dir):
    """Inject latest 10 entries into story.html, replacing FEED_STATIC marker."""
    story_path = os.path.join(output_dir, "story.html")
    try:
        with open(story_path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Warning: {story_path} not found, skipping story feed inject\n")
        return

    marker = "<!-- FEED_STATIC -->"
    if marker not in html:
        sys.stderr.write(f"Warning: {marker} not found in {story_path}\n")
        return

    latest = entries[:10]
    groups = group_entries(latest)
    rendered = "".join(render_group_html(g) for g in groups)
    html = html.replace(marker, rendered)

    with open(story_path, "w", encoding="utf-8") as f:
        f.write(html)
    sys.stdout.write(f"Injected {len(latest)} entries into story.html\n")
```

### Call site in `main()` — add after the existing `inject_static_feed` call:

```python
    inject_story_feed(entries, OUTPUT_DIR)
```

## File to Edit

`D:\my_ai_projects\isagawa-co.github.io\generate-feed.py`

## Acceptance Criteria
- [ ] `inject_story_feed` function exists in generate-feed.py
- [ ] Function is called from `main()` after `inject_static_feed`
- [ ] Function uses `entries[:10]` (latest 10 only)
- [ ] Function handles missing story.html gracefully (warns, doesn't crash)
- [ ] `grep -q "story.html" generate-feed.py` exits 0

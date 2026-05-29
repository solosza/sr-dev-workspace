# Build: Run generate-feed.py

**Type:** BUILD
**Phase:** 2
**Depends on:** 005

## Goal

Run `generate-feed.py` to inject the latest 10 feed entries into `story.html` and regenerate `feed-data.json` and `feed-count.txt`.

## Command

```bash
python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"
```

## Expected Output

```
Generated feed-data.json with N entries
Injected N entries into feed.html
Injected 10 entries into story.html
```

## Acceptance Criteria
- [ ] Command exits 0
- [ ] stdout includes "Injected" and "story.html"
- [ ] `story.html` no longer contains `<!-- FEED_STATIC -->` (replaced with rendered HTML)
- [ ] `story.html` contains `feed-entry` class in raw HTML

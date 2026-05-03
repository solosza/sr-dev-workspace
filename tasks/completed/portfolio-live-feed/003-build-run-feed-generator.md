# 003 — Run Feed Generator

**Type:** BUILD
**Depends on:** 002

## Requirements
Run the feed generator script to produce `feed.html` and `feed-count.txt` in `D:\my_ai_projects\isagawa-co.github.io\`.

```bash
python D:/my_ai_projects/isagawa-co.github.io/generate-feed.py
```

## Acceptance Criteria
- [ ] `python D:/my_ai_projects/isagawa-co.github.io/generate-feed.py` exits 0
- [ ] `D:\my_ai_projects\isagawa-co.github.io\feed.html` exists and contains `feed-entry` divs
- [ ] `D:\my_ai_projects\isagawa-co.github.io\feed-count.txt` exists and contains a number

# 009 — Verify All Files Exist (L1)

**Type:** TEST
**Depends on:** 001-008

## Requirements
Verify all deliverable files exist in `D:\my_ai_projects\isagawa-co.github.io\`:

```bash
test -f D:/my_ai_projects/isagawa-co.github.io/feed.html
test -f D:/my_ai_projects/isagawa-co.github.io/feed.css
test -f D:/my_ai_projects/isagawa-co.github.io/feed-count.txt
test -f D:/my_ai_projects/isagawa-co.github.io/generate-feed.py
test -f D:/my_ai_projects/isagawa-co.github.io/index.html
test -f D:/my_ai_projects/isagawa-co.github.io/styles.css
```

## Acceptance Criteria
- [ ] All 6 files exist
- [ ] `feed.html` is non-empty
- [ ] `feed-count.txt` contains a number > 0

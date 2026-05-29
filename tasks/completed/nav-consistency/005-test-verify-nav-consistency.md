# Test: Verify Nav Consistency Across All Pages

**Type:** TEST
**Phase:** 1
**Depends on:** 003, 004

## Goal

Verify that all 7 pages have the unified nav and no page contains the old on-page anchor links.

## Checks

```python
import os

pages = [
    'D:/my_ai_projects/isagawa-co.github.io/index.html',
    'D:/my_ai_projects/isagawa-co.github.io/feed.html',
    'D:/my_ai_projects/isagawa-co.github.io/attestation.html',
    'D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html',
    'D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html',
    'D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html',
    'D:/my_ai_projects/isagawa-co.github.io/story.html',
]

old_anchors = ['href="#seed"', 'href="#growth"', 'href="#self-extension"', 'href="#this-page"', 'href="#provenance"']
required = 'nav__dropdown'

for p in pages:
    html = open(p, encoding='utf-8').read()
    name = os.path.basename(p)

    # Check old anchors removed
    for anchor in old_anchors:
        assert anchor not in html, f'{name}: old anchor {anchor} still present'

    # Check dropdown present
    assert required in html, f'{name}: nav__dropdown missing'
    print(f'OK: {name}')

print('All 7 pages: nav consistent, old anchors removed, dropdown present')
```

## Acceptance Criteria
- [ ] All 7 assertions pass with exit 0
- [ ] No old on-page anchors remain in any page's nav

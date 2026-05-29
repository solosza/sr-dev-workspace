# Test: Verify Factory Origin Strip on All Product Pages

**Type:** TEST
**Phase:** 1
**Depends on:** 002

## Checks

```python
import os

product_pages = [
    'D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html',
    'D:/my_ai_projects/isagawa-co.github.io/attestation.html',
    'D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html',
    'D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html',
    'D:/my_ai_projects/isagawa-co.github.io/story.html',
]

for p in product_pages:
    html = open(p, encoding='utf-8').read()
    name = os.path.basename(p)
    assert 'factory-origin' in html, f'{name}: factory-origin strip missing'
    assert 'Built by the factory' in html, f'{name}: origin text missing'
    print(f'OK: {name} has factory origin strip')

# Verify NOT on index.html
index = open('D:/my_ai_projects/isagawa-co.github.io/index.html', encoding='utf-8').read()
assert 'factory-origin' not in index, 'index.html should NOT have factory-origin strip'
print('OK: index.html correctly has no factory-origin strip')
```

## Acceptance Criteria
- [ ] All 6 assertions pass with exit 0

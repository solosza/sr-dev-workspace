# Test: Verify story.html Structure + Feed Embed

**Type:** TEST
**Phase:** 2
**Depends on:** 006

## Goal

Mechanically verify that story.html is correctly structured and that the feed embed is visible in raw HTML without JavaScript.

## Checks to Run

### 1. File exists
```bash
test -f "D:/my_ai_projects/isagawa-co.github.io/story.html"
```

### 2. Six sections present
```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
count = html.count('anchor-section__number')
assert count >= 6, f'Expected 6+ sections, found {count}'
print(f'OK: {count} sections found')
"
```

### 3. Reveal classes present
```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
assert 'class=\"' in html and 'reveal' in html, 'No reveal classes found'
print('OK: reveal classes present')
"
```

### 4. Parallax present
```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
assert 'parallax-section' in html, 'parallax-section class missing'
print('OK: parallax-section present')
"
```

### 5. Terminal section present
```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
assert 'terminal__body' in html, 'terminal__body missing — Section 6 provenance terminal not found'
print('OK: terminal section present')
"
```

### 6. Feed entries in raw HTML (no JS required)
```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
assert 'feed-entry' in html, 'No feed entries in raw HTML — run generate-feed.py'
assert '<!-- FEED_STATIC -->' not in html, 'FEED_STATIC marker not replaced'
print('OK: feed entries visible without JS')
"
```

### 7. No changes to index.html
```bash
python -c "
import subprocess
result = subprocess.run(['git', '-C', 'D:/my_ai_projects/isagawa-co.github.io', 'diff', '--name-only'], capture_output=True, text=True)
modified = result.stdout.strip().split()
assert 'index.html' not in modified, f'index.html was modified — additive-only constraint violated'
print('OK: index.html unchanged')
"
```

## Acceptance Criteria
- [ ] All 7 checks pass with exit 0
- [ ] No check produces an AssertionError
- [ ] index.html confirmed unmodified

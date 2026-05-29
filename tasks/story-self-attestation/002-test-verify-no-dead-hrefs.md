# Test: Verify No Dead href="#" in story.html

**Type:** TEST
**Phase:** 1
**Depends on:** 001

## Goal

Confirm that all three fixes from task 001 landed correctly.

## Checks

```bash
python -c "
html = open('D:/my_ai_projects/isagawa-co.github.io/story.html').read()
dead = [i for i,c in enumerate(html.split('href=\"#\"')) if i > 0]
assert len(dead) == 0, f'Found {len(dead)} dead href=\"#\" link(s)'
print('OK: no dead href=\"#\" links')

assert 'attestation-pending' in html, 'attestation-pending anchor missing'
print('OK: attestation-pending present')

assert 'Pipeline 105' in html, 'Pipeline 105 footer entry missing'
print('OK: Pipeline 105 footer entry present')

assert 'sign to activate' in html, 'terminal line not updated'
print('OK: terminal line updated')
"
```

## Acceptance Criteria
- [ ] All 4 assertions pass with exit 0
- [ ] No AssertionError output

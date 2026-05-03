# Test Clone Command

## Type
TEST

## Description
Test the `/clone` command against a simple public website to verify end-to-end flow.

## Requirements
1. Run `/clone https://example.com` (example.com is a simple, static page — ideal test target)
2. Verify output directory created: `cloned-sites/example.com/`
3. Verify `index.html` exists and contains the page content
4. Verify `styles.css` exists (may be minimal for example.com)
5. Open `index.html` in browser and visually compare (screenshot if possible)

Note: This is a smoke test. The goal is to verify the skill runs without errors, not pixel-perfect accuracy.

## Acceptance Criteria
- [ ] Clone command runs without error
- [ ] `test -f cloned-sites/example.com/index.html`
- [ ] `grep -q "Example Domain" cloned-sites/example.com/index.html`

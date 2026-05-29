# Test — Verify Feed Entries Present in Raw HTML (No JS)

## Context
This task verifies the fix works from a no-JS perspective:
1. The raw HTML of feed.html contains feed entries (not just "Loading...")
2. "Loading..." does not appear anywhere in feed.html
3. generate-feed.py runs successfully and PRESERVES static entries after running
4. After generate-feed.py runs, the FEED_STATIC_START/END markers are still in place

Verification MUST use Python file reads and grep — NOT Playwright or any browser. The bug is invisible to browsers (JS fixes it at runtime).

## Type
TEST

## Execution
agent

## Dependencies
- 004-market-fix-generate-feed-markers.md

## Phase Gate
- [ ] `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0 (task 004 complete)
- [ ] `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (task 002 complete)

## Requirements
- Run all verification checks below using Python and grep
- DO NOT use Playwright or any browser tool
- Run `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` to verify script works
- Verify before AND after running the script

## Acceptance Criteria
- [ ] `python -c "h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert h.count('class=\"feed-entry ') > 5, f'Only {h.count(chr(34))}'; print('PASS: entries present')"` exits 0
- [ ] `python -c "h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert 'Loading...' not in h, 'Loading still present'; print('PASS: no Loading')"` exits 0
- [ ] `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0
- [ ] After generate-feed.py runs: `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (markers preserved)
- [ ] After generate-feed.py runs: `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 (count preserved)
- [ ] After generate-feed.py runs: `python -c "h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert h.count('class=\"feed-entry ') > 5, 'entries lost'; print('PASS')"` exits 0

## Gates Satisfied
- FUNC-01, FUNC-02, FUNC-03, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

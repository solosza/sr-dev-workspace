# Gate Contract — Portfolio Feed Server Render

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | feat/ branch exists in isagawa-co.github.io | run_code | `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --list "feat/feed-server-render*"` returns non-empty | Create branch |
| BUILD-02 | feed.html has static count (not "Loading...") | grep | `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` | Update count |
| BUILD-03 | feed.html nav-count has static value (not "--") | grep | `grep -v "feed-count" "D:/my_ai_projects/isagawa-co.github.io/feed.html" \| grep -q 'nav-count">[0-9]'` | Update nav-count |
| BUILD-04 | feed.html has FEED_STATIC start marker | grep | `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` | Add marker |
| BUILD-05 | feed.html has FEED_STATIC end marker | grep | `grep -q "FEED_STATIC_END" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` | Add marker |
| BUILD-06 | feed.html JS does NOT overwrite feed-entries innerHTML | grep | `grep -qv "feed-entries.*innerHTML" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` | Remove/guard JS overwrite |
| BUILD-07 | generate-feed.py uses FEED_STATIC_START/END markers | grep | `grep -q "FEED_STATIC_START" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` | Update inject_static_feed function |
| BUILD-08 | generate-feed.py updates static feed-count text | grep | `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` | Add count injection |
| FUNC-01 | Raw HTML contains feed entries (no JS) | run_code | `python -c "import re; h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert h.count('feed-entry') > 5, 'Less than 5 entries found'"` exits 0 | Fix static HTML |
| FUNC-02 | Raw HTML does not show "Loading..." for count | run_code | `python -c "import re; h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert 'Loading...' not in h, 'Loading... still present'"` exits 0 | Update static count |
| FUNC-03 | generate-feed.py runs without error on local data | run_code | `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py"` exits 0 | Fix script errors |
| TEST-01 | After generate-feed.py runs, feed.html still has static entries | run_code | `python "D:/my_ai_projects/isagawa-co.github.io/generate-feed.py" && grep -q "feed-entry" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0 | Fix marker replacement |

## Requirements Coverage
- BUILD-01 → task 001
- BUILD-02, BUILD-03 → task 002
- BUILD-04, BUILD-05, BUILD-06 → task 003
- BUILD-07, BUILD-08 → task 004
- FUNC-01, FUNC-02, FUNC-03, TEST-01 → task 005

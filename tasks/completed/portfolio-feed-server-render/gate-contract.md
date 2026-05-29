# Gate Contract — Portfolio Feed Server Render

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | feed.html has FEED_STATIC marker | grep | `grep -q "FEED_STATIC" "D:\my_ai_projects\isagawa-co.github.io\feed.html"` | Add marker to feed.html |
| BUILD-02 | generate-feed.py has inject_static_feed function | grep | `grep -q "inject_static_feed" "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"` | Add function to generate-feed.py |
| BUILD-03 | generate-feed.py has render_entry_html function | grep | `grep -q "render_entry_html" "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"` | Add function |
| BUILD-04 | generate-feed.py calls inject_static_feed in main | grep | `grep -q "inject_static_feed(entries" "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"` | Add call in main() |
| FUNC-01 | generate-feed.py runs without error | run_code | `python "D:\my_ai_projects\isagawa-co.github.io\generate-feed.py"` exits 0 | Fix errors |
| FUNC-02 | feed.html has feed-entry divs after generation | run_code | `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert 'feed-entry' in content"` exits 0 | Fix injection |
| TEST-01 | FEED_STATIC marker replaced by content | run_code | `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert '<!-- FEED_STATIC -->' not in content"` exits 0 | Fix injection logic |
| TEST-02 | Multiple entries present in static HTML | run_code | `python -c "content=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); assert content.count('feed-entry') > 10"` exits 0 | Fix rendering |

## Requirements Coverage
- BUILD-01 → task 001 (add marker)
- BUILD-02, BUILD-03, BUILD-04 → task 002 (add renderer)
- FUNC-01 → task 003 (run generator)
- FUNC-02, TEST-01, TEST-02 → task 004 (verify raw HTML)

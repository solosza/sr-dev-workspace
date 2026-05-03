# Gate Contract — Portfolio Live Feed

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Feature branch exists | run_code | `git -C D:/my_ai_projects/isagawa-co.github.io branch --list feature/live-feed-update` returns non-empty | Create branch |
| BUILD-02 | Feed generator script exists | file_exists | `test -f D:/my_ai_projects/isagawa-co.github.io/generate-feed.py` | Create file |
| BUILD-03 | Feed page HTML exists | file_exists | `test -f D:/my_ai_projects/isagawa-co.github.io/feed.html` | Run generator |
| BUILD-04 | Feed page CSS exists | file_exists | `test -f D:/my_ai_projects/isagawa-co.github.io/feed.css` | Create file |
| BUILD-05 | Nav has counter element | grep | `grep -q 'attested-counter' D:/my_ai_projects/isagawa-co.github.io/index.html` | Add counter |
| BUILD-06 | Self-Extension stats updated | grep | `grep -q '30+' D:/my_ai_projects/isagawa-co.github.io/index.html` | Update stats |
| BUILD-07 | Capability list has links | grep | `grep -q 'href.*feed\|href.*showcase' D:/my_ai_projects/isagawa-co.github.io/index.html` | Add links |
| BUILD-08 | Nav has feed link | grep | `grep -q 'feed.html' D:/my_ai_projects/isagawa-co.github.io/index.html` | Add link |
| FUNC-01 | Feed generator runs | run_code | `python D:/my_ai_projects/isagawa-co.github.io/generate-feed.py` exits 0 | Fix script |
| FUNC-02 | Feed HTML has timeline entries | grep | `grep -q 'feed-entry' D:/my_ai_projects/isagawa-co.github.io/feed.html` | Fix generator |
| FUNC-03 | Feed HTML has counter value | grep | `grep -c 'feed-entry' D:/my_ai_projects/isagawa-co.github.io/feed.html` returns > 0 | Fix generator |
| TEST-01 | All files on feature branch | run_code | `git -C D:/my_ai_projects/isagawa-co.github.io status --porcelain` is empty after commit | Commit files |

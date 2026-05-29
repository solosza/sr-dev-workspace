# Gate Contract — Portfolio Feed Duplicate Grouping

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | feed.html has groupEntries function | grep | `function groupEntries` found in `D:/my_ai_projects/isagawa-co.github.io/feed.html` | Re-apply fix |
| BUILD-02 | feed.html uses details/summary for groups | grep | `<details` found in renderGroup or equivalent in `feed.html` | Re-apply fix |
| BUILD-03 | feed.css has group styles | grep | `.feed-group` or `.feed-entry-group` class found in `D:/my_ai_projects/isagawa-co.github.io/feed.css` | Add styles |
| BUILD-04 | feed deployed — recent commit | run_code | `git -C D:/my_ai_projects/isagawa-co.github.io log --oneline -1` shows commit mentioning feed grouping | Push and commit |
| TEST-01 | Playwright: grouped entries visible, no "null tasks", Rekor links present | run_test | Playwright MCP browses feed, finds at least one `<details>` group, confirms all `<a class="rekor-link">` links present | Re-investigate |

## Requirements Coverage
- BUILD-01, BUILD-02, BUILD-03 → 001 acceptance criteria
- BUILD-04 → 001 deployment criteria
- TEST-01 → 002 acceptance criteria

# Fix feed.html — Replace "Loading..." with Static Count

## Context
Currently `feed.html` line 37 shows `<p class="feed-count" id="feed-count">Loading...</p>` and line 31 shows `<span id="nav-count">--</span>`. A no-JS crawler sees "Loading..." and "--" for the count. The fix is to replace these with static values that match the actual entry count in the pre-rendered HTML.

The current feed.html contains the pre-rendered entries inline at line 38 (all entries in the `#feed-entries` div). Count these entries by counting occurrences of `class="feed-entry` in the file. At time of writing there are approximately 73 entries — verify the actual count by running:
```
python -c "import re; h=open('D:/my_ai_projects/isagawa-co.github.io/feed.html').read(); print(h.count('class=\"feed-entry '))"
```

Also add a `<!-- FEED_COUNT -->` marker after the static count text so generate-feed.py can update it in future runs.
Add a `<!-- NAV_COUNT -->` marker after the nav-count value.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-build-create-branch.md

## Phase Gate
- [ ] `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --show-current` returns `feat/feed-server-render`

## Requirements
- Edit `D:/my_ai_projects/isagawa-co.github.io/feed.html`
- Replace `Loading...` in `<p class="feed-count" id="feed-count">Loading...</p>` with `{N} attested pipeline runs<!-- FEED_COUNT -->`
- Replace `--` in `<span id="nav-count">--</span>` with `{N}<!-- NAV_COUNT -->` where N is the actual entry count
- N must be the real count from the static HTML, not guessed

## Acceptance Criteria
- [ ] `grep -q "attested pipeline runs" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0
- [ ] `grep -q "Loading\.\.\." "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits non-zero (no "Loading...")
- [ ] `grep -q "FEED_COUNT" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0
- [ ] `grep -q "NAV_COUNT" "D:/my_ai_projects/isagawa-co.github.io/feed.html"` exits 0

## Gates Satisfied
- BUILD-02, BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

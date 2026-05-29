# Build Feed Entry Grouping

## Context
The isagawa.co feed contains duplicate entries — identical intent titles logged multiple times within minutes (reruns). These are authentic and must NOT be deleted. The fix is a presentation layer: group consecutive same-title entries into an expandable `<details>/<summary>` element showing "Title (N runs)" that expands to show each individual run with its own Rekor link and metadata.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements

### feed.html changes
1. Add a `groupEntries(entries)` function after the `renderEntry` function:
   - Input: sorted entries array (newest-first)
   - Groups consecutive entries with identical `title` values
   - Returns an array of groups: `{ title, entries: [...], count }`
   - Single-entry groups (count === 1) pass through as-is

2. Add a `renderGroup(group)` function:
   - If `group.count === 1`: return `renderEntry(group.entries[0])` (no wrapping)
   - If `group.count > 1`: return a `<details>` element:
     ```html
     <details class="feed-group cat-[category]">
       <summary class="feed-group__summary">
         <span class="feed-entry__cat">[category]</span>
         <h3 class="feed-entry__title">[title]</h3>
         <span class="feed-group__count">[N] runs</span>
       </summary>
       [individual entry divs inside, each with their Rekor link]
     </details>
     ```
   - Every individual entry inside keeps its full metadata and Rekor link

3. Replace `entries.map(renderEntry).join('')` with `groupEntries(entries).map(renderGroup).join('')`

### feed.css changes
Add styles for `.feed-group` and `.feed-group__summary`:
- `.feed-group` — similar padding/border to `.feed-entry`
- `.feed-group__summary` — cursor: pointer, list-style: none, flex layout matching entry header
- `.feed-group__count` — small badge showing run count (e.g., subdued color, smaller font)
- Individual entries inside `<details>` — slightly indented to show nesting

### Deployment
- Commit feed.html + feed.css changes
- Push to GitHub Pages

## Acceptance Criteria
- [ ] `feed.html` contains `function groupEntries` (grep match)
- [ ] `feed.html` contains `<details` in group renderer (grep match)
- [ ] `feed.css` contains `.feed-group` style (grep match)
- [ ] No feed-data.json changes — all 73 entries still present (data unchanged)
- [ ] Git commit pushed containing feed.html + feed.css changes

## Gates Satisfied
- BUILD-01, BUILD-02, BUILD-03, BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

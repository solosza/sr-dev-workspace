# Build: Update Product Pages Nav (feed, attestation, qa, ssh, vibe-coder, story)

**Type:** BUILD
**Phase:** 1
**Depends on:** 002

## Goal

Apply the unified nav to the 6 remaining pages. Each page gets the same nav structure with the appropriate "active" indicator on its own link.

## Unified Nav Template (for non-index pages)

```html
<ul class="nav__links">
  <li><a href="index.html">Home</a></li>
  <li><a href="feed.html" [ACTIVE_IF_FEED]>Feed</a></li>
  <li><a href="attestation.html" [ACTIVE_IF_ATTESTATION]>Attestation</a></li>
  <li class="nav__dropdown [ACTIVE_IF_PRODUCT]">
    <button class="nav__dropdown-trigger" aria-expanded="false" aria-haspopup="true">Products <span aria-hidden="true">▾</span></button>
    <ul class="nav__dropdown-menu">
      <li><a href="qa-platforms.html" [ACTIVE_IF_QA]>QA Platforms</a></li>
      <li><a href="ssh-compliance.html" [ACTIVE_IF_SSH]>SSH Compliance</a></li>
      <li><a href="vibe-coder.html" [ACTIVE_IF_VIBE]>Vibe Coder</a></li>
    </ul>
  </li>
  <li class="attested-counter"><a href="feed.html"><span class="counter-number" id="nav-count">--</span> ✓</a></li>
</ul>
```

Active indicator pattern: add `class="nav__active"` to the `<a>` tag for the current page. For product pages, also add `class="nav__dropdown nav__dropdown--active"` to the dropdown `<li>`.

## Per-Page Active Items

| File | Active item |
|------|------------|
| `feed.html` | Feed link gets `class="nav__active"` |
| `attestation.html` | Attestation link gets `class="nav__active"` |
| `qa-platforms.html` | QA Platforms link in dropdown gets `class="nav__active"`; outer `<li>` gets `nav__dropdown--active` |
| `ssh-compliance.html` | SSH Compliance link in dropdown gets `class="nav__active"`; outer `<li>` gets `nav__dropdown--active` |
| `vibe-coder.html` | Vibe Coder link in dropdown gets `class="nav__active"`; outer `<li>` gets `nav__dropdown--active` |
| `story.html` | No active item (story is a shareable page, not in the main nav flow) |

Also add the dropdown JS snippet (from task 003) to each page's `</body>` — check if it's already present before adding.

## Acceptance Criteria
- [ ] All 6 files have `nav__dropdown` present
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/feed.html` exits 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/attestation.html` exits 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html` exits 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` exits 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html` exits 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/story.html` exits 0

# Nav Overflow/Consolidation Patterns

Research for isagawa.co nav consolidation (Pipeline 106).

---

## Current State

isagawa.co `index.html` nav has 10 items:
1. Seed (anchor)
2. Growth (anchor)
3. Self-Extension (anchor)
4. This Page (anchor)
5. Provenance (anchor)
6. Feed (page)
7. Attestation (page)
8. QA Platforms (page)
9. SSH Compliance (page)
10. Vibe Coder (page)
11. Attested counter badge (page link)

Items 1-5 are on-page anchors (story sections). Items 6-11 are product/feature pages (spokes). This will keep growing as more pipelines ship products.

---

## Identified Patterns

### Pattern 1: Grouped Label Dropdown ("Products" / "Work")

**How it works:** Primary nav shows 3-4 always-visible items. Product/feature pages collapse under a single dropdown labeled "Products," "Work," or "Projects."

**Pros:**
- Preserves hub-spoke architecture: home page is the hub, dropdown groups all spokes
- Scales indefinitely (new products go in the dropdown)
- Clean, minimal appearance (3-4 visible items)
- Familiar pattern (Linear, Vercel, Stripe all use variants)
- Works well with monochrome aesthetic

**Cons:**
- Requires one click/hover to reach product pages
- Dropdown needs careful CSS to avoid steering problem (diagonal mouse path)
- Must decide on label ("Products" vs "Work" vs "Projects")

**Fit for isagawa.co:** Excellent. Matches the monochrome engineering aesthetic. Hub-spoke architecture is preserved by design. The dropdown label communicates "this is a factory that ships products."

### Pattern 2: Overflow Ellipsis / "More" Menu

**How it works:** Show as many nav items as fit the viewport. Items that overflow collapse into a "..." or "More" button at the end. Often implemented with ResizeObserver or CSS container queries.

**Pros:**
- Responsive by nature (adapts to viewport width)
- No hard decisions about primary vs secondary — the browser decides
- Progressive disclosure pattern

**Cons:**
- Unpredictable grouping (depends on viewport width, label length)
- "More" is a weak information scent — users don't know what's inside
- Doesn't communicate architecture (it's just an overflow bucket, not a semantic group)
- More complex implementation (ResizeObserver + JS)

**Fit for isagawa.co:** Poor. The nav items are semantically different (on-page anchors vs product pages). Viewport-based overflow would mix them unpredictably. Doesn't communicate the hub-spoke intent.

### Pattern 3: Mega Menu (Multi-Column Dropdown)

**How it works:** A large panel drops down showing all options organized in columns with headings, descriptions, and sometimes icons.

**Pros:**
- Shows entire information architecture at once
- Good for 50+ page sites with complex taxonomies
- Can include descriptions, icons, featured items

**Cons:**
- Overkill for sites with < 20 pages
- Heavy visual weight — breaks minimal aesthetic
- Complex implementation
- Feels "enterprise SaaS," not "solo engineer portfolio"

**Fit for isagawa.co:** Poor. isagawa.co has ~10 pages total. A mega menu would feel over-engineered and break the monochrome minimal aesthetic.

### Pattern 4: Tab-Scroll (Horizontal Overflow)

**How it works:** Nav items scroll horizontally with arrow indicators or scroll snap. Common on mobile and material design.

**Pros:**
- All items remain flat (no nesting)
- Works well on mobile
- No dropdown mechanics needed

**Cons:**
- Hidden items have zero discoverability (users must scroll to find them)
- Doesn't work well on desktop (horizontal scrolling feels wrong)
- No semantic grouping
- Uncommon on desktop portfolio sites

**Fit for isagawa.co:** Poor. Desktop users expect to see the full nav. Scroll-to-discover breaks the "everything visible at a glance" principle.

### Pattern 5: Hamburger-Only (All Items Hidden)

**How it works:** No visible nav items. Everything behind a hamburger/menu icon. Click to reveal full nav.

**Pros:**
- Maximum visual simplicity
- Works at any item count
- Consistent behavior desktop and mobile

**Cons:**
- Hamburger menus on desktop reduce discoverability by 20-50% (NNGroup research)
- Users can't see where they are in the site structure
- Feels like "hiding the navigation" not "designing the navigation"

**Fit for isagawa.co:** Acceptable for mobile (already has hamburger). Poor for desktop — the nav items serve as wayfinding for the hub-spoke architecture.

### Pattern 6: Two-Tier Nav (Sections + Pages)

**How it works:** On-page section anchors live in a secondary/sub nav or are removed from the primary nav entirely. Primary nav shows only page-level items.

**Pros:**
- Separates two fundamentally different nav types (intra-page vs inter-page)
- Primary nav stays short (only real pages)
- On-page anchors could become a scroll-spy sidebar or sticky sub-nav

**Cons:**
- More complex layout (two nav regions)
- Must decide where on-page anchors live
- May confuse users if the two navs aren't visually distinct

**Fit for isagawa.co:** Good complement to Pattern 1. On-page anchors (Seed, Growth, etc.) could be removed from the primary nav and handled by scroll-spy or in-page navigation. Primary nav then only has: Home, Feed, Attestation, [Products dropdown].

---

## Cognitive Load Research

- **Miller's Law (7 +/- 2):** Often cited as justification for limiting nav to 7 items. However, UX researchers note this is a misapplication — Miller's research was about short-term memory (recall), not recognition tasks. Menus are recognition-based since items remain visible.
- **Hick's Law** is more relevant: decision time increases logarithmically with the number of choices. More nav items = longer time to choose, even if users can see them all.
- **Practical consensus:** 5-7 primary nav items is the sweet spot. Not because of memory limits, but because it reduces decision friction and maintains visual clarity.
- **Progressive disclosure** (show essentials first, reveal more on demand) is the dominant pattern for managing complexity.

---

## Primary vs Secondary Split

For isagawa.co specifically:

**Always visible (primary):**
- Home (the hub)
- Feed (activity stream — high-frequency destination)
- Attestation (trust signal — differentiator)
- [Products/Work dropdown trigger]

**Collapsed under dropdown (secondary):**
- QA Platforms
- SSH Compliance
- Vibe Coder
- (future products)

**Removed from primary nav:**
- On-page anchors (Seed, Growth, Self-Extension, This Page, Provenance) — these are story sections, not site-level navigation. Could become in-page scroll navigation or be removed entirely.

---

## Recommendation

**Pattern 1 (Grouped Label Dropdown)** combined with **Pattern 6 (Two-Tier separation)**.

1. Remove on-page anchor links from the primary nav (they belong to the story page, not the site)
2. Add a "Products" dropdown containing QA Platforms, SSH Compliance, Vibe Coder (and future items)
3. Keep Home, Feed, Attestation as always-visible primary items
4. Result: 3 visible items + 1 dropdown = 4 nav elements total

**Implementation approach:** Pure vanilla CSS hover dropdown with JS enhancement for accessibility (keyboard nav, escape-to-close). CSS `:hover` + `position: absolute` for the dropdown panel. No frameworks.

**Mobile behavior:** Existing hamburger menu continues to show all items flat (no nesting needed in mobile view).

---

## Sources

- [Webflow — Navigation Bar Design Best Practices](https://webflow.com/blog/navigation-bar-design)
- [Eleken — UX Navigation Design Patterns](https://www.eleken.co/blog-posts/ux-navigation-design)
- [Userpilot — Navigation UX Pattern Types](https://userpilot.com/blog/navigation-ux/)
- [Lollypop — Dropdown Menu Design Tips](https://lollypop.design/blog/2025/december/dropdown-menu-design/)
- [UX Bulletin — Miller's Law in UX](https://www.ux-bulletin.com/millers-law-ux-design/)
- [Stephanie Walter — Your Menu Doesn't Need Miller's 7+/-2 Rule](https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7-plus-minus-2-rule/)
- [NNGroup — Hub-and-Spoke Model](https://www.nngroup.com/articles/customer-service-model/)
- [Noble Desktop — Hub and Spoke Model for Website Structure](https://www.nobledesktop.com/learn/digital-marketing/the-digital-marketing-hub-and-spoke-model-for-website-structure)
- [CodePen — Simple Dropdown Nav, Pure Vanilla CSS](https://codepen.io/msorce/pen/oZMNvZ)
- [Jeff Astor — Building a Dropdown in 10 Lines of JavaScript](https://www.jeffastor.com/blog/building-a-dropdown-menu-in-10-lines-of-javascript/)

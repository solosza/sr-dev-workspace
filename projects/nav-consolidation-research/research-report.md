# Nav Consolidation Research Report

**Pipeline:** 106
**Date:** 2026-05-29

---

## Problem Statement

### Current Nav Item Counts

| Page | Nav Items | Notes |
|------|-----------|-------|
| index.html | 11 | 5 on-page anchors + 5 product pages + attested counter |
| story.html | 11 | Same as index (5 anchors + 5 pages + counter) |
| feed.html | 4 | Home + 2 anchors + Feed (active) |
| attestation.html | 6 | Home + 4 product pages + counter |
| qa-platforms.html | 5 | Home + 4 sibling pages |
| ssh-compliance.html | 5 | Home + 4 sibling pages |
| vibe-coder.html | 5 | Home + 4 sibling pages |

### Why This Is a Problem

1. **index.html has 11 nav items** — nearly double the 5-7 item sweet spot. Each new product page adds another item.
2. **On-page anchors pollute global nav.** Seed, Growth, Self-Extension, This Page, Provenance are story sections — they only make sense on index.html and story.html but consume 5 nav slots.
3. **Inconsistent nav across pages.** feed.html shows 4 items, product pages show 5, index shows 11. There's no consistent site-wide nav.
4. **No semantic grouping.** Product pages (QA Platforms, SSH Compliance, Vibe Coder) sit alongside story anchors with no visual distinction. New visitors can't tell which are pages vs. sections.
5. **Won't scale.** Every pipeline that ships a new product page (RT Automation, Fraud Detection, etc.) adds another flat nav item. At 15+ items the nav will break visually.

---

## Patterns Evaluated

| Pattern | Pros | Cons | Fit for isagawa.co |
|---------|------|------|---------------------|
| **Grouped dropdown ("Products")** | Preserves hub-spoke; scales indefinitely; clean appearance; familiar (Stripe, Vercel, Anthropic all use it) | Requires click/hover; needs CSS dropdown implementation | Excellent |
| **Overflow ellipsis ("More")** | Responsive; no manual grouping | Weak info scent; mixes semantic types unpredictably | Poor |
| **Mega menu** | Shows full IA at once | Overkill for <20 pages; breaks minimal aesthetic | Poor |
| **Tab-scroll** | All items flat | Hidden items have zero discoverability on desktop | Poor |
| **Hamburger-only** | Maximum simplicity | Reduces discoverability 20-50% on desktop (NNGroup) | Poor for desktop |
| **Two-tier nav** | Separates intra-page from inter-page nav | More complex layout | Good (complement to grouped dropdown) |

---

## Reference Site Summary

| Site | Top-Level Items | Dropdown Label | Items in Dropdown | Pattern |
|------|----------------|----------------|-------------------|---------|
| **Vercel** | 5 text + 2 CTAs | Products, Resources, Solutions | 14+ per dropdown (sub-grouped) | Grouped dropdown with sub-sections |
| **Stripe** | 6 text + 2 CTAs | Products, Solutions, Developers, Resources | 10+ per dropdown | Grouped dropdown |
| **Anthropic** | 5 text + 1 CTA | Commitments, Learn, Try Claude | 5-10 per dropdown (sub-grouped) | Grouped dropdown with sub-sections |
| **Linear** | 5 flat links + 2 CTAs | N/A | N/A | Flat nav (single product) |
| **Railway** | ~8 flat links + 2 CTAs | N/A | N/A | Flat nav (few products) |

**Common pattern:** Multi-product sites use 5-7 top-level items with "Products" as the grouping label. Single-product sites use flat nav. isagawa.co is multi-product, so it needs the grouped dropdown pattern.

---

## Recommendation

### Chosen Pattern

**Grouped label dropdown ("Products")** combined with **two-tier separation** (remove on-page anchors from global nav).

### Primary Items (Always Visible)

| Item | Type | Rationale |
|------|------|-----------|
| **Home** | Link | Hub page (on product pages; omitted on index.html itself) |
| **Feed** | Link | High-frequency destination, activity stream |
| **Attestation** | Link | Trust differentiator, unique to isagawa.co |
| **Products** | Dropdown trigger | Groups all product/feature pages |
| **[count] checkmark** | Badge link | Attested counter (existing pattern) |

**Total visible: 4 items + 1 badge = 5 elements.** Consistent across all pages.

### Collapsed Items (Under "Products" Dropdown)

| Item | Current Page |
|------|-------------|
| QA Platforms | qa-platforms.html |
| SSH Compliance | ssh-compliance.html |
| Vibe Coder | vibe-coder.html |
| *(future products added here)* | |

When on a product page, that page's link gets an "active" indicator in the dropdown and the "Products" label also gets the active indicator.

### Removed From Global Nav

| Item | Disposition |
|------|------------|
| Seed, Growth, Self-Extension, This Page, Provenance | Remove from global nav entirely. These are on-page story sections. Could become a scroll-spy sub-nav on index.html/story.html only, or rely on the page's natural scroll flow. No reference site puts in-page anchors in the global nav. |

---

## Implementation Sketch

### HTML Structure

```html
<nav class="nav">
  <a href="index.html" class="nav__logo">isagawa</a>
  <ul class="nav__links">
    <li><a href="index.html">Home</a></li>
    <li><a href="feed.html">Feed</a></li>
    <li><a href="attestation.html">Attestation</a></li>
    <li class="nav__dropdown">
      <button class="nav__dropdown-trigger" aria-expanded="false" aria-haspopup="true">
        Products <span class="arrow">▾</span>
      </button>
      <ul class="nav__dropdown-menu">
        <li><a href="qa-platforms.html">QA Platforms</a></li>
        <li><a href="ssh-compliance.html">SSH Compliance</a></li>
        <li><a href="vibe-coder.html">Vibe Coder</a></li>
      </ul>
    </li>
    <li class="attested-counter"><a href="feed.html"><span class="counter-number" id="nav-count">--</span> ✓</a></li>
  </ul>
  <button class="nav__hamburger" aria-label="Toggle menu">...</button>
</nav>
```

### CSS (Key Rules)

```css
/* Dropdown container */
.nav__dropdown {
  position: relative;
}

/* Dropdown trigger button — styled like a nav link */
.nav__dropdown-trigger {
  background: none;
  border: none;
  color: inherit;
  font: inherit;
  cursor: pointer;
  padding: 0;
  /* Match existing .nav__links a styling */
}

/* Dropdown menu — hidden by default */
.nav__dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background: var(--bg, #0a0a0a);
  border: 1px solid var(--border, #222);
  padding: 0.5rem 0;
  min-width: 180px;
  z-index: 100;
}

/* Show on hover (desktop) */
.nav__dropdown:hover .nav__dropdown-menu,
.nav__dropdown:focus-within .nav__dropdown-menu {
  display: block;
}

/* Dropdown items */
.nav__dropdown-menu a {
  display: block;
  padding: 0.4rem 1rem;
  white-space: nowrap;
}

/* Active product indicator */
.nav__dropdown-menu a.nav__active {
  /* Use existing active pattern (underline or color) */
}
```

### JS (Accessibility Enhancement)

```javascript
// Keyboard support + aria management
document.querySelectorAll('.nav__dropdown-trigger').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', !expanded);
  });

  // Close on Escape
  btn.closest('.nav__dropdown').addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      btn.setAttribute('aria-expanded', 'false');
      btn.focus();
    }
  });
});
```

### CSS Changes Needed

1. Add `.nav__dropdown`, `.nav__dropdown-trigger`, `.nav__dropdown-menu` styles
2. Existing `.nav__links a` hover/underline animation applies to dropdown trigger too
3. Dropdown menu background matches site bg (`#0a0a0a` or similar dark)
4. Dropdown border uses existing border color pattern
5. No new fonts, colors, or spacing values — reuse existing design tokens

### Mobile Behavior

No change to mobile. The hamburger menu continues to show all items as a flat list. On mobile, the "Products" label becomes a section heading or the items just appear inline. The dropdown is a desktop-only enhancement.

### Files to Modify

| File | Change |
|------|--------|
| All HTML pages | Replace `<ul class="nav__links">` content with new nav structure |
| styles.css | Add dropdown CSS (~20 lines) |
| main.js (or inline) | Add keyboard/aria JS (~15 lines) |

---

## Validation Verdict

Research confirms the "consolidate products under a dropdown" direction. Every multi-product reference site (Stripe, Vercel, Anthropic) uses this exact pattern. The research did surface one additional insight: **on-page anchors should be removed from global nav entirely** — no reference site puts page-internal links in the site-wide nav bar. This simplification is more aggressive than the original backlog item anticipated but is clearly the right approach.

The recommendation produces a 4-item nav (Home, Feed, Attestation, Products dropdown) + 1 badge — down from 11 items. This is cleaner than any reference site studied while following the same structural pattern they all use.

# Build: Add Factory Origin Strip to All 5 Product Pages

**Type:** BUILD
**Phase:** 1
**Depends on:** 001

## Goal

Add the `.factory-origin` strip to the 5 product pages. It goes immediately after the closing `</header>` tag on each page.

## Strip HTML

```html
<div class="factory-origin"><a href="index.html">← Built by the factory</a></div>
```

## Pages to Update

| File | Location to insert |
|------|--------------------|
| `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html` | After `</header>` |
| `D:/my_ai_projects/isagawa-co.github.io/attestation.html` | After `</header>` |
| `D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html` | After `</header>` |
| `D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` | After `</header>` |
| `D:/my_ai_projects/isagawa-co.github.io/story.html` | After `</header>` |

Do NOT add to `index.html` — the factory strip only appears on product/spoke pages.

## Acceptance Criteria
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html` exits 0
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/attestation.html` exits 0
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html` exits 0
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html` exits 0
- [ ] `grep -q "factory-origin" D:/my_ai_projects/isagawa-co.github.io/story.html` exits 0
- [ ] `grep -c "factory-origin" D:/my_ai_projects/isagawa-co.github.io/index.html` returns 0

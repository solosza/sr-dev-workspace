# Build: Fix story.html Verify Links

**Type:** BUILD
**Phase:** 1

## Goal

Fix three places in `D:\my_ai_projects\isagawa-co.github.io\story.html` where verify links are dead or borrowed from the wrong pipeline:

1. **Line 129** — `href="#"` on `#story-rekor-link` → replace with `href="#attestation-pending"` and add text note
2. **Footer lines 146-148** — three April 26 Rekor indices borrowed from homepage → replace with a pipeline 105 pending entry
3. **Terminal line 194** — `rekor #PENDING` terminal text → update to `rekor #PENDING (unsigned — sign to activate)`

## Exact Edits

### Edit 1 — Section 6 verify link (line 129)
```
OLD:
<a href="#" class="rekor-link" id="story-rekor-link" target="_blank">Verify on Rekor ↗</a>

NEW:
<a href="#attestation-pending" class="rekor-link rekor-link--pending" id="story-rekor-link" title="Signing pending — run attest.py to activate">Signing pending ↗</a>
```

### Edit 2 — Footer verify section (lines 145-148)
```
OLD:
        <p class="footer__col-header">Verify</p>
        <a href="https://search.sigstore.dev/?logIndex=1387966928" target="_blank" rel="noopener">Rekor #1387966928</a>
        <a href="https://search.sigstore.dev/?logIndex=1388628067" target="_blank" rel="noopener">Rekor #1388628067</a>
        <a href="https://search.sigstore.dev/?logIndex=1389042818" target="_blank" rel="noopener">Rekor #1389042818</a>

NEW:
        <p class="footer__col-header">Verify</p>
        <a href="https://search.sigstore.dev/?logIndex=1387966928" target="_blank" rel="noopener">Rekor #1387966928</a>
        <a href="https://search.sigstore.dev/?logIndex=1388628067" target="_blank" rel="noopener">Rekor #1388628067</a>
        <a href="https://search.sigstore.dev/?logIndex=1389042818" target="_blank" rel="noopener">Rekor #1389042818</a>
        <span class="footer__pending">Pipeline 105 — signing pending</span>
```

### Edit 3 — Terminal script (line 194)
```
OLD:
      { text: '  ✓ rekor #PENDING', cls: 'terminal__line--success' },

NEW:
      { text: '  ⧖ rekor #PENDING — sign to activate', cls: 'terminal__line--comment' },
```

## Acceptance Criteria
- [ ] `grep -c 'href="#"' D:/my_ai_projects/isagawa-co.github.io/story.html` returns 0
- [ ] `grep -q 'attestation-pending' D:/my_ai_projects/isagawa-co.github.io/story.html` exits 0
- [ ] `grep -q 'Pipeline 105' D:/my_ai_projects/isagawa-co.github.io/story.html` exits 0

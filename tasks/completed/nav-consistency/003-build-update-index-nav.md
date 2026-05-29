# Build: Update index.html Nav

**Type:** BUILD
**Phase:** 1
**Depends on:** 002

## Goal

Replace the nav `<ul class="nav__links">` in `D:\my_ai_projects\isagawa-co.github.io\index.html` with the unified nav structure.

## Current Nav (to replace)

```html
<ul class="nav__links">
  <li><a href="#seed">Seed</a></li>
  <li><a href="#growth">Growth</a></li>
  <li><a href="#self-extension">Self-Extension</a></li>
  <li><a href="#this-page">This Page</a></li>
  <li><a href="#provenance">Provenance</a></li>
  <li><a href="feed.html">Feed</a></li>
  <li><a href="attestation.html">Attestation</a></li>
  <li><a href="qa-platforms.html">QA Platforms</a></li>
  <li><a href="ssh-compliance.html">SSH Compliance</a></li>
  <li><a href="vibe-coder.html">Vibe Coder</a></li>
  <li class="attested-counter"><a href="feed.html"><span class="counter-number" id="nav-count">--</span> ✓</a></li>
</ul>
```

## New Nav (exact replacement)

On index.html, "Home" link is OMITTED (you are already home).

```html
<ul class="nav__links">
  <li><a href="feed.html">Feed</a></li>
  <li><a href="attestation.html">Attestation</a></li>
  <li class="nav__dropdown">
    <button class="nav__dropdown-trigger" aria-expanded="false" aria-haspopup="true">Products <span aria-hidden="true">▾</span></button>
    <ul class="nav__dropdown-menu">
      <li><a href="qa-platforms.html">QA Platforms</a></li>
      <li><a href="ssh-compliance.html">SSH Compliance</a></li>
      <li><a href="vibe-coder.html">Vibe Coder</a></li>
    </ul>
  </li>
  <li class="attested-counter"><a href="feed.html"><span class="counter-number" id="nav-count">--</span> ✓</a></li>
</ul>
```

Also add this inline `<script>` block just before `</body>` (after the existing scripts, if any):

```html
<script>
  // Dropdown keyboard/aria support
  document.querySelectorAll('.nav__dropdown-trigger').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
    });
    btn.closest('.nav__dropdown').addEventListener('keydown', function(e) {
      if (e.key === 'Escape') { btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
    });
  });
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav__dropdown')) {
      document.querySelectorAll('.nav__dropdown-trigger').forEach(function(btn) {
        btn.setAttribute('aria-expanded', 'false');
      });
    }
  });
</script>
```

## Acceptance Criteria
- [ ] `grep -c 'href="#seed"\|href="#growth"\|href="#self-extension"\|href="#this-page"\|href="#provenance"' index.html` returns 0
- [ ] `grep -q "nav__dropdown" D:/my_ai_projects/isagawa-co.github.io/index.html` exits 0
- [ ] `grep -q "nav__dropdown-trigger" D:/my_ai_projects/isagawa-co.github.io/index.html` exits 0

# Gate Contract — Vibe Coder Showcase

## BUILD Gates

### BUILD-01: Feature branch exists
- **Method:** `run_code`
- **Check:** `git -C "D:/my_ai_projects/isagawa-co.github.io" branch --list "feature/showcase-vibe-coder" | grep -q "feature/showcase-vibe-coder"`

### BUILD-03: HTML file exists with required sections
- **Method:** `file_exists`
- **Check:** `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html`

### BUILD-04: CSS file exists with design system variables
- **Method:** `grep`
- **Check:** `grep -q ':root' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.css"`

### BUILD-05: JS file exists with terminal animation
- **Method:** `grep`
- **Check:** `grep -q 'terminal\|Terminal\|runTerminal\|typeText' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.js"`

### BUILD-06: Index nav updated
- **Method:** `grep`
- **Check:** `grep -q 'vibe-coder.html' "D:/my_ai_projects/isagawa-co.github.io/index.html"`

### BUILD-07: Attestation nav updated
- **Method:** `grep`
- **Check:** `grep -q 'vibe-coder.html' "D:/my_ai_projects/isagawa-co.github.io/attestation.html"`

### BUILD-08: SSH compliance nav updated
- **Method:** `grep`
- **Check:** `grep -q 'vibe-coder.html' "D:/my_ai_projects/isagawa-co.github.io/ssh-compliance.html"`

### BUILD-09: QA platforms nav updated
- **Method:** `grep`
- **Check:** `grep -q 'vibe-coder.html' "D:/my_ai_projects/isagawa-co.github.io/qa-platforms.html"`

## FUNCTIONAL Gates

### FUNC-01: Hero section present
- **Method:** `grep`
- **Check:** `grep -q 'class="hero"' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"`

### FUNC-02: Comparison table present
- **Method:** `grep`
- **Check:** `grep -qi 'bolt\|lovable\|freelanc' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"`

### FUNC-03: Loop badge present
- **Method:** `grep`
- **Check:** `grep -q 'loop-badge' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"`

### FUNC-04: Four-phase flow present
- **Method:** `grep`
- **Check:** `grep -qi 'discovery\|scaffold' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"`

## TEST Gates

### TEST-01: All 3 files exist
- **Method:** `run_code`
- **Check:** `test -f "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html" && test -f "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.css" && test -f "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.js"`

### TEST-02: HTML references CSS and JS
- **Method:** `run_code`
- **Check:** `grep -q 'vibe-coder.css' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html" && grep -q 'vibe-coder.js' "D:/my_ai_projects/isagawa-co.github.io/vibe-coder.html"`

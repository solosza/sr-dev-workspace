# Write Generation Reference

## Type
BUILD

## Description
Write the reference file for generating clean HTML/CSS from extracted data.

## Requirements
Create `.claude/skills/website-cloner/references/generation.md` with:
- How to convert extracted DOM + styles into clean semantic HTML
- CSS generation: organize by component, use CSS variables for colors/fonts
- Font handling: link Google Fonts or include @font-face declarations
- Image handling: download to assets/ folder, update src attributes
- Responsive: include media queries at original breakpoints
- Output structure:
  ```
  [output-dir]/
    index.html
    styles.css
    assets/
      images/
      fonts/
  ```
- Quality rules: no inline styles, semantic HTML tags, readable CSS

## Acceptance Criteria
- [ ] `test -f .claude/skills/website-cloner/references/generation.md`
- [ ] `grep -q "index.html" .claude/skills/website-cloner/references/generation.md`

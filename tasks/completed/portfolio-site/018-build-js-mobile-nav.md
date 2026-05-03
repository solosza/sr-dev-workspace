# Add Mobile Nav Toggle

## Context
The hamburger menu button needs JavaScript to toggle the mobile nav visibility. Minimal JS — just toggle a class on the nav links container.

## Type
BUILD

## Execution
inline

## Dependencies
- 017-build-js-smooth-scroll

## Phase Gate
- [ ] Smooth scroll CSS added

## Requirements
- Edit `D:\my_ai_projects\isagawa-portfolio-site\index.html`
- Add a small `<script>` block (can be at end of body, or combined with the Rekor verification script):
  - Select the hamburger button (`[data-menu-toggle]`)
  - On click, toggle class `nav__links--open` on the `.nav__links` element
  - Close menu when a nav link is clicked (remove `nav__links--open`)
- This is ~10 lines of JS, no framework needed

## Acceptance Criteria
- [ ] `index.html` contains JS that references `menu-toggle` or `hamburger`
- [ ] `index.html` JS toggles a class on nav links

## Gates Satisfied
- BUILD-17

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.

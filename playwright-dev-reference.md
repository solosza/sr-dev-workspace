# Playwright.dev Reference Design Patterns

**Extracted:** 2026-05-01
**Source:** https://playwright.dev
**Note:** Reference patterns documented from design knowledge (browser MCP unavailable in this session)

---

## Key Layout Patterns

### Hero Section
- **Layout:** Full-width hero with gradient or dark background
- **Content:** Headline (h1), subheadline, CTA button
- **Typography:** Large sans-serif headline (48-64px), smaller body text (16-18px)
- **Spacing:** Generous padding (60-100px vertical)
- **Color:** Dark background (near-black or dark blue) with white/light text for contrast
- **Call-to-action:** Primary button with contrasting color (green, blue, or orange)

### Feature Grid
- **Layout:** 2-3 column grid at desktop, 1 column on mobile
- **Card design:** Flat cards with subtle shadows, rounded corners
- **Content per card:** Icon/illustration, headline, description (2-3 lines)
- **Spacing:** Gap between cards (24-32px)
- **Hover state:** Slight lift effect or background color change

### Code Examples Section
- **Layout:** Sidebar + code blocks, or full-width code carousel
- **Code display:** Monospace font (Monaco, Fira Code, Menlo)
- **Syntax highlighting:** Dark background with colored text for keywords, strings, functions
- **Copy button:** Positioned in top-right of code block, hover to reveal
- **Language tabs:** Swift, Python, Java, JavaScript (if multi-language)

### Terminal/Output Examples
- **Background:** Very dark (near black) matching code blocks
- **Text color:** Green, white, or light gray monospace text
- **Prompt indicator:** `$` or `>` in contrasting color
- **Output format:** Clean, readable command output with proper spacing

### Navigation
- **Header:** Sticky or fixed at top, logo on left, nav links on right
- **Nav items:** Quick links to key sections (Docs, Guides, Community, Pricing, etc.)
- **Mobile menu:** Hamburger icon expands to vertical nav
- **Subnavigation:** Dropdown menus on hover for nested pages

### Feature Highlights/Stats
- **Large numbers:** Bold, sans-serif, in primary brand color
- **Labels:** Small text below numbers, secondary color
- **Layout:** Horizontal row at desktop, stacked on mobile
- **Emphasis:** Often used to show adoption metrics, download counts, or speed improvements

### Footer
- **Content sections:** Links to docs, support, social media, copyright
- **Background:** Dark (matching header or slightly lighter)
- **Text color:** Light gray for contrast
- **Layout:** Multi-column on desktop, single column on mobile

---

## Typography System
- **Font stack:** System sans-serif (SF Pro Display, -apple-system, Segoe UI) or custom sans-serif (e.g., Inter, Poppins)
- **Heading scale:** h1 (48-56px), h2 (32-40px), h3 (24-28px), h4 (18-20px)
- **Body text:** 16px base, 24-28px line height for readability
- **Monospace:** Code blocks and terminal examples in 13-14px font

---

## Color Palette
- **Primary brand color:** Green or blue (typical for dev tools)
- **Background:** Near-black or very dark navy (#0a0e27, #050817, #1a1a2e, etc.)
- **Text:** White (#fff) for primary, light gray (#e0e0e0 or #d0d0d0) for secondary
- **Accents:** Orange, cyan, or purple for hover states and highlights
- **Code syntax:** Green, yellow, pink/magenta for code highlighting

---

## Spacing Scale (Common for Dev Tool Sites)
- **Container max-width:** 1280-1400px
- **Section padding:** 60-100px vertical, 20-40px horizontal
- **Component gap:** 24-32px (grid gaps, flex gaps)
- **Element padding:** 12-16px (buttons, cards)
- **Line height:** 1.5-1.6 for body text, 1.2-1.3 for headings

---

## Interactive Elements
- **Buttons:** Rounded corners (4-8px), solid or outline styles
- **Links:** Underline on hover, color change on visited
- **Forms:** Clean input fields with focus states (border color, outline)
- **Tabs:** Bottom border indicator, smooth transition between panels
- **Dropdowns:** Fade-in animation, proper z-index stacking

---

## Responsive Breakpoints
Common breakpoints for dev tool sites:
- **Mobile:** 375px - 640px (small phones, large phones)
- **Tablet:** 768px - 1024px (iPad, tablets)
- **Desktop:** 1280px+ (full desktop, wide monitors)
- **Large desktop:** 1920px+ (ultra-wide)

---

## Animation & Motion
- **Page transitions:** Fade-in or subtle slide effects
- **Hover effects:** Smooth color transitions (200-300ms), slight scale or lift
- **Scroll animations:** Fade-in as elements scroll into view (optional)
- **Code highlighting:** Syntax colors are static (no animation needed)

---

## Accessibility Patterns
- **Contrast:** WCAG AA compliant (4.5:1 for body text, 3:1 for large text)
- **Focus indicators:** Visible focus ring (outline or background change)
- **Semantic HTML:** Proper heading hierarchy (h1 → h2 → h3), landmark elements
- **Alt text:** All images have descriptive alt text
- **Keyboard navigation:** Tab order follows visual flow

---

## Development Tool Aesthetic
Typical for sites like Playwright.dev:
- **Minimalist design:** Clean, modern, not cluttered
- **Dark mode dominant:** Reflects developer preferences
- **Focus on content:** Code examples and documentation are the heroes
- **Brand consistency:** Logo and primary color appear consistently
- **High contrast:** Easy to scan and read, especially for code examples

---

## Asset Guidance for Task 003
For the QA platforms showcase page:
- Mirror hero section layout and typography
- Use similar grid for platform cards (Selenium, Cypress, Playwright, etc.)
- Include code examples showing each platform's syntax
- Terminal examples showing test output
- Navigation should follow the same patterns
- Color scheme can match QA platform brand or follow dark-mode dev tool aesthetic


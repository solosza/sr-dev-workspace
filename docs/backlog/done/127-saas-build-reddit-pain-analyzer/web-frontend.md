# Web Frontend — User Interface & Experience

## Tech Stack

- **Framework:** Next.js 14 (React + SSR)
- **Styling:** Tailwind CSS
- **State management:** TanStack Query (React Query)
- **Auth:** NextAuth.js (JWT)
- **Forms:** React Hook Form + Zod validation
- **Deployment:** Vercel (optimized for Next.js)

## Pages & Routes

### Public Routes

| Route | Purpose | Elements |
|-------|---------|----------|
| `/` | Landing page | Hero, features, pricing, testimonials, CTA |
| `/auth/signup` | User registration | Email, password, T&Cs, submit |
| `/auth/login` | User login | Email, password, forgot password link |
| `/pricing` | Pricing table | 3 packages, features, FAQ |
| `/about` | About page | Mission, team, contact |

### Authenticated Routes

| Route | Purpose | Elements |
|-------|---------|----------|
| `/app` | Dashboard | Credit balance, input form, recent analyses |
| `/app/analyze` | Analysis form | Subreddit URL input, submit, job status |
| `/app/results/:jobId` | Results view | Pain points, ideas, scores, export button |
| `/app/history` | Analysis history | List of past analyses, re-run, export |
| `/app/account` | Account settings | Profile, password change, delete account |
| `/app/admin` | Admin dashboard | Usage stats, cost tracking, job queue |

## Key Components

### 1. Landing Page
**Copy reference:** https://redditpainanalyzer.com

**Sections:**
- Hero (headline, subheading, CTA)
- Features (4-5 key features with icons)
- How it works (3-step flow)
- Pricing (3-tier cards)
- Testimonials (3-5 quotes)
- FAQ
- Footer (links, social, copyright)

**Design:** Responsive, dark mode (optional), fast loading

### 2. Auth Flow
**Signup:**
- Email input
- Password input (strength indicator)
- T&Cs checkbox
- Submit button
- Error messages
- Link to login

**Login:**
- Email input
- Password input
- Remember me checkbox
- Submit button
- Forgot password link
- Error messages
- Link to signup

**Session:** JWT token in httpOnly cookie, refresh logic

### 3. Analysis Dashboard
**Layout:**
- Header: Logo, credit balance, user menu
- Main: Subreddit URL input form
- Results: List of recent analyses (sortable, filterable)
- Sidebar: Tips, FAQ, upgrade CTA

**Input form:**
- Label: "Enter subreddit URL"
- Input: text field, placeholder "https://reddit.com/r/entrepreneur"
- Button: "Analyze" (disabled until valid URL)
- Error: "Invalid subreddit URL" if needed
- Loading: Spinner while submitting

**Results list:**
- Table or card layout
- Columns: Date, Subreddit, Status, Pain Points, Action
- Status: Queued, Processing, Complete, Failed
- Actions: View results, delete, re-analyze

### 4. Results View
**Display:**
- Analysis metadata (date, subreddit, URL)
- Pain points section (list with frequency)
- Startup ideas section (cards with scores)
- Export button (JSON download)
- Share button (copy link to results)

**Pain points:**
```
1. Hard to find qualified contractors - 45% of posts
2. Expensive freelance platforms - 38% of posts
3. Time-consuming vetting process - 32% of posts
...
```

**Startup ideas:**
```
Card layout:
[Idea Title]
[Description]
Market Score: 8.5/10
[View details button]
```

### 5. Pricing Page
**Display:** 3-tier pricing with comparison

```
5 Credits    |  10 Credits  |  20 Credits (Popular)
€3.99        |  €4.99       |  €8.99
─────────────────────────────────────────────────
5 analyses   |  10 analyses |  20 analyses
Never expire |  Never expire|  Never expire
Buy Now [btn]|  Buy Now[btn]|  Buy Now [btn]
```

**Copy:**
- "Simple & Fair pricing"
- "You only pay when you analyze"
- "No subscriptions. No obligations."
- "Get 3 credits free on signup"

## Payment Integration

**Stripe setup:**
- Test mode for development
- Live mode for production
- Webhook handling (payment.intent.succeeded)
- Error handling (declined card, timeout, etc.)

**Flow:**
1. User clicks "Buy Now"
2. Stripe Checkout modal opens
3. User enters card details
4. Stripe processes payment
5. Webhook confirms payment
6. Credits added to account
7. Redirect to dashboard with success message

## Admin Dashboard

**Routes:** `/app/admin` (admin-only)

**Sections:**
1. **Usage metrics**
   - Total analyses this month
   - Revenue (MRR)
   - Active users
   - Avg cost per analysis

2. **Job monitoring**
   - Queue depth (processing jobs)
   - Failed jobs (with errors)
   - Slow jobs (>5 min processing)
   - Cost per job (real-time)

3. **User management**
   - Total signups
   - Conversion rate
   - Avg credits purchased
   - Top subreddits analyzed

4. **System health**
   - API uptime
   - Error rates
   - Database size
   - Cache hit rate

## Accessibility

- **WCAG 2.1 AA** compliance
- Semantic HTML (button, nav, main, etc.)
- ARIA labels for forms
- Keyboard navigation (Tab, Enter, Escape)
- Color contrast ratio >= 4.5:1
- Alt text for images

## Performance

- **Lighthouse target:** 90+ score
- Core Web Vitals: All green
- Lazy loading for images
- Code splitting per route
- Static generation where possible
- ISR (incremental static regeneration) for pricing page

## Mobile Optimization

- Responsive design (mobile-first)
- Touch-friendly buttons (min 48px)
- Readable text (min 16px font)
- Fast load on 3G/4G
- Offline support (optional: cache recent results)

## Security

- HTTPS only
- CSRF protection (NextAuth.js)
- XSS prevention (React escapes by default)
- SQL injection: Parameterized queries (Prisma ORM)
- Rate limiting (API routes)
- Password hashing (bcrypt, cost 12)

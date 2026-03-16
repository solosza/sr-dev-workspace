# Buyer Types and Matching Criteria — Lease Option Wholesaling

## Tenant-Buyer Profiles

Lease option tenant-buyers are people who **want to own** but have a **temporary obstacle** preventing traditional mortgage qualification. They are NOT renters — they are future homeowners on a defined path.

### Segment 1: Credit Repair Candidates

**Situation:** Had good credit, experienced a negative event (medical emergency, job loss, divorce), credit score dropped below mortgage threshold. Actively working to rebuild.

**Typical profile:**
- Credit score: 530-619 (needs to reach 620+ for conventional, 580+ for FHA)
- Income: Stable, often W-2 employed
- Timeline: 12-24 months to mortgage-ready
- Option fee capacity: Moderate ($5K-$10K) — had savings before the event
- Key need: Time to let negative items age off credit report + rebuild score

**How to frame the deal:** "Lock in today's price while your credit recovers. In 18-24 months, you'll qualify for a mortgage and this becomes YOUR home."

Sources: [Wendy Patton — Finding and Qualifying Tenant Buyers](https://wendypatton.com/finding-qualifying-tenant-buyer/), [Chase — Lease Option](https://www.chase.com/personal/mortgage/education/finding-a-home/lease-option)

---

### Segment 2: Self-Employed / 1099 Workers

**Situation:** Has the income but can't document it the way lenders require. Lenders want 2 years of tax returns showing consistent self-employment income. Newly self-employed (< 2 years) or writes off aggressively, reducing taxable income below qualifying thresholds.

**Typical profile:**
- Credit score: Often 620+ (credit isn't the issue)
- Income: Strong actual income, weak documented income
- Timeline: 12-24 months (need 2 years of self-employment tax history)
- Option fee capacity: Often high ($8K-$15K) — they have cash flow, just can't prove it to a lender
- Key need: Time to build a 2-year tax return history showing qualifying income

**How to frame the deal:** "You're earning well — you just need the paper trail. Lock in this home now, and by the time you have two years of tax returns, you'll sail through mortgage approval."

---

### Segment 3: Recent Life Transition

**Situation:** Divorce (assets split, credit dinged from joint accounts), recent immigrant (limited credit history in the US), military returning from deployment (transitioning to civilian employment), recently widowed (income change).

**Typical profile:**
- Credit score: Varies widely (500-680)
- Income: Often stable but recently changed
- Timeline: 12-36 months depending on situation
- Option fee capacity: Variable — divorce may have depleted savings, immigrants may have family support
- Key need: Time to establish or re-establish credit identity and stable income

**How to frame the deal:** "You're starting a new chapter. This gives you a home base while you get established. No rush — take the time you need to get mortgage-ready."

---

### Segment 4: First-Time Buyers Priced Out

**Situation:** Young professionals or families who can afford monthly payments but can't save enough for a traditional down payment (typically 3.5-20% of purchase price). May have student loan debt affecting DTI ratio.

**Typical profile:**
- Credit score: 600-680 (close but not qualifying with their DTI)
- Income: Growing (early career, raises expected)
- Timeline: 18-36 months (need to pay down debt and/or save more)
- Option fee capacity: Lower ($3K-$7K) — the down payment problem IS their problem
- Key need: A way to stop renting and start building toward ownership while their income grows

**How to frame the deal:** "Stop paying someone else's mortgage. Move in now, lock today's price, and your option fee goes toward your down payment when you're ready to buy."

---

### Segment 5: Burned by Previous Housing Situation

**Situation:** Previous foreclosure, short sale, or deed-in-lieu. These events stay on credit reports for 3-7 years. They may have fully recovered financially but the mark still disqualifies them from traditional lending.

**Typical profile:**
- Credit score: 580-640 (rebuilding, but the event itself is the barrier)
- Income: Often strong and stable (recovered from the crisis)
- Timeline: 24-36 months (waiting for the event to age off or fall below reporting threshold)
- Option fee capacity: Often high ($8K-$15K) — they've been saving and are financially stable now
- Key need: Time for the negative event to age off their credit report

**How to frame the deal:** "You've rebuilt your finances. You just need the clock to run. Lock in this home now and by the time the foreclosure ages off, you're ready to close."

Sources: [Rocket Mortgage — Lease Purchase](https://www.rocketmortgage.com/learn/lease-purchase-agreement), [NAR — Lease Option Purchases](https://www.nar.realtor/lease-option-purchases), [Wemert Group — Future of Rent-to-Own](https://wemertgrouprealty.com/future-of-rent-to-own-market-trends-and-predictions/)

---

## Matching Criteria

When a deal locks, the system matches deal attributes against buyer criteria. These are the fields that matter.

### Hard Filters (must match or deal is rejected for this buyer)

| Field | Data Type | Match Logic |
|-------|-----------|-------------|
| **Location** | array of strings (cities, zip codes, neighborhoods) | Deal's city/zip must be IN buyer's `target_areas` array |
| **Max price** | number ($) | Deal's purchase price must be ≤ buyer's `max_price` |
| **Max monthly payment** | number ($) | Deal's monthly rent must be ≤ buyer's `max_monthly_payment` |
| **Option fee budget** | number ($) | Deal's required option fee must be ≤ buyer's `option_fee_budget` |

If ANY hard filter fails → buyer is NOT a match for this deal. Do not contact.

### Soft Scoring Criteria (contribute to ranking, don't eliminate)

| Field | Data Type | Scoring |
|-------|-----------|---------|
| **Bedrooms** | number | Exact match: +20 / Within 1: +10 / Off by 2+: +0 |
| **Timeline alignment** | number (months) | Buyer ready within option period: +20 / Needs extension: +10 / Way over: +0 |
| **Option fee vs budget** | % of budget used | Fee < 50% of budget: +15 / 50-80%: +10 / 80-100%: +5 |
| **Monthly payment comfort** | % of max | Rent < 70% of max: +15 / 70-90%: +10 / 90-100%: +5 |
| **Segment fit** | enum | Strong segment match for this deal type: +10 / Neutral: +5 |
| **Last contact recency** | date | Active (< 30 days): +10 / Warm (30-90 days): +5 / Cold (90+ days): +0 |
| **Credit trajectory** | trend | Improving: +10 / Stable: +5 / Unknown: +0 |

### Scoring Weights and Tiers

**Total possible soft score: 100 points**

| Tier | Score Range | Action |
|------|------------|--------|
| **Excellent match** | 85-100 | Contact immediately in batch 1 |
| **Good match** | 65-84 | Contact in batch 2 (24h after batch 1) |
| **Moderate match** | 50-64 | Contact in batch 3 (48h after batch 1-2) |
| **Below threshold** | < 50 | Do NOT contact for this deal |

### Messaging Differentiation by Segment

The same deal gets framed differently depending on the buyer's segment:

| Segment | Lead With | Emphasize | De-emphasize |
|---------|-----------|-----------|-------------|
| **Credit repair** | "Your credit journey is almost done" | Timeline to mortgage-ready, credit counseling support | Monthly payment (they can afford it) |
| **Self-employed** | "Perfect for entrepreneurs" | No bank qualifying now, lock in price | Tax documentation (sensitive topic) |
| **Life transition** | "A fresh start" | New beginning, stability, community | Past situation (don't dwell on divorce/loss) |
| **First-time buyer** | "Your first home" | Building equity, option fee = down payment | Price (focus on monthly, not total) |
| **Previous foreclosure** | "You've rebuilt — now finish the journey" | Financial recovery, time heals, lock today's price | The past event (they're past it) |

---

## Buyer List Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Full name |
| `email` | string | Primary email |
| `phone` | string | Primary phone |
| `target_areas` | array[string] | Cities, zip codes, or neighborhoods they're interested in |
| `max_price` | number | Maximum purchase price they can consider |
| `max_monthly_payment` | number | Maximum monthly rent/payment |
| `option_fee_budget` | number | Maximum option fee they can pay |
| `min_bedrooms` | number | Minimum bedrooms needed |
| `credit_score_current` | number | Current credit score |
| `timeline_months` | number | Estimated months to mortgage-ready |
| `segment` | enum | One of: credit_repair, self_employed, life_transition, first_time_buyer, previous_foreclosure, other |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `bathrooms_preferred` | number | Preferred minimum bathrooms |
| `sqft_minimum` | number | Minimum square footage |
| `school_district` | string | Preferred school district |
| `income_type` | enum | W2, 1099, mixed |
| `monthly_income` | number | Gross monthly income |
| `credit_score_target` | number | Score needed for their loan type |
| `referral_source` | string | How they found you |
| `last_contact` | date | Date of most recent interaction |
| `notes` | string | Free-text notes |
| `status` | enum | new, active, matched, interested, scheduled, closed, inactive |

---

## Key Insight: The "Bad Credit with Reason" Filter

Wendy Patton identifies 4 credit categories for tenant-buyers:

1. **Good credit** — don't need a lease option, skip
2. **Deadbeats** — chronic poor money management, will never qualify, REJECT
3. **Bad credit with reason** — THE IDEAL CANDIDATE. Temporary setback, actively improving, will qualify with time
4. **Unknown** — unclear trajectory, needs lender evaluation before committing

The system should identify and prioritize **category 3** buyers. Red flags for category 2 (deadbeats):
- Blames others for financial problems
- Multiple strings of unpaid debts with no attempt to resolve
- Short employment tenure across many jobs
- Fraudulent items on credit report
- Cannot articulate a plan to improve their situation

Source: [Wendy Patton — Finding and Qualifying Tenant Buyers](https://wendypatton.com/finding-qualifying-tenant-buyer/)

# Nurse Visit Sign-Up — how the sheet actually works (from live artifact, Aug 12 view)

## Structure
- Month calendar → tap a day → **day detail** shows a fixed list of **predefined visits** for that day.
- "X/11 covered" = how many of that day's visits have a nurse signed up.
- Visits are grouped into time-of-day **sections**: Morning Visits, (Lunch?), Dinner, Bedtime.
- Each **visit** = { time, patient name, location/house, care task } + a "Sign up for this visit" button.
- A nurse claims an **individual visit** (not just "a slot"). So one nurse per visit → double-booking race is real here.

## The 11 visits shown for Wednesday, Aug 12, 2026 (0/11 covered)
Morning Visits
1. 6:00 AM — Frederick Brown · Dunrobin — Accucheck & sliding scale
2. 6:15 AM — Edwin Portillo · Faust — Accucheck only
3. 6:30 AM — Dennis Smith · Stoakes — Accucheck, Lantus long-acting insulin & Novolog sliding scale
4. 6:45 AM — Dennis Smith · Stoakes — Wound assessment
5. 7:00 AM — Rosa — All vitals & breathing treatment
6. 11:00 AM — Rosa — All vitals & breathing treatment
Dinner
7. 3:00 PM — Rosa — All vitals & breathing treatment
8. 3:30 PM — Dennis Smith · Stoakes — Accucheck & sliding scale
9. 4:00 PM — Frederick Brown · Dunrobin — Accucheck & sliding scale
Bedtime
10. 7:00 PM — Dennis Smith · Stoakes — Bedtime accucheck & Novolog sliding scale
11. 7:15 PM — Rosa — All vitals & breathing treatment

## Open questions (need user)
1. Same 11 visits EVERY day, or does each day have its own schedule? (Demo showed varying counts but that was random seed.)
2. Is the Aug 12 list REAL patient data or placeholder?  → privacy implications.
3. On "Sign up" — does it capture the nurse's NAME? (prompt / name field / login?)
4. Can a nurse cancel/un-sign-up?

## Data model implication (draft)
- `visits` table: id, visit_date, section, sort_order, time_label, patient_name, location, task, claimed_by (nullable)
- Claim = conditional update: SET claimed_by=X WHERE id=? AND claimed_by IS NULL  → wins the race, loser gets "already taken"
- Count "/11" = count of claimed visits that day.

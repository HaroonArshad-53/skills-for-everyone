# Examples & Expected Results — Skills for Everyone

One full use case for **every skill**: the situation, the exact prompt to type, which skill loads, and the **proper result** you should get.

> These are illustrative example outputs that follow each skill's defined output format. Your wording will differ — your *structure and honesty* should match. If your agent's output skips sections or invents facts, see Troubleshooting in [SETUP.md](SETUP.md).

---

## Freelancer Bundle

### 1. client-brief-analyzer — the vague job post

**Situation:** A job post says a lot and means little. You need to know what the job is before you price it.

**You type:**
> Analyze this job post: "Need someone to fix my website, it's slow and some pages broken, need it done ASAP, budget is small, maybe more work later..."

**Proper result:**
- **One-line summary:** Fix performance and broken pages on an existing website — scope undefined.
- **Deliverables:** Only what was stated: speed fix + broken pages (which pages: not stated).
- **Known facts:** Deadline = "ASAP" (undefined) · Budget = "small" (undefined) · Platform = UNKNOWN
- **Missing information:** Which pages are broken, current platform and hosting access, what "ASAP" means in days, the actual budget range.
- **Red flags:** "More work later" is being used to justify a low first budget.
- **Questions to send the client:** 1) Which pages are broken, and what happens on them? 2) What platform is the site on, and can you share hosting access? 3) What date do you need this live by? 4) What budget range is approved for this first job?
- **Verdict:** Workable after questions — quote this job on its own value.

### 2. proposal-writer — no reviews yet, still credible

**Situation:** You're new on Upwork. You can't fake a track record — the skill wins with specificity instead.

**You type:**
> Write my Upwork proposal for this logo job post [post pasted]. I've done 3 logos for local shops, I use Illustrator, no online reviews yet.

**Proper result (excerpt):**
> "Your post mentions the current logo looks fine on the shop sign but unreadable on Instagram — that's a scalability problem, not a design-taste problem, and it's fixable in the first concept round. My plan: (1) audit the current logo at small sizes, (2) deliver 3 simplified concepts built to stay readable at profile-picture size, (3) refine the one you pick, (4) export the full pack (sign, social, print). I've done this for 3 local shops in Illustrator. Happy to start with the concept round as a first milestone so you can judge the work before committing to the full pack."

Plus: **Why this angle** (targets the client's stated pain) and **one thing to personalise** before sending. Nothing about experience was invented.

### 3. project-scope-planner — from "yes" to a real plan

**Situation:** The client accepted. Now the project needs milestones a client can approve — and boundaries.

**You type:**
> Plan this project: 5-page WordPress site, I work 4 hours/day, start Monday, client wants it in 2 weeks.

**Proper result (excerpt):**
- **Milestone 1 (Days 1–3):** Setup + homepage draft the client can view — 10 hrs. *Done means: client has a staging link.*
- **Milestone 2 (Days 4–7):** Remaining 4 pages built from approved homepage style — 14 hrs.
- **Milestone 3 (Days 8–10):** Contact forms, mobile pass, speed check, handover — 8 hrs + buffer.
- **Client must provide:** logo + hosting login by Day 1 · page text by Day 3 · feedback within 24h per milestone.
- **Not included:** writing page copy, premium plugin licences, more than 5 pages, content changes after approval (quoted as new scope).
- **Revisions:** 2 rounds per milestone included.

### 4. pricing-calculator — a quote with its maths showing

**Situation:** You need a number you can defend — to the client and to yourself.

**You type:**
> How much should I charge for a 20-hour logo + brand kit on Upwork? I'm intermediate, $15/hr, due in 5 days, 3 revision rounds.

**Proper result:**
- **Inputs used:** 20h × $15 · Upwork fee 10% · rush <7 days (1.25×) · 3 revision rounds (+10%)
- **Low:** quote $389.58 → you keep $350.63 · **Recommended:** quote $458.33 → you keep $412.50 · **High:** quote $572.92 → you keep $515.63
- **Why:** the quote is grossed up so the fee comes out of the client's price, not your pocket; rush and the extra revision round are priced, not absorbed.
- (When Python is available the agent runs `scripts/pricing.py` and uses its exact output — same numbers as the demo on the README.)

### 5. professional-email — the angry payment follow-up, fixed

**Situation:** Second follow-up on an unpaid invoice. Your draft is honest but emotional.

**You type:**
> Make this professional, second follow-up: "bhai payment ka kya hua, 2 week ho gaye hain, kaam to kab ka deliver kar diya tha, please bata dein"

**Proper result:**
- **Subject:** Payment follow-up — Invoice #12, delivered 1 Oct
- **Body (Clear tone):** "I hope you're well. I'm following up on Invoice #12 for the delivered website work, due on 1 Oct. Could you please confirm the payment date this week? If any document is needed from my side, I'll send it today."
- **Tone used:** Clear — second attempt, so dates and a specific ask, still no threats.
- Facts kept exactly; frustration removed; nothing promised that you didn't write.

### 6. portfolio-case-study — proof without a single fake number

**Situation:** Project done, client happy, zero measurable metrics. Most people either skip the case study or invent percentages.

**You type:**
> Make a case study: I redesigned a bakery's logo and menu cards, small local bakery, 1 week, Illustrator, owner said customers compliment the new menu. No sales numbers.

**Proper result (excerpt):**
- **The Problem:** Text-only menu cards, hard to read at the counter; logo unreadable at small sizes.
- **The Process:** Readability audit → type hierarchy redesign → logo simplified for small sizes → in-store print test.
- **The Result:** "The owner reports customers now compliment the menu cards in-store." *(No percentage invented — because there isn't one.)*
- Plus a ready-to-paste LinkedIn version and the ordered list of visuals to attach.

---

## Student & First-Job Bundle

### 7. study-any-topic — learn it, then prove you learned it

**Situation:** Viva next week, the textbook chapter reads like a wall.

**You type:**
> Explain public key cryptography — I'm a 2nd-year CS student, viva next week.

**Proper result (structure):**
- **In one line:** Anyone can lock a box for you; only you have the key that opens it.
- **Real-life example → proper terms** (public key / private key) **→ how it works** step by step → **common mistake** (believing the public key decrypts).
- **Quiz (answers separated, with reasons):** includes the trap — *"If someone has your public key, can they decrypt your messages?"* (No.)
- **5 flashcards** + **3 "remember this" exam bullets.**

### 8. fyp-project-manager — a 5-month project, divided

**Situation:** Team of 3, AI attendance system, nothing started, deadline in 5 months, supervisor wants weekly updates.

**You type:**
> Plan my FYP and divide it into weekly tasks.

**Proper result (excerpt):**
- First, one round of interview questions (deliverables, deadline, team, tools) — *then* the plan.
- **PROJECT-PLAN.md:** phases Proposal → Research → Design → Build → Testing → Report → Presentation, with report writing starting in **month 3, not month 5**, a weekly task table with named owners and "done means…" lines, and 2 buffer weeks before testing.
- **Risk #1 flagged:** dataset collection — "if photos aren't collected by week 6, switch to a public dataset."
- **This week's tasks** ready to start, plus the 5-line supervisor update format.

### 9. assignment-researcher — real sources or an honest gap

**Situation:** 1,500-word assignment, APA style, and you refuse to submit fabricated references (your university checks).

**You type:**
> Help me research: "Impact of social media on student mental health", 1500 words, APA, undergrad.

**Proper result (structure):**
- **Outline** built on the actual question — both directions of impact, not a one-sided essay.
- **Research notes per section**, every point tagged **Fact / Interpretation / Gap** with the source type it needs.
- **Gap reported honestly:** "Recent Pakistan-specific statistics could not be verified from an official source — use WHO/global figures or your university's survey data instead." A skill that admits a gap is the whole point.
- **Reference list (APA)** — verified sources only — and **your argument in 5 bullets** so you write the prose yourself.

### 10. interview-griller — practice that doesn't lie to you

**Situation:** SOC analyst internship interview. Reading model answers feels productive and isn't.

**You type:**
> Grill me for a SOC analyst internship interview. I have CEH, fresh graduate.

**Proper result (how it runs):**
- **One question at a time.** Q1: *"A user reports their account sent emails they never wrote. Walk me through your first 15 minutes."* Then it waits.
- **After your answer — Score 6/10.** Strong: you checked the account first. Missing: you never preserved evidence or checked sign-in logs before resetting the password — order matters in SOC work. Then the 2-sentence strong version.
- Difficulty rises when you score 7+, drops back to teaching under 4. Ends with a **report card**: readiness /10, your 3 weak spots, and a focused revision list.

### 11. resume-builder — stronger bullets, zero invented facts

**Situation:** Messy notes + a real job post. Your current bullets say nothing; the temptation is to inflate them.

**You type:**
> Make my resume from these notes and tailor it to this SOC analyst job post. [notes + post pasted]

**Proper result (excerpt):**
- Bullet rewritten: before — *"Responsible for security monitoring."* After — *"Monitored sign-in and endpoint alerts during internship shifts; escalated 2 confirmed phishing incidents to the senior analyst with evidence preserved."* No metric invented — scope and action did the work.
- **Tailoring notes:** which keywords from the job post were matched, and where.
- **Honesty audit:** every claim that was softened or removed, and why.
- **Before you send:** correct filename (`Firstname-Lastname-Resume.pdf`) + final 3-point checklist. ATS structure throughout: standard headings, no tables, no graphics.

### 12. learn-in-30-days — a plan that survives contact with real life

**Situation:** Zero Python, 1.5 hours a day, wants a freelancing-ready small project in 30 days. Generic roadmaps would plan 6 hours a day and die by day 4.

**You type:**
> I want to learn Python for freelancing, I know zero, 1.5 hours a day, one small project done in 30 days.

**Proper result (structure):**
- **Your contract:** Python · true zero · one demo-able project · 1.5h/day — the plan is built from these numbers only.
- **4 weekly stages:** Foundations → Guided Practice → Independent Practice → Project + Test. Week 4's project is scoped to the contract: a *file-organiser script you can demo to clients* — not "build a web app."
- **One main task per day** (Day 1: install Python, write a program that renames one file — small, finished, motivating), a rest/light day each week, a self-test each week, and the **fall-behind rule**: drop the tasks marked optional, never the weekly project or test.
- Honest intro line included: 30 days builds a foundation and proof of work — not mastery.

---

**Want a skill that isn't here yet?** Open an issue describing the job, or add it yourself — see [CONTRIBUTING.md](../CONTRIBUTING.md).

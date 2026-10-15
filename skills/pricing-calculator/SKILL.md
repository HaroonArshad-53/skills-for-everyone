---
name: pricing-calculator
description: Calculate a fair freelance project price or hourly rate from hours, experience level, platform fees, rush deadlines, and revision rounds, and present a low, recommended, and high quote with the reasoning. Use when a user asks how much should I charge, price this project, is this budget fair, or wants to convert a monthly salary goal into an hourly rate. If Python is available, run the bundled scripts/pricing.py for exact numbers instead of estimating.
---

# Pricing Calculator

## When to use this skill
- Quoting a fixed-price project
- Deciding if a client budget is worth it
- Converting a monthly income goal into an hourly or project rate

## Workflow
1. Collect the inputs that change the price: estimated hours (use the project-scope-planner output if it exists), experience level (beginner, intermediate, expert), platform fee percent (Upwork 10, Fiverr 20, direct 0 by default - confirm with the user), deadline rush (normal, under 7 days, under 48 hours), revision rounds included.
2. If scripts/pricing.py is available in this skill folder, run it with these inputs and use its exact output. Otherwise calculate: base = hours x hourly rate; rush multiplier 1.25x for under 7 days, 1.5x for under 48 hours; each revision round beyond 2 adds 10 percent; then gross up so the user still receives the target after the platform fee: quote = target / (1 - fee).
3. Present three numbers: Low (win the job, thin margin - state the risk), Recommended (fair for both sides), High (premium positioning, faster or richer scope).
4. Show what the user actually keeps after the platform fee for each number. The take-home number is the truth, not the quote.
5. If the client stated budget is below the Low number, say that plainly and suggest either a reduced scope that fits the budget, or declining. Never just lower the price to match.

## Rules - never break these
- Never do the fee maths in your head if the script is available - run scripts/pricing.py.
- State every assumption (hours, rate, fee percent) next to the quote so the user can correct one number and recalculate.
- A quote is hours x value, not a guess. If hours are unknown, price a paid discovery or pilot milestone instead of guessing the whole project.
- Currency: use the user currency and, for international platforms, also show the USD figure if they gave a USD rate.

## Output format
- Inputs used - hours, rate, level, fee percent, rush, revisions
- Low / Recommended / High quotes - with take-home after fees for each
- Why - 2-3 lines of reasoning
- If the client says it is too much - the reduced scope that honestly fits their budget

## Example
**User:** How much should I charge for a 20-hour logo and brand kit project on Upwork? I am intermediate, my rate is 15 dollars per hour, client wants it in 5 days, 3 revision rounds.

**Good output (excerpt):** Run pricing.py: base 300, rush 1.25x = 375, extra revision round +10 percent = 412.50, grossed up for the Upwork 10 percent fee = 458 quote to keep 412. Recommended quote: 460. Take-home shown for all three tiers.

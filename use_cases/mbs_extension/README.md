# Use Case — MBS Extension Scenario

## PM question
A portfolio holds a $1,000,000 face, 6% WAC agency MBS pool, 30-year
amortization. Rates rise sharply to 8%. How does the pool's weighted
average life (WAL) respond, and why is that the opposite of what a
normal (positively convex) bond would do?

## Concepts
prepayment (CPR/SMM), refinancing incentive, weighted average life,
extension risk, negative convexity.

## First exercise
Using `pm.fixed_income.mbs.mortgage_amortization_schedule`,
`refinancing_incentive_cpr`, `single_monthly_mortality`,
`apply_prepayment`, and `weighted_average_life`:

1. compute WAL at a 4% market rate (rates fall — refinancing incentive
   kicks in)
2. compute WAL at an 8% market rate (rates rise — prepayments floor at
   the base CPR, no incentive to refinance)
3. compare: WAL at 4% ≈ 13.97 years, WAL at 8% ≈ 14.98 years — which
   direction is "extension," and why does that hurt a holder who was
   counting on the pool paying down faster?

## Extend
A plain option-free bond of similar duration would see its effective
duration *shorten* as rates rise (less time value left) — MBS extension
is the opposite. Read
`reference/fixed_income/mbs_convexity.md`'s "What's demonstrable here,
and what isn't" section, then explain in your own words why this WAL
shift is a correct, verifiable result even though full negative-
convexity price behavior isn't modeled here.

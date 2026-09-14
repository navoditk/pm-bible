# Prepayment Models: CPR, SMM, PSA

## One-line definition
CPR (Conditional Prepayment Rate) is the annualized rate at which a pool
prepays; SMM (Single Monthly Mortality) is its monthly equivalent; PSA is
a standard benchmark CPR ramp used to quote prepayment speeds.

## Formulas
`SMM = 1 - (1 - CPR)^(1/12)`

PSA benchmark (100% PSA): CPR ramps linearly from 0% to 6% over the first
30 months, then flat at 6%. `psa_cpr(month, psa_multiplier)` in
`src/pm/fixed_income/mbs.py` implements this (150% PSA = 1.5x the ramp).

## Behavioral prepayment (why CPR isn't constant)
`refinancing_incentive_cpr(wac, market_rate, base_cpr, sensitivity)` is a
simple model: prepayments speed up when the pool's coupon (WAC) is well
above current market rates (refinancing incentive), and floor at a base
rate when there's no incentive (rates have risen).

## Why PMs care
Prepayment speed assumptions drive WAL, effective duration, and price —
two analysts can disagree sharply on an MBS's value purely from different
prepayment speed assumptions, with no disagreement on the cash-flow model.

## Limitations
Real prepayment models also incorporate seasoning, burnout, seasonality,
and turnover (home sales) — this repo's `refinancing_incentive_cpr` only
captures the refinancing-incentive effect.

## Related
- [Pass-throughs](pass_throughs.md)
- [MBS negative convexity](mbs_convexity.md)
- [Effective duration](effective_duration.md)

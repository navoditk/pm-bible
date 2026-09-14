# Key-Rate Duration

## One-line definition
Sensitivity to a yield change at a selected maturity/key point while holding the rest of the curve according to the chosen bump methodology.

## Why PMs care
Two portfolios can have identical aggregate duration but very different curve exposure.

## Approximation
`dP/P ≈ -sum_k KRD_k * dy_k`

## Limitations
`key_rate_return_approximation` in `src/pm/fixed_income/curve.py` takes
KRDs as given inputs — unlike `modified_duration`, nothing in this repo
computes a bond's KRD profile from its cash flows (that needs bumping one
point on the curve at a time and repricing, holding the rest fixed).
Treat KRD as data you're given or estimate elsewhere, not something this
repo derives for you.

## Related
- [DV01](dv01.md)
- [Curve trades (steepener/flattener, butterfly)](curve_trades.md)

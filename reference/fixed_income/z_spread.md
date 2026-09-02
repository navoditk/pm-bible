# Z-Spread

## One-line definition
The constant spread added to every point on the zero (spot) curve that
reprices a bond to its observed market price.

## Formula
Solve for `s` in:

`Price = sum_t CF_t / (1 + (z(t) + s)/frequency)^(t*frequency)`

where `z(t)` is the interpolated zero rate at time `t`. No closed form —
`z_spread` in `src/pm/fixed_income/credit.py` root-finds it.

## Why PMs care
Z-spread is a cleaner credit-risk measure than a nominal yield spread
(YTM minus a benchmark yield) because it's measured against the whole
curve shape, not a single benchmark point — it isolates the compensation
for credit/liquidity risk from curve-shape effects.

## Limitations
Assumes the bond has no embedded optionality. For callable/putable bonds,
Z-spread overstates true credit compensation — see `oas.md`.

## Related
curve construction, OAS, spread duration.

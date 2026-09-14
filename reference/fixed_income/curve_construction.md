# Curve Construction (Bootstrapping)

## One-line definition
Deriving a zero (spot) rate curve from observed par yields.

## Method
For consecutive annual-pay par bonds, solve maturities shortest-to-longest:
already-known zero rates discount the earlier coupons, and the equation is
solved for the new zero rate at each new maturity.

## Why PMs care
Zero rates, not par yields, are the correct discount rates for pricing
arbitrary cash flows and computing forward rates.

## Limitations
`bootstrap_zero_rates` in `src/pm/fixed_income/curve.py` only handles
consecutive integer-year, annual-pay tenors. A real curve build needs
semiannual coupons and interpolation for sparse/off-cycle tenors
(e.g. 2Y/5Y/10Y/30Y) — see `interpolate_zero_rate` for the latter.

## Related
- [Forward rates](forward_rates.md)
- [Key-rate duration](key_rate_duration.md)
- [Curve trades](curve_trades.md)

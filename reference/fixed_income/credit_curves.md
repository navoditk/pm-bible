# Credit Curves, IG, and HY

## One-line definition
The term structure of credit spread by tenor for a given issuer or rating
bucket — same idea as a Treasury zero curve, applied to credit spread.

## Construction
Reuse `interpolate_zero_rate` from `src/pm/fixed_income/curve.py` on
spread points instead of yield points — a credit curve is interpolated
the same way a rates curve is.

## Vocabulary
- **Investment grade (IG)**: rated BBB-/Baa3 or above — lower spread,
  lower default probability.
- **High yield (HY)**: rated BB+/Ba1 or below — higher spread, higher
  default probability, more convex to spread widening.
- IG and HY often move together directionally but with very different
  magnitudes — see `use_cases/spread_shock/README.md`.

## Why PMs care
Credit curve shape (steep vs. flat, IG vs. HY) reflects the market's view
of near-term vs. long-term default risk for that issuer or sector.

## Related
- [Curve construction](curve_construction.md)
- [Z-spread](z_spread.md)
- [Default and recovery](default_recovery.md)
- [Sovereign and EM debt](sovereign_and_em_debt.md)

# Curve Trades (Steepeners, Flatteners, Butterflies)

## One-line definition
DV01-neutral positions across two or more points on the curve, expressing a
view on curve shape rather than the level of rates.

## Construction
Two-leg trade: use `hedge_ratio(target_dv01, hedge_instrument_dv01)` from
`src/pm/fixed_income/duration.py` to size the offsetting leg so the
combined position has ~zero net DV01. A steepener is long the short end /
short the long end (or vice versa for a flattener); a butterfly adds a
third, belly leg.

## Why PMs care
Two portfolios can share identical aggregate duration but react oppositely
to a steepening vs. flattening curve — curve trades isolate that exposure.

## Vocabulary
front end, belly, long end, 2s10s, 5s30s, twist — see
`notebooks/fixed_income/09_duration_curve_risk.ipynb`.

## Limitations
DV01-neutral is not curve-neutral under a non-parallel shock; use
[key-rate duration](key_rate_duration.md) to check the real exposure at
each tenor.

## Related
- [Key-rate duration](key_rate_duration.md)
- [Forward rates](forward_rates.md)
- [Carry and rolldown](carry_and_rolldown.md)
- [Repo and financing](repo_and_financing.md)
- [Stress testing (scenario analysis)](../concepts/stress_testing.md)

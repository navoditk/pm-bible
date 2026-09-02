# FX Spot, Forward, and Covered Interest Parity

## One-line definition
The FX forward rate is the spot rate adjusted for the interest-rate
differential between the two currencies — no independent forecast of
future spot is involved.

## Formula (covered interest parity, CIP)
`F = S * (1 + r_domestic*T) / (1 + r_foreign*T)`

`S` quoted as domestic currency per unit of foreign currency (e.g. USD
per EUR).

## Why PMs care
CIP means the forward rate is a mechanical, no-arbitrage function of
rates, not a market view on where spot is headed. A PM pricing a hedge
or a cross-currency trade needs the forward, not a spot forecast.

## Worked example
`Spot = 1.10` (USD/EUR), `r_USD = 5%`, `r_EUR = 3%`, `T = 1` year:

`F = 1.10 * 1.05 / 1.03 ≈ 1.1214`

The higher-rate currency (USD) trades forward at a *discount* relative to
the lower-rate currency's spot advantage — EUR is "expensive forward."

## Common mistakes
- treating the forward rate as a spot forecast
- getting the base/quote currency convention backwards (which rate goes
  in the numerator matters)

## Related
cross-currency basis, FX carry, forward rates (same no-arbitrage logic
applied to a single currency's curve).

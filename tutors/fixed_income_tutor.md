# Fixed-Income Tutor

## Coverage
bond math, duration, DV01, convexity, curve risk, KRD, spreads, curve
construction, forward rates, curve trades (steepener/flattener/butterfly),
swap DV01, swap spreads, Treasury futures hedging, carry and rolldown,
repo/specialness/on-the-run vs. off-the-run, TIPS and breakeven
inflation, Z-spread, credit curves, default/recovery, hazard rates, CDS
spreads, CDS-bond basis, credit indices (CDX/iTraxx), fundamental
credit analysis (leverage/coverage ratios, covenants), leveraged loans,
agency MBS pass-throughs, CPR/SMM/PSA prepayment, effective duration,
extension and contraction (WAL response to rates), TBA and the dollar
roll (implied financing rate), specified pools and pay-ups, CMO/REMIC
tranche structuring (sequential, PAC, support), municipal bonds
(tax-equivalent yield), convertible bonds (conversion value/premium),
preferred securities (perpetuity valuation, reusing the equity module's
Gordon growth function at zero growth), sovereign and EM debt (hard vs.
local currency).

Conceptual only, not implemented as code (be upfront about this if asked):
OAS (including MBS negative convexity in *price* terms - see
`reference/fixed_income/mbs_convexity.md` for exactly what is and isn't
shown), credit rating migration, non-agency/ABS/CMBS tranche waterfalls,
specified-pool pay-ups, CMO/REMIC tranche cash-flow waterfalls, municipal
and sovereign credit analysis (the fundamental-credit ratio machinery
applies to corporates, not governments), the straight-bond floor for
convertibles.
Not yet covered (later modules): FX, commodities.

## Diagnostic example
Before teaching duration, ask:
"What happens to the price of a fixed-rate bond when its required yield rises, and why?"

Adapt from there.

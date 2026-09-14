# CMO / REMIC Structuring

## One-line definition
A CMO (collateralized mortgage obligation), issued through a REMIC (real
estate mortgage investment conduit) tax structure, carves a single pool
of mortgage cash flows into multiple bonds ("tranches") with different
principal-payment priority — reshaping one pass-through's prepayment risk
into several bonds with different risk profiles, rather than eliminating
that risk.

## Vocabulary
- **Sequential-pay tranche**: the simplest structure — every tranche
  receives interest, but principal goes entirely to the first (shortest)
  tranche until it's fully retired, then entirely to the second, and so
  on. This turns one pool's prepayment uncertainty into a set of bonds
  with different, more defined *average lives*, even though total
  prepayment risk across all tranches combined is unchanged.
- **PAC (Planned Amortization Class) tranche**: designed to receive a
  predetermined principal paydown schedule as long as prepayments stay
  within a specified band (e.g., 90–300 PSA); a support tranche absorbs
  the variability outside that band, giving the PAC investor materially
  more certain cash flows than the underlying collateral itself has.
- **Support (companion) tranche**: absorbs whatever prepayment
  variability the PAC tranche is structured to avoid — if the pool
  prepays faster than expected, the support tranche shrinks faster; if
  slower, it extends longer. In exchange for bearing that variability,
  support tranches typically offer the highest yield in the structure.
- **REMIC**: the tax election that lets a CMO issuer split cash flows
  into multiple tranches without triggering double taxation at the
  entity level — a legal/tax wrapper, not a cash-flow mechanism in its
  own right.

## Why PMs care
A CMO doesn't create or destroy prepayment risk — it redistributes it.
Understanding tranche structure is what lets a PM pick the specific
risk/return profile they actually want (a PAC tranche for cash-flow
certainty, a support tranche for yield pickup in exchange for absorbing
someone else's prepayment risk) instead of taking a generic pass-through's
blended exposure. This is directly the flip side of [MBS
convexity](mbs_convexity.md): a plain pass-through's negative convexity
is the sum of extension risk (support/long-sequential tranches) and
contraction risk redistributed unevenly across a capital structure — a
PAC tranche is specifically engineered to look less negatively convex
than the collateral behind it, at the support tranche's expense.

## Why this isn't implemented in `src/pm`
Modeling how a specific prepayment path allocates across sequential, PAC,
and support tranches requires a full cash-flow waterfall engine —
tracking scheduled and unscheduled principal, interest, and the specific
priority rules of each tranche period by period under an assumed
prepayment path — which is a materially larger project than this repo's
"small transparent function" style, and the same reasoning that keeps
[non-agency structuring](non_agency_overview.md) and full OAS/negative-
convexity pricing conceptual-only applies here. The prepayment building
blocks that *would* feed such a waterfall — `psa_cpr`,
`refinancing_incentive_cpr`, `single_monthly_mortality`, and
`mortgage_amortization_schedule` — are already implemented in
[prepayment models](prepayment_models.md) and
[pass-throughs](pass_throughs.md); what's missing is the tranche-priority
allocation logic layered on top, not the underlying cash-flow math.

## Common mistakes
- assuming a PAC tranche's stated average life is guaranteed — it's
  guaranteed only within the PAC band; extreme prepayment speeds outside
  that band (very fast or very slow) can still cause a PAC tranche to
  extend or contract, once the support tranche protecting it is
  exhausted
- treating "senior" (paid first, sequential-pay) as synonymous with
  "safer" the way it is in a corporate capital structure — in a CMO, an
  early sequential tranche has *shorter* average-life uncertainty, not
  necessarily better credit quality (agency CMOs all carry the same
  agency guarantee regardless of tranche)
- forgetting that total prepayment risk across a REMIC's tranches sums to
  the same total risk in the underlying collateral — structuring
  reallocates risk, it doesn't reduce it; if a PAC tranche looks safer,
  something else in the same deal is bearing correspondingly more

## Related
- [MBS negative convexity](mbs_convexity.md)
- [Prepayment models](prepayment_models.md)
- [Non-agency overview](non_agency_overview.md)
- [Pass-throughs](pass_throughs.md)

## Free resources
- [Collateralized Mortgage Obligations (CMOs) — thisMatter.com](https://thismatter.com/money/bonds/types/collateralized-mortgage-obligations.htm) — plain-language walkthrough of sequential, PAC, and support tranche mechanics with worked examples
- [Investor's Guide to RMBS & CMOs — SIFMA](https://www.53.com/content/dam/fifth-third/docs/legal/fts-sifma-investors-guide.pdf) — the industry-association reference guide covering REMIC structuring conventions in more depth

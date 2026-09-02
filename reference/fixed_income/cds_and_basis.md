# CDS and CDS-Bond Basis

## One-line definition
A credit default swap (CDS) is insurance against an issuer's default; the
CDS-bond basis is the gap between the CDS spread and the equivalent cash
bond's spread for the same credit.

## Formulas
Par CDS spread (see `default_recovery.md`): `spread ≈ hazard_rate * (1 - recovery_rate)`

`basis = cds_spread - bond_spread`

## Why PMs care
CDS lets a PM take a pure credit view without funding a cash bond
position, and lets them short credit (hard to do in cash bonds). A
persistently nonzero basis is itself a tradeable signal — technicals
(funding costs, index positioning, cash bond supply) drive it as much as
credit fundamentals.

## Common mistakes
- assuming CDS and cash bond spreads should always be equal — the basis
  exists precisely because they're different instruments with different
  funding, counterparty, and liquidity profiles
- ignoring that a negative basis (CDS cheaper than bonds) versus positive
  basis calls for opposite trades

## Related
default and recovery, Z-spread, credit curves.

# Non-Agency Securitized: ABS, CMBS, Non-Agency MBS

## One-line definition
Securitizations backed by collateral other than agency-guaranteed
residential mortgages — auto loans, credit cards, student loans (ABS),
commercial mortgages (CMBS), or residential mortgages without a
government guarantee (non-agency/private-label MBS).

## Key difference from agency MBS
No government guarantee means credit risk is real and priced — these
structures use **tranching** (subordination) to redistribute credit risk:
senior tranches are protected by junior/subordinate tranches absorbing
losses first.

## Why PMs care
Yield pickup versus agency MBS or Treasuries compensates for credit risk,
structural complexity, and typically worse liquidity — the same
"is this spread paying for real risk or just complexity/illiquidity"
question that applies to corporate credit (`credit_curves.md`).

## Why this isn't implemented in `src/pm`
Tranche waterfall modeling (allocating collateral cash flows and losses
across a capital structure) is genuinely different machinery from the
pool-level pass-through math in `mbs.py` — this page is the conceptual
placeholder, not a working implementation.

## Related
- [Pass-throughs](pass_throughs.md)
- [Credit curves](credit_curves.md)
- [CDS and basis](cds_and_basis.md)
- [CMO/REMIC structuring](cmo_remic_structuring.md)

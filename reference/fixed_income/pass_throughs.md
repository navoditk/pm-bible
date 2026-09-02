# Agency MBS Pass-Throughs

## One-line definition
A pool of mortgages where scheduled principal, interest, and any
prepayments are passed straight through to investors pro rata.

## Mechanics
`mortgage_amortization_schedule` (in `src/pm/fixed_income/mbs.py`) gives
the scheduled (no-prepayment) amortization. `apply_prepayment` overlays a
prepayment assumption (an SMM per period) on top of it to get the actual
principal paydown investors receive.

## Why PMs care
Unlike a bullet bond, a pass-through's cash-flow timing is uncertain —
it depends on borrower behavior (refinancing, moving, default), not just
a fixed schedule. That uncertainty is the whole story of MBS risk.

## Related
prepayment models, WAL, effective duration.

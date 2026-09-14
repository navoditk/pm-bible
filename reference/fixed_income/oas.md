# Option-Adjusted Spread (OAS)

## One-line definition
Z-spread with the value of any embedded option (call, put, prepayment)
stripped out — the spread left over after accounting for optionality.

## Why PMs care
For a callable corporate bond or an agency MBS, part of the observed
Z-spread just compensates for the issuer's/borrower's option, not credit
risk. Comparing bonds on raw Z-spread instead of OAS overstates the
apparent value of the optioned bond.

## Why this isn't implemented in `src/pm`
Computing OAS requires simulating interest-rate paths against a
term-structure model (e.g. a short-rate lattice or Monte Carlo) and
averaging option-adjusted cash flows across paths — that's a materially
different kind of computation from the closed-form/root-finding functions
in this repo, and per `AGENTS.md` rule 5, this repo doesn't add that
complexity before the deterministic pieces (Z-spread, duration, curve
construction) are solid. Treat this page as the conceptual bridge to that
future work, not a working implementation.

## Related
- [Z-spread](z_spread.md)
- [Effective duration](effective_duration.md)

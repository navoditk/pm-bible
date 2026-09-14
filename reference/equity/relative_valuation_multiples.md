# Relative Valuation Multiples

## One-line definition
Pricing a stock relative to a fundamental (earnings, book value) instead
of discounting cash flows directly — faster than a DDM, but only as sound
as the peer group and growth assumptions behind it.

## Formula
Justified (fundamental) P/E from Gordon growth:
`P/E = payout_ratio / (r - g)`

PEG: `PEG = PE / expected_growth_%` (growth expressed in percentage
points, e.g. pass `15` for 15% growth, not `0.15`)

## Why PMs care
Multiples are the fastest way to screen a universe and to sanity-check a
DDM output. Dividing the Gordon-growth DDM formula through by
earnings-per-share turns it directly into the justified-P/E formula
above, so "cheap on P/E" and "high DDM value relative to price" are the
same claim viewed two different ways.

## Common mistakes
- comparing P/E across companies with very different growth or payout
  without adjusting for it — PEG is a partial fix, not a complete one
- treating a low multiple as automatically cheap rather than checking
  whether it's cheap *for a reason* (declining growth, higher risk,
  overleveraged balance sheet)

## Limitations
`justified_pe` and `peg_ratio` in `src/pm/equity/valuation.py` only cover
the P/E family. Multiples that need balance-sheet or enterprise-value
inputs beyond price/dividends/earnings — EV/EBITDA, P/B, P/S — aren't
implemented here.

## Related
Dividend discount model, CAPM and beta.

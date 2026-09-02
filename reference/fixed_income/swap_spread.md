# Swap Spread

## One-line definition
The swap rate minus the Treasury yield at the same tenor.

## Formula
`swap_spread = swap_rate - treasury_yield`

## Why PMs care
It reflects bank credit/liquidity conditions and funding-market technicals,
distinct from pure Treasury duration risk — a portfolio can be swap-spread
long or short independent of its outright rate view.

## Limitations
This is a par-yield-vs-par-yield approximation. A precise swap spread
compares the swap curve to the Treasury curve on a matched, zero-coupon
basis, not par yields.

## Related
swap DV01, curve construction, basis.

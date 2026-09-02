# Cross-Currency Basis

## One-line definition
The gap between the actual market FX forward and the forward implied by
pure covered interest parity — the market's deviation from the textbook
no-arbitrage relationship.

## Formula
Solve for the foreign rate that CIP would need to reproduce the observed
market forward, then subtract the actual foreign rate:

`implied_foreign_rate = ((1 + r_domestic*T) * S / F_market - 1) / T`

`basis = implied_foreign_rate - r_foreign`

## Why PMs care
In theory, CIP should hold exactly (it's a static no-arbitrage relation).
In practice, funding constraints, balance-sheet costs, and demand for
dollar funding make cross-currency basis persistently nonzero — a PM
using cross-currency swaps to fund or hedge foreign assets pays or earns
this basis on top of the rate differential.

## Common mistakes
- assuming CIP holds exactly and pricing a hedge without the basis
- treating basis as free money without accounting for the balance-sheet
  and counterparty costs of the trade that generates it

## Related
FX spot/forward, FX carry, swap spread (the fixed-income analogue).

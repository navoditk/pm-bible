# FX Carry and Hedging

## One-line definition
FX carry is the interest-rate differential earned (or paid) holding a
foreign currency unhedged; hedging removes that differential along with
the currency risk.

## Formula
`carry = r_foreign - r_domestic`

## Why PMs care
Uncovered interest rate parity (UIP) predicts spot should move to offset
this differential exactly — a carry trade is a bet that it won't, on
average, which has historically been a persistent (if crash-prone) risk
premium in FX markets.

## Hedging
Reuse `hedge_ratio()` from `src/pm/fixed_income/duration.py` — it's a
generic DV01/notional-sizing formula, not fixed-income-specific. Hedging
foreign currency exposure back to domestic currency uses a forward
contract sized to the foreign-currency notional; the cost of that hedge
is exactly the forward points implied by `fx_forward_rate` (i.e., you give
up the carry you'd otherwise earn/pay unhedged).

## Common mistakes
- forgetting the sign convention: carry is positive for the PM *earning*
  the higher rate, i.e. long the higher-yielding currency
- assuming carry is riskless income — it's compensation for the risk that
  UIP fails to hold and the currency depreciates by more than the
  differential (or crashes, as in a "carry unwind")

## Related
FX spot/forward, cross-currency basis, hedge ratio.

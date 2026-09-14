# Use Case — Commodity Futures Roll

## PM question
An oil futures index position has the near contract at $82 and the far
contract at $85. Spot oil itself is expected to return +3% over the
holding period. Is this a good position to hold through the roll, and
what does the index's total expected return actually look like once the
roll is accounted for?

## Concepts
contango, backwardation, roll yield, total return decomposition (spot
return + roll yield).

## First exercise
Hand-calculate:
1. the curve state (`pm.commodities.commodity_curve_state`)
2. the roll yield (`pm.commodities.roll_yield`)
3. the approximate total return = spot return + roll yield — does the
   roll help or hurt here, and by how much relative to the spot-only
   view?

## Extend
Compare against a second commodity trading in backwardation with the
same spot-return assumption. See `reference/commodities/roll_yield.md`
for why two commodities with identical spot performance can post very
different total returns depending on curve shape.

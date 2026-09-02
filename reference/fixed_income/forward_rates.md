# Forward Rates

## One-line definition
The interest rate implied between two future dates by today's zero curve.

## Formula
`(1+z2)^t2 = (1+z1)^t1 * (1+f)^(t2-t1)`

`f = ((1+z2)^t2 / (1+z1)^t1)^(1/(t2-t1)) - 1`

## Why PMs care
Forward rates are the market's break-even for future rates — a curve
position only makes money if realized rates differ from what's already
priced into the forwards.

## Common mistake
Treating the forward rate as a prediction rather than a break-even implied
by no-arbitrage.

## Related
curve construction, curve trades, carry and roll.

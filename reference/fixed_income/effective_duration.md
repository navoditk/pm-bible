# Effective Duration

## One-line definition
Duration measured by bumping yield up and down and repricing, rather than
from a closed-form price/yield formula.

## Formula
`EffectiveDuration = (Price_down - Price_up) / (2 * Price_base * bump)`

## Why PMs care
Modified [duration](duration.md) assumes price is
a smooth, closed-form function of yield. That breaks down for
instruments whose cash flows themselves change with rates — an MBS whose
prepayment speed responds to rates is the classic example. Effective
duration works regardless, because it never assumes a formula — it just
reprices.

## Worked example
`Price_base = 100`, `Price_up = 98` (yields +25bp), `Price_down = 102.5`
(yields -25bp):

`EffectiveDuration = (102.5 - 98) / (2 * 100 * 0.0025) = 9.0`

## Common mistakes
- using too large a bump (introduces convexity error) or too small a bump
  (numerical noise dominates)
- holding cash flows fixed when repricing an instrument whose cash flows
  should change with rates (e.g. forgetting to update the prepayment
  assumption when bumping an MBS's yield)

## Related
- [Duration](duration.md)
- [MBS negative convexity](mbs_convexity.md)
- [Prepayment models](prepayment_models.md)

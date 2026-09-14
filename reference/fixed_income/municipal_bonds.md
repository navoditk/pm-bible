# Municipal Bonds

## One-line definition
Debt issued by U.S. state and local governments, typically exempt from
federal (and often state, for in-state residents) income tax — which
means their yields can't be compared to taxable bonds without first
adjusting for that tax benefit.

## Formula
`tax_equivalent_yield = muni_yield / (1 - tax_rate)`

`pm.fixed_income.munis.tax_equivalent_yield` implements this directly.
`tax_rate` is the investor's relevant marginal rate — federal alone, or
federal plus state for an investor buying a muni issued in their own
state (which is typically exempt from both).

## Why PMs care
A muni's lower headline yield versus a comparable taxable bond isn't
automatically a worse deal — for a high-tax-bracket investor, the
after-tax comparison can favor the muni outright. Tax-equivalent yield
is the standard way to put munis and taxable bonds (Treasuries,
corporates) on the same footing before comparing spreads or making an
allocation decision. Munis also have their own credit-analysis
vocabulary — general obligation (GO) bonds are backed by a
municipality's taxing power, revenue bonds by a specific project's cash
flows (a toll road, a utility) — which changes the fundamental-credit
question from "how levered is this company" to "how reliable is this tax
base or revenue stream."

## Worked example
A 3.00% muni yield, investor in a 32% marginal federal tax bracket:

`tax_equivalent_yield = 0.03 / (1 - 0.32) = 4.41%`

A taxable corporate bond would need to yield at least 4.41% to match the
muni's after-tax return — below that, the muni is the better deal for
this investor (`tests/test_munis_and_convertibles.py::test_tax_equivalent_yield_hand_example`).

## Common mistakes
- comparing a muni's headline yield directly against a taxable bond's
  yield without adjusting — this understates the muni's relative
  attractiveness for a taxable investor
- applying one tax rate universally — the "right" `tax_rate` depends on
  the specific investor's bracket and state of residence, not a generic
  number; a tax-exempt investor (a pension fund) gets no benefit from
  munis at all and the calculation is moot for them
- ignoring the Alternative Minimum Tax (AMT) — some muni interest (private
  activity bonds) is taxable under AMT even though it's federally
  tax-exempt under the regular tax system, which this simplified formula
  doesn't account for

## Why the full picture isn't implemented in `src/pm`
GO-vs-revenue credit analysis for a specific municipality requires the
same kind of issuer-specific fundamental work as corporate credit
analysis ([leverage/coverage ratios](fundamental_credit_analysis.md))
but applied to public-sector financials (tax base, pension liabilities,
revenue-bond debt service coverage) this repo doesn't have data or a
tested model for — `tax_equivalent_yield` is the genuinely generic,
codeable piece; municipal credit analysis itself is conceptual only here.

## Related
- [Fundamental credit analysis](fundamental_credit_analysis.md)
- [TIPS and breakeven inflation](tips_and_breakevens.md)
- [Sovereign and EM debt](sovereign_and_em_debt.md)

## Free resources
- [Tax-Equivalent Yield — The Motley Fool](https://www.fool.com/terms/t/tax-equivalent-yield) — the formula and why munis and taxable bonds aren't directly comparable

# Dividend Discount Model (DDM)

## One-line definition
Values a share as the present value of all future dividends it will pay —
the equity analog of pricing a bond as the present value of its cash flows.

## Formula
Gordon growth (constant growth forever): `V = D1 / (r - g)`

Two-stage: discount an explicit growth rate for N years, then a
Gordon-growth terminal value at year N, discounted back to today.

## Why PMs care
Every multiples-based shortcut (P/E, PEG) is a compressed version of this
— `relative_valuation_multiples.md` shows the algebra connecting them.
When a stock's price doesn't match a DDM value at a defensible `(r, g)`,
that gap is either a real growth/risk difference the market is pricing
correctly, or a genuine mispricing — DDM is how you tell which.

## Worked example
See `src/pm/equity/valuation.py` (`gordon_growth_value`,
`two_stage_ddm_value`) and
`notebooks/equity/28_equity_valuation_and_capm.ipynb`.

## Common mistakes
- using this year's dividend (D0) in the Gordon-growth numerator instead
  of next year's (D1) — forgetting to grow it one period first
- picking `g >= r`, which makes the model diverge (infinite value) — a
  real constraint on the assumption, not a numerical accident
- applying constant-growth Gordon growth to a young, high-growth company
  where growth clearly isn't constant forever (use the two-stage version
  instead)

## Limitations
Real companies don't grow at a single rate forever, and the required
return `r` is itself an assumption — usually sourced from CAPM (see
`capm_and_beta.md`), not directly observable.

## Related
- [Relative valuation multiples](relative_valuation_multiples.md)
- [CAPM and beta](capm_and_beta.md)
- [Shareholder yield](shareholder_yield.md)
- [Preferred securities](../fixed_income/preferred_securities.md)

# Shareholder Yield and Total Shareholder Return

## One-line definition
The cash a company actually returns to equity holders (dividends plus
buybacks) as a percentage of its value, and the total return (price
change plus dividends) an investor actually realized.

## Formula
`dividend_yield = dividend_per_share / price`

`buyback_yield = buyback_value / market_cap`

`shareholder_yield = dividend_yield + buyback_yield`

`total_shareholder_return = (price_end - price_start + dividends_paid) / price_start`

`payout_ratio = dividend_per_share / earnings_per_share`

## Why PMs care
Buybacks and dividends are substitutes from the company's perspective
(both return cash) but very different from a shareholder's tax and
signaling perspective — shareholder yield captures both, so a
low-dividend, heavy-buyback company (common in the US) isn't mistaken
for one returning nothing to shareholders. `payout_ratio` is also the
direct input to `justified_pe` in `relative_valuation_multiples.md`.

## Common mistakes
- comparing dividend yield alone across markets or eras with very
  different buyback norms (US vs. Europe, pre- vs. post-2000) without
  also checking buyback yield
- assuming a high payout ratio is automatically bad — it depends
  entirely on whether the company has better reinvestment opportunities
  than its cost of capital

## Limitations
`buyback_yield` here is gross buyback value over market cap — it doesn't
net out dilution from stock-based compensation issuance, which some
"net buyback yield" definitions do.

## Related
- [Dividend discount model](dividend_discount_model.md)
- [Relative valuation multiples](relative_valuation_multiples.md)

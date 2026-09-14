# Convertible Bonds

## One-line definition
A bond that can be converted into a fixed number of the issuer's common
shares at the holder's option — a straight bond plus an embedded call
option on the issuer's stock, priced as a hybrid of the two.

## Formula
`conversion_value = conversion_ratio * stock_price` (also called
"parity" — what the bond is worth if converted right now)

`conversion_premium = (bond_price - conversion_value) / conversion_value`
(how much richer the bond trades than immediate conversion is worth)

`pm.fixed_income.convertibles.conversion_value` and
`conversion_premium` implement both directly.

## Why PMs care
A convertible's price behaves like a straight bond when the stock is far
below the conversion price (the embedded option is deep out-of-the-money
and worthless, so the bond trades on credit and rates like any other
bond) and increasingly like the stock itself as the stock price rises
past the conversion price (the option moves in-the-money and dominates
the bond's value). That means a convertible's *effective duration and
equity delta both change with the stock price* — a genuinely different
risk profile from either a plain bond or plain equity position, and
exactly the kind of instrument a multi-asset or credit-plus-equity PM
uses to get asymmetric exposure: bond-like downside protection with
equity-like upside participation.

## Worked example
A $1,000-par convertible bond, conversion ratio 20 (20 shares per bond),
trading at a price of 950 (95% of par) while the stock trades at $45:

`conversion_value = 20 * 45 = $900`
`conversion_premium = (950 - 900) / 900 ≈ 5.56%`

The bond trades 5.56% above its immediate conversion value — investors
are paying a premium for the option's remaining time value plus the
bond's downside floor
(`tests/test_munis_and_convertibles.py::test_conversion_premium_hand_example`).
If the stock instead traded at $47.50, conversion value would exactly
equal the bond price and the premium would be zero — the breakeven point
where converting immediately and holding the bond are worth the same.

## Common mistakes
- treating conversion premium as pure "overpayment" — some premium is
  expected and rational, since it reflects the value of the embedded
  option's remaining optionality (time value), not necessarily
  mispricing
- ignoring the straight-bond floor — a convertible shouldn't trade below
  what an equivalent non-convertible bond from the same issuer would be
  worth, even if the stock collapses; this repo's `conversion_premium` is
  a simplified version of the CFA-standard definition (which compares
  bond price against `max(conversion_value, straight_bond_value)`, not
  conversion value alone) — see Limitations
- assuming conversion ratio is fixed forever — most convertibles have
  anti-dilution adjustments that change the ratio around stock splits,
  spin-offs, or large dividends

## Why the straight-bond floor isn't implemented in `src/pm`
Pricing the straight-bond floor requires the same discounted-cash-flow
machinery as [bond pricing](bond_pricing.md) applied to the convertible's
coupon/maturity at a market-appropriate credit spread — genuinely doable
with functions this repo already has, but combining it correctly with
the option-value side (which behaves like the [Black-Scholes
framework](../derivatives/black_scholes_and_greeks.md), since a
convertible is economically a bond plus a call option) into one coherent
convertible-bond valuation model is a larger integration project than
this page's two formulas, which only capture the "as-converted" side of
the story.

## Related
- [Bond pricing](bond_pricing.md)
- [Black-Scholes pricing and the Greeks](../derivatives/black_scholes_and_greeks.md)
- [Preferred securities](preferred_securities.md)

## Free resources
- [Conversion Ratio — Wall Street Prep](https://www.wallstreetprep.com/knowledge/conversion-ratio/) — conversion price, ratio, value, and a worked example

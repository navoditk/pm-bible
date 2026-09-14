# Option Strategies: Covered Call, Protective Put, Collar

## One-line definition
The three standard ways a PM combines an existing stock position with
one or two options to reshape its return profile — trade away some
upside for income (covered call), pay for a downside floor (protective
put), or fund the floor with the upside (collar).

## Covered call (buy-write)
Own the stock, sell a call against it. Caps upside at the strike (plus
premium collected); the premium provides a small cushion on the
downside, but full downside risk below that cushion remains. Suits a
neutral-to-moderately-bullish view from an investor willing to have the
stock called away at the strike.

## Protective put (married put)
Own the stock, buy a put against it. Unlimited upside remains; downside
is floored at the strike (minus the put's cost). The put's premium is a
direct drag on returns if the stock doesn't fall — functionally an
insurance premium paid whether or not the "claim" is ever used.

## Collar
Own the stock, buy a put (the floor) and sell a call (the ceiling) at
the same expiry. The call premium collected offsets some or all of the
put premium paid — a "zero-cost collar" is one sized so the two premiums
exactly cancel. Trades away upside beyond the call strike in exchange for
a floor below the put strike, cheaper (or free) compared to a bare
protective put.

## Why PMs care
These aren't three unrelated ideas — they're the same building block
(an existing position plus a Black-Scholes-priced option, or two)
applied with different objectives: income (covered call), pure insurance
(protective put), or cheaper insurance funded by giving up some upside
(collar). A PM overlay desk uses exactly this toolkit to adjust a
portfolio's risk profile without transacting in the underlying itself —
useful when the underlying position is large, illiquid, or has a tax or
mandate reason not to be sold outright.

## Why this isn't implemented in `src/pm`
Each strategy's payoff is a linear combination of a stock position and
one or two Black-Scholes-priced legs — `pm.options.black_scholes_call_price`
and `black_scholes_put_price` already price every leg involved; no new
pricing formula is needed. What a real implementation would add is
payoff-diagram and breakeven-point construction across a price grid,
which is a plotting/composition exercise on top of the existing pricing
functions rather than new financial math — left as a notebook exercise
(construct each strategy's payoff yourself from the two priced legs)
rather than a `src/pm` function, consistent with this repo's rule that a
new function earns its place by encoding a formula, not by composing
existing ones for display purposes.

## Common mistakes
- describing a collar as "free" — a zero-cost collar has zero *premium*
  cost, not zero cost: the giveaway is the capped upside above the call
  strike, which has real value in a strong rally
- assuming a covered call is a pure income strategy with no risk — the
  written call limits upside, but the stock's full downside (beyond the
  small premium cushion) is still there
- forgetting time decay cuts the other way for a protective put than for
  a covered call: theta hurts the protective-put buyer (long the put) and
  helps the covered-call writer (short the call), for the same reasons
  covered in [Black-Scholes and the Greeks](black_scholes_and_greeks.md)

## Related
- [Black-Scholes pricing and the Greeks](black_scholes_and_greeks.md)
- [Put-call parity](put_call_parity.md)
- [Equity factor investing](../equity/equity_factor_investing.md)

## Free resources
- [Covered Call (Buy/Write) — Options Industry Council](https://www.optionseducation.org/strategies/all-strategies/covered-call-buy-write)
- [Protective Put (Married Put) — Options Industry Council](https://www.optionseducation.org/strategies/all-strategies/protective-put-married-put)
- [Collar (Protective Collar) — Options Industry Council](https://www.optionseducation.org/strategies/all-strategies/collar-protective-collar)

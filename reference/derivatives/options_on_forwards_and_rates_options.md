# Options on Forwards, and Rates Options (Swaptions, Caps, Floors)

## One-line definition
Black-76 prices a European option on a forward or futures price instead
of a spot price; it's also the model underneath interest-rate caps,
floors, and swaptions, just applied to a forward rate instead of a
forward price.

## Formula
`d1 = (ln(F/K) + 0.5*sigma^2*T) / (sigma*sqrt(T))`
`d2 = d1 - sigma*sqrt(T)`

`call = exp(-r*T) * (F*N(d1) - K*N(d2))`
`put = exp(-r*T) * (K*N(-d2) - F*N(-d1))`

where `F` is the forward/futures price. `pm.options.black76_call_price`
and `black76_put_price` implement this directly.

## Why this is the same model as Black-Scholes
Black-76 is Black-Scholes with `dividend_yield = rate` and the spot
replaced by the forward — that substitution makes the `S*exp((r-q)*T)`
forward-value term in Black-Scholes collapse to `F` directly.
`tests/test_options.py::test_black76_matches_black_scholes_at_the_matching_forward`
verifies this exactly: pricing Black-76 at `F = S*exp((r-q)*T)`
reproduces the Black-Scholes price to 8 decimal places, for both the call
and the put. This is why the same Greek intuition from [Black-Scholes and
the Greeks](black_scholes_and_greeks.md) carries over.

## From options on forwards to caps, floors, and swaptions
- **Cap** — a portfolio of "caplets," each a call option on a forward
  interest rate for one accrual period; pays off when that period's
  floating rate exceeds the cap's strike rate. **Floor** is the mirror
  image with floorlets (put options on the forward rate).
- **Swaption** — the right to enter an interest rate swap at a fixed rate
  agreed today; a payer swaption (pay fixed, receive floating) is priced
  as a call on the forward swap rate, a receiver swaption as a put,
  scaled by the swap's annuity (present value of $1 per period over the
  swap's life) instead of a simple discount factor.

Each of these applies the same Black-76 d1/d2 formula to a *forward rate*
rather than a forward price — the underlying pricing engine
(`black76_call_price`/`black76_put_price` above) is identical; what
changes is which forward rate goes in, and (for a cap/floor or swaption)
an annuity/accrual-factor layer on top.

## Why the annuity/curve layer isn't implemented in `src/pm`
Pricing a real caplet or swaption needs the discount factor and accrual
fraction for its specific period, and a swaption additionally needs the
full annuity (sum of discount factors across every remaining swap
payment date) — both depend on a bootstrapped curve
([curve construction](../fixed_income/curve_construction.md)) evaluated
at the option's specific dates, not just a single flat rate `r` the way
`black76_call_price` takes it. That composition (curve → forward rate →
annuity → Black-76) is a real project in its own right; this repo ships
the Black-76 engine itself (the genuinely reusable, well-defined part)
and stops there, rather than building a partial curve-integration layer
that would be easy to get subtly wrong.

## Why PMs care
Caps, floors, and swaptions are how a rates desk buys convexity and
optionality directly, rather than getting it implicitly through MBS
negative convexity ([MBS convexity](../fixed_income/mbs_convexity.md)) or
duration positioning alone. A borrower with floating-rate debt buys a cap
to bound their interest cost the same way a mortgage holder's prepayment
option bounds a lender's upside; a swaption is the cleanest way to
express a view on where rates will be *and* how volatile they'll be
between now and a future date, since its value depends on both.

## Common mistakes
- pricing a swaption with a simple discount factor instead of the full
  annuity — the annuity (not a single discount factor) is what converts
  a per-period Black-76 value into the value of an entire swap's worth of
  optionality
- assuming a cap's implied volatility and a swaption's implied volatility
  on the same underlying rate must match — they're quoted against
  different conventions (a strip of forward rates vs. one forward swap
  rate) and can and do diverge
- forgetting Black-76 assumes the forward rate is lognormal — this breaks
  down as rates approach zero or go negative, a real historical issue for
  EUR and JPY rates markets that led practitioners toward shifted-lognormal
  or normal-model variants not covered here

## Related
- [Black-Scholes pricing and the Greeks](black_scholes_and_greeks.md)
- [Curve construction](../fixed_income/curve_construction.md)
- [Swap DV01](../fixed_income/swap_dv01.md)
- [MBS convexity](../fixed_income/mbs_convexity.md)

## Free resources
- [Black model — Wikipedia](https://en.wikipedia.org/wiki/Black_model) — the formula and its four standard applications (futures options, caps/floors, swaptions, pension inflation guarantees)
- [Black Model for Interest Rate Options and Swaptions — AnalystPrep (CFA Level II)](https://analystprep.com/study-notes/cfa-level-2/black-model-valuation-of-interest-rate-options-and-swaptions/) — the annuity-factor distinction for swaptions specifically

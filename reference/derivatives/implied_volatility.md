# Implied Volatility

## One-line definition
The volatility that, plugged into Black-Scholes, reprices the model
exactly to a given market option price — the market's own forward-looking
volatility estimate, backed out rather than forecast.

## Formula
No closed form — solved numerically. `pm.options.implied_volatility_call`
and `implied_volatility_put` use bisection (`scipy.optimize.brentq`) to
find the `sigma` where `black_scholes_call_price(..., sigma, ...) ==
market_price`, bracketed over a wide `[1e-6, 5.0]` volatility range (this
always brackets a root because Black-Scholes price is strictly increasing
in volatility — see the last row of the worked example below).

## Why PMs care
Historical (realized) volatility describes what already happened;
implied volatility (IV) is priced off what the market expects to happen
over the option's remaining life, which is what actually determines an
option's cost today. Comparing IV across strikes at the same expiry (the
"volatility smile/skew") and across expiries (the "term structure")
reveals the market's own view of tail risk and near-term event risk —
information no historical-volatility number carries. The VIX index is
exactly this idea aggregated across the S&P 500 option chain into one
number: a market-implied volatility reading, not a statistical estimate
from past returns.

## Worked example
Take this repo's own Black-Scholes hand example forward: price a call at
`sigma = 20%` (`S=K=100, r=5%, T=1, q=0`) to get `market_price ≈
10.4506`, then solve backward for the implied volatility that reproduces
that price. It recovers `sigma = 0.20` to 8 decimal places
(`tests/test_options.py::test_implied_volatility_call_round_trips`) —
because Black-Scholes price is monotonic in volatility (verified directly
in `test_call_price_increases_with_volatility`), the solver has exactly
one root to find, which is what makes bisection both fast and reliable
here.

## Common mistakes
- treating implied volatility as a forecast of what will actually happen
  — it's the market's *current price* of uncertainty, which itself moves
  with supply/demand for options, not only with a view on realized
  volatility
- assuming one IV number describes an entire option chain — in reality
  IV varies by strike (skew/smile) and expiry (term structure); a single
  "the IV is X%" statement is always an approximation of a richer surface
- solving for implied volatility on an option price that itself violates
  a no-arbitrage bound (e.g. below intrinsic value) — no real volatility
  reproduces it, and a numerical solver may fail to converge or return a
  meaningless answer instead of erroring cleanly

## Limitations
This repo solves implied volatility only against the flat-volatility
Black-Scholes formula, which is exactly why a *smile* exists in real
markets: if a single volatility number correctly priced every strike,
there would be nothing to plot. Building an actual volatility surface
(smile/skew across strikes, term structure across expiries, and a
consistent interpolation/extrapolation scheme between them) is materially
more machinery than one root-find per quote and isn't implemented here.

## Related
- [Black-Scholes pricing and the Greeks](black_scholes_and_greeks.md)
- [Put-call parity](put_call_parity.md)

## Free resources
- [VIX Index — Cboe](https://www.cboe.com/tradable-products/vix/) — how a market-wide implied-volatility measure is actually built and used

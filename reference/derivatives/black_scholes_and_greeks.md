# Black-Scholes Pricing and the Greeks

## One-line definition
Black-Scholes-Merton prices a European option as the risk-neutral
expected discounted payoff under the assumption the underlying follows
geometric Brownian motion with constant volatility; the Greeks are the
option price's sensitivities to each of its inputs.

## Formula
`d1 = (ln(S/K) + (r - q + 0.5*sigma^2)*T) / (sigma*sqrt(T))`
`d2 = d1 - sigma*sqrt(T)`

`call = S*exp(-q*T)*N(d1) - K*exp(-r*T)*N(d2)`
`put = K*exp(-r*T)*N(-d2) - S*exp(-q*T)*N(-d1)`

where `S` = spot, `K` = strike, `r` = risk-free rate, `q` = continuous
dividend yield (0 for a non-dividend stock), `sigma` = volatility,
`T` = time to expiry in years, `N` = the standard normal CDF.

## The Greeks
| Greek | Meaning | Call | Put |
|---|---|---|---|
| Delta | dV/dS | `exp(-qT)*N(d1)`, in [0,1] | `-exp(-qT)*N(-d1)`, in [-1,0] |
| Gamma | d(delta)/dS | `exp(-qT)*N'(d1) / (S*sigma*sqrt(T))` (same for call and put) | — |
| Vega | dV/d(sigma) | `S*exp(-qT)*N'(d1)*sqrt(T)` (same for call and put) | — |
| Theta | -dV/dT (time decay) | see `theta_call`/`theta_put` in `src/pm/options.py` | differs by sign on the `q` and `r` terms |
| Rho | dV/dr | `K*T*exp(-rT)*N(d2)` | `-K*T*exp(-rT)*N(-d2)` |

`pm.options` implements each as its own function (`delta_call`,
`delta_put`, `gamma`, `vega`, `theta_call`, `theta_put`, `rho_call`,
`rho_put`), matching this repo's one-formula-per-function style.

## Why PMs care
A single option's price tells you what it's worth today; the Greeks tell
you how that value moves with the market, which is what a PM actually
manages day to day. Delta-hedging a book means holding enough of the
underlying to offset aggregate delta; gamma is the rate that hedge goes
stale as the underlying moves, forcing rebalancing; vega is direct
exposure to implied volatility itself, independent of direction; theta is
the daily cost (for a long option position) or income (for a short one)
of simply holding the position as time passes.

## Worked example
`S = K = 100`, `r = 5%`, `sigma = 20%`, `T = 1` year, `q = 0` — the
classic textbook ATM case:

`d1 = 0.35`, `d2 = 0.15`
`call ≈ 10.4506`, `put ≈ 5.5735`
`delta_call ≈ 0.6368`, `delta_put ≈ -0.3632`
`gamma ≈ 0.01876`, `vega ≈ 37.52` (per 1.0 = 100 vol points)
`theta_call ≈ -6.41/year ≈ -0.0176/day`
`rho_call ≈ 53.23`, `rho_put ≈ -41.89`

Every Greek above is independently verified in `tests/test_options.py`
against a finite-difference bump of the pricing function itself (e.g.
`gamma` checked against `(C(S+e) - 2*C(S) + C(S-e)) / e^2`), not just
against the closed-form formula — so a sign error in the analytic
derivative would fail even if it matched a memorized textbook number.

## Common mistakes
- forgetting the continuous-dividend-yield term `q` — for a
  dividend-paying stock, omitting it overstates both call delta and call
  price
- reading vega/theta/rho as "per basis point" the way DV01 is — they're
  reported per whole unit of their input (per 1.00 of vol, per year, per
  1.00 of rate) unless explicitly rescaled
- assuming gamma and vega differ between a call and a put at the same
  strike/expiry — they don't; only delta, theta, and rho do

## Limitations
Black-Scholes assumes constant volatility, continuous trading with no
transaction costs, and European exercise (no early exercise) — real
markets violate all three to varying degrees, which is exactly what
[implied volatility](implied_volatility.md) skew/smile reflects: the
market pricing in a distribution Black-Scholes' own assumptions can't
represent.

## Related
- [Put-call parity](put_call_parity.md)
- [Implied volatility](implied_volatility.md)
- [Options on forwards and rates options](options_on_forwards_and_rates_options.md)
- [Option strategies](option_strategies.md)

## Free resources
- [Black–Scholes model — Wikipedia](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) — full derivation, formula reference, and the volatility-smile limitation
- [Greeks (finance) — Wikipedia](https://en.wikipedia.org/wiki/Greeks_(finance)) — the full Greek family with formulas, including the Black model variants

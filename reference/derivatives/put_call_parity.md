# Put-Call Parity

## One-line definition
For European options on the same underlying, strike, and expiry, a call
and a put's prices aren't independent — they're tied together by a
fixed, no-arbitrage relationship.

## Formula
`call - put = S*exp(-q*T) - K*exp(-r*T)`

Equivalently: `call + K*exp(-r*T) = put + S*exp(-q*T)` — a call plus cash
equal to the discounted strike is worth the same as a put plus the stock
itself (both sides pay off `max(S_T, K)` at expiry).

`pm.options.put_call_parity_residual(call_price, put_price, spot, strike,
rate, time_to_expiry, dividend_yield)` returns the left side minus the
right side — 0 when parity holds, nonzero when a quoted call/put pair is
inconsistent.

## Why PMs care
Parity is the fastest sanity check on a quoted options market: if it's
violated by more than the bid-ask spread and transaction costs, there's a
risk-free arbitrage (buy the underpriced side, sell the overpriced side,
lock in the difference) — in practice this also means it's the
relationship that keeps a market's calls and puts from being priced by
two independently wrong models. It's also the reason
[delta_call - delta_put = exp(-qT)](black_scholes_and_greeks.md) exactly:
differentiate both sides of the parity identity with respect to `S`.

## Worked example
Using this repo's own Black-Scholes hand example (`S=K=100, r=5%,
sigma=20%, T=1, q=0`): `call ≈ 10.4506`, `put ≈ 5.5735`.

`call - put ≈ 4.8771`
`S*exp(-q*T) - K*exp(-r*T) = 100 - 100*exp(-0.05) ≈ 4.8771`

They match exactly (`tests/test_options.py::test_put_call_parity_holds_for_consistent_bs_prices`)
— as they must, since both prices come from the same model. The more
useful test is the other direction: feed in two *quoted* prices that
didn't come from the same consistent model
(`test_put_call_parity_residual_nonzero_for_inconsistent_quotes`) and the
residual is nonzero, flagging the inconsistency.

## Common mistakes
- applying parity to American options without adjustment — early
  exercise breaks the exact equality (it becomes an inequality instead);
  parity as stated here is for European options only
- forgetting the dividend/foreign-rate term `q` — for a dividend-paying
  stock or an FX option (where `q` is the foreign interest rate), omitting
  it makes a correctly-priced call/put pair look like it's violating
  parity when it isn't
- treating a *small* parity deviation as free money — real markets have
  bid-ask spreads, financing costs, and (for early-exercise-style
  products) borrow costs that eat into any apparent arbitrage

## Related
- [Black-Scholes pricing and the Greeks](black_scholes_and_greeks.md)
- [Implied volatility](implied_volatility.md)
- [Option strategies](option_strategies.md)

## Free resources
- [Put/Call Parity — Options Industry Council](https://www.optionseducation.org/advancedconcepts/put-call-parity) — the formula plus a real arbitrage-trade example

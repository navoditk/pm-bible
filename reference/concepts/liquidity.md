# Liquidity Risk

## One-line definition
The risk that a position can't be traded near its marked price, especially
under stress — distinct from market risk (the price itself moving).

## Why PMs care
A portfolio can pass every VaR/duration/tracking-error check and still
blow up if it can't actually exit positions during a redemption or margin
call without moving the market against itself.

## Why this isn't implemented in `src/pm`
Realistic liquidity/market-impact modeling (cost as a nonlinear function
of trade size relative to average daily volume, bid-ask spread regime
shifts under stress) needs market microstructure data this repo doesn't
have — `transaction_cost`'s flat-bps model is a stand-in, not a liquidity
model. This page is the conceptual placeholder.

## Common mistakes
- treating a position's liquidity as constant across calm and stressed
  markets — spreads widen and depth disappears exactly when you need to
  trade
- sizing positions purely on volatility/duration limits without a
  liquidity overlay

## Related
transaction costs and rebalancing, stress testing.

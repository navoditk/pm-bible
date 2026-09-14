# Swap DV01

## One-line definition
Dollar change in an interest rate swap's value for a one-basis-point move
in the fixed rate.

## Approximation
`swap_dv01` in `src/pm/fixed_income/swaps.py` treats the swap's fixed leg as
a par bond (coupon = swap rate, priced at par) and reuses `dv01()`.

## Why PMs care
Swaps let a PM add or remove duration without trading the cash bond market
— sizing that trade requires the swap's DV01, same units as a bond's.

## Limitations
This is a fixed-leg proxy. It ignores floating-leg resets and Libor/OIS
discounting basis, and is least accurate for deeply off-market swaps.

## Related
- [Swap spread](swap_spread.md)
- [DV01](dv01.md)

# Use Case — Equity Factor Tilt Review

Given portfolio weights, benchmark weights, and a value-factor score per
holding:
1. calculate active share
2. calculate the portfolio's and benchmark's value-factor exposure
   (`pm.factors.portfolio_factor_exposure`)
3. calculate the active style tilt (`pm.equity.factors.style_tilt`)
4. calculate shareholder yield for the largest overweight name
5. decide whether the fund's active share is explained mostly by this
   single style tilt, or by stock-specific bets uncorrelated with it

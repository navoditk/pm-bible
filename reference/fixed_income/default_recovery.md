# Default, Recovery, and Hazard Rate

## One-line definition
Modeling credit loss as a probability of default times the loss given
default, using a constant hazard rate as the simplifying assumption.

## Formulas
Survival to time `t`: `S(t) = exp(-hazard_rate * t)`

Expected loss: `EL = Notional * PD * (1 - RecoveryRate)`

Implied par spread: `spread ≈ hazard_rate * (1 - RecoveryRate)`

## Why PMs care
This is the building block behind both CDS pricing and risky-bond
valuation — a credit spread is compensation for exactly this expected
loss (plus a risk premium above the pure actuarial expectation).

## Common mistakes
- treating recovery rate as constant across the cycle — recoveries fall
  in systemic downturns, exactly when defaults rise
- confusing a constant hazard rate (memoryless) with a real issuer's
  actual default-timing profile, which usually isn't constant

## Limitations
Constant hazard rate is a simplification. Real credit curves imply a
term structure of hazard rates, and real spreads include a risk premium
above the pure expected-loss compensation shown here.

## Related
CDS and basis, Z-spread, credit curves.

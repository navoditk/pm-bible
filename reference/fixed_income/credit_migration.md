# Credit Migration Risk

## One-line definition
The risk that an issuer's credit rating changes (upgrade or downgrade)
before it defaults or matures, repricing the bond's spread even without a
default event.

## Why PMs care
Most credit losses over a normal holding period come from spread widening
after a downgrade, not from actual default — migration risk is the more
common, less extreme version of the same underlying credit risk.

## Why this isn't implemented in `src/pm`
A real migration-risk model needs a rating transition matrix (a Markov
chain of annual upgrade/downgrade/default probabilities by starting
rating) and a way to reprice the bond in each resulting state — materially
more machinery than the constant-hazard-rate default/recovery model this
repo builds. This page is the conceptual placeholder; `default_recovery.md`
is the buildable piece.

## Related
- [Default and recovery](default_recovery.md)
- [Credit curves](credit_curves.md)
- [Stress testing (portfolio credit scenarios)](../concepts/stress_testing.md)

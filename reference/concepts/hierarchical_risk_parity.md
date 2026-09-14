# Hierarchical Risk Parity (HRP)

## One-line definition
A portfolio construction method (López de Prado) that clusters assets by
correlation structure, then allocates risk recursively down the resulting
hierarchy — avoiding the covariance-matrix inversion that makes
mean-variance optimization unstable.

## Why PMs care
Mean-variance and even standard risk parity still require inverting (or
optimizing over) the full covariance matrix, which is exactly what's
noisiest in a large universe. HRP never inverts the covariance matrix at
all — it only uses it to build a distance/clustering structure, which is
much more robust to estimation noise.

## Why this isn't implemented in `src/pm`
The full method has real algorithmic subtlety: a correlation-based
distance metric, hierarchical clustering (`scipy.cluster.hierarchy`),
quasi-diagonalizing the covariance matrix by cluster order, and a
recursive bisection that splits risk down the resulting tree. That's
meaningfully more intricate than this repo's other "small transparent
function" building blocks, and getting the recursive-split step subtly
wrong would be easy to miss without extensive testing — the same risk
that showed up (and was caught) while building MBS negative convexity in
Phase 8. Better to leave this conceptual than ship an unverified
implementation.

## Related
- [Risk parity](risk_parity.md)
- [Covariance shrinkage](covariance_shrinkage.md)

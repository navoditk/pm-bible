# Tutor session — 2026-09-02

**Persona:** `tutors/fixed_income_tutor.md`
**Topic:** duration, DV01, key-rate duration, convexity (routing table: "duration, DV01, convexity, key-rate duration")

## Questions asked
1. What happens to bond price when yield rises, and why? (diagnostic)
2. Apply `dP/P ≈ -D_mod*dy`: duration 7, +50bp shock → % price change?
3. Apply `DV01 ≈ D_mod*P*0.0001`: duration 7, price 98 → DV01?
4. How can two portfolios share the same aggregate duration but react differently to a curve move?
5. Concrete KRD scenario: bullet (all 10Y) vs. barbell (2Y/30Y), symmetric steepener — work through `dP/P ≈ -sum(KRD_k*dy_k)`.
6. Why does convexity's `dy²` term matter more for large shocks than small ones?

## Concepts confirmed solid
- Price/yield inverse relationship and the discounting mechanism behind it.
- Modified duration and DV01 formula application, including basis-point unit conversion (0.0001, not 0.001) after a self-corrected slip.
- Key-rate duration: correctly derived that a bullet and a symmetric barbell can both net to zero P&L under a linear KRD model for a symmetric twist — talked out of an initial unjustified "barbell wins" claim by applying the weighted formula instead of reasoning from direction alone.
- Convexity as the second-order (`dy²`) term, and why duration-only approximation degrades for large shocks.

## Concepts flagged weak
None — every early slip (skipping the "why," a 10x basis-point error, an unjustified "which portfolio wins" claim) was corrected in the same turn once challenged. No misconception persisted.

## Gap surfaced (repo, not learner)
No `convexity()` function exists in `src/pm/fixed_income/duration.py` despite the formula being taught in `notebooks/fixed_income/09_duration_curve_risk.ipynb` and referenced in `duration.md`. Flagged to the user, who asked to close it and audit the repo for similar gaps — that work follows this session, outside `/tutor`.

## Suggested next action
Revisit curve trades (`reference/fixed_income/curve_trades.md`) with convexity in hand, once the gap above is closed — the barbell-vs-bullet resolution in this session sets that up directly.

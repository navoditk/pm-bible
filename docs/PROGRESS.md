# Progress

## Current stage
The PM/FICC foundation is in place, extended one phase beyond FICC into equity portfolio management (Phase 13), and Phase 3 (active management) is now fully built out - it previously had only active weights and tracking error despite a reference page describing information ratio, IC, breadth, and the Fundamental Law as if they existed. A correctness-fix pass also closed several bugs a detailed audit surfaced (Black-Litterman round-trip, NaN propagation, silent optimizer failures, MBS domain errors), each with a regression test. That same audit's remaining findings are now closed too: the optimizer can trace an efficient frontier and find the tangency/min-TE portfolios (previously promised by a notebook title and never implemented), and ex-post risk analytics (realized volatility/tracking error, downside deviation, MCTE/CCTE, group risk decomposition) fill the gap where everything used to be ex-ante only.

## Current health
- Test status: passing
- Last validated: `pytest -q`
- Result: `144 passed`

## Completed modules
- Foundations bootcamp structure in place
- Core PM analytics library implemented under `src/pm/`
- Fixed-income, optimization, integration, FX/commodities, equity, and active-management notebooks present
- Reference pages added across portfolio foundations, optimization, risk, FICC, equity, and active management (information ratio, information coefficient, Fundamental Law, efficient frontier, downside risk, MCTE/group risk) - each with real external sources
- `docs/OVERVIEW.md` added as a quick-read repo summary
- `/master` rebuilt as a single self-contained trainer (lesson/quiz/scenario/exam/status modes) with `docs/mastery-guide.md` as its walkthrough
- Correctness-fix pass on `src/pm` (Black-Litterman round-trip, NaN propagation, silent solver failures, MBS domain errors)
- Efficient frontier / tangency portfolio / min-tracking-error optimizers added; notebook 04 now actually plots a frontier (previously titled but empty)
- Ex-post risk analytics added (realized volatility/tracking error, downside deviation, MCTE/CCTE, group risk decomposition); notebook 19 now plots the VaR/ES tail and checks a risk model's assumption against realized data

## In progress
- Documentation consolidation and onboarding cleanup
- Keeping the root README and docs hub aligned with the actual repo state
- Maintaining a clean learning-first workflow around each new concept

## Next recommended action
Open:
- `curriculum/bootcamp_01_foundations/README.md`
- `notebooks/foundations/01_returns_and_compounding.ipynb`

## Completion rule
Only mark a module complete when:
- the manual exercise has been attempted,
- the relevant tests pass,
- the reference page has been reviewed or updated,
- the concept can be explained in plain PM language.

## Branch / PR tracking

Current branch:
`feat/frontier-tangency-expost-risk`

Current issue:
_Use issue/branch naming for each learning unit_

Current PR:
_None open — #1 (Phase 13 equity, repo overview, /master skill), #2 (correctness-fix pass), and #3 (Phase 3 active management) merged to `main`_

Last pushed checkpoint:
_Not pushed yet — local commits only_

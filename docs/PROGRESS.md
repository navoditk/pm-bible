# Progress

## Current stage
The PM/FICC foundation is in place, extended one phase beyond FICC into equity portfolio management (Phase 13), and Phase 3 (active management) is now fully built out - it previously had only active weights and tracking error despite a reference page describing information ratio, IC, breadth, and the Fundamental Law as if they existed. A correctness-fix pass also closed several bugs a detailed audit surfaced (Black-Litterman round-trip, NaN propagation, silent optimizer failures, MBS domain errors), each with a regression test. That same audit's remaining findings are now closed too: the optimizer can trace an efficient frontier and find the tangency/min-TE portfolios (previously promised by a notebook title and never implemented), ex-post risk analytics (realized volatility/tracking error, downside deviation, MCTE/CCTE, group risk decomposition) fill the gap where everything used to be ex-ante only, and a pedagogy review's findings (thin early notebooks, zero plots, zero self-checks, a Day-0-shaped hole for true beginners, a stub capstone) are addressed: notebooks 02/03/05/07/11/12 rebuilt with self-checks and plots, a new Day 0 orientation notebook, `reference/glossary.md`, and a real capstone notebook using the three data CSVs no other notebook touched.

## Current health
- Test status: passing
- Last validated: `pytest -q`
- Result: `165 passed`
- Notebooks: 34, all valid JSON (`python scripts/check_repo.py`)

## In-progress: rates/credit/mortgages PM-practitioner layer
A user-requested audit found the fixed-income coverage strong on pricing
and risk mechanics but missing the practitioner/market-structure layer:
carry-and-rolldown was a broken ROADMAP Phase 5 promise, and TBA/dollar
roll, repo specialness, TIPS breakevens, credit indices, and fundamental
credit analysis had zero coverage. Rates is done (carry/rolldown, repo
and financing, TIPS/breakevens). Credit is done (fundamental credit
analysis/leverage-coverage ratios, credit indices/CDX-iTraxx, leveraged
loans). Mortgages is done (TBA/dollar roll implied financing rate,
specified pools, CMO/REMIC structuring) - all three areas now have code
(where genuinely codeable), reference pages, notebooks, and verified
external sources, all wired in. Also caught and fixed mid-mortgages-work:
the Credit PR had shipped its three new reference pages without adding
matching rows to `docs/mastery.md` or the `/tutor` routing table - fixed
here, and `/master`'s confirmed-count level table (stale at "all 55"
since before the Rates PR) updated to the true total of 70 concepts.
Next: a "zero to hero" rates/credit/mortgages roadmap document tying it
all together with external resources at each step - the user's original
ask that started this whole workstream.

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
- Zero-to-proficiency pedagogy pass: notebooks 02/03/05/07/11/12 rebuilt (self-check asserts, plots, PREDICT before code); `notebooks/foundations/00_orientation.ipynb` added for true beginners (environment check, learning-cycle explainer, `w'Sigma*w` by hand); `reference/glossary.md` added (49 terms, every link verified); `notebooks/integration/30_capstone_portfolio_review.ipynb` added, the repo's first real capstone, using `data/mock_portfolio.csv`, `mock_benchmark.csv`, and `mock_bonds.csv` for the first time
- Rates PM-practitioner layer: `carry_and_rolldown.md`/`repo_and_financing.md`/`tips_and_breakevens.md` (each tested `src/pm` code + real external sources), notebook 31, closing the broken "carry and roll" ROADMAP Phase 5 promise
- Credit PM-practitioner layer: `fundamental_credit_analysis.md`/`credit_indices.md`/`leveraged_loans.md` (leverage/coverage ratios and CDX/iTraxx intrinsic-value/basis are tested `src/pm` code; leveraged loans and covenant/rating-agency mechanics are conceptual-only, same honesty pattern as OAS), notebook 32
- Mortgages PM-practitioner layer: `tba_and_dollar_roll.md` (tested `src/pm` code - `dollar_roll_implied_financing_rate`, verified against a real published worked example), `specified_pools.md` and `cmo_remic_structuring.md` (conceptual-only, same honesty pattern as OAS/leveraged loans), notebook 33 - closes the rates/credit/mortgages PM-practitioner-layer audit entirely

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
`feat/mortgages-pm-practitioner-layer`

Current issue:
_Use issue/branch naming for each learning unit_

Current PR:
_None open — #1 (Phase 13 equity), #2 (correctness-fix pass), #3 (Phase 3 active management), #4 (efficient frontier/ex-post risk), #5 (zero-to-proficiency pedagogy), #6 (rates PM-practitioner layer), and #7 (credit PM-practitioner layer) merged to `main`_

Last pushed checkpoint:
_Not pushed yet — local commits only_

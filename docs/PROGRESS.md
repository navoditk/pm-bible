# Progress

## Current stage
The PM/FICC foundation is in place and the repository now extends one phase beyond FICC into equity portfolio management (Phase 13). It includes structured curriculum, a reusable analytics library, notebooks, reference pages, tests, a documentation hub, and a repo-level overview doc.

## Current health
- Test status: passing
- Last validated: `pytest -q`
- Result: `94 passed`

## Completed modules
- Foundations bootcamp structure in place
- Core PM analytics library implemented under `src/pm/`
- Fixed-income, optimization, integration, FX/commodities, and equity notebooks present
- Reference pages added across portfolio foundations, optimization, risk, FICC, and equity
- `docs/OVERVIEW.md` added as a quick-read repo summary
- `/master` rebuilt as a single self-contained trainer (lesson/quiz/scenario/exam/status modes) with `docs/mastery-guide.md` as its walkthrough

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
`main`

Current issue:
_Use issue/branch naming for each learning unit_

Current PR:
_None open — #1 (Phase 13 equity, repo overview, /master skill) merged to `main`_

Last pushed checkpoint:
`7ffa5ac` — stop bare `/tutor` from half-replicating `/master`'s job

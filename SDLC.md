# SDLC for the Portfolio Management Bible

This repo follows a lightweight but disciplined SDLC.

## Lifecycle

```text
Issue / learning objective
        ↓
Short-lived branch
        ↓
Read + derive manually
        ↓
Notebook implementation
        ↓
Checkpoint commit + push
        ↓
Reusable src implementation
        ↓
Tests
        ↓
Reference/documentation
        ↓
Agent review / human review
        ↓
Pull request
        ↓
CI / quality gates
        ↓
Squash merge to main
        ↓
Update roadmap/progress
```

## Work item types

### Learning unit
Examples:
- covariance
- duration
- spread duration

Creates or updates:
- notebook
- reference page
- `src/` implementation if computational
- tests
- progress

### Feature
Examples:
- scenario engine
- optimizer constraints
- Treasury curve loader

### Use case
Examples:
- duration hedge
- curve steepener
- credit spread shock

### Reference enhancement
Example:
- add OAS vs Z-spread comparison

## Definition of Ready

Before implementing:
- topic/use case is named,
- required reference material is identified,
- expected output is understood,
- relevant reference page/template exists or will be created.

## Definition of Done

A computational concept is done when:
- learning objective completed manually,
- formula and units documented,
- notebook has a worked example,
- reusable code exists if needed,
- deterministic tests pass,
- limitations/approximations stated,
- reference page links sources,
- progress updated,
- PR reviewed and merged.

## Checkpoint policy

Commit logical states, not every keystroke.

Typical notebook unit:
1. `learn:` manual lab complete
2. `feat:` reusable implementation + tests
3. `docs:` reference/progress complete

Push after each checkpoint.

## Main branch policy

`main` should remain:
- runnable,
- test-passing,
- documented,
- suitable as the quick-reference version of the repository.

Do experimental learning on branches.

## Releases

Suggested milestones:

```text
v0.1-foundations
v0.2-fixed-income-foundations
v0.3-rates
v0.4-credit
v0.5-ficc-risk
v0.6-attribution
v0.7-use-cases
v0.8-tutors
v1.0-pm-bible
```

Create annotated releases after meaningful roadmap phases, not after each notebook.

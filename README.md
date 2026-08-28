# Portfolio Management Bible — Starter Repository

A living, build-first reference and learning system for portfolio management, portfolio construction, optimization, risk, and FICC.

This repository is intended to serve three modes simultaneously:

1. **LEARN** — follow structured learning paths and interactive notebooks.
2. **LOOK UP** — use concise reference pages, formulas, vocabulary, and code recipes.
3. **APPLY** — work through realistic portfolio-management use cases.

The long-term goal is not a one-time course. It is a continuously evolving portfolio-management knowledge and analytics platform.


## GitHub-first development model

This repository is meant to be version-controlled from the first session.

Before opening the first notebook, follow `SETUP.md` to:
1. create the remote GitHub repository,
2. clone it locally,
3. commit the starter baseline,
4. bootstrap Python,
5. create the first short-lived learning branch.

Then use the branch → checkpoint commit → push → PR → review → merge lifecycle in `SDLC.md`.

GitHub's `main` branch should remain a stable, test-passing quick-reference version of the PM/FICC knowledge base.

## Start here

1. Read `GETTING_STARTED.md`.
2. Run `scripts/bootstrap.sh` or follow `SETUP.md`.
3. Read `ROADMAP.md`.
4. Choose a path in `LEARNING_PATHS.md`.
5. For the initial sprint, start at `curriculum/bootcamp_01_foundations/README.md`.
6. Open the matching notebook.
7. At each `MANUAL FIRST` checkpoint, type the implementation yourself.
8. Use the corresponding code recipe only after your own attempt.
9. Run tests.
10. Write a short explanation in your own words.

## Three navigation modes

### I want to learn
`LEARNING_PATHS.md` → curriculum → notebook → exercise → code → test → oral quiz

### I need a quick reference
`reference/index.md` → concept/instrument/formula → example → code recipe → links

### I have a PM problem
`use_cases/index.md` → realistic problem → analytics → interpretation → extensions

## Main directories

- `curriculum/` — structured courses and bootcamps
- `reference/` — durable PM/FICC encyclopedia
- `notebooks/` — interactive learning labs
- `src/pm/` — reusable analytics library
- `tests/` — correctness checks
- `use_cases/` — realistic PM workflows
- `tutors/` — tutor-agent specifications and prompts
- `resources/` — curated free learning references
- `agents/` — Codex / Claude Code / Copilot operating instructions
- `templates/` — templates for adding new concepts, notebooks, and use cases

## Core learning rule

**Read → Predict → Derive → Type code yourself → Experiment → Compare to reference → Promote to library → Test → Explain**

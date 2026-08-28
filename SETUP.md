# Setup — Remote-First GitHub Workflow

This repository is designed to use Git/GitHub from the very beginning.

The recommended model is:

**Create remote GitHub repo → clone locally → copy starter contents into clone → commit baseline → work on short-lived branches → commit/push at learning checkpoints → open PR → review → merge to `main`.**

This keeps `main` stable while still allowing frequent learning commits.

## Prerequisites

Install:
- Git
- GitHub CLI (`gh`)
- Python 3.12+
- VS Code and/or JupyterLab
- Codex recommended; Claude Code optional; GitHub Copilot optional

Check:

```bash
git --version
gh --version
python3 --version
```

Authenticate GitHub CLI:

```bash
gh auth login
gh auth status
```

## Step 1 — Create the remote GitHub repository

Choose a repository name, for example:

```text
portfolio-management-bible
```

From the terminal:

```bash
gh repo create portfolio-management-bible --private
```

Use `--public` instead if you want it public immediately.

Do **not** add generated starter files on GitHub first. Keep the remote clean so the local starter can become the first meaningful commit.

## Step 2 — Clone the remote locally

Choose the parent directory where you keep GitHub projects:

```bash
cd ~/GitHub
gh repo clone <YOUR_GITHUB_USERNAME>/portfolio-management-bible
cd portfolio-management-bible
```

Confirm:

```bash
git remote -v
git status
git branch --show-current
```

You should be on `main`, with `origin` pointing to GitHub.

## Step 3 — Copy this starter repository into the clone

Unzip the starter somewhere temporary, then copy **the contents** into the cloned repository.

Example:

```bash
unzip ~/Downloads/portfolio-management-bible-github-starter.zip -d /tmp/pmb-starter
cp -R /tmp/pmb-starter/portfolio-management-bible-starter/. .
```

Do not copy a nested `.git` directory. This starter ZIP intentionally contains project files, not Git history.

Check:

```bash
git status
```

You should see the starter files as untracked.

## Step 4 — Create the baseline commit

Before doing any learning work:

```bash
git add .
git commit -m "chore: initialize PM/FICC learning repository"
git push -u origin main
```

This establishes a clean baseline.

## Step 5 — Bootstrap Python

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e ".[dev]"

pytest
python scripts/check_repo.py
```

Start Jupyter:

```bash
jupyter lab
```

## Step 6 — Never do substantial learning work directly on `main`

For the first module:

```bash
git switch -c learn/01-returns-compounding
```

Work through:

```text
notebooks/foundations/01_returns_and_compounding.ipynb
```

Your branch should contain only work related to that learning unit and any directly supporting tests/docs.

## Step 7 — Commit at meaningful checkpoints

Recommended checkpoints for a notebook:

### Checkpoint A — manual understanding
After:
- reading resources,
- completing prediction questions,
- doing the hand calculation,
- implementing the first version manually.

```bash
git add notebooks/foundations/01_returns_and_compounding.ipynb
git commit -m "learn: complete returns and compounding exercises"
git push -u origin learn/01-returns-compounding
```

### Checkpoint B — reusable implementation
After:
- reviewing with Codex if desired,
- extracting the function into `src/`,
- adding tests.

```bash
git add src tests
git commit -m "feat: add reusable return calculations"
git push
```

### Checkpoint C — documentation and completion
After:
- updating the concept/reference page,
- updating `docs/PROGRESS.md`,
- ensuring tests pass.

```bash
pytest
git add reference docs README.md
git commit -m "docs: complete returns learning module"
git push
```

## Step 8 — Open a pull request

```bash
gh pr create   --base main   --head learn/01-returns-compounding   --title "Learn: returns and compounding"   --body-file .github/PULL_REQUEST_TEMPLATE.md
```

Review the diff:

```bash
gh pr diff
gh pr view --web
```

Use Codex or Claude Code as a reviewer if useful, but review the financial logic yourself.

## Step 9 — Merge only after quality gates pass

Required:
- manual checkpoint completed,
- tests pass,
- concept/reference page exists,
- notebook still teaches rather than merely imports a solution,
- `docs/PROGRESS.md` updated.

Then:

```bash
gh pr merge --squash --delete-branch
```

Return to local `main`:

```bash
git switch main
git pull --ff-only
```

## Step 10 — Start the next unit from fresh `main`

```bash
git switch -c learn/02-covariance-diversification
```

Repeat the same lifecycle.

## Branch naming conventions

Use:

```text
learn/<module>
feat/<capability>
fix/<bug>
docs/<topic>
refactor/<area>
chore/<maintenance>
```

Examples:

```text
learn/09-duration-curve-risk
feat/key-rate-duration
docs/fixed-income-glossary
fix/dv01-frequency-handling
```

## Commit-message conventions

Recommended lightweight Conventional Commit style:

```text
learn: complete duration hand calculations
feat: add key-rate duration approximation
test: cover spread-duration sign convention
docs: add curve-steepener reference page
fix: correct annualization units
refactor: separate rates and credit risk helpers
chore: update development dependencies
```

## Sync discipline

At the start of every session:

```bash
git switch main
git pull --ff-only
git switch <your-working-branch>
git rebase main
```

Before pushing:

```bash
git status
git diff
pytest
git push
```

Avoid `git push --force` unless you understand why it is needed. If you must update a rebased personal branch, prefer:

```bash
git push --force-with-lease
```

## Recommended GitHub settings

Once the repo exists, configure:

- `main` as default branch
- require pull requests before merging
- require status checks when CI is added
- squash merge preferred
- automatically delete head branches after merge
- Issues enabled
- Actions enabled

For a personal learning repository these can start lightweight, then become stricter as collaborators are added.

## Daily end-of-session checklist

```bash
pytest
python scripts/check_repo.py
git status
git log --oneline -5
git push
```

Update:

```text
docs/PROGRESS.md
```

with:
- what you learned,
- what you implemented manually,
- what an agent changed,
- tests run,
- next branch/module.

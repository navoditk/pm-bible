# Agent Instructions for This Repository

This is a learning-first financial analytics repository.

## Hard rules

1. Never fill `MANUAL FIRST`, `PREDICT`, `HAND CALCULATION`, or `ORAL CHECK` sections unless the user explicitly says they completed or want the answer.
2. Financial logic must have:
   - a documented definition,
   - clear units,
   - a worked deterministic example,
   - tests.
3. Preserve notebooks as teaching artifacts.
4. Reusable code belongs in `src/pm/`.
5. Do not add market-data/API complexity before the deterministic calculation works.
6. Prefer small transparent functions over opaque frameworks.
7. State approximation limitations for risk sensitivities.

## Git / SDLC rules

8. Before making repo-wide edits, inspect `git status` and the current branch.
9. Do not make learning-feature changes directly on `main`.
10. Keep changes scoped to the current issue/module.
11. Run relevant tests before proposing a commit.
12. Update `docs/PROGRESS.md` at module completion.
13. Never commit secrets, credentials, tokens, generated virtual environments, or local `.env` files.
14. After pushing or merging to `main` a change that touches `reference/`,
    `curriculum/`, or `use_cases/` (the content the Claude Artifact
    preview embeds), refresh and republish it: run
    `scripts/build_artifact_preview.py`, then republish to the *same*
    URL already linked from `README.md` — never a new one. This needs
    the Claude Code Artifact tool. If you're working via Codex or
    Copilot CLI, you don't have that tool — say so explicitly and tell
    the developer to ask Claude Code to publish the refresh, rather than
    silently skipping it. See `agents/CLAUDE_CODE_WORKFLOW.md`,
    `agents/CODEX_WORKFLOW.md`, `agents/COPILOT_WORKFLOW.md`.

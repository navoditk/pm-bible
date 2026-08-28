# Coding-Agent Operating Model

## Recommended split

| Task | Primary |
|---|---|
| learn / derive / prediction questions | human |
| first formula implementation | human |
| repo-wide refactor, integration, tests | Codex |
| deliberate second review | Claude Code |
| small inline edits | GitHub Copilot |
| GitHub-native PR / CLI workflow | Copilot CLI or Codex |

Do not use three agents simultaneously on the same edit.

The financial source of truth is:
reference page + formula + unit tests.

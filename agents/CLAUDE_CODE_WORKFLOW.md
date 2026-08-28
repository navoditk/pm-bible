# Claude Code Workflow

Use Claude Code as a deliberate independent reviewer rather than a second continuous implementation agent.

Good moments:
- after completing an optimization module,
- after designing a risk-model abstraction,
- before major architecture changes,
- when a calculation and test both pass but intuition is uncertain.

Suggested prompt:

> Independently review this module as a portfolio analytics reviewer. Do not assume the existing implementation is correct merely because tests pass. Check the financial definition, mathematical formulation, units, numerical stability, edge cases, and whether the API could cause conceptual misuse. Rank findings by severity. Do not edit until I approve.

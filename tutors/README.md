# Tutor Agents

Tutor agents are an optional learning layer over the repository, not a replacement for the repository.

Run one interactively with `/tutor <topic-or-persona>` (see `.claude/skills/tutor/SKILL.md`
for routing and behavior). Session outcomes are logged to `docs/tutor_sessions/`
and tracked in `docs/mastery.md`.

For a direct analytics answer instead of a teaching session, use
`/pm-query <question>` (`.claude/skills/pm-query/SKILL.md`) — it calls the
actual `src/pm` function and cites it, rather than teaching toward the
answer. See `reference/concepts/agentic_pm_analytics.md` for how the two
skills relate.

All tutors should ground themselves in:
- relevant reference pages,
- current notebook,
- tests/examples,
- curated resources.

Initial tutor roles:
- Concept Tutor
- Fixed-Income Tutor
- Portfolio Construction Tutor
- Assessment Tutor

The tutors should adapt depth from diagnostic questions.

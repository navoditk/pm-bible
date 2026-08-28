# Repository Architecture

## Knowledge layer
`reference/`, `resources/`

## Learning layer
`curriculum/`, `notebooks/`, `tutors/`

## Analytics layer
`src/pm/`, `tests/`

## Application layer
`use_cases/`

## Agent layer
`agents/`

The repository should never depend on an LLM for deterministic financial arithmetic. Agents may orchestrate, explain, review, and teach; calculations live in tested code.

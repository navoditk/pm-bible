---
name: master
description: Drives an end-to-end guided pass through the entire pm-bible curriculum — sequences every concept in curriculum order, launches a /tutor session on whatever is next untested or weak, tracks aggregate progress against docs/mastery.md, and reports how much is left. Use for "/master" to start or resume a full curriculum pass, rather than studying one topic at a time.
---

# Curriculum Mastery Driver

`/tutor` teaches one concept per session, reactively — you name a topic,
or it offers whatever's `weak`. `/pm-query` answers one direct question.
Neither one drives you through the *entire* curriculum end to end. This
skill is that driver: it doesn't teach the material itself (that's
`/tutor`'s job, unchanged), it sequences it, tracks aggregate completion,
and tells you what's next and how far you have left — the same role a
mastery-tracking skill plays for working through a large tool or CLI
surface one feature at a time until nothing is left untested.

## Step 1 — build the curriculum order

The canonical sequence is the bootcamp day order in
`curriculum/bootcamp_01_foundations/README.md` (Days 1–5 core, then
Extension Days 6–14), which is itself built from `ROADMAP.md` Phases
1–13 in order. Read both to construct one ordered list of concepts —
the same concepts as the rows in `docs/mastery.md`, but in curriculum
order rather than the table's listing order.

## Step 2 — read current state

Read `docs/mastery.md` in full. For every concept in the ordered list
from Step 1, note its Status column: `confirmed`, `weak`, or `untested`.

## Step 3 — report position

Before doing anything else, tell the learner, concisely:
- how many of the total concepts are `confirmed` (a count and a
  fraction, e.g. "14 / 45 confirmed")
- the single next concept to work on, chosen as: the first `weak`
  concept in curriculum order if any exist, otherwise the first
  `untested` concept in curriculum order
- which bootcamp day / roadmap phase that concept falls under, so the
  learner has context for where they are

If every concept is `confirmed`, skip straight to the Completion section
below instead of Step 4.

## Step 4 — hand off to `/tutor`

Do not teach the concept yourself and do not re-implement `/tutor`'s
routing logic by hand. Invoke `/tutor` with the concept identified in
Step 3 as its topic argument, exactly as if the learner had typed it
themselves, and let `.claude/skills/tutor/SKILL.md` run its normal
persona selection, session, and end-of-session logging
(`docs/tutor_sessions/...`, `docs/mastery.md` update).

## Step 5 — loop or stop

Once the `/tutor` session ends and `docs/mastery.md` is updated, re-read
it, recompute position (Step 2–3), and ask the learner directly: continue
to the next concept now, or stop here and resume later with `/master`.
Never chain multiple `/tutor` sessions into one turn without checking in
— a mastery pass is real study time across multiple sessions, not a
batch job to run to completion unattended.

## Completion

When every concept in curriculum order shows `confirmed` in
`docs/mastery.md`, say so explicitly, report the final count, and point
to `use_cases/index.md` as the next step — applying the now-mastered
concepts to realistic portfolio workflows instead of more concept study.

## Non-negotiable

Every rule in `.claude/skills/tutor/SKILL.md`'s "Non-negotiable behavior"
section (itself carried from `AGENTS.md` rule 1) applies here without
exception, since the actual teaching in a `/master` pass happens entirely
inside the `/tutor` session it launches: one question at a time, never
fill `MANUAL FIRST` / `PREDICT` / `HAND CALCULATION` / `ORAL CHECK` cells
for the learner, adapt depth from their answers, name the specific
misconception on a wrong answer, and ground every explanation in this
repo's own materials.

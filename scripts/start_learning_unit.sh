#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: scripts/start_learning_unit.sh <slug>"
  echo "Example: scripts/start_learning_unit.sh 01-returns-compounding"
  exit 1
fi

slug="$1"

if [ -n "$(git status --porcelain)" ]; then
  echo "Working tree is not clean. Commit/stash changes before starting a new unit."
  exit 1
fi

git switch main
git pull --ff-only
git switch -c "learn/$slug"

echo "Created branch learn/$slug"
echo "Next: open the matching notebook and complete the manual learning checkpoint."

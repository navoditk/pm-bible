from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]

required = [
    "README.md","ROADMAP.md","LEARNING_PATHS.md","AGENTS.md",
    "reference/index.md","use_cases/index.md","tutors/README.md"
]
for rel in required:
    p = root/rel
    assert p.exists(), f"Missing {rel}"

nbs = list((root/"notebooks").rglob("*.ipynb"))
assert len(nbs) >= 12
for p in nbs:
    json.loads(p.read_text())

print(f"Repository structure OK. {len(nbs)} notebooks validated.")

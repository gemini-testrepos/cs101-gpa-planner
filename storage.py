"""Transcript persistence helpers (JSON and CSV)."""

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import List

from gpa_planner import Course


def save_json(path: Path, courses: List[Course]) -> None:
    payload = [asdict(c) for c in courses]
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_json(path: Path) -> List[Course]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Course(**item) for item in raw]


def export_csv(path: Path, courses: List[Course]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["code", "credits", "grade", "semester"])
        writer.writeheader()
        for course in courses:
            writer.writerow(asdict(course))

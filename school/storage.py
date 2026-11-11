"""JSON persistence for school records."""
import json
from dataclasses import asdict
from pathlib import Path

from .grades import Student


def save_students(students: list[Student], path: Path) -> None:
    path.write_text(json.dumps([asdict(student) for student in students], indent=2), encoding="utf-8")


def load_students(path: Path) -> list[Student]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Student(**item) for item in data]

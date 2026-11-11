# Ahmad, Roll No: __________, 2026-11-11
"""Exceptions, diary and CSV/JSON result storage."""
import csv
import datetime
import json
from pathlib import Path


def safe_division(first_text: str, second_text: str) -> float:
    try:
        return float(first_text) / float(second_text)
    except ValueError as error:
        raise ValueError("Please enter numbers") from error
    except ZeroDivisionError as error:
        raise ZeroDivisionError("Cannot divide by zero") from error


def save_results(results: dict[str, list[int]], csv_path: Path, json_path: Path) -> None:
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "mark1", "mark2", "mark3", "average"])
        for name, marks in results.items():
            writer.writerow([name, *marks, sum(marks) / len(marks)])
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")


def csv_topper(csv_path: Path) -> str:
    with csv_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    if not rows:
        raise ValueError("No results found")
    return max(rows, key=lambda row: float(row["average"]))["name"]


def diary(note: str, path: Path = Path("diary.txt")) -> None:
    with path.open("a", encoding="utf-8") as file:
        file.write(f"{datetime.date.today()}: {note}\n")


if __name__ == "__main__":
    note = input("Today's note: ")
    diary(note)
    print("Note saved.")

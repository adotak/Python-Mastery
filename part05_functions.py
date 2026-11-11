# Ahmad, Roll No: __________, 2026-11-11
"""Functions and comprehensions."""
from math import pi
from typing import Iterable


def area_of_circle(radius: float) -> float:
    return pi * radius * radius


def is_even(number: int) -> bool:
    return number % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    return f"Salaam, {name}" if lang == "ur" else f"Hello, {name}"


def average(marks: Iterable[float]) -> float:
    values = list(marks)
    return sum(values) / len(values) if values else 0.0


def grade(avg: float) -> str:
    if not 0 <= avg <= 100:
        raise ValueError("Marks must be between 0 and 100")
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"


def report(name: str, marks: Iterable[float]) -> str:
    result = average(marks)
    return f"{name}: average {result:.1f}, grade {grade(result)}"


def main() -> None:
    print([x * x for x in range(1, 11)])
    print([name for name in ["Ali", "Sara", "Hamza", "Ayesha"] if len(name) > 4])
    print(report("Ali", [80, 72, 91]))


if __name__ == "__main__":
    main()

# Ahmad, Roll No: __________, 2026-11-11
"""Debugging examples; the corrected passing-mark average is 80.0."""


def passing_average(marks: list[int]) -> float:
    passing = [mark for mark in marks if mark >= 33]
    return sum(passing) / len(passing)


if __name__ == "__main__":
    print(passing_average([90, 25, 70]))

# Ahmad, Roll No: __________, 2026-11-11
"""Standard library tour and reusable module examples."""
import datetime
import math
import random
import statistics

from part05_functions import area_of_circle, average, grade, greet, is_even, report


def main() -> None:
    marks = [55, 70, 80, 90, 95]
    days = (datetime.date(2026, 12, 31) - datetime.date.today()).days
    print(math.sqrt(144), random.choice(["Ali", "Sara", "Hamza"]))
    print(days, statistics.mean(marks), statistics.median(marks))
    print(area_of_circle(2), is_even(4), greet("Ali"), average(marks), grade(average(marks)))
    print(report("Ali", marks))


if __name__ == "__main__":
    main()

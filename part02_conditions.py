# Ahmad, Roll No: __________, 2026-11-11
"""Conditional statements."""


def grade(marks: float) -> str:
    if not 0 <= marks <= 100:
        return "Invalid marks"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 33:
        return "D"
    return "Fail"


def electricity_bill(units: float) -> float:
    if units < 0:
        raise ValueError("Units cannot be negative")
    first = min(units, 100) * 10
    second = min(max(units - 100, 0), 100) * 15
    extra = max(units - 200, 0) * 20
    return first + second + extra + 50


def main() -> None:
    number = int(input("Number: "))
    print("Positive" if number > 0 else "Negative" if number < 0 else "Zero")
    print("Even" if number % 2 == 0 else "Odd")
    marks = float(input("Marks: "))
    print(grade(marks))
    units = float(input("Electricity units: "))
    print(f"Bill: Rs {electricity_bill(units):.2f}")


if __name__ == "__main__":
    main()

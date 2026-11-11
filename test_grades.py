"""Tests for grading and the School Manager."""
import pytest

from part09_oop import BankAccount
from school.grades import Student, class_ranking, grade, make_comment, report_card
from school.storage import load_students, save_students


@pytest.mark.parametrize(("marks", "expected"), [
    (32, "Fail"), (33, "D"), (59, "D"), (60, "C"),
    (69, "C"), (70, "B"), (79, "B"), (80, "A"),
])
def test_grade_boundaries(marks: float, expected: str) -> None:
    assert grade(marks) == expected


def test_grade_rejects_out_of_range() -> None:
    with pytest.raises(ValueError):
        grade(101)


def test_student_report_and_comment() -> None:
    student = Student("Ali", 12, [80, 85, 90])
    assert "average 85.0" in report_card(student)
    assert "Excellent" in make_comment(student)


def test_ranking() -> None:
    students = [Student("Low", 1, [40]), Student("High", 2, [90])]
    assert class_ranking(students)[0].name == "High"


def test_save_and_load(tmp_path) -> None:
    path = tmp_path / "school.json"
    save_students([Student("Ali", 1, [80])], path)
    assert load_students(path)[0].name == "Ali"


@pytest.fixture
def account() -> BankAccount:
    return BankAccount("Ali", 1000)


def test_account_transactions(account: BankAccount) -> None:
    account.deposit(200)
    account.withdraw(100)
    assert account.balance == 1100
    assert len(account.history) == 2


def test_account_errors(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.deposit(-1)
    with pytest.raises(ValueError):
        account.withdraw(2000)

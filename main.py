# Ahmad, Roll No: __________, 2026-11-11
"""Menu-driven School Manager."""
import json
import logging
from pathlib import Path

from school.grades import Student, class_ranking, make_comment, report_card
from school.storage import load_students, save_students

DATA_FILE = Path("school.json")
MENU = "\n1. Add student\n2. Add marks\n3. Show report card\n4. Class ranking\n5. Write comment\n6. Save and exit"


def find_student(students: list[Student], roll_number: int) -> Student | None:
    return next((student for student in students if student.roll_number == roll_number), None)


def add_student(students: list[Student]) -> None:
    name = input("Name: ").strip()
    roll_number = int(input("Roll number: "))
    if find_student(students, roll_number) is not None:
        raise ValueError("Roll number already exists")
    students.append(Student(name, roll_number))


def add_marks(students: list[Student]) -> None:
    student = find_student(students, int(input("Roll number: ")))
    if student is None:
        raise ValueError("Student not found")
    values = input("Marks separated by spaces: ").split()
    marks = [float(value) for value in values]
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")
    student.marks.extend(marks)


def show_report(students: list[Student]) -> None:
    student = find_student(students, int(input("Roll number: ")))
    if student is None:
        raise ValueError("Student not found")
    print(report_card(student))


def show_ranking(students: list[Student]) -> None:
    for position, student in enumerate(class_ranking(students), 1):
        print(f"{position}. {report_card(student)}")


def run(data_file: Path = DATA_FILE) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    students = load_students(data_file)
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_marks(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                show_ranking(students)
            elif choice == "5":
                student = find_student(students, int(input("Roll number: ")))
                if student is None:
                    raise ValueError("Student not found")
                print(make_comment(student))
            elif choice == "6":
                save_students(students, data_file)
                print("Saved.")
                return
            else:
                print("Choose a menu number.")
        except (ValueError, OSError, json.JSONDecodeError) as error:
            logging.error("%s", error)


if __name__ == "__main__":
    run()

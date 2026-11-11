"""Student records and grading logic."""
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[float] = field(default_factory=list)

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0


def grade(average: float) -> str:
    if not 0 <= average <= 100:
        raise ValueError("Marks must be between 0 and 100")
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 33:
        return "D"
    return "Fail"


def report_card(student: Student) -> str:
    return f"{student.name} (Roll {student.roll_number}): average {student.average():.1f}, grade {grade(student.average())}"


def class_ranking(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda student: student.average(), reverse=True)


def make_comment(student: Student) -> str:
    if not student.marks:
        return "Add marks to receive a comment."
    if all(mark >= 80 for mark in student.marks):
        return "Excellent in all subjects, keep it up."
    if student.average() >= 60:
        return "Good work, keep improving."
    if any(mark < 33 for mark in student.marks):
        return "Please focus on subjects below passing marks."
    return "Keep practising for better results."

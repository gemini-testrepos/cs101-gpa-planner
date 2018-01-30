"""Core GPA calculations for CS101 GPA Planner."""

from dataclasses import dataclass
from typing import Iterable

GRADE_SCALE = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0,
}


@dataclass
class Course:
    code: str
    credits: float
    grade: str

    @property
    def grade_points(self) -> float:
        key = self.grade.strip().upper()
        if key not in GRADE_SCALE:
            raise ValueError(f"Unknown grade: {self.grade}")
        return GRADE_SCALE[key]


def compute_gpa(courses: Iterable[Course]) -> float:
    total_credits = 0.0
    weighted_points = 0.0
    for course in courses:
        total_credits += course.credits
        weighted_points += course.credits * course.grade_points
    if total_credits == 0:
        return 0.0
    return round(weighted_points / total_credits, 3)

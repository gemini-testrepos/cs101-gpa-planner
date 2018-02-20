"""Core GPA calculations and target planner for CS101."""

from dataclasses import dataclass
from typing import Iterable, Optional

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
    semester: str = "Winter 2018"

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
        if course.credits <= 0:
            raise ValueError("Credits must be positive")
        total_credits += course.credits
        weighted_points += course.credits * course.grade_points
    if total_credits == 0:
        return 0.0
    return round(weighted_points / total_credits, 3)


def required_gpa_for_target(
    current_gpa: float,
    completed_credits: float,
    target_gpa: float,
    upcoming_credits: float,
) -> Optional[float]:
    """Compute average GPA needed over upcoming credits to reach target."""
    if upcoming_credits <= 0:
        return None
    total_needed = target_gpa * (completed_credits + upcoming_credits)
    remaining_points = total_needed - (current_gpa * completed_credits)
    needed = remaining_points / upcoming_credits
    if needed > 4.0:
        return None
    return round(max(0.0, needed), 3)

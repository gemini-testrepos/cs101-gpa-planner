import unittest
from gpa_planner import Course, compute_gpa, required_gpa_for_target


class TestGPAPlanner(unittest.TestCase):
    def test_weighted_gpa(self):
        courses = [
            Course("CS101", 4.0, "A"),
            Course("MATH110", 4.0, "B"),
        ]
        self.assertAlmostEqual(compute_gpa(courses), 3.5)

    def test_target_gpa(self):
        needed = required_gpa_for_target(3.2, 15.0, 3.5, 15.0)
        self.assertAlmostEqual(needed, 3.8)


if __name__ == "__main__":
    unittest.main()

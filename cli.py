"""CLI entrypoint for CS101 GPA Planner."""

import argparse
from pathlib import Path

from gpa_planner import compute_gpa, required_gpa_for_target
from storage import load_json


def main() -> None:
    parser = argparse.ArgumentParser(description="CS101 GPA Planner")
    parser.add_argument("transcript", type=Path, help="Path to JSON transcript")
    parser.add_argument("--target", type=float, default=None, help="Target cumulative GPA")
    parser.add_argument("--next-credits", type=float, default=15.0)
    args = parser.parse_args()

    courses = load_json(args.transcript)
    gpa = compute_gpa(courses)
    credits = sum(c.credits for c in courses)
    print(f"Courses: {len(courses)} | Credits: {credits:.1f} | GPA: {gpa:.3f}")
    if args.target is not None:
        needed = required_gpa_for_target(gpa, credits, args.target, args.next_credits)
        if needed is None:
            print("Target GPA is not achievable in the next semester alone.")
        else:
            print(f"Required GPA over next {args.next_credits:.1f} credits: {needed:.3f}")


if __name__ == "__main__":
    main()

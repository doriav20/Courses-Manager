import json
from pathlib import Path

from course import Course


def get_total_points(courses: list[Course]) -> float:
    return sum(course.points for course in courses)


def get_average_grade(courses: list[Course]) -> float:
    total_points = get_total_points(courses)
    return sum((course.grade * course.points) for course in courses) / total_points


def load_courses_from_file(grades_file_path: Path) -> list[Course]:
    with open(grades_file_path) as grades_file:
        grades = json.load(grades_file)
        return [Course.from_dict(grade) for grade in grades]

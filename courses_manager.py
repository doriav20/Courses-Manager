import json
from pathlib import Path

from course import Course


def get_total_points(courses: list[Course]) -> float:
    filtered_courses = [course for course in courses if course.grade > 0]
    return sum(course.points for course in filtered_courses)


def get_gpa(courses: list[Course]) -> float:
    filtered_courses = [course for course in courses if course.grade > 0]
    total_points = get_total_points(filtered_courses)
    return sum((course.grade * course.points) for course in filtered_courses) / total_points


def load_courses_from_file(courses_file_path: Path) -> list[Course]:
    with open(courses_file_path) as courses_file:
        courses = json.load(courses_file)
        return [Course.from_dict(course) for course in courses]

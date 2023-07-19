import json
from pathlib import Path

from configuration import Configuration
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


def print_courses_by_configuration(courses: list[Course], config: Configuration) -> None:
    print(f'{"Name":<{config.name_length}}' f'{"Grade":<{config.grade_length}}' f'{"Points":<{config.points_length}}')
    for course in courses:
        print(
            f'{course.name:<{config.name_length}} '
            f'{course.grade:>{config.grade_length}} '
            f'{course.points:>{config.points_length}}'
        )

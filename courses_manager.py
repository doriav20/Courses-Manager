import json
from pathlib import Path

from configuration import Configuration
from course import Course


def get_total_points(courses: list[Course]) -> float:
    return sum(course.points for course in courses)


def get_gpa(courses: list[Course]) -> float:
    total_points = get_total_points(courses)
    return sum((course.grade * course.points) for course in courses) / total_points


def load_courses_from_file(courses_file_path: Path) -> list[Course]:
    with open(courses_file_path) as courses_file:
        courses = json.load(courses_file)
        return [Course.from_dict(course) for course in courses]


def print_courses_by_configuration(courses: list[Course], config: Configuration) -> None:
    name_title = 'Name'
    grade_title = 'Grade'
    points_title = 'Points'

    name_alignment = max(config.name_length, len(name_title))
    grade_alignment = max(config.grade_length, len(grade_title))
    points_alignment = max(config.points_length, len(points_title))

    print(f'{name_title:<{name_alignment}}', end=' ')
    print(f'{grade_title:<{grade_alignment}}', end=' ')
    print(f'{points_title:<{points_alignment}}', end=' ')
    print()

    print(f'{"‾" * len(name_title):<{name_alignment}}', end=' ')
    print(f'{"‾" * len(grade_title):<{grade_alignment}}', end=' ')
    print(f'{"‾" * len(points_title):<{points_alignment}}', end=' ')
    print()

    for course in sorted(courses, key=lambda course: course.name):
        print(f'{course.name:<{name_alignment}}', end=' ')
        print(f'{course.grade:<{grade_alignment}}', end=' ')
        print(f'{course.points:<{points_alignment}}', end=' ')
        print()

    print()

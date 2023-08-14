# courses_display.py

from configuration import Configuration
from course import Course
from courses_manager import get_gpa, get_total_points


def get_alignment(title: str, width: int) -> int:
    return max(width, len(title))


def print_headers(
    name_alignment: int, year_alignment: int, semester_alignment: int, grade_alignment: int, points_alignment: int
) -> None:
    print(f'{"Name":<{name_alignment}}', end=' ')
    print(f'{"Year":<{year_alignment}}', end=' ')
    print(f'{"Semester":<{semester_alignment}}', end=' ')
    print(f'{"Grade":<{grade_alignment}}', end=' ')
    print(f'{"Points":<{points_alignment}}', end=' ')
    print()

    print(f'{"‾" * len("Name"):<{name_alignment}}', end=' ')
    print(f'{"‾" * len("Year"):<{year_alignment}}', end=' ')
    print(f'{"‾" * len("Semester"):<{semester_alignment}}', end=' ')
    print(f'{"‾" * len("Grade"):<{grade_alignment}}', end=' ')
    print(f'{"‾" * len("Points"):<{points_alignment}}', end=' ')
    print()


def print_courses(
    courses: list[Course],
    name_alignment: int,
    year_alignment: int,
    semester_alignment: int,
    grade_alignment: int,
    points_alignment: int,
) -> None:
    filtered_courses = [course for course in courses if course.grade > 0]
    sorted_courses = sorted(filtered_courses)
    for course in sorted_courses:
        print(f'{course.name:<{name_alignment}}', end=' ')
        print(f'{course.year:<{year_alignment}}', end=' ')
        print(f'{course.semester:<{semester_alignment}}', end=' ')
        print(f'{course.grade:<{grade_alignment}}', end=' ')
        print(f'{course.points:<{points_alignment}}', end=' ')
        print()
    print()


def print_gpa_and_total_points(courses: list[Course], config: Configuration) -> None:
    gpa = get_gpa(courses)
    total_points = get_total_points(courses)

    print(f'GPA: {gpa:.2f}')
    print(f'Total Points: {total_points:.1f}')

    print()


def display_courses(courses: list[Course], config: Configuration) -> None:
    name_alignment = get_alignment('Name', config.name_column_width)
    year_alignment = get_alignment('Year', config.year_column_width)
    semester_alignment = get_alignment('Semester', config.semester_column_width)
    grade_alignment = get_alignment('Grade', config.grade_column_width)
    points_alignment = get_alignment('Points', config.points_column_width)

    print_headers(name_alignment, year_alignment, semester_alignment, grade_alignment, points_alignment)

    print_courses(courses, name_alignment, year_alignment, semester_alignment, grade_alignment, points_alignment)

    print_gpa_and_total_points(courses, config)

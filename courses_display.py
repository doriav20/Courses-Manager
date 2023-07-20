from configuration import Configuration
from course import Course
from courses_manager import get_gpa, get_total_points


def get_alignment(title: str, length: int) -> int:
    return max(length, len(title))


def print_headers(name_alignment: int, grade_alignment: int, points_alignment: int) -> None:
    print(f'{"Name":<{name_alignment}}', end=' ')
    print(f'{"Grade":<{grade_alignment}}', end=' ')
    print(f'{"Points":<{points_alignment}}', end=' ')
    print()

    print(f'{"‾" * len("Name"):<{name_alignment}}', end=' ')
    print(f'{"‾" * len("Grade"):<{grade_alignment}}', end=' ')
    print(f'{"‾" * len("Points"):<{points_alignment}}', end=' ')
    print()


def print_courses(courses: list[Course], name_alignment: int, grade_alignment: int, points_alignment: int) -> None:
    filtered_courses = [course for course in courses if course.grade > 0]
    courses_sorted_by_name = sorted(filtered_courses, key=lambda course: course.name)
    for course in courses_sorted_by_name:
        print(f'{course.name:<{name_alignment}}', end=' ')
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
    name_alignment = get_alignment('Name', config.name_length)
    grade_alignment = get_alignment('Grade', config.grade_length)
    points_alignment = get_alignment('Points', config.points_length)

    print_headers(name_alignment, grade_alignment, points_alignment)

    print_courses(courses, name_alignment, grade_alignment, points_alignment)

    print_gpa_and_total_points(courses, config)

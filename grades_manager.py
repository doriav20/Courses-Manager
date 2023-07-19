from course import Course


def get_total_points(courses: list[Course]) -> float:
    return sum(course.points for course in courses)


def get_average_grade(courses: list[Course]) -> float:
    total_points = get_total_points(courses)
    return sum((course.grade * course.points) for course in courses) / total_points

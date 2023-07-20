# main.py

from arguments_handler import get_configuration_path
from configuration import load_configuration
from courses_display import display_courses
from courses_manager import load_courses_from_file
from utils import press_any_key_to_continue


def main() -> None:
    configuration_path = get_configuration_path()
    configuration = load_configuration(configuration_path)

    courses = load_courses_from_file(configuration.courses_file_path)
    display_courses(courses, configuration)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
        print()
    finally:
        press_any_key_to_continue()

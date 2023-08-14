# Courses Manager App

This repository contains a course management system implemented in Python. It allows you to load courses from a JSON
file, display them in a table format, calculate GPA, and perform other related operations.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/doriav20/Courses-Manager.git
   ```

2. Navigate to the project directory:

   ```
   cd courses-manager
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the course manager, follow these steps:

1. Prepare a JSON file containing the course information. The file should have the following structure:

   ```json
   [
     {
       "name": "Course 1",
       "grade": 85,
       "points": 3.5
     },
     {
       "name": "Course 2",
       "grade": 90,
       "points": 4.0
     },
     ...
   ]
   ```

2. Run the `main.py` script:

   ```
   python main.py
   ```

   The script will prompt you to select a configuration file. If a valid configuration file is found, it will be loaded.
   Otherwise, a default configuration will be created.

3. The courses will be loaded from the JSON file and displayed in a table format. The table includes columns for the
   course name, grade, and points.

4. The script will also calculate the GPA (Grade Point Average) and total points for the courses and display them.

5. Press any key to exit the program.

## Customization

The course manager provides some customization options through the configuration file. The default configuration values
can be modified to suit your preferences. To create a configuration file, run the `main.py` script and choose the option
to create a new configuration file.

The configuration file is an ini file with the following structure:

```json
{
  "courses_file_path": "courses.json",
  "name_length": 30,
  "grade_length": 3,
  "points_length": 4
}
```

- `courses_file_path` (optional): The path to the JSON file containing the course information. By default, it is set
  to `"courses.json"`.
- `name_length` (optional): The maximum length of the course name column in the table. By default, it is set to `30`.
- `grade_length` (optional): The maximum length of the grade column in the table. By default, it is set to `3`.
- `points_length` (optional): The maximum length of the points column in the table. By default, it is set to `4`.

Modify these values according to your requirements before running the `main.py` script.

## Compiling the Application

To compile the course manager into an executable file, you can use the `compile_app.py` script provided. This script
uses PyInstaller to create a standalone executable.

1. Run the `compile_app.py` script:

   ```
   python compile_app.py
   ```

   This script will use PyInstaller to create a single executable file named `courses_manager.exe`.

2. The compiled executable file will be generated in the root of the project.

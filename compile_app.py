# compile_app.py

import os
import shutil
import subprocess


def main():
    subprocess.call(["pyinstaller", "--onefile", "app/main.py"])

    shutil.rmtree("build", ignore_errors=True)
    shutil.move("dist/main.exe", "courses_manager.exe")
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("__pycache__", ignore_errors=True)
    os.remove("main.spec")


if __name__ == "__main__":
    main()

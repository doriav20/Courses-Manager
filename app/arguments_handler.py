# arguments_handler.py

import sys
from pathlib import Path
from typing import Optional


def get_configuration_path_from_arguments() -> Optional[Path]:
    args = sys.argv[1:]

    if args and Path(args[0]).exists():
        return Path(args[0])

    return None


# Get configuration path by selecting file (ends with ini) and start from current dir from file explorer
def get_configuration_path_from_file_explorer() -> Optional[Path]:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    filename = askopenfilename(
        title="Select configuration file",
        filetypes=[("Configuration ini files", "*.ini")],
        initialdir=Path.cwd(),
    )

    if filename:
        return Path(filename)

    return None


def get_configuration_path() -> Optional[Path]:
    configuration_path = get_configuration_path_from_arguments()
    if configuration_path:
        return configuration_path

    configuration_path = get_configuration_path_from_file_explorer()
    if configuration_path:
        return configuration_path

    return None

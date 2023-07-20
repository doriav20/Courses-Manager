# utils.py

import msvcrt
import os


def press_any_key_to_continue() -> None:
    print("Press any key to continue...")
    if os.getenv('PYCHARM_HOSTED') == '1':
        input()
    elif os.name == 'nt':
        msvcrt.getch()
    else:
        input()

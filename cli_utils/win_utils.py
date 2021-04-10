import sys
import msvcrt

import os

__all__ = ["get_input", "prepare_terminal", "clear_screen"]

ARROW_CODES = {"H": "up", "P": "down", "M": "right", "K": "left"}

# Waits for a single character of input and returns the string
# "left", "down", "right", "up", "exit", or None.
def get_input():
    key = msvcrt.getwch()
    if key == "\xe0":
        character = msvcrt.getwch()
        return ARROW_CODES.get(character)
    elif key == "\x03":
        return "exit"
    return key

def prepare_terminal():
    pass

def clear_screen():
    cls = lambda: os.system('cls')
    cls()
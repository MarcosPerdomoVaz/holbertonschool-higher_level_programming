#!/usr/bin/python3
"""
Append module
"""


def append_write(filename="", text=""):
    """Append to file with text
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)

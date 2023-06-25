#!/usr/bin/python3
"""
write method
"""


def write_file(filename="", text=""):
    """write to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        if f.write(text):
            return len(text)

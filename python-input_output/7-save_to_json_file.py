#!/usr/bin/python3
"""
Save Module
"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file
    """

    with open(filename, "w", encoding="utf-8") as f:
        written = json.dump(my_obj, f)
    return written

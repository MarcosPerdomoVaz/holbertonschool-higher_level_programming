#!/usr/bin/python3
"""
Json Module
"""
import json


def from_json_string(my_str):
    """convert str to object
    """

    return json.loads(my_str)

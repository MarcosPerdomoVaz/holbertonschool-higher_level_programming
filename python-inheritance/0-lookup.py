#!/usr/bin/python3
"""
Attribute lookup
"""


def lookup(obj):
    """Lookup all attributes in Class
    """
    return [i for i in dir(obj)]

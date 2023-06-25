#!/usr/bin/python3
""" Write a function that writes a string to a text file """


def number_of_lines(filename=""):
    """
    must use the with
    """
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_num += 1
    return line_numi

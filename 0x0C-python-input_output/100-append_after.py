#!/usr/bin/python3
"""
Module append after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append word after string match in file
    """
    with open(filename, "r+") as f:
        new = ""
        for line in f:
            if search_string in line:
                new += new_string
            else:
                new += line
        f.seek(0)
        f.write(new)

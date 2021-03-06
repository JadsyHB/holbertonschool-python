#!/usr/bin/python3
"""
Module read lines
"""


def read_lines(filename="", nb_lines=0):
    """
    prints n lines of file
    """
    with open(filename, "r") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")

#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    return the fewest amount of operations needed
    """
    if n <= 1:
        return 0
    elif n % 3 != 0 and n % 2 != 0:
        return n
    elif n % 2 == 0:
        return 2 + minOperations(n // 2)
    elif n % 3 == 0:
        return 3 + minOperations(n // 3)
    else:
        return 0

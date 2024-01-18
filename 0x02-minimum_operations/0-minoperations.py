#!/usr/bin/python3
"""Minimum Operations to print n times of a letter (H)"""


def minOperations(n):
    """Returns the min num of operations to
    result exactly in n times H chars"""

    if type(n) is not int or n < 2:
        return 0

    facts = [0]
    x = n
    i = n - 1

    while i > 0:
        if x % i == 0:
            facts.append(int(x/i))
            x = i
        i -= 1

    return sum(facts)

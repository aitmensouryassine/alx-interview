#!/usr/bin/python3
"""Minimum Operations to print n times of a letter (H)"""


def minOperations(n):
    """Returns the min num of operations to
    result exactly in n times H chars"""

    facts = [0]
    x = n
    div = 2

    while x > 1:
        while x % div == 0:
            facts.append(div)
            x = x / div
        div += 1

    return int(sum(facts))

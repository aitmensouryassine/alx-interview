#!/usr/bin/python3
"""N Queen Problem With Backtracking"""
from sys import argv


def errorHandler(msg):
    """Print error message and exit with status 1"""
    print(msg)
    exit(1)


if len(argv) != 2:
    errorHandler("Usage: nqueens N")

try:
    n = int(argv[1])
except ValueError:
    errorHandler("N must be a number")

if n < 4:
    errorHandler("N must be at least 4")

print(n)

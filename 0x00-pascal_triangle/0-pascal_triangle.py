#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if (n <= 0):
        return []

    triangle = [[1]]
    row = []

    for i in range(n - 1):
        for j in range(len(triangle[i]) + 1):
            if j - 1 >= 0:
                prev = triangle[i][j-1]
            else:
                prev = 0

            try:
                curr = triangle[i][j]
            except Exception as err:
                curr = 0

            row.append(prev + curr)

        triangle.append(row)
        row = []

    return triangle

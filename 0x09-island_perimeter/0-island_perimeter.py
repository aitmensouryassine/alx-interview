#!/user/bin/python3
"""Island Perimeter Problem"""


def land(grid, rows, cols):
    """Searches for land"""
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col]:
                return (row, col)

    return (-1, -1)


def calc_perimeter(grid, x, y, visited, perimeter):
    """Calculates perimeter
        if cell == 0: +1 perimeter
        if cell == 1: go to top, left, bottom, right => recursion
    """
    if grid[x][y] == 0:
        perimeter.append(1)
        return

    visited.add((x, y))

    if (x, y - 1) not in visited:
        calc_perimeter(grid, x, y - 1, visited, perimeter)
    if (x, y + 1) not in visited:
        calc_perimeter(grid, x, y + 1, visited, perimeter)
    if (x - 1, y) not in visited:
        calc_perimeter(grid, x - 1, y, visited, perimeter)
    if (x + 1, y) not in visited:
        calc_perimeter(grid, x + 1, y, visited, perimeter)


def island_perimeter(grid):
    """Calculated the perimeter of an island"""

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    perimeter = []

    x, y = land(grid, rows, cols)

    if x != -1 and y != -1:
        calc_perimeter(grid, x, y, visited, perimeter)

    return sum(perimeter)

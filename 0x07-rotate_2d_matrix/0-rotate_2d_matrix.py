#!/usr/bin/python3
"""Rotate a 2D matrix clockwise by 90deg"""


def rotate_2d_matrix(matrix):
    """Rotate (n x n) 2D Matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        matrix[i].reverse()

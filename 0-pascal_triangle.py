#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    row = [1] * n
    result = []
    for r in range(n):
        result.append(row[:r + 1])
        for k in range(r, 0, -1):
            row[k] += row[k - 1]
    return result

#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """
    Returns the Pascal’s triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)
    return pascal

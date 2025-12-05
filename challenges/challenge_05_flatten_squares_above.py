"""
Challenge 05 — Nested list comprehension (Challenging)

Task: Rewrite `flattened_squares_above` to use a nested list comprehension.
Given a matrix (list of lists of numbers) and a threshold, return a flat list
containing the square of every value greater than `threshold`.

Example:
    >>> flattened_squares_above([[1,5],[3,8]], 4)
    [25, 64]

Hint: nested comprehensions can replace nested loops: [expr for row in matrix for x in row if ...]
"""

def flattened_squares_above(matrix, threshold):
    out = []
    for row in matrix:
        for x in row:
            if x > threshold:
                out.append(x * x)
    return out


mat = [[0, 2, 5], [10, 3, 4]]
print(flattened_squares_above(mat, 3))  # expected: [25, 100, 16]

"""
Challenge 01 — List comprehension

Task: Rewrite the function `squares_of_evens` so it uses a list comprehension
instead of a `for` loop. The function returns the square of every even
number in the input list, preserving order.

Example:
    >>> squares_of_evens([1,2,3,4,5])
    [4, 16]

Hint: use a conditional inside the list comprehension: [x*x for x in nums if ...]
"""

def squares_of_evens(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n * n)
    return result


sample = [0, 1, 2, 3, 4, 5]
print(squares_of_evens(sample))  # expected: [0, 4, 16]
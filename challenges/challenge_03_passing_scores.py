"""
Challenge 03 — Dict comprehension

Task: Rewrite `passing_scores` to use a dict comprehension. Given a list of
tuples `(name, score)`, return a dictionary mapping names to scores, but
include only the students who scored at least `min_pass`.

Example:
    >>> passing_scores([('Alice', 72), ('Bob', 48), ('Cara', 90)], 50)
    {'Alice': 72, 'Cara': 90}

Hint: dict comprehensions look like `{k: v for k, v in items if ...}`
"""


def passing_scores(pairs, min_pass=50):
    result = {}
    for name, score in pairs:
        if score >= min_pass:
            result[name] = score
    return result


students = [('Alice', 72), ('Bob', 48), ('Cara', 90)]
print(passing_scores(students))  # expected: {'Alice': 72, 'Cara': 90}

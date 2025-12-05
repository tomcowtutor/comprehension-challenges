"""
Challenge 02 — List comprehension

Task: Rewrite `upper_long_words` to use a list comprehension. Given a list of
strings, return a new list containing the uppercase version of each word that
has length strictly greater than `min_len`.

Example:
    >>> upper_long_words(["hi","hello","friend"], 3)
    ['HELLO', 'FRIEND']

Hint: Use the `.upper()` string method inside the comprehension.
"""


def upper_long_words(words, min_len=3):
    out = []
    for w in words:
        if len(w) > min_len:
            out.append(w.upper())
    return out


print(upper_long_words(["a","ab","abc","abcd"], 2))  # expected: ['ABC', 'ABCD']

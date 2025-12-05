"""
Challenge 04 — Dict comprehension

Task: Rewrite `vowel_counts` to use a dict comprehension. Given a list of
words, return a dictionary mapping each word to the number of vowels in it.

Example:
    >>> vowel_counts(['apple','sky','queue'])
    {'apple': 2, 'sky': 0, 'queue': 4}

Hint: you can use `sum(1 for ch in word.lower() if ch in 'aeiou')` to count vowels.
"""


def vowel_counts(words):
    counts = {}
    for w in words:
        count = 0
        for ch in w.lower():
            if ch in 'aeiou':
                count += 1
        counts[w] = count
    return counts


print(vowel_counts(['apple', 'sky', 'queue']))  # expected: {'apple':2,'sky':0,'queue':4}

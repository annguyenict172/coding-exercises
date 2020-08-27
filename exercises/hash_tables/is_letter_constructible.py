"""
Is an anonymous letter constructible: EPI 12.2
"""

import collections


def is_constructible(magazine, letter):
    char_count = collections.Counter()
    for char in magazine:
        char_count[char] += 1

    for char in letter:
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


print(is_constructible('aaabbbccc', 'abc'))
print(is_constructible('abc', 'aaabbbccc'))

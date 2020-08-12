"""
Check if a string can form a palindrome: EPI 12.1
"""

import collections


# 1. Even num of characters: all characters appear even number of times
# 2. Odd num of characters: only one character can appear odd number of times,
# other characters must appear even number of times
def can_form_palindrome(string):
    char_counter = collections.Counter()
    for c in string:
        char_counter[c] += 1

    even_num_of_chars = len(string) % 2 == 0
    has_odd = False

    for c in char_counter.keys():
        if char_counter[c] % 2 != 0:
            if even_num_of_chars or (not even_num_of_chars and has_odd):
                return False
            elif not even_num_of_chars and not has_odd:
                has_odd = True
    return True

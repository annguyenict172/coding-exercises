"""
Leet Code #3
"""
import unittest


def length_of_longest_substr(s):
    if not s:
        return 0
    left = 0
    right = 0
    appears = set()
    max_length = 0
    while right < len(s):
        if s[right] in appears:
            # We have to move the left pointer until we don't have repeated characters
            # in our window anymore
            while s[left] != s[right]:
                appears.remove(s[left])
                left += 1
            left += 1
            right += 1
        else:
            # If we haven't seen this character before, move forward
            appears.add(s[right])
            right += 1
            max_length = max(max_length, right - left)
    return max_length


class TestResult(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(length_of_longest_substr(''), 0)

    def test_single_character_string(self):
        self.assertEqual(length_of_longest_substr('a'), 1)

    def test_single_repeated_character_string(self):
        self.assertEqual(length_of_longest_substr('aaaaa'), 1)

    def test_long_string(self):
        self.assertEqual(length_of_longest_substr('aabcdcegdfbcagh'), 7)

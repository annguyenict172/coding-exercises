import unittest
import collections


def is_anonymous_letter_constructible(letter, magazine):
    magazine_char_counts = collections.defaultdict(int)
    for char in magazine:
        magazine_char_counts[char] += 1

    for char in letter:
        if magazine_char_counts[char] == 0:
            return False
        else:
            magazine_char_counts[char] = magazine_char_counts[char] - 1

    return True


class TestResult(unittest.TestCase):

    def test_empty_letter_and_magazine(self):
        self.assertTrue(is_anonymous_letter_constructible('', ''))

    def test_empty_letter(self):
        self.assertTrue(is_anonymous_letter_constructible('', 'abcde'))

    def test_empty_magazine(self):
        self.assertFalse(is_anonymous_letter_constructible('abcde', ''))

    def test_letter_constructible(self):
        self.assertTrue(is_anonymous_letter_constructible('abcde', 'aabbccddee'))

    def test_letter_not_constructible(self):
        self.assertFalse(is_anonymous_letter_constructible('abcdefffgh', 'abcdefgh'))

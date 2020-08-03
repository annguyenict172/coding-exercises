"""
Interview Cake: Reverse Words
"""
import unittest


def reverse_string(string, start, end):
    mid = (end - start) // 2
    for i in range(0, mid+1):
        string[start+i], string[end-i] = string[end-i], string[start+i]


def reverse_words(message):
    reverse_string(message, 0, len(message)-1)
    lower = upper = 0
    while upper < len(message):
        if message[upper] == ' ':
            reverse_string(message, lower, upper-1)
            lower = upper + 1
        upper += 1

    reverse_string(message, lower, upper - 1)


class TestResult(unittest.TestCase):

    def test_correct_solution(self):
        message = ['c', 'a', 'k', 'e', ' ',
                   'p', 'o', 'u', 'n', 'd', ' ',
                   's', 't', 'e', 'a', 'l']
        reverse = ['s', 't', 'e', 'a', 'l', ' ',
                   'p', 'o', 'u', 'n', 'd', ' ',
                   'c', 'a', 'k', 'e']
        reverse_words(message)
        self.assertEqual(message, reverse)

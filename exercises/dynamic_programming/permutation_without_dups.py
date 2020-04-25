"""
Permutation Without Dups: return all permutation of a string of unique characters

Example 1:
Input: ab
Output: ab, ba

Example 2:
Input: abc
Output: cab, abc, acb, cba, bca, bac
"""

from io import StringIO
import unittest


def permutation(stdin):
    string = ''
    for line in stdin:
        string = line.strip()

    return sorted(permutation_recursive(string))


def permutation_recursive(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        first_char = string[0]
        permutations_of_rest = permutation_recursive(string[1:])
        permutations = []
        for permutation in permutations_of_rest:
            for i in range(len(permutation)+1):
                new_permutation = permutation[:i] + first_char + permutation[i:]
                permutations.append(new_permutation)
        return permutations


class TestResult(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(permutation(StringIO('\n')), sorted([]))

    def test_string_of_two(self):
        self.assertEqual(permutation(StringIO('ab\n')), sorted(['ab', 'ba']))

    def test_string_of_three(self):
        self.assertEqual(permutation(StringIO('abc\n')), sorted(['abc', 'acb', 'cab', 'bac', 'bca', 'cba']))

    def test_string_of_four(self):
        self.assertEqual(permutation(StringIO('abcd\n')), sorted(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))


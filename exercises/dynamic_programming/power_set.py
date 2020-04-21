"""
Power Set: return all subsets of a set

Example 1:
Input: 1,2
Output: {1}, {2}, {1, 2}

Example 2:
Input: 1,2,3
Output: {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3}

"""

from io import StringIO
import unittest


def power_set(stdin):
    original_set = set()
    for line in stdin:
        line = line.split(',')
        original_set = set(list(map(lambda x: int(x), line)))

    subsets = [set()]
    for element in original_set:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset)
            new_subsets.append(subset | {element})

        subsets = new_subsets

    # Return in sorted order for testing purpose
    return subsets.sort()


class TestResult(unittest.TestCase):

    def test_set_of_one(self):
        self.assertEqual(power_set(StringIO('1\n')), [set(), {1}].sort())

    def test_set_of_two(self):
        self.assertEqual(power_set(StringIO('1,2\n')), [set(), {1}, {2}, {1, 2}].sort())

    def test_set_of_three(self):
        self.assertEqual(power_set(StringIO('1,2,3\n')), [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}].sort())

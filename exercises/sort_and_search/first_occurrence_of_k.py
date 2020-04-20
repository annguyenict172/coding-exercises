"""
Find the first occurrence of k in a sorted array_and_string
If k is not present, return -1
Ex:
[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108 => 3
[2, 3, 4, 5], 1 => -1
"""
import unittest
import bisect


def first_occurrence_of_k_pythonic(numbers, k):
    target_index = bisect.bisect_left(numbers, k)
    if target_index == len(numbers):
        return -1
    return target_index


def first_occurrence_of_k(numbers, k):
    lower = 0
    upper = len(numbers) - 1
    target_index = -1

    # Sanity check
    if upper <= lower:
        return -1

    while lower <= upper:
        middle = lower + int((upper - lower) / 2)
        if numbers[middle] == k:
            target_index = middle
            upper = upper - 1
        elif numbers[middle] < k:
            lower = middle + 1
        else:
            upper = middle - 1
    return target_index


class TestResult(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_occurrence_of_k([], 1), -1)

    def test_single_repeated_number_list(self):
        self.assertEqual(first_occurrence_of_k([1, 1, 1, 1, 1, 1, 1], 1), 0)

    def test_long_array(self):
        self.assertEqual(first_occurrence_of_k([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108), 3)

    def test_long_array_2(self):
        self.assertEqual(first_occurrence_of_k([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285), 6)

    def test_no_occurrence(self):
        self.assertEqual(first_occurrence_of_k([2, 3, 4, 5], 1), -1)

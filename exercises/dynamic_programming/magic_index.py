"""
Magic Index: an index where A[index] == index
Find a magic index in a sorted array

Example 1:
Input: 2,3,7,10,12,20
Output: None

Example 2:
Input: 0,1,2,5,7,8
Output: 0 or 1 or 2

Example 3:
Input: -2,-1,0,3,7,8
Output: 3

"""

from io import StringIO
import unittest


def find_magic_index(stdin):
    nums = []
    for line in stdin:
        line = line.split(',')
        nums = list(map(lambda x: int(x), line))

    return find_magic_index_recursive(nums, 0, len(nums)-1)


def find_magic_index_recursive(nums, start, end):
    if start > end:
        return None

    mid = start + (end-start) // 2
    if nums[mid] == mid:
        return mid

    # Search left
    left_idx = min(mid-1, nums[mid])
    left_magic_idx = find_magic_index_recursive(nums, start, left_idx)
    if left_magic_idx:
        return left_magic_idx

    # Search right
    right_idx = max(mid+1, nums[mid])
    right_magic_idx = find_magic_index_recursive(nums, right_idx, end)
    if right_magic_idx:
        return right_magic_idx


class TestResult(unittest.TestCase):

    def test_no_magic_index(self):
        self.assertEqual(find_magic_index(StringIO('2,3,7,10,12,20\n')), None)

    def test_three_magic_indexes(self):
        self.assertIn(find_magic_index(StringIO('0,1,2,5,7,8\n')), [0, 1, 2])

    def test_one_magic_index(self):
        self.assertEqual(find_magic_index(StringIO('-2,-1,0,3,7,8\n')), 3)

    def test_array_with_repeated_numbers(self):
        self.assertEqual(find_magic_index(StringIO('-10,-5,2,2,2,3,4,8,9,13\n')), 2)

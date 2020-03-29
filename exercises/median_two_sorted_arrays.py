"""
Leet Code #4
"""
import unittest


def find_median(array_x, array_y):
    if not len(array_x):
        return find_median_single_array(array_y)
    if not len(array_y):
        return find_median_single_array(array_x)

    length_left_side = (len(array_x) + len(array_y) + 1) // 2
    start_x = 0
    end_x = len(array_x) - 1
    while True:
        partition_x = (start_x + end_x) // 2
        partition_y = length_left_side - partition_x
        if partition_x == 0:
            max_left_x = float('-inf')
        else:
            max_left_x = array_x[partition_x-1]

        if partition_y == 0:
            max_left_y = float('-inf')
        else:
            max_left_y = array_y[partition_y-1]

        min_right_x = array_x[partition_x]

        # If there is an index error, it means that we choose all elements of Y
        # to add to the left half
        try:
            min_right_y = array_y[partition_y]
        except IndexError:
            min_right_y = float('+inf')

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (len(array_x) + len(array_y)) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_y, max_left_x)
        elif max_left_x > min_right_y:
            end_x = partition_x - 1
        else:
            start_x = partition_x + 1


def find_median_single_array(array):
    mid_idx = len(array) // 2
    if len(array) % 2 == 0:
        return (array[mid_idx] + array[mid_idx-1]) / 2
    else:
        return array[mid_idx]


class TestResult(unittest.TestCase):

    def test_first_list_empty(self):
        self.assertEqual(find_median([], [1, 2, 3, 4]), 2.5)

    def test_second_list_empty(self):
        self.assertEqual(find_median([1, 2, 3], []), 2)

    def test_median_lies_in_first_list(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6], [7, 8]), 4.5)

    def test_median_lies_in_second_list(self):
        self.assertEqual(find_median([7, 8], [1, 2, 3, 4, 5, 6]), 4.5)

    def test_median_lies_in_two_list(self):
        self.assertEqual(find_median([1, 3, 5], [2, 4, 6]), 3.5)

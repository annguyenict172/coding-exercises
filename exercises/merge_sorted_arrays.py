"""
Merge k sorted arrays into a single sorted arrays
Ex:
[1, 9, 10], [0, 6, 9], [1, 2, 3]
=> [0, 1, 1, 2, 3, 6 , 9, 9, 10]
"""
import heapq
import unittest


def merge_sorted_arrays(arrays):
    final_list = []

    # This is to keep track of where we at in each array
    last_index = [0] * len(arrays)

    # Initialize the min heap with the first element from each array
    min_heap = [(a[0], array_index) for array_index, a in enumerate(arrays) if len(a)]
    heapq.heapify(min_heap)

    while len(min_heap):
        # Get the minimum number along with the array where it comes from
        num, array_index = heapq.heappop(min_heap)

        final_list.append(num)

        # Increment the write index for this array
        last_index[array_index] += 1

        # Check if there is any other number in this array
        if last_index[array_index] == len(arrays[array_index]):
            continue
        else:
            # If not, we will push the next number in this array into the min heap
            next_number = arrays[array_index][last_index[array_index]]
            heapq.heappush(min_heap, (next_number, array_index))
    return final_list


class TestResult(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sorted_arrays([]), [])

    def test_two_lists_with_equal_length(self):
        self.assertEqual(merge_sorted_arrays([[1, 3, 5], [2, 4, 6]]), [1, 2, 3, 4, 5, 6])

    def test_three_lists_with_equal_length(self):
        self.assertEqual(merge_sorted_arrays([[1, 9, 10], [0, 6, 9], [1, 2, 3]]), [0, 1, 1, 2, 3, 6 , 9, 9, 10])

    def test_two_lists_with_unequal_length(self):
        self.assertEqual(merge_sorted_arrays([[1, 3, 5], [2]]), [1, 2, 3, 5])

    def test_three_lists_with_unequal_length(self):
        self.assertEqual(merge_sorted_arrays([[1, 9, 10], [0, 6], [9, 10, 23, 67, 94]]), [0, 1, 6, 9, 9, 10, 10, 23, 67, 94])

    def test_three_lists_with_an_empty_list(self):
        self.assertEqual(merge_sorted_arrays([[1, 9, 10], [0, 6, 9], []]), [0, 1, 6, 9, 9, 10])

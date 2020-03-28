"""
Leet Code #904
"""
import unittest


# Use sliding windows technique
def total_fruit(tree):
    lower = 0
    upper = 0
    basket = set()
    max_fruits = 0

    while upper < len(tree):
        if tree[upper] not in basket and len(basket) == 2:
            # Add this fruit and the one before it to the basket
            lower = upper - 1
            basket = {tree[lower], tree[upper]}

            # Check if we have a chain of fruits in the back that are similar to the "lower" fruit
            for i in range(lower-1, -1, -1):
                if tree[i] != tree[lower]:
                    break
                else:
                    lower = i
        else:
            basket.add(tree[upper])
            upper += 1
            max_fruits = max(max_fruits, upper - lower)
    return max_fruits


class TestResult(unittest.TestCase):

    def test_one_tree(self):
        self.assertEqual(total_fruit([1]), 1)

    def test_long_sequence(self):
        self.assertEqual(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_medium_sequence(self):
        self.assertEqual(total_fruit([0, 1, 6, 6, 4, 4, 6]), 5)

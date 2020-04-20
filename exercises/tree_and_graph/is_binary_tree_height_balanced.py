"""
The binary tree is considered balance if the difference between the height of its left subtree
and right subtree is not larger than 1
"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


# Perform post-order traversal to get the height of the left subtree and right subtree
# Then decide if the tree is balanced or not
def is_height_balanced(tree):
    is_balanced, height = get_balanced_status_and_height(tree)
    return is_balanced


def get_balanced_status_and_height(tree):
    if tree is None:
        return True, -1

    is_left_balanced, left_height = get_balanced_status_and_height(tree.left)
    if not is_left_balanced:
        return False, 0

    is_right_balanced, right_height = get_balanced_status_and_height(tree.right)
    if not is_right_balanced:
        return False, 0

    is_balanced = abs(right_height - left_height) <= 1
    height = max(right_height, left_height) + 1
    return is_balanced, height


class TestResult(unittest.TestCase):

    def test_null_tree(self):
        self.assertTrue(is_height_balanced(None))

    def test_tree_with_single_node(self):
        root = Node(1)
        self.assertTrue(is_height_balanced(root))

    def test_left_skewed_tree(self):
        root = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        root.add_left(second_node)
        second_node.add_left(third_node)
        third_node.add_left(fourth_node)

        self.assertFalse(is_height_balanced(root))

    def test_right_skewed_tree(self):
        root = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        root.add_right(second_node)
        second_node.add_right(third_node)
        third_node.add_right(fourth_node)

        self.assertFalse(is_height_balanced(root))

    def test_balanced_tree(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        left_left = Node(4)
        left_right = Node(5)
        root.add_left(left)
        root.add_right(right)
        left.add_left(left_left)
        left.add_right(left_right)

        self.assertTrue(is_height_balanced(root))

    def test_unbalanced_tree(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        left_left = Node(4)
        left_right = Node(5)
        left_left_left = Node(6)
        root.add_left(left)
        root.add_right(right)
        left.add_left(left_left)
        left.add_right(left_right)
        left_left.add_left(left_left_left)

        self.assertFalse(is_height_balanced(root))

"""
Check if a binary tree is a Binary Search Tree - EPI 14.1
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BSTStatusWithMinMax(object):
    def __init__(self, is_bst, max_val, min_val):
        self.is_bst = is_bst
        self.max_val = max_val
        self.min_val = min_val


def check_bst(tree):
    if tree is None:
        return BSTStatusWithMinMax(True, float('-inf'), float('inf'))

    left_info = check_bst(tree.left)
    if not left_info.is_bst:
        return BSTStatusWithMinMax(False, float('-inf'), float('inf'))

    right_info = check_bst(tree.right)
    if not right_info.is_bst:
        return BSTStatusWithMinMax(False, float('-inf'), float('inf'))

    is_bst = left_info.max_val <= tree.value <= right_info.min_val
    max_val = max(tree.value, left_info.max_val, right_info.max_val)
    min_val = min(tree.value, left_info.min_val, right_info.min_val)

    return BSTStatusWithMinMax(is_bst, max_val, min_val)


def is_bst(tree):
    return check_bst(tree).is_bst


root = TreeNode(5)
left = TreeNode(2)
right = TreeNode(8)

left_left = TreeNode(1)
left_right = TreeNode(3)

right_left = TreeNode(7)
right_right = TreeNode(9)

root.left = left
root.right = right

left.left = left_left
left.right = left_right

right.left = right_left
right.right = right_right

assert is_bst(root) is True

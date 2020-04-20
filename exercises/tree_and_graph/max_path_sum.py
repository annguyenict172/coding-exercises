"""
LeetCode #124
"""
from copy import copy
import unittest


def max_path_sum_brute_force(root):
    paths = []
    queue = [root]
    # Perform BFS
    while len(queue):
        current = queue.pop()

        # Add it self to the list of path - a single node is a valid path itself
        paths.append([current])

        new_paths = []
        for path in paths:
            # If there is a path going through this node,
            # that same path can go through its children as well
            if current in path:
                if current.left is not None:
                    new_path = copy(path)
                    new_path.append(current.left)
                    new_paths.append(new_path)
                if current.right is not None:
                    new_path = copy(path)
                    new_path.append(current.right)
                    new_paths.append(new_path)

                # We can also go left -> parent -> right
                if current.left is not None and current.right is not None:
                    new_paths.append([current, current.left, current.right])
        paths = paths + new_paths

        # Add children to the queue
        if current.left is not None:
            queue.insert(0, current.left)
        if current.right is not None:
            queue.insert(0, current.right)

    # Map the list of paths to the list of sums, then extract the maximum
    max_sum = max(map(lambda p: sum(map(lambda n: n.val, p)), paths))
    return max_sum


def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum

        if node is None:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        gain = node.val + left_gain + right_gain
        max_sum = max(max_sum, gain)

        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum

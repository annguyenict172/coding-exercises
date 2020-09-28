"""
Find k largest nodes in a BST - EPI 14.3
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_k_largest_node(tree, k):
    top_k = []
    def post_order(tree):
        nonlocal top_k, k
        if not tree:
            return
        else:
            post_order(tree.right)
            if len(top_k) < k:
                top_k.append(tree.value)
                post_order(tree.left)
            else:
                return
    post_order(tree)
    return top_k


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


top_k_nodes = find_k_largest_node(root, 3)
print(top_k_nodes)

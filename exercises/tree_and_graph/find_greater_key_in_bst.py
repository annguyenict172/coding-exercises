class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_greater_key(tree, value):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.value > value:
            subtree, first_so_far = subtree.left, subtree
        else:
            # Root and all keys in left subtree are <= value, skip them
            subtree = subtree.right
    return first_so_far


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

print(find_greater_key(root, 3).value)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_palindrome(l):
    lower, upper = 0, len(l) - 1
    while lower < upper:
        if l[lower] != l[upper]:
            return False
        lower += 1
        upper -= 1
    return True


def test_symmetric(root):
    nodes = []

    def inorder_traversal(tree):
        if not tree:
            return
        inorder_traversal(tree.left)
        nodes.append(tree.value)
        inorder_traversal(tree.right)

    inorder_traversal(root)
    return check_palindrome(nodes)


def test_symmetric_better(root):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_1 and subtree_0:
            return (subtree_0.value == subtree_1.value
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left)
                    )
        return False
    return not root or check_symmetric(root.left, root.right)


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(2)

left_left = TreeNode(3)
left_right = TreeNode(4)

right_left = TreeNode(4)
right_right = TreeNode(3)

root.left = left
root.right = right

left.left = left_left
left.right = left_right

right.left = right_left
right.right = right_right

print(test_symmetric_better(root))

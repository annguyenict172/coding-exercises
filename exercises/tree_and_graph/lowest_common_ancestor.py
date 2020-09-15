"""
Compute the lowest common ancestor in a binary tree - EPI 9.3
"""
import collections


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_ancestor(tree, node1, node2):
    if not tree:
        return False
    
    found_node_1, found_node_2 = False, False

    def traverse(root):
        nonlocal found_node_1
        nonlocal found_node_2
        if not root:
            return
        traverse(root.left)
        if root == node1:
            found_node_1 = True
        if root == node2:
            found_node_2 = True
        traverse(root.right)
    
    traverse(tree)
    return found_node_1 and found_node_2


def find_lowest_common_ancestor(tree, node1, node2):
    subtree = tree
    while True:
        if is_ancestor(subtree.left, node1, node2):
            subtree = subtree.left
        elif is_ancestor(subtree.right, node1, node2):
            subtree = subtree.right
        else:
            break
    
    return subtree


def lca(tree, node1, node2):
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    def lca_helper(tree, node1, node2):
        if not tree:
            return Status(0, None)
        
        left_result = lca_helper(tree.left, node1, node2)
        if left_result.num_target_nodes == 2:
            return left_result
        
        right_result = lca_helper(tree.right, node1, node2)
        if right_result.num_target_nodes == 2:
            return right_result
        
        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes
                            + int(tree is node1) + int(tree is node2))
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)
    
    return lca_helper(tree, node1, node2).ancestor


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

print(lca(root, right_left, right_right).value)
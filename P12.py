# The Gate: Challenge 9 (The BST Search Engine)
# You are writing the search algorithm for a Binary Search Tree. You must use the Cloning Factory (recursion) to navigate the maps.
#
# Your Logic Rules:
#
# If the node doesn't exist (None), the target is not in the tree. Return False.
#
# If the node.value is exactly equal to the target, you found it. Return True.
#
# If the target is less than the node.value, you must clone the function and send it down the left map.
#
# If the target is greater than the node.value, you must clone the function and send it down the right map.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Building a slightly larger tree to test the engine
root = TreeNode(50)
root.left = TreeNode(25)
root.right = TreeNode(75)
root.left.left = TreeNode(10)
root.left.right = TreeNode(30)

def search_bst(node, target):
    # Rule 1: Dead end
    if node is None:
        return False

    # Rule 2: Found it
    if node.value == target:
        return True

print(search_bst(root, 99)) # Should print False
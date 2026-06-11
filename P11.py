# Challenge 8: In-Order Traversal (Depth-First Search)
# The most important algorithm for a Binary Tree is the In-Order Traversal.
# If you build a Binary Search Tree correctly, an In-Order Traversal will read the numbers in perfect ascending order,
# from smallest to largest, no matter how massive the tree is.
#
# The physical law of In-Order Traversal dictates three steps that must be executed in this exact sequence:
#
# Go Left: Follow the left map as far down as possible until you hit a dead end (None).
#
# Process: Read the treasure inside the box you are currently standing on.
#
# Go Right: Follow the right map.

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


def traverse_in_order(node):
    # BASE CASE: If the box doesn't exist (you fell off the tree), stop and go back.
    if node is None:
        return

    # STEP 1: GO LEFT.
    # (Call this exact function again, passing in the left map)
    # Write Step 1 here:

    traverse_in_order(node.left)

    # STEP 2: PROCESS.
    # (Print the value of the current node)
    # Write Step 2 here:
    print(node.value)


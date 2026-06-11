# Here is the exact blueprint for a Binary Tree node. It is identical to a Linked List node, but it has two maps instead of one.
# Challenge 7: The Branch
# Your objective is to build a microscopic tree and prove that you can navigate its pointers.
#
# The Root: Create a root node with the value 50.
#
# The Left Branch: Create a left child node with the value 25.
#
# The Right Branch: Create a right child node with the value 75.
#
# The Links: Physically link them together so that the node holding 50 points its left map to 25 and its right map to 75.
#
# The Traversal: Prove the connections by writing two print statements:
# One that uses the root variable to print the left value (25), and one that uses the root variable to print the right value (75).

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(50)
left_branch = TreeNode(25)
right_branch = TreeNode(75)

root.left = left_branch
root.right = right_branch

print(root.left.value)
print(root.right.value)
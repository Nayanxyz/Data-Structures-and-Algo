# o navigate a Linked List of any size, we don't chain dots. We use a moving pointer and a loop.
#
# The Gate: Challenge 4 (The Traversal Engine)
# This is the most important loop you will ever write for Linked Lists.
#
# Instead of jumping directly from A to C, you create a new variable called current. Think of current as a spotlight.
#
# You shine the spotlight on the first node.
#
# You print the treasure inside it.
#
# You move the spotlight to the next node.
#
# You repeat this until the spotlight hits None (the end of the road).
#
# Here is your exact starting code:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node_a = Node(10)
node_b = Node(20)
node_c = Node(30)

node_a.next = node_b
node_b.next = node_c

# 1. Put the spotlight on the first node
current = node_a

# 2. WRITE A WHILE LOOP HERE
# The loop should run as long as 'current' is not None.
# Inside the loop:
#   a) Print the value of the current node.
#   b) Move the 'current' spotlight to the next node (current = current.next)



while current != None:
    print(current.value)
    current = current.next


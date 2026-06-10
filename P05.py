# The Linked List.
#
# A Linked List does not need to be side-by-side. The memory can be scattered randomly across the entire computer.
# How does it stay connected? Every piece of data physically holds the GPS coordinates (a Pointer) to the next piece of data.



class Node:
    def __init__(self, value):
        self.value = value  # The actual data (e.g., the number 84)
        self.next = None   # The pointer to the next node (Defaults to nothing)


# Using the Node class above, write the Python code to do exactly this:
#
# Create three separate nodes with the values 10, 20, and 30.
#
# Manually link them together so that 10 points to 20, and 20 points to 30.
#
# Prove they are linked by writing a single print statement that starts at the first node,
# follows the pointers, and prints the number 30.


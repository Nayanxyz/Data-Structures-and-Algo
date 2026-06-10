# The Linked List.
#
# A Linked List does not need to be side-by-side. The memory can be scattered randomly across the entire computer.
# How does it stay connected? Every piece of data physically holds the GPS coordinates (a Pointer) to the next piece of data.



class Node:
    def __init__(self, value):
        self.value = value  # The actual data (e.g., the number 84)
        self.next = None   # The pointer to the next node (Defaults to nothing)



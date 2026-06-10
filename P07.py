class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node_a = Node(10)
node_b = Node(20)

node_a.next = node_b

node_x = Node(15)
    # The new stone, currently pointing to nothing


# Your Task:
# Write exactly TWO lines of Python code to safely insert node_x between node_a and node_b without causing a memory leak.
#
# Remember the simulation.
#
# Build the new bridge forward from node_x first.
#
# Break the old bridge from node_a and point it to node_x.

# --- 2. THE INSERTION ---
# We do not use 'node_b' here because in a real system, we only know about the node we are standing on (node_a).

# Step 1: Secure the rest of the list
node_x.next = node_a.next

# Step 2: Break the old bridge and connect it to the new node
node_a.next = node_x

# --- 3. THE PROOF (TRAVERSAL) ---
current = node_a
while current is not None:
    print(current.value)
    current = current.next

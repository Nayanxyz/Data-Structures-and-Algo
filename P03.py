# The Problem:
#
# You have the exact same array as before: $ N+1 $ slots, numbers 1 through $ N $, with one duplicate.
# Example: [3, 1, 4, 2, 2]
#
# The New Constraints:
# You must solve it in $O(N)$ Time. (You cannot use nested loops).
# You must solve it in $O(1)$ Space. (You cannot use a set(), a list(), or any extra memory. No notebooks allowed).
# You are not allowed to modify the original array (no sorting).
#
# How do you find a duplicate quickly without using extra memory and without a brute-force loop?
# (Hint: Think about the numbers as arrows pointing to indices. If the number is 3, go look at index 3.
# This is called "Cycle Detection" or "Two Pointers").

def find_duplicate_optimized(arr):
    # PHASE 1: Find the Crash
    # Start both pointers at the very beginning
    slow = arr[0]
    fast = arr[0]

    # We use 'while True' because we know mathematically a cycle exists.
    # It will run until they crash into each other.
    while True:
        slow = arr[slow]  # Tortoise takes 1 step
        fast = arr[arr[fast]]  # Hare takes 2 steps

        # Did the fast pointer lap the slow pointer?
        if slow == fast:
            break  # CRASH! Exit Phase 1.

    # PHASE 2: Find the Doorway (The Duplicate)
    # Move the slow pointer back to the start line.
    # Leave the fast pointer exactly where it crashed.
    slow = arr[0]

    # Now, both take exactly 1 step at a time.
    # Mathematical law dictates they will collide exactly at the cycle entrance.
    while slow != fast:
        slow = arr[slow]  # Takes 1 step
        fast = arr[fast]  # Takes 1 step (Slowed down to match)

    # The place they collide is the duplicate number.
    return slow


# Execute the engine
print("The duplicate is:", find_duplicate_optimized([3, 1, 4, 2, 2]))


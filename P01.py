# The Problem:You are given an array of integers where every integer is between 1 and $N$ (inclusive).
# The array has $N+1$ elements, meaning there is at least one duplicate number.
#
# Your tasks:
# Write a Python function find_duplicate_brute(arr) that finds a duplicate number using a brute-force approach.
#
# Write a second Python function find_duplicate_optimized(arr) that solves the exact same problem but is highly optimized.
#
# State the exact Time Complexity (Big-O) and Space Complexity (Memory) for both of your functions.
#
# If your "optimized" solution is $O(N^2)$ in time, you fail.
# If your code relies on built-in Python tricks like arr.count() instead of raw logic, you fail.

def find_duplicate_brute(arr):
    n = len(arr)

    # Outer loop (Left Finger)
    # This picks the number we are currently testing
    for i in range(n):

        # Inner loop (Right Finger)
        # It starts at 'i + 1' so we only check the numbers AFTER our Left Finger.
        # This prevents comparing a number to itself, and prevents checking backwards.
        for j in range(i + 1, n):

            # The Comparison
            # If the value at the Left Finger equals the value at the Right Finger...
            if arr[i] == arr[j]:
                return arr[i]  # We found the duplicate, exit the function.


# Test it
print("Duplicate found:", find_duplicate_brute([3, 1, 4, 2, 2]))

# second question
notebook = set()       # 1. Create an empty set
notebook.add(5)        # 2. Add the number 5 to it
notebook.add(3)        # 3. Add the number 3 to it
notebook.add(3)        # 3. Add the number 3 to it
notebook.add(4)        # 3. Add the number 3 to it
notebook.add(1)        # 3. Add the number 3 to it
notebook.add(2)        # 3. Add the number 3 to it

# 4. Check if a number is already inside (This is instant!)
if 3 in notebook:
    print("3 is a duplicate!")

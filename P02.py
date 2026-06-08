#  HASH SETS

# I want you to write the function find_duplicate_fast(arr).
#
# Instead of two loops, you will only use one loop.
#
# Create your empty notebook (a Python set) before the loop starts.
#
# Start your for loop to look at each number in the array.
#
# Inside the loop, write an if statement: check if the current number is already in the notebook.
#
# If it is, return that number. You found the clone.
#
# If it is not, .add() that number to the notebook so you remember it for later.

def find_duplicate_fast(arr):
    notebook = set()
    for x in arr:

         if x in notebook:
             return x

         else :
            notebook.add(x)

print("Duplicate found:", find_duplicate_fast([3, 1, 4, 2, 2]))



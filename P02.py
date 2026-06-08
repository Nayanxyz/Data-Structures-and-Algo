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

# The Set is incredibly fast because it uses a mathematical trick called Hashing.
# Here is how it actually works under the hood.Imagine you work in a post office with 100 mailboxes.
# The List Method ($O(N)$): Someone asks, "Do we have a package for John?" You start at mailbox 1 and open every single
# box until you find John's package.
#
# The Set Method ($O(1)$): Someone asks, "Do we have a package for John?" You use a mathematical formula (a Hash Function)
# that turns the word "John" into a specific number. Let's say the formula spits out the number 42.
# You walk directly to mailbox 42. You open it.
# If it's there, you found him. If it's empty, you instantly know he's not in the system.

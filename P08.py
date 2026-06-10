# The Stack.
#
# A Stack is not a new type of memory. It is just an Array or a Linked List with a handcuff placed on it.
#
# The Constraint (LIFO):
# LIFO stands for Last In, First Out.
# Imagine a stack of heavy plates at a buffet.
#
# If you want to add a plate, you can only put it on the TOP (push).
#
# If you want to remove a plate, you can only take it from the TOP (pop).
#
# You are physically forbidden from pulling a plate out of the middle or the bottom.
#
# Every time you hit "Undo" in a text editor, or every time your browser hits the "Back" button, you are using a Stack.
# The last page you visited is the first one you return to.


# Your Objective:
# Write a Python class called BrowserHistory.
#
# It must have exactly three functions:
#
# __init__(self): Creates an empty list called self.history = [].
#
# visit_page(self, url): Pushes a new URL onto the top of the stack and prints "Visited: [url]".
#
# click_back(self): Pops the top URL off the stack and prints "Going back to: [url]".
# (If the stack is empty, it must print "No history left").


class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, url):
        self.history.append(url)
        print(f"Visited: {url}")


    def click_back(self):
        last_page = self.history.pop()
        print(f"Going back to: {last_page}")
        return last_page





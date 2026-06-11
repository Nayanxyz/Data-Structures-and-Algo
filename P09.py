# Module 4: Queues (FIFO)
# We are immediately moving to the exact opposite constraint.
#
# If a Stack is a pile of heavy plates, a Queue is a line of people waiting at a coffee shop.
# It operates on First In, First Out (FIFO).
#
# The first person who gets in line is the first person who gets their coffee.
#
# You cannot skip the line.
#
# If you build a server that handles print jobs, or a matchmaking system for a multiplayer game, you use a Queue. You want the person who has been waiting the longest to be served first.
#
# The Challenge: The Printer Queue
# You are going to build a PrinterQueue class.
# It is almost identical to the structure of your BrowserHistory, but the physical removal constraint is on the opposite end of the data.
#
# When a document is added, it goes to the back of the line (.append()).
# When a document is printed, it must be removed from the FRONT of the line.
#
# Hint: In a Python list, .pop() removes the last item. If you want to remove the very first item (Index 0), you use .pop(0).
#
# Here is your exact objective:

# Write the PrinterQueue class. Create the __init__, add_job, and print_job methods.
# Apply the FIFO constraint. Paste the code.


class PrinterQueue:
    def __init__(self):
        self.save = []

    def add_job(self, add):
        self.save.append(add)

    def print_job(self):
        remove = self.save.pop(0)
        print(f"printing: {remove}")
        return remove


# TEST SCRIPT
printer = PrinterQueue()

printer.add_job("Financial_Report.pdf")
printer.add_job("Employee_Handbook.docx")
printer.add_job("Resignation_Letter.txt")

printer.print_job() # Should print: "Printing: Financial_Report.pdf"
printer.print_job() # Should print: "Printing: Employee_Handbook.docx"
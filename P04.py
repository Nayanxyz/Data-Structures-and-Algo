# The Objective:
# Find the absolute highest number in that stack of 100 cards.
#
# Your Task:
# Write the algorithm in plain English step-by-step instructions.
# Do not write code. Write the instructions so clearly and unambiguously that a
# mindless robot could follow them and successfully find the highest card, without a single logical error or assumption.


# Think about it like holding a "King of the Hill" position in your mind.
# If you flip a card and it's a 10, the King is 10.
# You throw the card away.If you flip the next card and it's a 4, does it beat the King? No.
# You throw it away and immediately forget it.If you flip the next card and it's a 99, it beats the King.
# The old King (10) is erased. The new King is 99.
# This changes your memory requirement from 100 slots ($O(N)$ Space) to exactly 1 slot ($O(1)$ Space).



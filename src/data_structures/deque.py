"""deque.py

_summary_

_extended_summary_
"""

from collections import deque
from helper_function import process_csv_supplies

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!

# Checkpoint #1
supplies_deque = deque()

# Checkpoint #2
for row in csv_data:
    if row[2] == 'important':
        supplies_deque.appendleft(tuple(row))
    else:
        supplies_deque.append(tuple(row))

# Checkpoint #3
ordered_important_supplies = deque()
for _ in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

# Checkpoint #4
ordered_unimportant_supplies = deque()
for _ in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())

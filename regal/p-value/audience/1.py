import numpy as np

# Read the number of shelves
n = int(input())

# Read the descriptions of each shelf and store them in a list
shelves = [input().strip() for _ in range(n)]

# Calculate the number of balls in each box and sort the shelves accordingly
sorted_indices = np.argsort([sum(map(lambda x: x == 'O', shelf)) for shelf in shelves])

# Print the sorted shelves
for i in sorted_indices:
    print(shelves[i])

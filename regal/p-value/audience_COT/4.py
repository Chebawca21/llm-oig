import numpy as np

# Read the number of shelves
n = int(input())

# Read and store the shelves in a numpy array
shelves = []
for _ in range(n):
    shelf_description = input()
    shelves.append(shelf_description)

# Calculate the number of balls on each shelf
balls_count = np.array([shelf.count('O') for shelf in shelves])

# Sort the shelves based on the number of balls
sorted_indices = np.argsort(balls_count)

# Output the sorted shelves
for index in sorted_indices:
    print(shelves[index])

import numpy as np

# Read the number of shelves
n = int(input())

# Initialize an array to store the number of balls on each shelf
balls_on_shelves = np.zeros(n, dtype=int)

# Read the descriptions of each shelf and update the array
for i in range(n):
    shelf_description = input()
    balls_on_shelves[i] = len(shelf_description)

# Sort the shelves based on the number of balls
sorted_indices = np.argsort(balls_on_shelves)

# Output the sorted collection
for i in sorted_indices:
    print('O' * balls_on_shelves[i])

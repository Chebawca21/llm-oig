import numpy as np

# Read the number of shelves
n = int(input())

# Read the shelves descriptions into a list
shelves = [input().strip() for _ in range(n)]

# Calculate the number of balls in each shelf and create a numpy array
balls_count = np.array([len(shelf) for shelf in shelves])

# Sort the shelves based on the number of balls
sorted_indices = np.argsort(balls_count)

# Output the sorted shelves
for index in sorted_indices:
    print(shelves[index])
 
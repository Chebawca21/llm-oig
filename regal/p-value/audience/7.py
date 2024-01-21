import numpy as np

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Count the number of balls in each box
balls_count = np.array([len(box) for box in shelves])

# Sort shelves based on the number of balls
sorted_indices = np.argsort(balls_count)

# Output the sorted shelves
for idx in sorted_indices:
    print(shelves[idx])

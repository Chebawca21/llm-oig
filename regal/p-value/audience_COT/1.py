import numpy as np

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Convert shelves to numpy array and calculate the number of balls in each box
balls_count = np.array([sum(map(lambda x: x == 'O', shelf)) for shelf in shelves])

# Sort shelves based on the number of balls
sorted_indices = np.argsort(balls_count)

# Output the sorted shelves
for i in sorted_indices:
    print(shelves[i])

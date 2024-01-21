import numpy as np

# Read the number of shelves
n = int(input())

# Read the descriptions of shelves and store them in a numpy array
shelves = np.array([input().strip() for _ in range(n)])

# Sort the shelves based on the number of balls in each box
sorted_shelves = sorted(shelves, key=lambda x: sum(1 for ball in x if ball == 'O'))

# Print the sorted shelves
for shelf in sorted_shelves:
    print(shelf)

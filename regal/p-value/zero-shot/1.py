import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    ball_counts = np.zeros(n, dtype=int)

    # Count the number of balls on each shelf
    for i in range(n):
        ball_counts[i] = len(shelves[i])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(ball_counts)

    # Create a new list of shelves in the sorted order
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
result = organize_boxes(n, shelves)
for shelf in result:
    print(shelf)

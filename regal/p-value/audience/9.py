import numpy as np

def organize_boxes(n, shelves):
    # Create an array to store the number of balls on each shelf
    ball_counts = np.array([len(shelf) for shelf in shelves])

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(ball_counts)

    # Organize the shelves according to the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Solve the task
result = organize_boxes(n, shelves)

# Print the output
for shelf in result:
    print(shelf)

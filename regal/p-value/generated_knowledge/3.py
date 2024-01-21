import numpy as np

def organize_boxes(n, shelves):
    # Create a NumPy array to represent the number of balls on each shelf
    balls_on_shelves = np.array([len(shelf) for shelf in shelves])

    # Sort the array in ascending order and get the sorted indices
    sorted_indices = np.argsort(balls_on_shelves)

    # Rearrange the shelves according to the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
result = organize_boxes(n, shelves)
for shelf in result:
    print(shelf)

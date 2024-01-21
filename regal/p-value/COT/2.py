import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    balls_count = np.zeros(n, dtype=int)

    # Calculate the number of balls on each shelf
    for i, shelf in enumerate(shelves):
        balls_count[i] = len(shelf)

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(balls_count)

    # Create the sorted collection
    sorted_collection = [shelves[i] for i in sorted_indices]

    return sorted_collection

# Input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize and print the sorted collection
sorted_collection = organize_boxes(n, shelves)
for box in sorted_collection:
    print(box)

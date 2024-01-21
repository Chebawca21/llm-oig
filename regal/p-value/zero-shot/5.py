import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    balls_on_shelves = np.zeros(n, dtype=int)

    # Populate the array with the number of balls on each shelf
    for i, shelf in enumerate(shelves):
        balls_on_shelves[i] = len(shelf)

    # Sort the shelves based on the number of balls in ascending order
    sorted_indices = np.argsort(balls_on_shelves)
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
organized_boxes = organize_boxes(n, shelves)
for shelf in organized_boxes:
    print(shelf)

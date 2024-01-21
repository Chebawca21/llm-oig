import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Fill the boxes array with the number of balls on each shelf
    for i, shelf in enumerate(shelves):
        boxes[i] = len(shelf)

    # Sort the boxes based on the number of balls
    sorted_indices = np.argsort(boxes)

    # Organize the shelves based on the sorted order
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Get the organized shelves
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)

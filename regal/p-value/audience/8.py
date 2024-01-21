import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Iterate through the shelves and count the number of balls in each box
    for i, shelf in enumerate(shelves):
        boxes[i] = len(shelf)

    # Sort the boxes in ascending order based on the number of balls
    sorted_indices = np.argsort(boxes)
    sorted_boxes = [shelves[i] for i in sorted_indices]

    return sorted_boxes

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
result = organize_boxes(n, shelves)
for box in result:
    print(box)

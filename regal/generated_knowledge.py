import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Iterate through each shelf and count the number of balls in each box
    for i, shelf in enumerate(shelves):
        boxes[i] = len(shelf)

    # Sort the boxes in ascending order based on the number of balls
    sorted_indices = np.argsort(boxes)

    # Create the sorted collection based on the sorted indices
    sorted_collection = [shelves[i] for i in sorted_indices]

    return sorted_collection

# Input reading
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
sorted_collection = organize_boxes(n, shelves)
for box in sorted_collection:
    print(box)

import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Fill the boxes array with the number of balls on each shelf
    for i in range(n):
        boxes[i] = len(shelves[i])

    # Sort the boxes array in ascending order
    sorted_boxes = np.argsort(boxes)

    # Print the sorted shelves
    for i in sorted_boxes:
        print(shelves[i])

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Call the function to organize the boxes and print the result
organize_boxes(n, shelves)

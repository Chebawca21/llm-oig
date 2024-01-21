import numpy as np

def organize_boxes(n, shelves):
    # Create an array to store the number of balls in each box
    boxes = np.zeros(n, dtype=int)

    # Calculate the number of balls in each box and store in the array
    for i in range(n):
        boxes[i] = shelves[i].count('O')

    # Sort the boxes based on the number of balls
    sorted_indices = np.argsort(boxes)

    # Output the sorted collection
    for index in sorted_indices:
        print(shelves[index])

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Solve and print the result
organize_boxes(n, shelves)

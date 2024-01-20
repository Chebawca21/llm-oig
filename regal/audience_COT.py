import numpy as np

def sort_boxes(n, shelves):
    # Create an array to represent the number of balls in each box
    boxes = np.array([len(shelf) for shelf in shelves])

    # Sort the boxes based on the number of balls
    sorted_indices = np.argsort(boxes)

    # Output the sorted shelves
    for idx in sorted_indices:
        print(shelves[idx])

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Call the function to solve the task
sort_boxes(n, shelves)

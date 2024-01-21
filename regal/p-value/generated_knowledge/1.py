import numpy as np

def organize_boxes(n, shelves):
    # Create a list of tuples with the number of balls and the original description
    boxes = [(len(box), box) for box in shelves]

    # Sort the list of tuples based on the number of balls in ascending order
    sorted_boxes = sorted(boxes, key=lambda x: x[0])

    # Print the sorted descriptions
    for _, description in sorted_boxes:
        print(description)

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Call the function with input values
organize_boxes(n, shelves)

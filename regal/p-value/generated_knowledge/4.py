import numpy as np

# Function to organize the boxes based on the number of balls
def organize_boxes(n, shelves):
    # Create a list of tuples (description, number of balls)
    boxes = [(shelf, len(shelf)) for shelf in shelves]

    # Sort the boxes based on the number of balls
    sorted_boxes = sorted(boxes, key=lambda x: x[1])

    # Print the sorted descriptions
    for box in sorted_boxes:
        print(box[0])

# Input reading
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize and print the boxes
organize_boxes(n, shelves)

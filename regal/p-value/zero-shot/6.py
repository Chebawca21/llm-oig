import numpy as np

def organize_boxes(n, shelves):
    # Create an array to store the number of balls in each box
    box_counts = np.zeros(n, dtype=int)

    # Count the number of balls in each box
    for i, shelf in enumerate(shelves):
        box_counts[i] = len(shelf)

    # Sort the boxes based on the number of balls
    sorted_indices = np.argsort(box_counts)

    # Organize the shelves based on the sorted order
    organized_shelves = [shelves[i] for i in sorted_indices]

    return organized_shelves

# Input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the shelves
organized_shelves = organize_boxes(n, shelves)

# Output
for shelf in organized_shelves:
    print(shelf)

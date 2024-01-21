import numpy as np

def sort_boxes(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    balls_count = np.zeros(n, dtype=int)

    # Count the number of balls on each shelf
    for i in range(n):
        balls_count[i] = len(shelves[i])

    # Sort the shelves based on the number of balls using numpy.argsort
    sorted_indices = np.argsort(balls_count)

    # Arrange the shelves based on the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Input reading
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Sorting shelves
sorted_shelves = sort_boxes(n, shelves)

# Output the sorted shelves
for shelf in sorted_shelves:
    print(shelf)

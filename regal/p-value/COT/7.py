import numpy as np

def organize_boxes(n, shelves):
    # Create a numpy array to store the number of balls on each shelf
    balls_count = np.zeros(n, dtype=int)

    # Iterate through each shelf and count the number of balls on it
    for i, shelf in enumerate(shelves):
        balls_count[i] = len(shelf)

    # Sort the shelves based on the number of balls
    sorted_indices = np.argsort(balls_count)

    # Create a new array to store the sorted shelves
    sorted_shelves = np.empty_like(shelves, dtype='U1')

    # Fill the sorted shelves array based on the sorted indices
    for i in range(n):
        sorted_shelves[i] = shelves[sorted_indices[i]]

    return sorted_shelves

# Input
n = int(input())
shelves = [input() for _ in range(n)]

# Output
result = organize_boxes(n, shelves)
for shelf in result:
    print(shelf)

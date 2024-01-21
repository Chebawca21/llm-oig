import numpy as np

def organize_boxes(n, shelves):
    # Convert each shelf's description to the number of balls
    balls_counts = np.array([len(shelf) for shelf in shelves])

    # Get the indices that would sort the array
    sorted_indices = np.argsort(balls_counts)

    # Use the sorted indices to rearrange the shelves
    sorted_shelves = np.array(shelves)[sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes
result = organize_boxes(n, shelves)

# Print the result
for shelf in result:
    print(shelf)

import numpy as np

def organize_boxes(n, shelves):
    # Convert the shelves to a numpy array
    boxes = np.array([len(shelf) for shelf in shelves])

    # Get the indices that would sort the array
    sorted_indices = np.argsort(boxes)

    # Arrange the shelves based on the sorted indices
    sorted_shelves = [shelves[i] for i in sorted_indices]

    return sorted_shelves

# Read input
n = int(input())
shelves = [input().strip() for _ in range(n)]

# Organize the boxes and print the result
result = organize_boxes(n, shelves)
for shelf in result:
    print(shelf)
